from cProfile import label
from cgitb import text
import tkinter as tk
from tkinter import CENTER, LEFT, ttk
from tkinter import font
from turtle import color, left, position
import tkinter.font as tkFont

Inicio_roles = tk.Tk()
Inicio_roles.config(width=1360, height=768, bg= '#7EADB0')
Inicio_roles.title("INICIO DE SESION")
BienvenidaLabel = tk.Label(Inicio_roles, text="BIENVENIDO A \nINNOVATE WITH\nPROYECTS",font=10,background='#7EADB0',justify=LEFT)
BienvenidaLabel.place(x=20, y=20)
FontLabel = tkFont.Font(size = 20, weight= "bold")
TextoLabel = tk.Label(Inicio_roles,text="ELIGA SU TIPO DE USUARIO\nPARA INGRESAR AL APLICATIVO",font=FontLabel,background='#7EADB0',justify=CENTER)
TextoLabel.place(x=450, y=100)

# IMAGENES

estudiante = tk.PhotoImage(file= "IMAGENES/estudiante.png")
lbl_estu = tk.Label(Inicio_roles, image = estudiante)
lbl_estu.place(x=200, y=200)

admin = tk.PhotoImage(file= "IMAGENES/administrador.png")
lbl_admin = tk.Label(Inicio_roles, image = admin)
lbl_admin.place(x=550, y=200)

coordinador = tk.PhotoImage(file= "IMAGENES/coordinador.png")
lbl_coordinador = tk.Label(Inicio_roles, image = coordinador)
lbl_coordinador.place(x=900, y=200)

# BOTONES

Estudiante_btn = tk.Button(Inicio_roles, text = "ESTUDIANTE", font=20)
Estudiante_btn.place(x=240, y=450)

Administrador_btn = tk.Button(Inicio_roles, text = "ADMINISTRADOR", font=20)
Administrador_btn.place(x=575, y=450)

Coordinador_btn = tk.Button(Inicio_roles, text = "COORDINADOR", font=20)
Coordinador_btn.place(x=930, y=450)

Invitado_btn = tk.Button(Inicio_roles, text = "INGRESAR COMO INVITADO", font=30)
Invitado_btn.place(x=525, y=550)
Inicio_roles.mainloop()



