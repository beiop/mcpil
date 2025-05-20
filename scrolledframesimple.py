from scrollable import ScrollFrame
from tkinter import *

root = Tk()

scrollFrame = ScrollFrame(root)  # add a new scrollable frame.

# Now add some controls to the scrollframe.
# NOTE: the child controls are added to the view port (scrollFrame.viewPort, NOT scrollframe itself)
def close():
    root.destroy()

sf = scrollFrame.viewPort
Button(sf, text="Close", command=close).pack()

# when packing the scrollframe, we pack scrollFrame itself (NOT the viewPort)
scrollFrame.pack(side="top", fill="both", expand=True)

root.mainloop()

from scrollable import ScrollFrame
scrollFrame = ScrollFrame(root)  # add a new scrollable frame.
sf = scrollFrame.viewPort
scrollFrame.pack(side="top", fill="both", expand=True)