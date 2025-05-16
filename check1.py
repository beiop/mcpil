import tkinter as tk
from tkinter import ttk

# ——— 1. PARSER — build nested structure from indented file

def parse_flags(filename):
    root = {}
    stack = [(-1, root)]
    with open(filename, 'r') as f:
        for raw in f:
            if not raw.strip(): continue
            indent = len(raw) - len(raw.lstrip(' '))
            parts = raw.strip().split(' ', 1)
            key = parts[-1]
            node = {} if parts[0] == 'CATEGORY' else (parts[0] == 'TRUE')
            while stack and stack[-1][0] >= indent:
                stack.pop()
            parent = stack[-1][1]
            parent.setdefault('children', []).append((key, node))
            if isinstance(node, dict):
                stack.append((indent, node))
    return root['children']

# ——— 2. MAIN APP — a Toplevel that hides the root

class FeatureFlagsApp(tk.Toplevel):
    def __init__(self, master, data):
        super().__init__(master)
        self.title("Feature Flags")
        self.data = data
        self.panels = []
        self._build_ui()
        self.after(0, self._auto_select_first)

    def _build_ui(self):
        self.pw = ttk.Panedwindow(self, orient=tk.HORIZONTAL)
        self.pw.pack(fill=tk.BOTH, expand=True)
        for _ in range(4):
            frame = ttk.Frame(self.pw, relief=tk.SUNKEN)
            self.pw.add(frame, weight=1)
            self.panels.append(frame)
        self._populate_panel(0, self.data)

    def _clear_panel(self, depth):
        for w in self.panels[depth].winfo_children():
            w.destroy()
        if depth + 1 < 4:
            self._clear_panel(depth + 1)

    def _populate_panel(self, depth, items):
        frm = self.panels[depth]
        frm.selection = None
        for (name, node) in items:
            if isinstance(node, dict):
                btn = ttk.Button(frm, text=name)
                btn.pack(fill=tk.X, padx=2, pady=2)
                btn.config(command=lambda d=depth, nd=node, b=btn: (
                    setattr(self.panels[d], 'selection', b),
                    self._on_category_click(d, nd)
                ))
            else:
                var = tk.BooleanVar(value=node)
                cb = ttk.Checkbutton(frm, text=name, variable=var)
                cb.pack(anchor='w', padx=5)

    def _on_category_click(self, depth, node):
        # Deselect others and mark this one pressed
        for w in self.panels[depth].winfo_children():
            if isinstance(w, ttk.Button):
                w.state(('!pressed',))
        btn = self.panels[depth].selection
        if btn:
            btn.state(('pressed',))

        # Clear deeper panes
        for d in range(depth + 1, 4):
            self._clear_panel(d)

        # Populate next pane
        if isinstance(node, dict) and node.get('children'):
            self._populate_panel(depth + 1, node['children'])
            # Auto-select first in the next pane and onward
            self._auto_select_from(depth + 1)

        # Hide empty panes
        self._hide_unused()

    def _auto_select_first(self):
        # Walk down from pane 0 selecting first category
        self._auto_select_from(0)

    def _auto_select_from(self, depth):
        if depth >= 4:
            return
        frm = self.panels[depth]
        btns = [w for w in frm.winfo_children() if isinstance(w, ttk.Button)]
        if not btns:
            return
        btns[0].invoke()

    def _hide_unused(self):
        for frm in self.panels:
            if not frm.winfo_children():
                try:
                    self.pw.forget(frm)
                except tk.TclError:
                    pass
            else:
                if str(frm) not in self.pw.panes():
                    self.pw.add(frm, weight=1)

# ——— 3. STYLING — selected buttons turn blue when pressed

style = ttk.Style()
style.configure('TButton', padding=5)
style.map('TButton',
          background=[('pressed', 'blue'), ('!pressed', 'SystemButtonFace')])

# ——— 4. ENTRY POINT — hide root, launch Toplevel

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    data = parse_flags('available-feature-flags')
    app = FeatureFlagsApp(root, data)
    app.geometry('900x500')
    app.mainloop()
