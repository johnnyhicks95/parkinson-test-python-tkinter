from tkinter import *
from PIL import ImageTk,Image

def tratamiento():
    newWindow = Toplevel(ventana)
    trata=Label(newWindow, text='''
         Tratamiento! 
         ++++++++++++++++++++++++++++++++++++++++++++ 

         ++++++++++++++++++++++++++++++++++++++++++++

         +++++++++++++++++++++++++++++++++++++++++++++++++
         ++++++++++++++++++++++++++++++++++++++++++++++++

         ++++++++++++++++++++++++++++++

         ++++++++++++++++++++++++++++++++++++++++++++++
         +++++++++++++++++++++++++++++++++++++++++++.''', 
         bg = '#f9f9f9', pady=10,bd=1, anchor=W )
    trata.grid(column=2, row= 3)
    buttonQuit = Button(newWindow,bg="#d9534f" ,fg="#fff", text="Cerrar programa", command= ventana.quit)
    buttonQuit.grid(column=3, row=5)

def diagnostico():
    newWindow = Toplevel(ventana)
    diag=Label(newWindow, text='''
         Diagnóstico! 
         ++++++++++++++++++++++++++++++++++++++++++++ 

         ++++++++++++++++++++++++++++++++++++++++++++

         +++++++++++++++++++++++++++++++++++++++++++++++++
         ++++++++++++++++++++++++++++++++++++++++++++++++

         ++++++++++++++++++++++++++++++

         ++++++++++++++++++++++++++++++++++++++++++++++
         +++++++++++++++++++++++++++++++++++++++++++.''', 
         bg = '#f9f9f9', pady=10,bd=1, anchor=W )
    diag.grid(column=2, row= 3)

    continueBut= Button(newWindow, text='Continuar' , bg='#428bca', command= tratamiento)
    continueBut.grid(column=2 , row=5)
    buttonQuit = Button(newWindow,bg="#d9534f" ,fg="#fff", text="Cerrar programa", command= ventana.quit)
    buttonQuit.grid(column=3, row=5)

def ventanaDiez():
    newWindow = Toplevel(ventana)
    pregunta = Label(newWindow, text= " Pregunta N° 10")
    pregunta.pack()
    preguntas = Label(newWindow, text= " ¿Le han dicho que su voz es baja o que usted suena ronco cuando habla?  ")
    preguntas.pack()
    respuesta= Radiobutton(newWindow, text='Si', value=1)
    respuestaDos= Radiobutton(newWindow, text='No', value=2)
    respuesta.pack()
    respuestaDos.pack()
    continueBut= Button(newWindow, text='Continuar' , bg='#428bca',command=diagnostico)
    continueBut.pack()
    buttonQuit = Button(newWindow,bg="#d9534f" ,fg="#fff", text="Cerrar programa", command= ventana.quit)
    buttonQuit.pack()

def ventanaNueve():
    newWindow = Toplevel(ventana)
    pregunta = Label(newWindow, text= " Pregunta N° 9 ")
    pregunta.pack()
    preguntas = Label(newWindow, text= " ¿Siente rigidez en su cuerpo, brazos o piernas? ")
    preguntas.pack()
    respuesta= Radiobutton(newWindow, text='Si', value=1)
    respuestaDos= Radiobutton(newWindow, text='No', value=2)
    respuesta.pack()
    respuestaDos.pack()
    continueBut= Button(newWindow, text='Continuar' , bg='#428bca',command=ventanaDiez)
    continueBut.pack()
    buttonQuit = Button(newWindow,bg="#d9534f" ,fg="#fff", text="Cerrar programa", command= ventana.quit)
    buttonQuit.pack()

def ventanaOcho():
    newWindow = Toplevel(ventana)
    pregunta = Label(newWindow, text= " Pregunta N° 8 ")
    pregunta.pack()
    preguntas = Label(newWindow, text= " ¿Le han comentado que usted se ve enojado, serio o deprimido, aun cuando usted no está de mal humor? ")
    preguntas.pack()
    respuesta= Radiobutton(newWindow, text='Si', value=1)
    respuestaDos= Radiobutton(newWindow, text='No', value=2)
    respuesta.pack()
    respuestaDos.pack()
    continueBut= Button(newWindow, text='Continuar' , bg='#428bca',command=ventanaNueve)
    continueBut.pack()
    buttonQuit = Button(newWindow,bg="#d9534f" ,fg="#fff", text="Cerrar programa", command= ventana.quit)
    buttonQuit.pack()

