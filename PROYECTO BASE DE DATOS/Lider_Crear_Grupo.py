from cProfile import label
from cgitb import text
from optparse import Values
import tkinter as tk
from tkinter import CENTER, LEFT, ttk
from tkinter import font
from turtle import color, left, position
import tkinter.font as tkFont
from tkinter import *

Lider_Crear_Grupo = tk.Tk()
Lider_Crear_Grupo.config(width=1360, height=768, bg= '#7EADB0')
Lider_Crear_Grupo.title("ESTUDIANTE LIDER - CREAR GRUPO")
BienvenidaLabel_Lider_Grupo = tk.Label(Lider_Crear_Grupo, text="BIENVENIDO A \nINNOVATE WITH \nPROYECTS",font=10,background='#7EADB0',justify=LEFT).place(x=20, y=20)
FontLabel_Lider_Grupo = tkFont.Font(size = 20, weight= "bold")
TextoLabel_Lider_Grupo = tk.Label(Lider_Crear_Grupo,text="BIENVENIDO LIDER",font=FontLabel_Lider_Grupo,background='#7EADB0',justify=CENTER).place(x=500, y=50)

# ESTUDIANTES
FontText_Lider_Grupo = tkFont.Font(size = 15, weight= "bold")
FontText_Lider_Grupo2 = tkFont.Font(size = 13)
Administrar_Lider_Grupo = tk.Label(Lider_Crear_Grupo, text="AGREGAR ESTUDIANTES A LA INICIATIVA:",font=FontText_Lider_Grupo,background='#7EADB0').place(x=300, y=150)
Buscar_Lider_Grupo = tk.Label(Lider_Crear_Grupo, text="BUSCAR USUARIO\nPOR MEDIO DE ID:",background='#7EADB0', font=FontText_Lider_Grupo2).place(x=300, y=220)
TexBox_Buscar_Lider_Grupo = tk.Entry(Lider_Crear_Grupo, width=100,background="#D9D9D9").place(x=490, y=230)
Participantes_Lider_Grupo = tk.Label(Lider_Crear_Grupo, text="PARTICIPANTES EN LA INICIATIVA:",font=FontText_Lider_Grupo,background='#7EADB0').place(x=300, y=400)
#LIST BOX
Estudiantes_Lider_Grupo = Listbox(Lider_Crear_Grupo, width=100, bg="#D9D9D9")
Estudiantes_Lider_Grupo.pack()
Estudiantes_Lider_Grupo.insert(0,"ESTUDIANTE #1", "ESTUDIANTE #2")
Estudiantes_Lider_Grupo.place(x=300, y=450)
# BOTONES

Agregar_Lider_Grupo = tk.Button(text="AGREGAR", font=15, bg= "#f4a020", width=20).place(x=400, y=300)
Eliminar_Lider_Grupo = tk.Button(text="ELIMINAR", font=15, bg= "#f4a020", width=20).place(x=800, y=300)


Lider_Crear_Grupo.mainloop()