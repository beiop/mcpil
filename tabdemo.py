if False:
    with open("available-feature-flags","r") as affFile: #open file
        affLines = affFile.readlines()
        with open('feature-flags', 'w') as ffFile:
            ffLines = []
            for line in range(len(affLines)):
                ffLines.append(affLines[line])
            ffFile.writelines(ffLines)
from tkinter import *
import tkinter as tk
from tkextrafont import Font



class App(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")

        font = Font(file="assets/mojangles.ttf", family="Mojangles")
        Label(self, text="Hello", font=font).pack()


        # Left side - buttons
        button_frame = Frame(self, width=150, bg="gray")
        button_frame.pack(side=LEFT, fill=Y)
        button_frame.pack_propagate(False)

        # Right side - container for pages
        self.page_container = Frame(self, bg="white")
        self.page_container.pack(side=RIGHT, fill=BOTH, expand=True)

        #range
        len = 100#1000

        # Create pages
        self.pages = {}
        for i in range(len):
            page = Frame(self.page_container, bg=f"#f{i}{i}f{i}0")
            label = Label(page, text=f"Page {i+1}", font=("Mojangles",24))
            label.pack(expand=True)
            page.place(relx=0, rely=0, relwidth=1, relheight=1)
            self.pages[f"Page{i+1}"] = page

        # Create buttons to switch pages
        from scrollable import ScrollFrame
        scrollFrame = ScrollFrame(button_frame)  # add a new scrollable frame.
        sf = scrollFrame.viewPort

        for i in range(len):
            Button(sf, text=f"Page {i+1}", command=lambda i=i: self.show_page(f"Page{i+1}"),font=("Mojangles",10)).pack(fill=X)

        
        scrollFrame.pack(expand=True,fill=BOTH)

        self.show_page("Page1")  # Show first page by default

    def show_page(self, name):
        page = self.pages.get(name)
        if page:
            page.tkraise()

if __name__ == "__main__":
    app = App()
    app.mainloop()
