from tkinter import *

def Login_Window_open() :

    Login_window = Tk()
    Login_window.title("Login :")
    Login_window.geometry("1000x1000")
    Login_window.minsize(470,400)
    Login_window.maxsize(470,400)
    Login_window.config(background="#282882")
    Login_frame = Frame(Login_window,bg="#6D6DE3")
    Nom = Label(Login_frame,text="Nom :",font=("Arial",20),width=15,height=1,bg="#6D6DE3",fg="black")
    Nom.grid(row=0,column=0)
    global Nomlogin_entry
    Nomlogin_entry = Entry(Login_frame,font=("Arial",18),bg="white",fg="black",width=25)
    Nomlogin_entry.grid(row=0,column=1)

    #Space
    Space = Label(Login_frame,text="",bg="#6D6DE3",height=1)
    Space.grid(row=1,column=0)

    Pass = Label(Login_frame, text="Mot de passe :", font=("Arial", 20), width=15, height=1, bg="#6D6DE3", fg="black")
    Pass.grid(row=2, column=0)
    global Passlogin_entry
    Passlogin_entry = Entry(Login_frame, font=("Arial", 18), bg="white", fg="black", width=25)
    Passlogin_entry.grid(row=2, column=1)

    # Space
    Space = Label(Login_frame, text="", bg="#6D6DE3", height=1)
    Space.grid(row=4, column=0)

    #Bouton Login
    Login_button = Button(Login_frame,text="Login",font=("Arial",18),bg="white",fg="black")
    Login_button.grid(row=4,column=1)
    Login_frame.pack(expand=YES)
    Login_window.mainloop()

def Inscription_Window_open() :

    Inscription_window = Tk()
    Inscription_window.title("Inscription :")
    Inscription_window.geometry("470x400")
    Inscription_window.minsize(470,400)
    Inscription_window.maxsize(470,400)
    Inscription_window.config(background="#282882")
    Inscription_frame = Frame(Inscription_window,bg="#6D6DE3")
    Nom = Label(Inscription_frame,text="Nom :",font=("Arial",20),width=15,height=1,bg="#6D6DE3",fg="black")
    Nom.grid(row=0,column=0)
    global NomInscrition_entry
    NomInscrition_entry = Entry(Inscription_frame,font=("Arial",18),bg="white",fg="black",width=25)
    NomInscrition_entry.grid(row=0,column=1)

    #Space
    Space = Label(Inscription_frame,text="",bg="#6D6DE3",height=1)
    Space.grid(row=1,column=0)

    Pass = Label(Inscription_frame, text="Mot de passe :", font=("Arial", 20), width=15, height=1, bg="#6D6DE3", fg="black")
    Pass.grid(row=2, column=0)
    global PassInscription_entry
    PassInscription_entry = Entry(Inscription_frame, font=("Arial", 18), bg="white", fg="black", width=25)
    PassInscription_entry.grid(row=2, column=1)

    # Space
    Space = Label(Inscription_frame, text="", bg="#6D6DE3", height=1)
    Space.grid(row=4, column=0)

    #Bouton Login
    Inscription_button = Button(Inscription_frame,text="Inscription",font=("Arial",18),bg="white",fg="black")
    Inscription_button.grid(row=4,column=1)
    Inscription_frame.pack(expand=YES)
    Inscription_window.mainloop()

Menu_window = Tk()
Menu_window.title("Menu :")
Menu_window.geometry("350x175")
Menu_window.minsize(350,175)
Menu_window.maxsize(350,175)
Menu_window.config(background="#007082")
Menu_frame = Frame(Menu_window,width=310,height=135,bg="black")
#Création du bouton Login :
Login_bouton = Button(Menu_frame,text="Login",font=("Arial",20), bg="white",fg="black", width=8, height=3,command=Login_Window_open)
Login_bouton.grid(row=0,column=0)
#Création du bouton Inscription :
Inscription_bouton = Button(Menu_frame,text="Inscription",font=("Arial",20), bg="white",fg="black", width=8, height=3,command=Inscription_Window_open)
Inscription_bouton.grid(row=0,column=1)

Menu_frame.pack(expand=YES)
Menu_window.mainloop()