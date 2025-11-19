import tkinter as tk
from tkinter import ttk

def estructura_pestaña_principal(parent):
    #Define frame de pestañas
    frame_pestañas = ttk.Notebook(parent)
    frame_pestañas.pack(pady=10,padx=10,fill="both",expand=True)

    #pestaña de inicio
    frame_inicio = ttk.Frame(frame_pestañas)
    #texto para pestaña principal
    tk.Label(frame_inicio,text="Sistema de gestion de tráfico ferroviario EFE Chile",bg="#f5f2f4",font=("Arial", 14)).pack(padx=50, pady=50)
    #añadir pestaña
    frame_pestañas.add(frame_inicio,text="Inicio")

    #referencias
    return {
        "frame": frame_pestañas,
        "frame de inicio": frame_inicio
    }














   

