from cProfile import label
import tkinter as tk
from tkinter import ttk
import tkinter
from turtle import color


root = tk.Tk()
root.config(width=1360, height=768)
root.title("BIENVENIDO")
frame = tk.Frame(root)
frame.place(x=0, y=0, width=1360, height=768)
frame.config(bg= '#7EADB0')
buttonRegistrar = tk.Button(frame, text="REGISTRARSE",command=root.destroy)
buttonRegistrar.place(x=1200, y=20)
buttonIniciar = tk.Button(frame, text="INICIAR SESION")
buttonIniciar.place(x=1090, y=20)
buttonTerminos = tk.Button(frame, text="TERMINOS Y CONDICIONES")
buttonTerminos.place(x=915, y=20)
buttonInformacion = tk.Button(frame, text="POLITICAS DE PRIVACIDAD")
buttonInformacion.place(x=745, y=20)
buttonContacto = tk.Button(frame, text="CONTACTO")
buttonContacto.place(x=655, y=20)
labelTitulo = tk.Label(frame, text="BIENVENIDO A INNOVATE WITH PROYECTS",font=10,background='#7EADB0')
labelTitulo.place(x=20, y=20)
labelTexto = tk.Label(frame, text="INNOVATE WITH PROYECTS es una aplicacion que te permite como estudiante subir tus iniciativas tecnologicas \n\n"
                      "para que todas aquellas personas interesadas ya sean otros estudiantes, profesores,\n\n" 
                      "empresarios, coordinadores e incluso invitados puedan observar, comentar,\n\n" 
                      "valorar y ponerse en contacto con todas aquellas iniciativas tecnologicas \n\n"
                      "que les llame la atencion \n\n\n"
                      "¡ NO ESPERES MAS !",font=10,background='#7EADB0')
labelTexto.place(x=180, y=360)
buttonIniciativa = tk.Button(frame, text="SUBE TU INICIATIVA TECNOLOGICA", font= "20", bg="#f4a020")
buttonIniciativa.place(x=500, y=690)
logo = tk.PhotoImage(file= "IMAGENES/logo.png")
lbl_img = tk.Label(frame, image = logo)
lbl_img.place(x=560, y=100)
root.mainloop()
