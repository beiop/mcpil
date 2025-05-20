import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

# ——— 1. PARSE the indented file into a nested structure

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

# ——— 2. SCROLLABLE FRAME FOR RIGHT PANE

class ScrollableFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = tk.Canvas(self)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

# ——— 3. MAIN APP — left buttons + right scrolling content

class FeatureFlagsApp(tk.Tk):
    def __init__(self, data):
        super().__init__()
        self.title("Feature Flags")
        self.data = data
        self._build_ui()

    def _build_ui(self):
        # Left frame for top-level categories
        left_frame = ttk.Frame(self, width=200, relief=tk.SUNKEN)
        left_frame.pack(side=tk.LEFT, fill=tk.Y)
        # Right scrollable pane
        right_scroll = ScrollableFrame(self)
        right_scroll.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        self.right_container = right_scroll.scrollable_frame

        # Populate left buttons
        for (name, node) in self.data:
            btn = ttk.Button(left_frame, text=name,
                             command=lambda n=name, nd=node: self._on_left_click(n, nd))
            btn.pack(fill=tk.X, pady=2, padx=2)

        # Auto-select first on startup
        if self.data:
            first_name, first_node = self.data[0]
            self._on_left_click(first_name, first_node)

    def _clear_right(self):
        for w in self.right_container.winfo_children():
            w.destroy()

    def _on_left_click(self, name, node):
        # clear and display contents of selected category
        self._clear_right()
        # display subtree under node
        # root label
        ttk.Label(self.right_container, text=f"Category: {name}",
                  font=('TkDefaultFont', 12, 'bold')).pack(anchor='w', pady=(5,2))
        self._display_subtree(self.right_container, node)

    def _display_subtree(self, parent, node):
        # node is dict with 'children'
        for (name, child) in node.get('children', []):
            if isinstance(child, dict):
                # label and its children
                lf = ttk.LabelFrame(parent, text=f"Category: {name}")
                lf.pack(fill=tk.X, padx=10, pady=5, anchor='w')
                self._display_subtree(lf, child)
            else:
                var = tk.BooleanVar(value=child)
                cb = ttk.Checkbutton(parent, text=name, variable=var)
                cb.pack(anchor='w', padx=20, pady=2)

if __name__ == '__main__':
    data = parse_flags('available-feature-flags')
    app = FeatureFlagsApp(data)
    app.geometry('900x600')
    app.mainloop()
    