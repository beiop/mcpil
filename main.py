#Mango juice is pretty good!

from tkinter import *
from tkinter import filedialog #idk why I even have to import this but ig i do


#Generate window to put things in
window = Tk()
window.geometry("400x480")
window.title("McBeiopyll")
icon = PhotoImage(file="icon.png")
window.iconphoto(True,icon)

appimageEntry = Frame()
appimageEntry.pack()
def openFile():
   global filepath
   filepath = filedialog.askopenfilename(
      initialdir="/home",
      title="Select a Reborn Appimage",
      filetypes=(("Appimages","*.AppImage"),("something else?","*"))
   )
   print(filepath)
   entry.delete(0,END)
   entry.insert(0,filepath)

entry = Entry(appimageEntry,font=("Ubuntu Mono",10),width=50)
entry.pack(side="left")

Button(appimageEntry,command=openFile).pack(side="right")



window.mainloop() #display window and wait/listen for input