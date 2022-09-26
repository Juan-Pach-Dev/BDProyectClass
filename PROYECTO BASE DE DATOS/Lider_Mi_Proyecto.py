from cProfile import label
from cgitb import text
from optparse import Values
import tkinter as tk
from tkinter import CENTER, LEFT, ttk
from tkinter import font
from turtle import color, left, position
import tkinter.font as tkFont
from tkinter import *
from tkinter import filedialog as fd

Lider_Mi_Proyecto = tk.Tk()
Lider_Mi_Proyecto.config(width=1360, height=768, bg= '#7EADB0')
Lider_Mi_Proyecto.title("ESTUDIANTE LIDER - MI GRUPO")
BienvenidaLabel_Lider_Mi_Proyecto = tk.Label(Lider_Mi_Proyecto, text="BIENVENIDO A \nINNOVATE WITH \nPROYECTS",font=10,background='#7EADB0',justify=LEFT).place(x=20, y=20)
FontLabel_Lider_Mi_Proyecto = tkFont.Font(size = 20, weight= "bold")
TextoLabel_Lider_Mi_Proyecto = tk.Label(Lider_Mi_Proyecto,text="BIENVENIDO LIDER",font=FontLabel_Lider_Mi_Proyecto,background='#7EADB0',justify=CENTER).place(x=500, y=50)

# TEXTO
FontText_Lider_Mi_Proyecto = tkFont.Font(size = 15, weight= "bold")
Texto_Lider_Mi_Proyecto = tk.Label(Lider_Mi_Proyecto, text="Subir los archivos solicitados para publicar la Iniciativa Tecnologica:",font=FontText_Lider_Mi_Proyecto,background='#7EADB0', justify="left").place(x=300, y=100)

Titulo_Lider_Mi_Proyecto = tk.Label(Lider_Mi_Proyecto, text= "TITULO PROYECTO:",font=15,background='#7EADB0').place(x=300, y=175)
TexBox_Titulo_Lider_Mi_Proyecto = tk.Entry(Lider_Mi_Proyecto, width=100,background="#D9D9D9").place(x=525, y=180)

Txt_Lider_Mi_Proyecto = tk.Label(Lider_Mi_Proyecto, text= "SUBIR ARCHIVO .TXT:",font=15,background='#7EADB0').place(x=300, y=220)


Ppt_Lider_Mi_Proyecto = tk.Label(Lider_Mi_Proyecto, text= "SUBIR ARCHIVO .PPT:",font=15,background='#7EADB0').place(x=300, y=265)


Video_Lider_Mi_Proyecto = tk.Label(Lider_Mi_Proyecto, text= "SUBIR ARCHIVO .MP4:",font=15,background='#7EADB0').place(x=300, y=310)

# BOTONES

Editar_Lider_Mi_Proyecto = tk.Button(text="SUBIR INICIATIVA TECNOLOGICA", font=15, bg= "#f4a020", width=30).place(x=450, y=600)




Lider_Mi_Proyecto.mainloop()