import tkinter as tk
from tkinter import ttk

def estructura_pestaña_principal(parent):
    #Define frame de pestañas
    frame_pestañas = ttk.Notebook(parent)
    frame_pestañas.pack(pady=10,padx=10,fill="both",expand=True)

    #pestaña de inicio
    frame_inicio = ttk.Frame(frame_pestañas)
    #pestaña de simulacion
    frame_config  = ttk.Frame(frame_pestañas)
    #pestaña configuracion
    frame_simulacion = ttk.Frame(frame_pestañas)
    #texto para pestaña principal y fondos
    tk.Label(frame_inicio,text="Sistema de gestion de tráfico ferroviario EFE Chile",bg="#f5f2f4",font=("Arial", 14)).pack(padx=50, pady=50)
    tk.Label(frame_config,text="Gestion de trenes:",font=("Arial",12)).pack(side="top")
    tk.Label(frame_simulacion, font=("Arial",12)).pack(side="top")
    #añadir pestaña=
    frame_pestañas.add(frame_inicio,text="Inicio")
    frame_pestañas.add(frame_config,text="Configuracion")
    frame_pestañas.add(frame_simulacion,text="Simulacion")
    #referencias
    return frame_pestañas














   

