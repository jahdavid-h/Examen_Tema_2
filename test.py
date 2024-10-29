import tkinter as tk
from tkinter import ttk
import requests

class Registros:
    def __init__(self, treeview):
        self.__treeview = treeview  # Atributo privado

    def obtener_registros(self):
        try:
            url = "https://671be43c2c842d92c381a619.mockapi.io/test"
            response = requests.get(url)
            response.raise_for_status()

            data = response.json()

            # Limpiar el Treeview antes de mostrar nuevos registros
            for i in self.__treeview.get_children():
                self.__treeview.delete(i)

            if data:
                for registro in data:
                    self.__mostrar_registro(registro)
            else:
                self.__treeview.insert("", "end", values=("No se encontraron registros.",))
        except requests.exceptions.RequestException as e:
            self.__treeview.insert("", "end", values=(f"Error: {e}",))

    def buscar_registros(self, criterio):
        try:
            url = "https://671be43c2c842d92c381a619.mockapi.io/test"
            response = requests.get(url)
            response.raise_for_status()

            data = response.json()
            registros_encontrados = [
                r for r in data
                if criterio.lower() in r['Titulo'].lower() or
                   criterio.lower() in r['id'] or
                   criterio.lower() in r['Autor'].lower()
            ]

            for i in self.__treeview.get_children():
                self.__treeview.delete(i)

            if registros_encontrados:
                for registro in registros_encontrados:
                    self.__mostrar_registro(registro)
            else:
                self.__treeview.insert("", "end", values=("No se encontraron registros con ese criterio.",))
        except requests.exceptions.RequestException as e:
            self.__treeview.insert("", "end", values=(f"Error: {e}",))

    def mostrar_ultimo_registro(self):
        try:
            url = "https://671be43c2c842d92c381a619.mockapi.io/test"
            response = requests.get(url)
            response.raise_for_status()

            data = response.json()

            # Limpiar el Treeview antes de mostrar el último registro
            for i in self.__treeview.get_children():
                self.__treeview.delete(i)

            if data:
                ultimo_registro = data[-1]
                self.__mostrar_registro(ultimo_registro)
            else:
                self.__treeview.insert("", "end", values=("No se encontraron registros.",))
        except requests.exceptions.RequestException as e:
            self.__treeview.insert("", "end", values=(f"Error: {e}",))

    def __mostrar_registro(self, registro):
        self.__treeview.insert("", "end", values=(
            registro['id'],
            registro['Titulo'],
            registro['Autor'],
            registro['Fecha_Publicacion'],
            registro['Ciudad_Publicacion'],
            registro['Ejemplares_Disponibles']
        ))

class App:
    def __init__(self, root):
        self.__root = root
        self.__root.title("Examen Tema_2")
        self.__root.geometry("700x420")
        self.__root.resizable(width=False, height=False)

        # Treeview para mostrar los registros
        self.__treeview = ttk.Treeview(root, columns=("ID", "Titulo", "Autor", "Fecha", "Ciudad", "Ejemplares"), show="headings")
        self.__treeview.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Definir las columnas
        for col in self.__treeview["columns"]:
            self.__treeview.heading(col, text=col)
            self.__treeview.column(col, anchor="center", width=100)

        # Scrollbar para el Treeview
        scrollbar = ttk.Scrollbar(root, orient="vertical", command=self.__treeview.yview)
        self.__treeview.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky="ns")  # Coloca la barra de desplazamiento al lado del Treeview

        # Crear instancia del controlador
        self.__controller = Registros(self.__treeview)

        # Botón para mostrar todos los registros
        boton_mostrar = tk.Button(root, text="Mostrar Registros", command=self.__obtener_registros)
        boton_mostrar.grid(row=1, column=0, pady=1)

        # Entrada y botón para buscar registros
        self.__criterio_entry = tk.Entry(root)
        self.__criterio_entry.grid(row=2, column=0, pady=5)
        boton_buscar = tk.Button(root, text="Buscar Registros", command=self.__buscar_registros)
        boton_buscar.grid(row=3, column=0, pady=5)

        # Botón para mostrar el último registro
        boton_ultimo = tk.Button(root, text="Mostrar Último Registro", command=self.__mostrar_ultimo_registro)
        boton_ultimo.grid(row=4, column=0, pady=5)

        # Botón para salir
        boton_salir = tk.Button(root, text="Salir", command=self.__root.quit)
        boton_salir.grid(row=5, column=0, pady=5)

        # Configurar la expansión de las filas y columnas
        root.grid_rowconfigure(0, weight=1)  # Hacer que la primera fila (Treeview) se expanda
        root.grid_columnconfigure(0, weight=1)  # Hacer que la primera columna (donde están los botones) se expanda

    def __obtener_registros(self):
        self.__controller.obtener_registros()

    def __buscar_registros(self):
        criterio = self.__criterio_entry.get()
        self.__controller.buscar_registros(criterio)

    def __mostrar_ultimo_registro(self):
        self.__controller.mostrar_ultimo_registro()