def ventanaSiete():
    newWindow = Toplevel(ventana)
    pregunta = Label(newWindow, text= " Pregunta N° 7 ")
    pregunta.pack()
    preguntas = Label(newWindow, text= " ¿Siente usted que se marea cuando se levanta de una silla o de su cama? ")
    preguntas.pack()
    respuesta= Radiobutton(newWindow, text='Si', value=1)
    respuestaDos= Radiobutton(newWindow, text='No', value=2)
    respuesta.pack()
    respuestaDos.pack()
    continueBut= Button(newWindow, text='Continuar' , bg='#428bca',command=ventanaOcho)
    continueBut.pack()
    buttonQuit = Button(newWindow,bg="#d9534f" ,fg="#fff", text="Cerrar programa", command= ventana.quit)
    buttonQuit.pack()

def ventanaSeis():
    newWindow = Toplevel(ventana)
    pregunta = Label(newWindow, text= " Pregunta N° 6 ")
    pregunta.pack()
    preguntas = Label(newWindow, text= " ¿Ha notado que ya no puede oler ciertos alimentos igual que antes? ")
    preguntas.pack()
    respuesta= Radiobutton(newWindow, text='Si', value=1)
    respuestaDos= Radiobutton(newWindow, text='No', value=2)
    respuesta.pack()
    respuestaDos.pack()
    continueBut= Button(newWindow, text='Continuar' , bg='#428bca',command=ventanaSiete)
    continueBut.pack()
    buttonQuit = Button(newWindow,bg="#d9534f" ,fg="#fff", text="Cerrar programa", command= ventana.quit)
    buttonQuit.pack()

def ventanaCinco():
    newWindow = Toplevel(ventana)
    pregunta = Label(newWindow, text= " Pregunta N° 5 ")
    pregunta.pack()
    preguntas = Label(newWindow, text= " ¿Ha disminuido el tamaño de su escritura y junta más las palabras? ")
    preguntas.pack()
    respuesta= Radiobutton(newWindow, text='Si', value=1)
    respuestaDos= Radiobutton(newWindow, text='No', value=2)
    respuesta.pack()
    respuestaDos.pack()
    continueBut= Button(newWindow, text='Continuar' , bg='#428bca',command=ventanaSeis)
    continueBut.pack()
    buttonQuit = Button(newWindow,bg="#d9534f" ,fg="#fff", text="Cerrar programa", command= ventana.quit)
    buttonQuit.pack()

def ventanaCuatro():
    newWindow = Toplevel(ventana)
    pregunta = Label(newWindow, text= " Pregunta N° 4 ")
    pregunta.pack()
    preguntas = Label(newWindow, text= " ¿Ha notado que la forma en que usted escribe las palabras ha cambiado? ")
    preguntas.pack()
    respuesta= Radiobutton(newWindow, text='Si', value=1)
    respuestaDos= Radiobutton(newWindow, text='No', value=2)
    respuesta.pack()
    respuestaDos.pack()
    continueBut= Button(newWindow, text='Continuar' , bg='#428bca',command=ventanaCinco)
    continueBut.pack()
    buttonQuit = Button(newWindow,bg="#d9534f" ,fg="#fff", text="Cerrar programa", command= ventana.quit)
    buttonQuit.pack()

def ventanaTres():
    newWindow = Toplevel(ventana)
    pregunta = Label(newWindow, text= " Pregunta N° 3 ")
    pregunta.pack()
    preguntas = Label(newWindow, text= " ¿Ha notado que su escritura es mas pequeña que en el pasado? ")
    preguntas.pack()
    respuesta= Radiobutton(newWindow, text='Si', value=1)
    respuestaDos= Radiobutton(newWindow, text='No', value=2)
    respuesta.pack()
    respuestaDos.pack()
    continueBut= Button(newWindow, text='Continuar' , bg='#428bca',command=ventanaCuatro)
    continueBut.pack()
    buttonQuit = Button(newWindow,bg="#d9534f" ,fg="#fff", text="Cerrar programa", command= ventana.quit)
    buttonQuit.pack()

