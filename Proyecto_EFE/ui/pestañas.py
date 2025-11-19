import tkinter as tk
from tkinter import ttk

def estructura_pestaña_principal(parent):
    #
    frame_pestañas = ttk.Notebook(parent)
    frame_pestañas.pack(pady=10,padx=10,fill="both",expand=True)

    frame_inicio = ttk.Frame(frame_pestañas)

    tk.Label(frame_inicio,text="Sistema de gestion de tráfico ferroviario EFE Chile",bg="#f5f2f4",font=("Arial", 14)).pack(padx=50, pady=50)

    frame_pestañas.add(frame_inicio,text="Inicio")

    return {
        "frame": frame_pestañas,
        "frame de inicio": frame_inicio
    }














   

