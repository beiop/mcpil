if False:
    with open("available-feature-flags","r") as affFile: #open file
        affLines = affFile.readlines()
        with open('feature-flags', 'w') as ffFile:
            ffLines = []
            for line in range(len(affLines)):
                ffLines.append(affLines[line])
            ffFile.writelines(ffLines)
from tkinter import *
from scrollable import ScrollFrame


class App(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")

        # Left side - buttons
        button_frame = Frame(self, width=2 , bg="gray")
        button_frame.pack(side=LEFT, fill=Y)

        # Right side - container for pages
        self.page_container = Frame(self, bg="white")
        self.page_container.pack(side=RIGHT, fill=BOTH, expand=True)

        #range
        len = 10#1000

        # Create pages
        self.pages = {}
        for i in range(len):
            page = Frame(self.page_container, bg=f"#f{i}{i}f{i}0")
            label = Label(page, text=f"Page {i+1}", font=("Arial", 24))
            label.pack(expand=True)
            page.place(relx=0, rely=0, relwidth=1, relheight=1)
            self.pages[f"Page{i+1}"] = page

        scrollFrame = ScrollFrame(button_frame)
        sf = scrollFrame.viewPort

        # Create buttons to switch pages
        for i in range(len):
            Button(sf, text=f"Page {i+1}", command=lambda i=i: self.show_page(f"Page{i+1}")).pack(fill=X)
        scrollFrame.pack(side="top", fill="both", expand=True)

        self.show_page("Page1")  # Show first page by default

    def show_page(self, name):
        page = self.pages.get(name)
        if page:
            page.tkraise()

if __name__ == "__main__":
    app = App()
    app.mainloop()
