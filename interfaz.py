
import tkinter as tk
from tkinter import messagebox
from equipo import AireConvencional, AireInverter
from mantenimiento import Mantenimiento


class Interfaz:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("AIREX - Mantenimiento de Aires Acondicionados")
        self.ventana.geometry("600x500")

        self.equipos = []

        titulo = tk.Label(
            ventana,
            text="AIREX - Registro de equipos",
            font=("Arial", 18, "bold")
        )
        titulo.pack(pady=15)

        tk.Label(ventana, text="Marca:").pack()
        self.marca = tk.Entry(ventana)
        self.marca.pack()

        tk.Label(ventana, text="Capacidad (BTU):").pack()
        self.capacidad = tk.Entry(ventana)
        self.capacidad.pack()

        tk.Label(ventana, text="Modelo:").pack()
        self.modelo = tk.Entry(ventana)
        self.modelo.pack()

        tk.Label(ventana, text="Tipo de aire:").pack()
        self.tipo = tk.StringVar(value="Convencional")

        tk.OptionMenu(
            ventana,
            self.tipo,
            "Convencional",
            "Inverter"
        ).pack()

        tk.Button(
            ventana,
            text="Registrar equipo",
            command=self.registrar_equipo
        ).pack(pady=10)

        tk.Button(
            ventana,
            text="Ver equipos registrados",
            command=self.ver_equipos
        ).pack(pady=5)

        tk.Button(
            ventana,
            text="Registrar mantenimiento",
            command=self.registrar_mantenimiento
        ).pack(pady=5)

        tk.Button(
            ventana,
            text="Ver mantenimientos",
            command=self.ver_mantenimientos
        ).pack(pady=5)

    def registrar_equipo(self):
        marca = self.marca.get().strip()
        capacidad = self.capacidad.get().strip()
        modelo = self.modelo.get().strip()

        if not marca or not capacidad or not modelo:
            messagebox.showwarning("Aviso", "Completa todos los campos.")
            return

        if not capacidad.isdigit() or int(capacidad) <= 0:
            messagebox.showwarning("Aviso", "Ingresa una capacidad válida.")
            return

        if self.tipo.get() == "Convencional":
            equipo = AireConvencional(marca, int(capacidad), modelo)
        else:
            equipo = AireInverter(marca, int(capacidad), modelo)

        self.equipos.append(equipo)

        messagebox.showinfo("Éxito", "Equipo registrado correctamente.")

        self.marca.delete(0, tk.END)
        self.capacidad.delete(0, tk.END)
        self.modelo.delete(0, tk.END)

    def ver_equipos(self):
        ventana_lista = tk.Toplevel(self.ventana)
        ventana_lista.title("Equipos registrados")
        ventana_lista.geometry("500x350")

        lista = tk.Listbox(ventana_lista, width=65, height=15)
        lista.pack(padx=10, pady=10)

        for i, equipo in enumerate(self.equipos):
            lista.insert(tk.END, f"{i + 1}. {equipo.mostrar_informacion()}")

        if not self.equipos:
            lista.insert(tk.END, "No hay equipos registrados.")

    def registrar_mantenimiento(self):
        if not self.equipos:
            messagebox.showwarning("Aviso", "Primero registra un equipo.")
            return

        ventana_mant = tk.Toplevel(self.ventana)
        ventana_mant.title("Registrar mantenimiento")
        ventana_mant.geometry("400x350")

        tk.Label(ventana_mant, text="Selecciona el equipo:").pack(pady=5)

        opciones = [
            f"{i + 1}. {equipo.mostrar_informacion()}"
            for i, equipo in enumerate(self.equipos)
        ]

        seleccion = tk.StringVar(value=opciones[0])
        tk.OptionMenu(ventana_mant, seleccion, *opciones).pack()

        tk.Label(ventana_mant, text="Fecha:").pack(pady=5)
        fecha = tk.Entry(ventana_mant)
        fecha.pack()

        tk.Label(ventana_mant, text="Descripción del mantenimiento:").pack(pady=5)
        descripcion = tk.Entry(ventana_mant, width=40)
        descripcion.pack()

        tk.Label(ventana_mant, text="Técnico:").pack(pady=5)
        tecnico = tk.Entry(ventana_mant)
        tecnico.pack()

        def guardar():
            if not fecha.get().strip() or not descripcion.get().strip() or not tecnico.get().strip():
                messagebox.showwarning("Aviso", "Completa todos los campos.")
                return

            indice = opciones.index(seleccion.get())
            mantenimiento = Mantenimiento(
                fecha.get().strip(),
                descripcion.get().strip(),
                tecnico.get().strip()
            )

            self.equipos[indice].agregar_mantenimiento(mantenimiento)

            messagebox.showinfo("Éxito", "Mantenimiento registrado.")
            ventana_mant.destroy()

        tk.Button(
            ventana_mant,
            text="Guardar mantenimiento",
            command=guardar
        ).pack(pady=15)

    def ver_mantenimientos(self):
        ventana_lista = tk.Toplevel(self.ventana)
        ventana_lista.title("Historial de mantenimientos")
        ventana_lista.geometry("550x400")

        lista = tk.Listbox(ventana_lista, width=75, height=18)
        lista.pack(padx=10, pady=10)

        encontrados = False

        for equipo in self.equipos:
            for mantenimiento in equipo.mantenimientos:
                lista.insert(
                    tk.END,
                    f"{equipo.marca} - {equipo.modelo}: "
                    f"{mantenimiento.fecha} - {mantenimiento.descripcion}"
                )
                encontrados = True

        if not encontrados:
            lista.insert(tk.END, "Todavía no hay mantenimientos registrados.")
