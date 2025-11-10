import tkinter as tk
from tkinter import ttk

def pestaña_principal(parent=tk.Tk()):
    notebook = ttk.Notebook(parent)
    notebook.pack(pady=10, padx=10, fill='both', expand=True)

    frame_inicio = ttk.Frame(notebook)
    frame_simulacion = ttk.Frame(notebook)

    tk.Label(frame_inicio, text="Sistema de gestion de tráfico ferroviario EFE Chile",bg="#f5f2f4",font=("Arial", 14)).pack(padx=50, pady=50)

    notebook.add(frame_inicio, text="Inicio")
    notebook.add(frame_simulacion, text="Simulación")

