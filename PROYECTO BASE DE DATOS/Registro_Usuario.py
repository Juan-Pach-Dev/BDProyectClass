from cProfile import label
from cgitb import text
import tkinter as tk
from tkinter import CENTER, LEFT, ttk
from tkinter import font
from turtle import color, left, position
import tkinter.font as tkFont

Registro_Usuario = tk.Tk()
Registro_Usuario.config(width=1360, height=768, bg= '#7EADB0')
Registro_Usuario.title("REGISTRO USUARIOS")
BienvenidaLabel_Usu = tk.Label(Registro_Usuario, text="FORMULARIO\nREGISTRO\nUSUARIOS",font=10,background='#7EADB0',justify=LEFT).place(x=20, y=20)
FontLabel_Usu = tkFont.Font(size = 20, weight= "bold")
TextoLabel_Usu = tk.Label(Registro_Usuario,text="REGISTRO USUARIOS\nRELLENE CON SUS DATOS",font=FontLabel_Usu,background='#7EADB0',justify=CENTER).place(x=450, y=50)

# FORMULARIO
Nombrelbl_Usu = tk.Label(Registro_Usuario, text= "NOMBRE:",font=15,background='#7EADB0').place(x=300, y=175)
TexBox_Nombre_Usu = tk.Entry(Registro_Usuario, width=100,background="#D9D9D9").place(x=450, y=180)

Apellidolbl_Usu = tk.Label(Registro_Usuario, text= "APELLIDO:",font=15,background='#7EADB0').place(x=300, y=220)
TexBox_Apellido_Usu = tk.Entry(Registro_Usuario, width=100,background="#D9D9D9").place(x=450, y=225)

Correolbl_Usu = tk.Label(Registro_Usuario, text= "CORREO:",font=15,background='#7EADB0').place(x=300, y=265)
TexBox_Correo_Usu = tk.Entry(Registro_Usuario, width=100,background="#D9D9D9").place(x=450, y=270)

Fechalbl_Usu = tk.Label(Registro_Usuario, text= "FECHA DE NACIMIENTO:",font=15,background='#7EADB0').place(x=300, y=310)

#BOTONES

Registrarbtn_Usu = tk.Button(text="REGISTRARSE", font=15, bg= "#f4a020").place(x=500, y=400)
Borrarbtn_Usu = tk.Button(text="BORRAR", font=15, bg= "#f4a020").place(x=700, y=400)

Registro_Usuario.mainloop()