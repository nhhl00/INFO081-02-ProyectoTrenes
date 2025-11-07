import tkinter as tk
from tkinter import ttk, messagebox

#config:
TITULO_VENTANA = "Gestion de Trenes"
DIMENSION_VENTANA = "800x600"
COLOR_VENTANA = "#f5f2f4"



#ui(ventanas):

def main():
    root = tk.Tk()
    root.title(TITULO_VENTANA)
    root.geometry(DIMENSION_VENTANA)
    root.configure(bg=COLOR_VENTANA)

    #ui(ventana):
    tk.Label(root, text="Sistema de gestion de tráfico ferroviario EFE Chile",bg="#f5f2f4",font=("Arial", 14)).pack(padx=50, pady=50)


    #ui(botones):
    boton_nueva_simulacion = ttk.Button(root, text="Nueva Simulación", command = lambda:print("hiciste click en nueva simulacion"))
    boton_nueva_simulacion.pack(padx = 10, pady = 5)
    boton_cargar_simulacion = ttk.Button(root, text="Cargar Simulación", command = lambda:print("hiciste click en cargar simulacion"))
    boton_cargar_simulacion.pack(padx = 10, pady = 5)



    root.mainloop()

main()




