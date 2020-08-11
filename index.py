# main file for app

# imports
from tkinter import *
from PIL import ImageTk,Image

# root tkinter instance
root = Tk()
# window title
root.title('Universidad Técnica de Ambato  - Facultad de ingeniería en Software')
# title logo
root.iconbitmap('public\education-logo.ico')
#window size
root.geometry("950x650")


# header title
frame = LabelFrame(root, text='Facultad de ingeniería en Sistemas, Electrónica e Industrial')
frame.pack(padx=10, pady=20)

logouta = ImageTk.PhotoImage(Image.open("public\escudo-uta.png"))
my_logo = Label(frame, image=logouta)
my_logo.pack()
#my_logo.grid(row=1, column=0)

# tsecond title
appTitle = Label(frame, text='"Test para anticipar el Parkinson"', bg='#3EB489')
appTitle.pack()

description= Label(frame, text=''''
    Proyecto de final de curso de Programacion orientada a objetos 

    Qué es la enfermedad del "Parkinson"?
    Es un trastorno del sistema nervioso central que afecta el movimiento y suele ocasionar temblores.

    Qué hace este programa?
    Esta aplica un test para dar una probabilidad de si usted padeceria de la enfermedad de Parkinson.


  ''', bg = '#428bca', pady=10,bd=1, anchor=W )
description.pack()

authorsNames = Label(frame, text=''''
    Autores:

    -> Sr. Guamanquispe Johnny
    -> Srta. López Cristina

    © 2020
  ''', bg = '#f9f9f9', relief=SUNKEN, pady=10,bd=1, anchor=W )
authorsNames.pack()
# more code here !! xD
# ....



# control buttons
continueBut= Button(root, text='Continuar', bg='#428bca', relief=RAISED)
# continueBut.grid(row=1, column=0)
continueBut.pack()

# button: closes program
buttonQuit = Button(root,bg="#d9534f",fg="#fff", text="Cerrar programa", command=root.quit)
# buttonQuit.grid(row=1, column=1)
buttonQuit.pack()

# keeps open execution
root.mainloop()