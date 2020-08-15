# Here some indications, and pre window for begin test( windows questions )
# 
#  from tkinter import *
from tkinter import *
Home = Tk()
#window size
# Home.geometry("950x650")
Home.title('Algunas Indicaciones antes del test')


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

indicationsLabel = Label(frame1, text='Instrucciones : ', bg='#3EB489',width=30)
indicationsLabel.grid(column=3 , row=2)


indicationsBTest= Label(frame1, text='''
    - El siguientes test consta de 10 preguntas.
    - Trate de contestar sinceramente las preguntas para
     poder aproximar mejor el resultado.
    - El test tiene una duración de aproximadamente 5 minutos.
    ''', 
    bg = '#f9f9f9', pady=10,bd=1, anchor=W )
indicationsBTest.grid(column=3, row= 3)

warnLabel= Label(frame1, text='''
    Observación:

    - El siguiente programa *SOLAMENTE aproxima en porcentaje
     si podría o no tener la enfermedad, no reemplaza a exámenes
     o diagnóstico de alguien con estudios de medicina.
    - Si tiene dudas solicite ayuda temprana a su médico de 
     confianza.''', 
    bg = '#f9f9f9', pady=10,bd=1, anchor=W )
warnLabel.grid(column=3, row= 4)

# Buttons
continueBut = Button(frame1, text='Continuar', bg='#428bca', relief=RAISED, width=14, height=1)
continueBut.grid(column=2 , row=5)

exitBut = Button(frame1, text='Salir', bg="#d9534f",fg="#fff", command=Home.quit, width=14, height=1)
exitBut.grid(column=3, row=5)


Home.mainloop()
