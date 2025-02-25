import tkinter as tk
from tkinter import Toplevel, Listbox, Button

class VersionSelector:
    def __init__(self, root, profiles, version_names):
        self.root = root
        self.profiles = profiles
        self.version_names = version_names
        self.profile_selected = None
        self.current_window = None

        # Create Main Window for Profile Selection
        self.main_window = tk.Toplevel(self.root)
        self.main_window.title("Profile Selection")
        self.main_window.geometry("300x200")

        # Profile Listbox
        self.profile_listbox = Listbox(self.main_window)
        self.profile_listbox.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        for profile in self.profiles:
            self.profile_listbox.insert(tk.END, profile)

        # Select Button
        select_button = Button(self.main_window, text="Select Profile", command=self.open_version_select)
        select_button.pack(pady=5)

    def open_version_select(self):
        """Opens the version selection window after selecting a profile."""
        if not self.profile_listbox.curselection():  # Check if something is selected
            print("No selection in profile listbox")
            return

        self.profile_selected = self.profiles[self.profile_listbox.curselection()[0]]
        print("Selected Profile:", self.profile_selected)

        self.exit_window()  # Close existing window if open
        self.current_window = Toplevel(self.root)
        self.current_window.transient(self.root)
        self.current_window.title("Version Select")
        self.current_window.geometry("400x300")

        # Close Button
        exit_button = Button(self.current_window, text="Close", command=self.exit_window)
        exit_button.place(x=305, y=220, width=95)

        # Add Version Button
        add_version_button = Button(self.current_window, text="Add Version", command=self.add_version)
        add_version_button.pack()

        # Version Listbox
        self.version_select_listbox = Listbox(self.current_window)
        self.version_select_listbox.place(x=5, y=20, width=285, height=200)

        for version in self.version_names:
            self.version_select_listbox.insert(tk.END, version)

        # Save Button
        save_button = Button(self.current_window, text="Save", command=self.save_version)
        save_button.pack()

    def exit_window(self):
        """Closes the version selection window."""
        if self.current_window:
            self.current_window.destroy()
            self.current_window = None

    def add_version(self):
        """Placeholder for adding a version."""
        print("Add version functionality goes here")

    def save_version(self):
        """Placeholder for saving the selected version."""
        print("Save version functionality goes here")


# Example usage:
if __name__ == "__main__":
    root = tk.Tk()
    #root.withdraw()  # Hide the root window

    profiles = ["Profile1", "Profile2", "Profile3"]
    version_names = ["v1.0", "v2.0", "v3.0"]

    selector = VersionSelector(root, profiles, version_names)

    root.mainloop()
