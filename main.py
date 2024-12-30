
# Program by Beiop
# with code yoinked by TBR and Chechubben
# with additional help (sometimes unknowingly) by FG6, OXMC
# and sometimes chatgpt :/
# okay a lot from chatgpt,
# and a little from whatever vs has when you press tab
# and don't forget, about 3 hours of brocode tutorials!
# idk how licenses work, whether I require one or know how to spell one
# Just cite these people ^ or link to this program if you use a portion of this code.
# Though I really doubt you will use any of this code.

# from this point on, just notes to myself and/or anyone trying to understand my code.

#Mango juice is pretty good!
# we are using double-quotes for every string
# we are using 3 spaces for indents
# we are using whateverFormatThisIsForNamingThings cuz underscores_are_lame
#Window
#  profileFrame
#       addProfile
#  rectangleFrame
#    versionSelect -- previously known as appimageSelect
#      addVersion
#  launchFrame

#Set to profiles:
#   version selector
#   Mod selector
#   flag selector
#   startup apps selector
#   startup modes (server, debug)
#   Texture selector
#Global:
#   Skin selector
#   server selector
#   render distance

#launchScript -- string output to Launch & XPort
#!  profiles -- list
#       profileSelect -- list of profiles as they show in the menu (with errors)
#       not implememnted --> versionSelected -- name of the version selected
#!      profileSelected -- name of the profile selected (should be without errors, but currently I'm chasing someone down the street)
#!      profileVersionNames -- dictionary listing what profile has what version name

#!          versionNames -- list
#!              versionNamesDictionary -- list of what those names mean
#       profileFlags -- dictionary listing what flags to what profile
#       profileStartup -- dictionary listing what startup script to what profile

# also before opening a dialog box, we gonna kill the last one.

# also this is turning into A LOT of defining of A LOT of functions...
# props to all you out there who write this kind of code, GUIs and even web pages
# idk what that even means "props to you". Ah ues, here's a fake sword, gun, and a pirate ship. Thank you for your hard work!

# This is also a full page of comments. I didn't know that was possible unless there was a license in there, which there is, spelled wrong again.

from tkinter import *
from tkinter import filedialog #idk why I even have to import this but ig i do
from tkinter import messagebox
from tktooltip import ToolTip
from ping import chechubben # absolutly never open this file in VS code, or on windows. The original creator of this code reqires that it only be accessed in a proper text editor. Actually, don't tell chechubben this, but I'm uploading this whole project to GitHub and editing it in VS Code on Windows. But I doubt he can read this unless he has wordwrap on in Notepad ++. (actuall I think he uses something else... I'm not too sure)
import os
import pickle

#global variable to track the open window hi mom. this is a program i'm writing that is not for school. I could be doing homework, but that's boring.
currentWindow = None


SAVE_FILE = "save.pkl"



def launch():
    global profileSelected
    if profileSelect.curselection():  # Checks if nothing is selected
        profileSelected = profiles[profileSelect.curselection()[0]]
    else:
        print("No selection in profileSelect with refreshProfiles Function")
    print(profileSelected)
    launchScript = versionNamesDictionary.get(profileVersionNames.get(profileSelected))
    print(launchScript)
    

def load():
    #ooh, turns out you can globalize multiple variables at once
    global profiles, profileSelected, profileVersionNames, versionNames, versionNamesDictionary, launchScript
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "rb") as file:
            data = pickle.load(file)
            profiles = data.get("profiles", [])
            profileSelected = data.get("profileSelected")
            profileVersionNames = data.get("profileVersionNames", {})
            versionNames = data.get("versionNames", [])
            versionNamesDictionary = data.get("versionNamesDictionary", {})
            launchScript = data.get("launchScript", "echo beans")
        print("Loaded data from save file.")
    else:
        print("No save file found. Using default values.")
        profiles = []
        profileSelected = None
        profileVersionNames = {}
        versionNames = ["Flatpak"]
        versionNamesDictionary = {"Flatpak": "/usr/bin/flatpak run --branch=stable --command=minecraft-pi-reborn-client com.thebrokenrail.MCPIReborn"}
        launchScript = "echo beans"

