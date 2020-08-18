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
root.geometry("800x600")



# ************
# New window class - config
# class SampleApp(tk.Tk):

#     def __init__(self, *args, **kwargs):
#         tk.Tk.__init__(self, *args, **kwargs)

#         self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

#         # the container is where we'll stack a bunch of frames
#         # on top of each other, then the one we want visible
#         # will be raised above the others
#         container = tk.Frame(self)
#         container.pack(side="top", fill="both", expand=True)
#         container.grid_rowconfigure(0, weight=1)
#         container.grid_columnconfigure(0, weight=1)

#         self.frames = {}
#         for F in (StartPage, PageOne, PageTwo):
#             page_name = F.__name__
#             frame = F(parent=container, controller=self)
#             self.frames[page_name] = frame

#             # put all of the pages in the same location;
#             # the one on the top of the stacking order
#             # will be the one that is visible.
#             frame.grid(row=0, column=0, sticky="nsew")
#             self.show_frame("StartPage")

#     def show_frame(self, page_name):
#         '''Show a frame for the given page name'''
#         frame = self.frames[page_name]
#         frame.tkraise()



# *******************
# Functions 
def hola():
    print ("Hola!")

def ventanaTres():
    pass
    print('Ventana 3')

def ventanaDos():
    newWindow = Toplevel(root)
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
    buttonQuit = Button(newWindow,bg="#d9534f" ,fg="#fff", text="Cerrar programa", command= root.quit)
    buttonQuit.pack()

def ventanaUno():
    newWindow = Toplevel(root)
    newWindow.config(width=600, height=400)
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
    buttonQuit = Button(newWindow,bg="#d9534f" ,fg="#fff", text="Cerrar programa", command=root.quit)
    buttonQuit.grid(column=2 , row=6)


def instrucciones():
    newWindow = Toplevel(root)
    newWindow.config(width=600, height=400)
    description = Label(newWindow, text='''
         Instrucciones! 

    - El siguientes test consta de 10 preguntas.
    - Trate de contestar sinceramente las preguntas para
     poder aproximar mejor el resultado.
    - El test tiene una duración de aproximadamente 5 minutos.

    Observación:

    - El siguiente programa *SOLAMENTE aproxima en porcentaje
     si podría o no tener la enfermedad, no reemplaza a exámenes
     o diagnóstico de alguien con estudios de medicina.
    - Si tiene dudas solicite ayuda temprana a su médico de 
     confianza''', 
         bg = '#f9f9f9', pady=10,bd=1, anchor=W )
    description.grid(column=2, row= 3)
    continueBut= Button(newWindow, text='Continuar' , bg='#428bca',command=ventanaUno )
    continueBut.grid(column=2 , row=5)
    buttonQuit = Button(newWindow,bg="#d9534f" ,fg="#fff", text="Cerrar programa", command=root.quit)
    buttonQuit.grid(column=2 , row=6)
    root.iconify()

# End Functions
# *************************


# Crear el menu principal
navMenu = Menu(root)


# Crea un menu desplegable y lo agrega al menu barra
fileMenu = Menu(navMenu, tearoff=0)
fileMenu.add_command(label="Ir a Home", command=hola)
fileMenu.add_command(label="Ver estadísticas", command=hola)
fileMenu.add_separator()
fileMenu.add_command(label="Salir", command=root.quit)
navMenu.add_cascade(label="Archivo", menu=fileMenu)

# Crea dos menus desplegables mas
menuEdit = Menu(navMenu, tearoff=0)
menuEdit.add_command(label="Instrucciones", command=instrucciones)
menuEdit.add_command(label="Pregunta 1", command=ventanaUno)
menuEdit.add_command(label="Pregunta 2", command=ventanaDos)
menuEdit.add_command(label="Pregunta 3", command=hola)
menuEdit.add_command(label="Pregunta 4", command=hola)
menuEdit.add_command(label="Pregunta 5", command=hola)
menuEdit.add_command(label="Pregunta 6", command=hola)
menuEdit.add_command(label="Pregunta 7", command=hola)
menuEdit.add_command(label="Pregunta 8", command=hola)
menuEdit.add_command(label="Pregunta 9", command=hola)
menuEdit.add_command(label="Pregunta 10", command=hola)
navMenu.add_cascade(label="Cuestionario", menu=menuEdit)
menuayuda = Menu(navMenu, tearoff=0)
menuayuda.add_command(label="Ver tratamientos...", command=hola)
navMenu.add_cascade(label="Más sobre ...", menu=menuayuda)

# Mostrar el menu
root.config(menu=navMenu)

# Mostrar la ventana
root.mainloop()