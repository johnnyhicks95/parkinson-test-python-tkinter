# index for multiple windows
# primero intenta conectar a tkinter con un alias
# si es tknter en py2 lo importa con mayusculas
try:
    import tkinter as tk                # python 3
    from tkinter import font as tkfont  # python 3
except ImportError:
    import Tkinter as tk     # python 2
    import tkFont as tkfont  # python 2

# modulo para mostrar imagenes
from PIL import ImageTk,Image

# seria la clase padre con la configuracion de la ventana
class MultiWindows(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        # own father properties
        self.geometry('1000x700')
        # window title
        self.title('Universidad Técnica de Ambato  - Facultad de ingeniería en Software')
        # title logo
        self.iconbitmap('public\education-logo.ico')
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (HomePage, Test, Tratamientos):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")
            self.show_frame("HomePage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()  # catches the windows


class HomePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='#5cb85c')
        label = tk.Label(self, text="Página de inicio", font=controller.title_font)
        label.grid(column=0 , row=0)
        # label.pack(side="top", fill="x", pady=10)

        frame1 =tk.Frame(self)
        frame1.grid(row=1, column=0, padx=(50,50), pady=(20,30) )
        frame1.columnconfigure(0 , weight=1)
        frame1.rowconfigure(0 , weight=1)

        # nombre de la universidad
        nameUta = tk.Label(frame1, text='Universidad Técnica de Ambato', 
                        bg='#d9534f', width=40,height=2)
        nameUta.grid(column=2 , row=1)

        appName = tk.Label(frame1, text='Test de Parkinson', bg='#3EB489',width=30)
        appName.grid(column=2 , row=2)

        description= tk.Label(frame1, text='''
            Bienvenido! 
            Este es el proyecto de final de curso de Programacion orientada a objetos 

            Qué es la enfermedad del "Parkinson"?

            Es un trastorno del sistema nervioso central que afecta el 
            movimiento y suele ocasionar temblores.

            Qué hace este programa?

            Esta aplica un test para dar una probabilidad de si usted 
            podría padecer de la enfermedad de Parkinson.''', 
            bg = '#f9f9f9', pady=10,bd=1)
        description.grid(column=2, row= 3)


        authorsNames = tk.Label(frame1, text='''Autores:

        -> Sr. Guamanquispe Johnny      
        -> Srta. López Cristina         

         FISEI-Software © 2020''', 
        # bg = '#f9f9f9', relief=SUNKEN, pady=10,bd=1, anchor=W )
        bg = '#f9f9f9',  pady=10,bd=1 )
        authorsNames.grid(column=0, row=4)

        comments = tk.Label(frame1, text='''*******  Indicaciones  ***********
        ->Empezar el test, click en "Continuar"
        ->Terminar el programa, click en "Salir" ''', 
            # bg = '#f9f9f9', relief=SUNKEN, pady=10,bd=1, anchor=W )
            bg = '#f9f9f9',  pady=10,bd=1 )
        comments.grid(column=3, row=4)

        # Buttons
        # continueBut = tk.Button(self, text='Continuar', bg='#428bca',  width=14, height=1)
        # continueBut.grid(column=1 , row=5)

        # exitBut = tk.Button(frame1, text='Salir', bg="#d9534f",fg="#fff", command=self.destroy(), width=14, height=1)
        exitBut = tk.Button(self, text='Salir', bg="#d9534f",fg="#fff",command=self.quit , width=14, height=1)
        exitBut.grid(column=0, row=7)

        button1 = tk.Button(self, text="Ir a 'Cuestionaro'",
                            command=lambda: controller.show_frame("Test"))
        button2 = tk.Button(self, text="Ver 'Tratamientos'",
                            command=lambda: controller.show_frame("Tratamientos"))
        button1.grid(column=0, row=5)
        button2.grid(column=0, row=6)
        # button1.pack()
        # button2.pack()

# **********************8
#  Preguntas del test

def ventanaDos():
    print("ventana 2 en consola")

def ventanaUno():
    newWindow = tk.Toplevel()
    pregunta = tk.Label(newWindow, text= " Pregunta N° 1 ")
    pregunta.grid(column=2 , row=0)

    imagen1 = ImageTk.PhotoImage(Image.open("public\pregunta1.jpeg"))
    cuadro1 = tk.Label(image=imagen1)
    pregunta.grid(column=2 , row=1)

    preguntas = tk.Label(newWindow, text= " ¿Ha notado temblor en sus dedos, manos, mentón o labios? ")
    preguntas.grid(column=2 , row=3)
    respuesta= tk.Radiobutton(newWindow, text='Si', value=1)
    respuestaDos= tk.Radiobutton(newWindow, text='No', value=2)
    respuesta.grid(column=2 , row=4)
    respuestaDos.grid(column=2 , row=5)
    continueBut= tk.Button(newWindow, text='Continuar' , bg='#428bca',command=ventanaDos)
    continueBut.grid(column=3 , row=5)
    # buttonQuit = tk.Button(newWindow,bg="#d9534f" ,fg="#fff", text="Cerrar test", command=self.quit)
    buttonQuit = tk.Button(newWindow,bg="#d9534f" ,fg="#fff", text="Cerrar test")
    buttonQuit.grid(column=4 , row=5)

class Test(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='#5cb85c')
        label = tk.Label(self, text="Empezemos el test", font=controller.title_font, bg="#5bc0de")
        label.grid(row=0, column=2)
        # label.pack(side="top", fill="x", pady=10)

            # windows content
        description = tk.Label(self, text='''
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
            bg = '#f9f9f9', pady=10,bd=1 )
        description.grid(column=2, row= 1)
        continueBut= tk.Button(self, text='Continuar' , bg='#428bca',command=ventanaUno, width=20 )
        continueBut.grid(column=2 , row=3)
        # buttonQuit = Button(newWindow,bg="#d9534f" ,fg="#fff", text="Cerrar programa", command=ventana.quit)
        # buttonQuit.grid(column=2 , row=6)       

        # bu8ttona
        button = tk.Button(self, text="Ir a Página de inicio",
                           command=lambda: controller.show_frame("HomePage"), bg="#428bca")
        button.grid(column=0, row=4)
        exitBut = tk.Button(self, text='Salir', bg="#d9534f",fg="#fff",command=self.quit , width=14, height=1)
        exitBut.grid(column=1, row=4)


class Tratamientos(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='#5bc0de')

        label = tk.Label(self, text="El diagnóstico temprano le puede ayudar a tener una vida más larga y saludable.", font=controller.title_font)
        label.grid(row=0, column=0)
        # label.pack(side="top", fill="x", pady=10)


                    # windows content
        descriptionTreatment = tk.Label(self, text='''
        Hable con su médico para desarrollar un plan de cuidado, el cual puede incluir lo siguiente:

        
        ->Evaluación de un neurólogo, el cual es un médico especializado en el cerebro, 
        para que le haga una evaluación completa sobre sus síntomas.

        ->Evaluación y atención de un terapista ocupacional, terapista físico y/o terapista de lenguaje.

        ->Consulta con un trabajador social

        ->Comience una rutina de ejercicio para retardar el avance de síntomas más severos.

        ->Hable con sus familiares y amigos quien le pueden brindar el apoyo que usted necesita.''', 
            bg = '#f9f9f9', pady=10,bd=1 )
        descriptionTreatment.grid(column=0, row= 1)
        button = tk.Button(self, text="Ir a Página de inicio",
                           command=lambda: controller.show_frame("HomePage"))
        # button.pack()
        button.grid(row=2, column=0)

if __name__ == "__main__":
    app = MultiWindows()
    app.mainloop()