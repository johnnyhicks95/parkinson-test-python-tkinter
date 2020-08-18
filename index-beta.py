# index for multiple windows
# primero intenta conectar a tkinter con un alias
# si es tknter en py2 lo importa con mayusculas
try:
    import tkinter as tk                # python 3
    from tkinter import font as tkfont  # python 3
except ImportError:
    import Tkinter as tk     # python 2
    import tkFont as tkfont  # python 2

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


def ventanaUno():
    print('Ventana uno en consola')

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
        label = tk.Label(self, text="Aquí son los tratamientos", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Ir a Página de inicio",
                           command=lambda: controller.show_frame("HomePage"))
        button.pack()


if __name__ == "__main__":
    app = MultiWindows()
    app.mainloop()