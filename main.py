#malpractice
#last cleaned up: may 10, 13:36. Took one hour.
#classes are capitalized, everything else is camelCase
#underscores are chatgpt's fault.

from tkinter import *
#from ttkbootstrap import *
import os # just to stop it from erroring on windows
osname = os.name
import subprocess

class Window(Tk):

    def __init__(self,title,geometry):
        super().__init__() # Initialize the Tk class, apparently...??
        self.geometry(geometry)
        self.title(title)
        self.resizable(False, False)
        try: #image loading
            icon = PhotoImage(file="assets/icon.png")
            self.iconphoto(True,icon)
            
            self.bgImage = PhotoImage(file="assets/background.png")
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
            formatted_output = output.replace("\n", "|")[0:-1]
            return formatted_output

        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")
    
class CurrentWindow(Toplevel):

    _last_instance = None

    #def __init__(self, master):
    #    super().__init__(master) #no clue what this does
        

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
        icon = PhotoImage(file="assets/icon.png")
        self.iconphoto(True,icon)
        self.resizable(False, False)
        if bgFile != None:
            print(f"bgFile: {bgFile}")
            self.bgImage = PhotoImage(file=bgFile)
            Label(self, image=self.bgImage).place(x=0,y=0)


    def openFeatureFlagWindow(self):
        self.buildCurrentWindow("Feature Flags","1200x780","assets/test.png")
        
        Button(self,bg="#4AFF00",activebackground="red",text="close",command=self.close).place(x=100,y=0)
        self.mainloop()
    
    
    def close(self):
        self.destroy()

root = Window("McBeiopyll2","400x480")
root.mainloop()
