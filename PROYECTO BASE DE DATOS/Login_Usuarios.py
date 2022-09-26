from cProfile import label
from cgitb import text
import tkinter as tk
from tkinter import CENTER, LEFT, ttk
from tkinter import font
from turtle import color, left, position
import tkinter.font as tkFont

Login_Usuario = tk.Tk()
Login_Usuario.config(width=1360, height=768, bg= '#7EADB0')
Login_Usuario.title("INICIAR SESION")
BienvenidaLabel_Log = tk.Label(Login_Usuario, text="BIENVENIDO A \nINNOVATE WITH \nPROYECTS",font=10,background='#7EADB0',justify=LEFT).place(x=20, y=20)
FontLabel_Log = tkFont.Font(size = 20, weight= "bold")
TextoLabel_Log = tk.Label(Login_Usuario,text="LOGIN USUARIO\nINGRESE SUS DATOS",font=FontLabel_Log,background='#7EADB0',justify=CENTER).place(x=550, y=50)

# INICIO

Email_Log = tk.Label(Login_Usuario, text= "EMAIL:",font=15,background='#7EADB0').place(x=300, y=175)
TexBox_Email_Log = tk.Entry(Login_Usuario, width=100,background="#D9D9D9").place(x=475, y=180)

Contraseña_Log = tk.Label(Login_Usuario, text= "CONTRASEÑA:",font=15,background='#7EADB0').place(x=300, y=220)
TexBox_Contraseña_Log = tk.Entry(Login_Usuario, width=100,background="#D9D9D9").place(x=475, y=225)

Texto_Olvidar = tk.Label(text="¿Olvidaste tu contrseña?", fg="BLACK", cursor="hand2",background='#7EADB0').place(x=600, y=300)
Texto_Info = tk.Label(text="¿No tienes una cuenta?",background='#7EADB0').place(x=560, y=330)
FontLabel_Regis = tkFont.Font(weight= "bold", size=10)
Texto_Registrar = tk.Label(text="REGISTRATE",background='#7EADB0',font=FontLabel_Regis, cursor="hand2", fg="blue").place(x=700, y=330)

# BOTON

Iniciar_Log = tk.Button(text="INICIAR SESION", font=15, bg= "#f4a020").place(x=600, y=400)

# IMAGENES

logo = tk.PhotoImage(file= "IMAGENES/logo.png")
lbl_img = tk.Label(Login_Usuario, image = logo).place(x=555, y=500)

Login_Usuario.mainloop()