def ventanaDos():
    newWindow = Toplevel(ventana)
    pregunta = Label(newWindow, text= " Pregunta N° 2 ")
    pregunta.pack()
    preguntas = Label(newWindow, text= " ¿Le tiembla la pierna cuando se sienta o se relaja?  ")
    preguntas.pack()
    respuesta= Radiobutton(newWindow, text='Si', value=1)
    respuestaDos= Radiobutton(newWindow, text='No', value=2)
    respuesta.pack()
    respuestaDos.pack()
    continueBut= Button(newWindow, text='Continuar' , bg='#428bca',command=ventanaTres)
    continueBut.pack()
    buttonQuit = Button(newWindow,bg="#d9534f" ,fg="#fff", text="Cerrar programa", command= ventana.quit)
    buttonQuit.pack()
    
    

def ventanaUno():
    newWindow = Toplevel(ventana)
    pregunta = Label(newWindow, text= " Pregunta N° 1 ")
    pregunta.grid(column=2 , row=0)
    preguntas = Label(newWindow, text= " ¿Ha notado temblor en sus dedos, manos, mentón o labios? ")
    preguntas.grid(column=2 , row=1)
    respuesta= Radiobutton(newWindow, text='Si', value=1)
    respuestaDos= Radiobutton(newWindow, text='No', value=2)
    respuesta.grid(column=2 , row=2)
    respuestaDos.grid(column=2 , row=3)
    continueBut= Button(newWindow, text='Continuar' , bg='#428bca',command=ventanaDos)
    continueBut.grid(column=2 , row=5)
    buttonQuit = Button(newWindow,bg="#d9534f" ,fg="#fff", text="Cerrar programa", command=ventana.quit)
    buttonQuit.grid(column=2 , row=6)


def instrucciones():
    newWindow = Toplevel(ventana)
    description = Label(newWindow, text='''
         Instrucciones! 
         ++++++++++++++++++++++++++++++++++++++++++++ 

         ++++++++++++++++++++++++++++++++++++++++++++

         +++++++++++++++++++++++++++++++++++++++++++++++++
         ++++++++++++++++++++++++++++++++++++++++++++++++

         ++++++++++++++++++++++++++++++

         ++++++++++++++++++++++++++++++++++++++++++++++
         +++++++++++++++++++++++++++++++++++++++++++.''', 
         bg = '#f9f9f9', pady=10,bd=1, anchor=W )
    description.grid(column=2, row= 3)
    continueBut= Button(newWindow, text='Continuar' , bg='#428bca',command=ventanaUno )
    continueBut.grid(column=2 , row=5)
    buttonQuit = Button(newWindow,bg="#d9534f" ,fg="#fff", text="Cerrar programa", command=ventana.quit)
    buttonQuit.grid(column=2 , row=6)
    ventana.iconify()

# root tkinter instance
ventana = Tk()
# window title
ventana.title('Universidad Técnica de Ambato  - Facultad de ingeniería en Software')
# title logo
ventana.iconbitmap('public\education-logo.ico')
# ventana.title('Home screen')

frame1 =Frame(ventana)
frame1.grid(row=0, column=0, padx=(50,50), pady=(20,30))
frame1.columnconfigure(0 , weight=1)
frame1.rowconfigure(0 , weight=1)
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

comments =Label(frame1, text='''*******  Indicaciones ***********
->Empezar el test, click en "Continuar"
->Terminar el programa, click en "Salir" ''', 
    bg = '#f9f9f9', relief=SUNKEN, pady=10,bd=1, anchor=W )
comments.grid(column=3, row=4)

# Buttons
continueBut = Button(frame1, text='Continuar', bg='#428bca', width=14, height=1, command= instrucciones )
continueBut.grid(column=2 , row=5)

exitBut = Button(frame1, text='Salir', bg="#d9534f",fg="#fff", command=ventana.quit, width=14, height=1)
exitBut.grid(column=3, row=5)

ventana.mainloop()