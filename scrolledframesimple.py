from tkinter import *
from ttkbootstrap.scrolled import ScrolledFrame

app = Tk()

sf = ScrolledFrame(app, autohide=True)
sf.pack(fill=BOTH, expand=YES, padx=10, pady=10)

# add a large number of checkbuttons into the scrolled frame

bgFile = "assets/test.png"
if bgFile != None:
            print(f"bgFile: {bgFile}")
            bgImage = PhotoImage(file=bgFile)
            Label(sf,image=bgImage).pack(anchor=W)#place(x=30,y=0)
for x in range(20):
    Checkbutton(sf, text=f"Checkbutton {x}").pack(anchor=W)
    Checkbutton(sf, text=f"Checkbutton {x}").pack(anchor=W)

app.mainloop()