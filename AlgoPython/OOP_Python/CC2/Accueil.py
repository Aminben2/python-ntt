from tkinter import *
from tkinter import messagebox
from tkinter.font import Font

screen = Tk()
screen.title("App")
screen.geometry('600x500')
screen.config(bg='white')
PoppinsBig = Font(
    family='poppins',
    size=30,
    weight='bold'
)
PoppinsNormal = Font(
    family='poppins',
    size=17,
    weight='normal'
)
PoppinsSmall = Font(
    family='poppins',
    size=12,
    weight='bold'
)


Label(screen, text='Hello Everyone!',
      bg='#fff', font=('Poppins', 50, 'bold')).pack(expand=True)
screen.mainloop()
