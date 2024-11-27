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
   selection = listbox.curselection()
   if selection:
      print(selection[0])
   else:
      print("no profile selected")
   entry.delete(0,END)
   
   if len(filepath) > 40:
      for i in range(40):
         entry.insert(0,filepath[-(i+1)])
   else:
      entry.insert(0,filepath)
   entry.insert(0,"...")
   entry.config(state="disabled")
   

# Create a Listbox and add some items
listbox = Listbox(window)

listbox.pack(padx=20, pady=10)

items = ["Apple", "Banana", "Orange", "Grapes", "Mango"]
for item in items:
    listbox.insert(END, item)
listbox.select_set(0)


entry = Entry(appimageEntry,font=("Ubuntu Mono",10),width=50)
entry.pack(side="left")

Button(appimageEntry,command=openFile).pack(side="right")



window.mainloop() #display window and wait/listen for input