#malpractice
from tkinter import *
import subprocess

class Window(Tk):

    def __init__(self,title,geometry):
        super().__init__()
        self.geometry(geometry)
        self.title(title)
        icon = PhotoImage(file="assets/icon.png")
        self.iconphoto(True,icon)
        self.resizable(False, False)
        self.bg_image = PhotoImage(file="assets/background.png")
        Label(self, image=self.bg_image).place(x=0,y=0)

        Button(self,bg="#4AFF00",activebackground="red",text="Launch",command=self.launch).place(x=0,y=0)
        Button(self,bg="#4AFF00",activebackground="red",text="Feature Flags",command=self.launch).place(x=0,y=30)

    def cook(self):
        self.mainloop()
    
    
    def launch(self):
        #command = ["flatpak", "run", "com.thebrokenrail.MCPIReborn"]
        command = ["./minecraft-pi-reborn-3.0.0-amd64.AppImage"]
        self.destroy()
        try:
            # Execute the Flatpak command
            subprocess.run(command, check=True)
            print(f"Successfully launched")
            
        except subprocess.CalledProcessError as e:
            print(f"Error running Flatpak app: {e}")

class CurrentWindow(Tk):
    #def __init__(self):
    #    super().__init__() #Not sure where to put this
    def buildCurrentWindow(self,title,geometry):
        #destroy current window if it exists
        #try:
        #    self.destroy()
        #except AttributeError:
        #    pass
        #create new window
        
        self.geometry(geometry)
        self.title(title)
        #icon = PhotoImage(file="assets/icon.png")
        #self.iconphoto(True,icon)
        self.resizable(False, False)
        #self.bg_image = PhotoImage(file="assets/background.png")
        #Label(self, image=self.bg_image).place(x=0,y=0)


    def openFeatureFlagWindow(self):
        self.buildCurrentWindow("Feature Flags","400x480")
        
        Button(self,bg="#4AFF00",activebackground="red",text="close",command=self.close).place(x=0,y=0)
        self.destroy()
        self.mainloop()

    
    
    def close(self):
        self.destroy

root = Window("McBeiopyll2","400x480")
#CurrentWindow.openFeatureFlagWindow(CurrentWindow("400x40"))
root.cook()