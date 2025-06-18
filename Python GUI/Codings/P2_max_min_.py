from tkinter import *

ut_root = Tk()

ut_root.geometry("644x434")
      # width * height --Geometry is the default size of the application when it opened

ut_root.minsize(200,100)
      #width,height -- application can be minimized less than this

ut_root.maxsize(1200,988)
      #width,height

step = Label(text="Shakaib is a good boy and this is his GUI")
step.pack()

ut_root.mainloop()