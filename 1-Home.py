from tkinter import *

Home = Tk()
#window size
# Home.geometry("950x650")
Home.title('Home screen')

# label1 = Label(Home, width='20', height='3', bg='red', text='Hello')
# label2 = Label(Home, width='20', height='3', bg='green', text='world')

# label1.grid(row=0, column = 1)
# label2.grid(row=0, column = 6)

frame1 =Frame(Home)
frame1.grid(row=0, column=0, padx=(50,50), pady=(20,30) )
frame1.columnconfigure(0 , weight=1)
frame1.rowconfigure(0 , weight=1)

# nombre de la universidad
nameUta = Label(frame1, text='Universidad Técnica de Ambato', 
                bg='#5cb85c', width=40,height=2)
nameUta.grid(column=2 , row=1)

appName = Label(frame1, text='Test de Parkinson', bg='#3EB489',width=30)
appName.grid(column=2 , row=2)

description= Label(frame1, text='''
    Bienvenido! 
    Este es el proyecto de final de curso de Programacion orientada a objetos 

    Qué es la enfermedad del "Parkinson"?

    Es un trastorno del sistema nervioso central que afecta el 
    movimiento y suele ocasionar temblores.

    Qué hace este programa?

    Esta aplica un test para dar una probabilidad de si usted 
    podría padecer de la enfermedad de Parkinson.''', 
    bg = '#f9f9f9', pady=10,bd=1, anchor=W )
description.grid(column=2, row= 3)


authorsNames = Label(frame1, text='''Autores:

-> Sr. Guamanquispe Johnny      
-> Srta. López Cristina         

FISEI-Software © 2020''', bg = '#f9f9f9', relief=SUNKEN, pady=10,bd=1, anchor=W )
authorsNames.grid(column=0, row=4)

comments =Label(frame1, text='''*******  Indicaciones  ***********
->Empezar el test, click en "Continuar"
->Terminar el programa, click en "Salir" ''', 
    bg = '#f9f9f9', relief=SUNKEN, pady=10,bd=1, anchor=W )
comments.grid(column=3, row=4)

# Buttons
continueBut = Button(frame1, text='Continuar', bg='#428bca', relief=RAISED, width=14, height=1)
continueBut.grid(column=2 , row=5)

exitBut = Button(frame1, text='Salir', bg="#d9534f",fg="#fff", command=Home.quit, width=14, height=1)
exitBut.grid(column=3, row=5)


Home.mainloop()