def save():
    data = {
        "profiles": profiles,
        "profileSelected": profileSelected,
        "profileVersionNames": profileVersionNames,
        "versionNames": versionNames,
        "versionNamesDictionary": versionNamesDictionary,
        "launchScript": launchScript,
    }
    with open(SAVE_FILE, "wb") as file:
        pickle.dump(data, file)
    print("Data saved successfully.")

def refreshProfiles():
    global profileSelected
    if profileSelect.curselection():  # Checks if nothing is selected
        print("refresh profiles Selected:", profileSelect.get(profileSelect.curselection()))
        profileSelected = profileSelect.get(profileSelect.curselection())
        A = True
        
    elif profileSelected != None:
        A = True
    else:
        print("No selection in profileSelect with refreshProfiles Function")
        A = False
    
    profileSelect.delete(0,END)
    for profile in profiles:
        warning = ""
        if profile not in profileVersionNames:
            warning += "[No Version] "
        if warning != "":
            warning = "Warning: " + warning
        profileSelect.insert(END, warning + profile)
    if A == True:
        for i , item in enumerate(profileSelect.get(0,END)): #code that idk how it works I got from google ai overview at the airport. 
            if item == profileSelected:
                profileSelect.selection_set(i)
    #   Future Beiop Here:
    #   I think I understand it now, and it does the same as the code below, but I have yet to test it...
    #   But I still have no idea what it does with "for i, item in..." WHY/HOW is there a COMMA?

    #   for i in range(len(profileSelect.get(0,END))):
    #   if profileSelect[i] == profileSelected:
    #       profileSelect.selection_set(i)

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

def versionSelect():
    global pathEntry
    global versionNames
    global profileSelect
    global currentWindow #this little block of code you're going to see everywhere. It is mostly the same process to create the popup windows
    global versionSelectListbox
    global profileSelected

    if not profileSelect.curselection():  # Checks if nothing is selected
        print("No selection in profileSelect")
        return
    else:
        profileSelected = profiles[profileSelect.curselection()[0]]
        print("Selected:", profileSelected)
    
    if currentWindow is not None:
        currentWindow.destroy() # kill window if it already exists
    currentWindow = Toplevel(window)
    currentWindow.transient(window)
    currentWindow.title("Version Select")
    currentWindow.geometry("400x300")
    exitButton = Button(currentWindow,text="Close Dialouge",command=exitWindow)
    exitButton.place(x=305,y=220,width=95)
    ToolTip(exitButton, msg="Clothes Dialoughe")
    openAddVersion = Button(currentWindow, text="add", command=addVersion)
    openAddVersion.pack()
    versionSelectListbox = Listbox(currentWindow)
    versionSelectListbox.place(x=5,y=20,width=285,height=330)
    for version in versionNames:
        versionSelectListbox.insert(END, version)
    save = Button(currentWindow, text="save this",command=saveVersion)
    save.pack()
def saveVersion():
    if not versionSelectListbox.curselection():  # Checks if nothing is selected
        print("No selection in versionselectlistbox")
        return
    else:
        #versionSelectListbox.get(versionSelectListbox.curselection())
        profileSelected, versionSelectListbox.get(versionSelectListbox.curselection())
        profileVersionNames[profileSelected] = versionSelectListbox.get(versionSelectListbox.curselection())
        print(profileVersionNames)
        refreshProfiles()
    
