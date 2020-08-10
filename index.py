# main file for app

# imports
from tkinter import *
from PIL import ImageTk,Image

# root tkinter instance
root = Tk()
# window title
root.title('Universidad Técnica de Ambato  - Test de parkinson')
# title logo
root.iconbitmap('public\education-logo.ico')


# in frame
logouta = ImageTk.PhotoImage(Image.open("public\escudo-uta.png"))
my_logo = Label(image=logouta)
my_logo.pack()

# more code here !! xD
# ....


# button: closes program
button_quit = Button(root,bg="#d9534f",fg="#fff", text="Cerrar programa", command=root.quit)
button_quit.pack()

# keeps open execution
root.mainloop()