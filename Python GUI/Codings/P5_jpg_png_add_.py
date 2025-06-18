from tkinter import *
from PIL import Image, ImageTk
import os


bob_root = Tk()
bob_root.title("Image Viewer")
bob_root.geometry("955x944")


image_path = "../Images/2.jpg" 


if not os.path.exists(image_path):
    print("Image file not found:", os.path.abspath(image_path))
else:
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)

    
    arun_label = Label(bob_root, image=photo)
    arun_label.pack()

    
    arun_label.image = photo


bob_root.mainloop()
