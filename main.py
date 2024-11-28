# Program by Beiop
# with code yoinked by TBR and Chechubben
# with additional help (sometimes unknowingly) by FG6, OXMC
# and sometime chatgpt :/
# idk how licenses work, whether I require one or know how to spell one
# Just cite these people ^ or link to this program if you use a portion of this code.

#Mango juice is pretty good!
# we are using double-quotes for every string
# we are using 3 spaces for indents
# we are using whateverFormatThisIsForNamingThings cuz underscores_are_lame
#Window
#  profileFrame
#  rectangleFrame
#  launchFrame

# also before opening a dialog box, we gonna kill the last one.


from tkinter import *
from tkinter import filedialog #idk why I even have to import this but ig i do
from tkinter import messagebox
from tktooltip import ToolTip
import ping # absolutly never open this file in VS code, or on windows. The original creator of this code reqires that it only be accessed in a proper text editor. Actually, don't tell chechubben this, but I'm uploading this whole project to GitHub and editing it in VS Code on Windows. But I doubt he can read this unless he has wordwrap on in Notepad ++. (actuall I think he uses something else... I'm not too sure)

#global variable to track the open window hi mom
currentWindow = None

launchScript = "echo beans"

def launch():
    listbox.insert(END, launchScript)

def export():
    global currentWindow #this little block of code you're going to see everywhere. It is mostly the same process to create the popup windows
    if currentWindow is not None:
        currentWindow.destroy() # kill window if it already exists
    currentWindow = Toplevel(window)
    currentWindow.transient(window)
    currentWindow.title("Goober XPORT")
    currentWindow.geometry("400x200")
    text = Text(currentWindow, wrap=WORD, height=10, width=40)
    text.pack(padx=10)
    text.insert("1.0",launchScript)
    text.config(state="disabled")
    

def exitWindow():
    global currentWindow
    if currentWindow is not None:
        currentWindow.destroy()
        #currentWindow = None

def appimageMenu():
    global entry
    global currentWindow #this little block of code you're going to see everywhere. It is mostly the same process to create the popup windows
    if currentWindow is not None:
        currentWindow.destroy() # kill window if it already exists
    currentWindow = Toplevel(window)
    currentWindow.transient(window)
    currentWindow.title("Appimage Select")
    currentWindow.geometry("400x80")
    exitButton = Button(currentWindow,text="Close Dialouge",command=exitWindow)
    exitButton.place(x=305,y=20,width=95)
    ToolTip(exitButton, msg="Clothes Dialoughe")
    entry = Entry(currentWindow,font=("random something",10),width=50)
    entry.place(x=5,y=0,width=390)
    entry.insert(0,"<path to .AppImage>")
    Button(currentWindow,text="Open",command=openFile).place(x=5,y=20,width=90)  
def openFile():
   global filepath
   global entry
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

#Generate window to put things in
window = Tk()
window.geometry("400x480")
window.title("McBeiopyll")
icon = PhotoImage(file="icon.png")
window.iconphoto(True,icon)

launchFrame = Frame(window,bd=5,relief="sunken")
launchFrame.place(x=0,y=360,height=120,width=400)

launchButton = Button(launchFrame,bg="#4AFF00",activebackground="red",text="Launch",command=launch)
launchButton.pack()
exportButton = Button(launchFrame,bg="#4AFF00",activebackground="red",text="X Port",command=export)
exportButton.pack()

profileFrame = Frame(window,bd=5,relief="groove")
profileFrame.place(x=0,y=0,height=360,width=300)

label = Label(profileFrame,text="Profiles",relief="flat")
label.place(x=0,y=0,height=20)
listbox = Listbox(profileFrame)
listbox.place(x=5,y=20,width=285,height=330)
items = ["Cached", "Reborn", "MCPE", "MCPI"]
for item in items:
    listbox.insert(END, item)
listbox.select_set(0)


rectangleFrame = Frame(window,bd=5,relief="raised")
rectangleFrame.place(x=300,y=0,height=360,width=100)

appimageRectangle = Button(rectangleFrame,bg="#4AFF00",activebackground="red",text="Appimage",command=appimageMenu)
appimageRectangle.pack()


if (244 - 92) == 212:
    print("It's happening again!")

window.mainloop() #display window and wait/listen for input