def addVersion():
    global pathEntry
    global nameEntry
    global currentWindow #this little block of code you're going to see everywhere. It is mostly the same process to create the popup windows
    if currentWindow is not None:
        currentWindow.destroy() # kill window if it already exists
    currentWindow = Toplevel(window)
    currentWindow.transient(window)
    currentWindow.title("Add Version")
    currentWindow.geometry("400x180")
    backButton = Button(currentWindow,text="Back",command=versionSelect)
    backButton.place(x=305,y=40,width=95)
    pathEntry = Entry(currentWindow,font=("random something",10),width=50)
    pathEntry.place(x=5,y=0,width=390)
    pathEntry.insert(0,"<path to .AppImage>, executable, or mcpi startup command")
    nameEntry = Entry(currentWindow,font=("random something",10),width=50)
    nameEntry.place(x=5,y=20,width=390)
    nameEntry.insert(0,"Name of Version u gonna add")
    addButton = Button(currentWindow,text="Add",command=addNewVersion)
    addButton.place(x=0,y=40,width=95)
    Button(currentWindow,text="Open",command=openFile).place(x=5,y=60,width=90)
def addNewVersion():
    if nameEntry.get() in versionNamesDictionary:
        print("IT EXISTS")
    else:
        versionNamesDictionary[nameEntry.get()] = pathEntry.get()
        versionNames.append(nameEntry.get())
    versionSelect()

def openFile():
   #global filepath -- still learning how global variables work
   global pathEntry
   filepath = filedialog.askopenfilename(
      initialdir="/home",
      title="Select a Reborn Appimage",
      filetypes=(("Appimages","*.AppImage"),("something else?","*"))
      )
   print(filepath)
   selection = profileSelect.curselection()
   if selection:
      print(selection[0])
   else:
      print("no profile selected")
   pathEntry.delete(0,END)
   
   if len(filepath) > 40:
      for i in range(40):
         pathEntry.insert(0,filepath[-(i+1)])
   else:
      pathEntry.insert(0,filepath)
   pathEntry.insert(0,"...")
   pathEntry.config(state="disabled")

def addProfile(): #Function behind Add button in the profileFrame & creation of addProfile window
    global currentWindow
    global entry
    if currentWindow is not None:
        currentWindow.destroy() # kill window if it already exists
    currentWindow = Toplevel(window)
    currentWindow.transient(window)
    currentWindow.title("Add Profile")
    currentWindow.geometry("400x80")
    label = Label(currentWindow,text="Name your new Profule")
    label.pack(side=TOP)
    entry = Entry(currentWindow,font=("random something",10),width=50)
    entry.pack(side=TOP)
    back = Button(currentWindow,text="Escape!!",command=exitWindow)
    back.pack(side=RIGHT)
    save = Button(currentWindow,text="Save :)",command=addNewProfile)
    save.pack(side=LEFT)
def addNewProfile():
    global profileSelect
    profiles.append(entry.get())
    refreshProfiles()
    exitWindow()

def copyProfile():
    print("dev copyProfile does nothing rn")
def removeProfile():
    print("dev copyProfile does nothing rn")

load() #load data from save file

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
exportButton = Button(launchFrame,bg="#4AFF00",activebackground="red",text="save",command=save)
exportButton.pack()

profileFrame = Frame(window,bd=5,relief="groove")
profileFrame.place(x=0,y=0,height=360,width=300)

label = Label(profileFrame,text="Profiles",relief="flat")
label.place(x=0,y=0,height=20)
profileSelect = Listbox(profileFrame)
profileSelect.place(x=5,y=20,width=285,height=300)
refreshProfiles()
add = Button(profileFrame,text="Add",command=addProfile)
add.pack(side=BOTTOM)
remove = Button(profileFrame,text="Remove",command=removeProfile)
remove.pack(side=RIGHT)
copy = Button(profileFrame,text="Copy",command=copyProfile)
copy.pack(side=TOP)


rectangleFrame = Frame(window,bd=5,relief="raised")
rectangleFrame.place(x=300,y=0,height=360,width=100)

appimageRectangle = Button(rectangleFrame,bg="#4AFF00",activebackground="red",text="Version",command=versionSelect)
appimageRectangle.pack()


if (244 - 92) == 212:
    print("It's happening again!")

window.mainloop() #display window and wait/listen for input