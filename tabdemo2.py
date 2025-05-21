from tkinter import *
from tkextrafont import Font

class App(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.title("Tabbed Page Demo")

        font = Font(file="assets/mojangles.ttf", family="Mojangles")
        Label(self, text="Hello", font=font).pack()

        # Left side - buttons
        button_frame = Frame(self, width=150, bg="gray")
        button_frame.pack(side=LEFT, fill=Y)
        button_frame.pack_propagate(False)

        # Right side - container for pages
        self.page_container = Frame(self, bg="white")
        self.page_container.pack(side=RIGHT, fill=BOTH, expand=True)

        self.pages = {}

        # Create pages using the function
        for i in range(5):  
            name, page = self.create_page(f"Page{i+1}")
            Label(page, text=f"Page {i+1}", font=("Mojangles",24)).pack(expand=True)


        for name in self.pages:
            Button(button_frame, text=name, command=lambda n=name: self.show_page(n), font=("Mojangles",10)).pack(fill=X)

        self.show_page("Page1")

        # Example: Add a widget to a page later
        _, page3 = "Page3", self.pages["Page3"]
        Label(page3, text="You can add widgets later!", fg="red").pack()

    def create_page(self, name):
        page = Frame(self.page_container, bg="#fff")
        page.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.pages[name] = page
        return name, page

    def show_page(self, name):
        page = self.pages.get(name)
        if page:
            page.tkraise()

if __name__ == "__main__":
    app = App()
    app.mainloop()