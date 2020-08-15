from tkinter import *

# **** Main
# title
window = Tk()
window.title('My first progam Gui')
#   all whole window background
window.configure(background='black')

# # My photo
# photo1 = PhotoImage(file='me.png')
# label( window, image=photo1, bg='black').grid(comlumn=0, row=0, sticky=E)

# create label
Label( window, text='Ingrese su nombre y correo electronico', bg='black', fg='white', font='none 12 bold').grid(column=0, row=1, sticky=E)

# create a text entry box
textentry = Entry( window, width=20, bg='white')
textentry.grid(row=2, column=0, sticky=W)

# click function
def click():
    enteredText = textentry.get() # collect the text from the text entry box
    # clears the output variable box
    output.delete(0.0, END) 
    # control for errors
    try:
        definition = exampDict[enteredText]
    except:
        definition = 'sorry there is no word like that please try again'
    output.insert(END, definition)

# add a submit button . width value should be like text length
Button( window, text='Submit', width=6, command=click).grid(row=3, column=0, sticky=W )

# another label
Label( window, text='\nDefinition: ', bg='black', fg='white', font='none 12 bold' ) .grid(row=4, column=0, sticky=W)

# create a text box
output = Text( window, width=75, height=6, wrap=WORD, background='white' )
output.grid( row = 5, column=0, columnspan=2, sticky=W )

# dictionary example
exampDict = {
    'algorithm': 'step by step instructions to complete task',
    'bug': 'piece of coude that couses client dont pay you xD'
}

# exit label
Label( window, text='click to exit', bg='black', fg='white', font='none 12 bold' ).grid(row=6, column=0, sticky=W)

# exit function
def closeWindow():
    window.destroy()
    exit()
# add exit button
Button(window, text='Exit', width='14', command=closeWindow ).grid( row=7, column=0, sticky=W )


# keeps window opened
window.mainloop()