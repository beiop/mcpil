import tkinter as tk
from tkextrafont import Font

window = tk.Tk()
font = Font(file="assets\mojangles.ttf", family="mojangles")
tk.Label(window, text="Hello", font=font).pack()
window.mainloop()