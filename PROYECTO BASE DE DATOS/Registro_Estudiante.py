from cProfile import label
from cgitb import text
import tkinter as tk
from tkinter import CENTER, LEFT, ttk
from tkinter import font
from turtle import color, left, position
import tkinter.font as tkFont

Registro_estudiantes = tk.Tk()
Registro_estudiantes.config(width=1360, height=768, bg= '#7EADB0')
Registro_estudiantes.title("REGISTRO ESTUDIANTES")
BienvenidaLabel_Estu = tk.Label(Registro_estudiantes, text="FORMULARIO\nREGISTRO\nESTUDIANTES",font=10,background='#7EADB0',justify=LEFT).place(x=20, y=20)
FontLabel_Estu = tkFont.Font(size = 20, weight= "bold")
TextoLabel_Estu = tk.Label(Registro_estudiantes,text="REGISTRO ESTUDIANTE\nRELLENE CON SUS DATOS",font=FontLabel_Estu,background='#7EADB0',justify=CENTER).place(x=450, y=50)


# FORMULARIO
Nombrelbl_Estu = tk.Label(Registro_estudiantes, text= "NOMBRE:",font=15,background='#7EADB0').place(x=300, y=175)
TexBox_Nombre_Estu = tk.Entry(Registro_estudiantes, width=100,background="#D9D9D9").place(x=450, y=180)

Apellidolbl_Estu = tk.Label(Registro_estudiantes, text= "APELLIDO:",font=15,background='#7EADB0').place(x=300, y=220)
TexBox_Apellido_Estu = tk.Entry(Registro_estudiantes, width=100,background="#D9D9D9").place(x=450, y=225)

Correolbl_Estu = tk.Label(Registro_estudiantes, text= "CORREO:",font=15,background='#7EADB0').place(x=300, y=265)
TexBox_Correo_Estu = tk.Entry(Registro_estudiantes, width=100,background="#D9D9D9").place(x=450, y=270)

Fechalbl_Estu = tk.Label(Registro_estudiantes, text= "FECHA DE NACIMIENTO:",font=15,background='#7EADB0').place(x=300, y=310)

Semestrelbl_Estu = tk.Label(Registro_estudiantes, text= "SEMESTRE APROBADO:",font=15,background='#7EADB0').place(x=300, y=355)
Combox_Semestre_Estu = ttk.Combobox(state="readonly", values=[1,2,3,4,5,6,7,8,9,10],background='#D9D9D9').place(x=550, y=360)

Facultadlbl_Estu = tk.Label(Registro_estudiantes, text= "FACULTAD:",font=15,background='#7EADB0').place(x=300, y=400)
Combox_Facultad_Estu = ttk.Combobox(state="readonly", values=["Administración de Empresas","Administración de Negocios Internacionales","Ciencias Políticas y Gobierno","Comunicación Social - Periodismo","Derecho","Diseño Gráfico","Ingeniería Ambiental","Ingeniería Civil","Ingeniería Electrónica","Ingeniería Eléctrica","Ingeniería Industrial","Ingeniería Mecánica","Ingeniería de Sistemas e Informática","Psicología"], width=40,background='#D9D9D9').place(x=430, y=405)

Promediolbl_Estu = tk.Label(Registro_estudiantes, text= "PROMEDIO PONDERADO:",font=15,background='#7EADB0').place(x=300, y=445)
TexBox_Promedio_Estu = tk.Entry(Registro_estudiantes, width=20,background="#D9D9D9").place(x=560, y=450)

Universidadlbl_Estu = tk.Label(Registro_estudiantes, text= "UNIVERSIDAD:",font=15,background='#7EADB0').place(x=300, y=490)
Combox_Semestre_Estu = ttk.Combobox(state="readonly", values=["UNIVERSIDAD PONTIFICIA BOLIVARIANA SECCIONAL BUCARAMANGA"],background='#D9D9D9', width=70).place(x=470, y=495)


# BOTONES

Registrarbtn_Estu = tk.Button(text="REGISTRARSE", font=15, bg= "#f4a020").place(x=500, y=600)
Borrarbtn_Estu = tk.Button(text="BORRAR", font=15, bg= "#f4a020").place(x=700, y=600)

Registro_estudiantes.mainloop()