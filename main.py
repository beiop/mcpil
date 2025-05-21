#malpractice
#last cleaned up: may 10, 13:36. Took one hour.
#classes are capitalized, everything else is camelCase
#underscores are chatgpt's fault.

from tkinter import *
import os # just to stop it from erroring on windows
osname = os.name
import subprocess
from scrollable import ScrollFrame # when packing the scrollframe, we pack scrollFrame itself (NOT the viewPort)
#import re #apparently needed for splitting by spaces and not tabs
from tkextrafont import Font


def custom_split(line):
    # Count leading spaces
    leading_spaces = len(line) - len(line.lstrip(' '))
    depth = leading_spaces // 4
    # Remove leading spaces
    content = line.lstrip(' ')
    # Split the rest by spaces (default split)
    words = content.split()
    # Return a list: one "word" for each depth, then the split words
    return (['    '] * depth) + words

if  os.name == "posix":
    assetsDir = "assets/"
else:
    assetsDir = "assets\\"


class Window(Tk):
    
    def __init__(self,title,geometry):
        super().__init__() # Initialize the Tk class, apparently...??
        self.geometry(geometry)
        self.title(title)
        self.resizable(False, False)
        try: #image loading
            icon = PhotoImage(file=f"{assetsDir}icon.png")
            self.iconphoto(True,icon)
            
            self.bgImage = PhotoImage(file=f"{assetsDir}background.png")
            Label(self, image=self.bgImage).place(x=0,y=0)
        except Exception as e:
            print(f"Error loading images in Window.__init__: {e}")
            print("likely not exectuting from the correct directory.")
        Button(self,bg="#4AFF00",activebackground="red",text="Launch",command=self.launch).place(x=100,y=0)
        
        Button(self,bg="#4AFF00",activebackground="red",text="Feature Flags",command=lambda:CurrentWindow().openFeatureFlagWindow()).place(x=100,y=30)

        Button(self,bg="#4AFF00",activebackground="red",text="print ff",command=lambda:print(self.getAvailableFeatureFlags())).place(x=100,y=60)
    
    def launch(self):
        #command = ["flatpak", "run", "com.thebrokenrail.MCPIReborn"]
        command = ["./minecraft-pi-reborn-3.0.0-amd64.AppImage"]
        if  os.name == "posix":
            try:
                subprocess.run(command, check=True)
                print(f"Successfully launched")
                self.destroy() # Close the main window after launching
            except FileNotFoundError:
                print("Error: The specified file was not found.")
            except PermissionError:
                print("Error: Permission denied. Please check your permissions.")
                
            except subprocess.CalledProcessError as e:
                print(f"Error in Window.launch: {e}")
        else:
            print("chechubben is disapointed in you for using Windows")
            print("task failed successfully")
            self.destroy()

    def getAvailableFeatureFlags(self):
        
        command = ["./minecraft-pi-reborn-3.0.0-amd64.AppImage","--print-available-feature-flags"]
        try:
            # Execute the command and capture the output
            result = subprocess.run(command, check=True, capture_output=True, text=True)
            output = result.stdout
            # Replace newlines with | and remove the last character
            settings_string = output.replace("\n", "|")[0:-1]
            #return formatted_output

        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")
        
        # Convert the string into a dictionary
        settings = {}
        for item in settings_string.split('|'):
            parts = item.strip().split(' ', 1)
            if len(parts) == 2:
                value_str, name = parts
                value = value_str.strip().lower() == "true"
                settings[name.strip()] = value
        return settings
    
class CurrentWindow(Toplevel):

    _last_instance = None


    def buildCurrentWindow(self,title,geometry,bgFile=None):
        # destroy previous if still open
        if CurrentWindow._last_instance is not None:
            try:
                CurrentWindow._last_instance.destroy()
            except:
                pass
        
        
        CurrentWindow._last_instance = self
        
        # Get position of parent window
        x = self.master.winfo_rootx()
        y = self.master.winfo_rooty()

        # Offset for the new window
        new_x = x + 0
        new_y = y + 0
    
        self.transient(root) #set this window as an annoying child that gets in the way
        self.geometry(geometry+f"+{new_x}+{new_y}")
        self.title(title)
        icon = PhotoImage(file=f"{assetsDir}icon.png")
        self.iconphoto(True,icon)
        self.resizable(False, False)
        if bgFile != None:
            print(f"bgFile: {bgFile}")
            self.bgImage = PhotoImage(file=bgFile)
            Label(self, image=self.bgImage).place(x=0,y=0)

    def showPage(self, name):
        page = self.pages.get(name)
        if page:
            page.tkraise()
    def createPage(self, name):
        page = Frame(self.flagFrame, bg="#fff")
        page.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.pages[name] = page
        return name, page
    def openFeatureFlagWindow(self):
        self.buildCurrentWindow("Feature Flags","400x400")
        
        Label(self, text="Hello", font=font).pack()
        
        # Left side - container for buttons
        buttonFrame = Frame(self, width=150, bg="gray")
        buttonFrame.pack(side=LEFT, fill=Y)
        buttonFrame.pack_propagate(False)
        
        # Right side - container for pages
        self.flagFrame = Frame(self, bg="white")
        self.flagFrame.pack(side=RIGHT, fill=BOTH, expand=True)

        self.pages = {}

        
        
        #make two dictionaries, one to store button status and one to list remaining 
        with open(f"{assetsDir}possibly-available-feature-flags", "r") as file:
            lines = file.readlines()

            for line in lines:
                depth = 0
                lineSplit = custom_split(line.rstrip('\n'))
                for word in lineSplit:
                    if word != '    ':
                        continue
                    depth += 1
                if lineSplit[depth] == "CATEGORY":
                    if depth == 0:
                        name, page = self.createPage(' '.join(lineSplit[depth+1:]))
                        Label(page, text=lineSplit[depth+1:], font=("Mojangles",20),wraplength=220).pack(side=TOP,anchor=W)
                        from scrollable import ScrollFrame
                        scrollFrame = ScrollFrame(page)  # add a new scrollable frame.
                        lastCatagory = scrollFrame.viewPort
                        scrollFrame.pack(expand=True,fill=BOTH)

                    else:
                        Label(lastCatagory, text=lineSplit[depth+1:],font=("Mojangles",15)).pack(side=TOP,anchor=W)

                if lineSplit[depth] == "TRUE" or lineSplit[depth] == "FALSE":
                    print(f"feature flag: {lineSplit[depth+1:]} at depth {depth}")
                    Checkbutton(lastCatagory, text=lineSplit[depth+1:], variable=IntVar(), font=("Mojangles",10),wraplength=200).pack(side=TOP,anchor=W)

        #build buttons for cats
        for name in self.pages:
            Button(buttonFrame, text=name, command=lambda n=name: self.showPage(n), font=("Mojangles",10)).pack(fill=X)

        self.showPage("Additions")

        #Dictionary
        Window.getAvailableFeatureFlags(Window)
        
        scrollFrame.pack(expand=True,fill=BOTH)
        self.mainloop()
    
    
    def close(self):
        self.destroy()

root = Window("McBeiopyll2","400x480")
font = Font(file="assets/mojangles.ttf", family="Mojangles")
root.mainloop()

