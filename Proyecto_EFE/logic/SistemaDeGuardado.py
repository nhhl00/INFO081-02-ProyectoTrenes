import tkinter as tk
from tkinter import messagebox


class SistemaDeGuardado:
    def __init__(self, ruta_base="data/"):
        self.ruta_base = ruta_base

    def guardar_simulacion(self, estado_simulacion):
        def guardar():
            nombre = entrada_nombre.get().strip()
            if not nombre:
                messagebox.showwarning("Debes ingresar un nombre de archivo")
                return

            ruta = f"{self.ruta_base}{nombre}.txt"

            try:
                if hasattr(estado_simulacion, "__dict__"):
                    datos = estado_simulacion.__dict__
                else:
                    datos = estado_simulacion

                with open(ruta, "w", encoding="utf-8") as archivo:
                    for clave, valor in datos.items():
                        archivo.write(f"{clave}={valor}\n")

                messagebox.showinfo("Exito", f"Simulación guardada en:\n{ruta}")
                ventana.destroy()

            except Exception as e:
                messagebox.showerror("Error", f"No se pudo guardar la simulación:\n{e}")

        ventana = tk.Tk()
        ventana.title("Guardar Simulación")
        ventana.geometry("350x150")

        tk.Label(ventana, text="Nombre del archivo a guardar:", font=("Arial", 10)).pack(pady=10)
        entrada_nombre = tk.Entry(ventana, width=30)
        entrada_nombre.pack()

        tk.Button(ventana, text="Guardar", command=guardar).pack(pady=15)
        ventana.mainloop()

    def cargar_simulacion(self):
        datos = {}
        def cargar():
            nombre = entrada_nombre.get().strip()
            if not nombre:
                messagebox.showwarning("Debes ingresar un nombre de archivo.")
                return

            ruta = f"{self.ruta_base}{nombre}.txt"
            try:
                with open(ruta, "r", encoding="utf-8") as archivo:
                    for linea in archivo:
                        if "=" in linea:
                            clave, valor = linea.strip().split("=", 1)
                            datos[clave] = valor

                messagebox.showinfo("Exito", f"Simulación cargada desde:\n{ruta}")
                ventana.destroy()

            except FileNotFoundError:
                messagebox.showerror("Error", f"No se encontró el archivo '{ruta}'.")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo cargar la simulación:\n{e}")

        ventana = tk.Tk()
        ventana.title("Cargar Simulacion")
        ventana.geometry("350x150")

        tk.Label(ventana, text="Nombre del archivo a cargar:", font=("Arial", 10)).pack(pady=10)
        entrada_nombre = tk.Entry(ventana, width=30)
        entrada_nombre.pack()

        tk.Button(ventana, text="Cargar", command=cargar).pack(pady=15)
        ventana.mainloop()

        return datos if datos else None
