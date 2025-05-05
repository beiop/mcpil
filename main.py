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

    def cook(self):
        self.mainloop()
    
    
    def launch(self):
        #command = ["flatpak", "run", "com.thebrokenrail.MCPIReborn"]
        command = ["/home/beiop/Downloads/minecraft-pi-reborn-client-2.5.4-amd64.AppImage"]
        self.destroy()
        try:
            # Execute the Flatpak command
            subprocess.run(command, check=True)
            print(f"Successfully launched")
            
        except subprocess.CalledProcessError as e:
            print(f"Error running Flatpak app: {e}")

class Current

root = Window("McBeiopyll2","400x480")

root.cook()
