import tkinter as tk
from tkinter import ttk
from Registros import Registros

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Examen Tema_2")
        self.root.geometry("750x420")
        self.root.resizable(width=False, height=False)

        self.treeview = ttk.Treeview(root, columns=("ID", "Titulo", "Autor", "Fecha", "Ciudad", "Ejemplares"), show="headings")
        self.treeview.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        for col in self.treeview["columns"]:
            self.treeview.heading(col, text=col)
            self.treeview.column(col, anchor="center", width=100)

        scrollbar = ttk.Scrollbar(root, orient="vertical", command=self.treeview.yview)
        self.treeview.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky="ns")

        self.controller = Registros(self.treeview)

        self.criterio_entry = tk.Entry(root)
        self.criterio_entry.grid(row=1, column=0, pady=5)
        boton_buscar = tk.Button(root, text="Buscar Registros", command=self.buscar_registros)
        boton_buscar.grid(row=2, column=0, pady=5)

        boton_random = tk.Button(root, text="Generar Registro Aleatorio", command=self.generar_dato_random)
        boton_random.grid(row=3, column=0, pady=5)

        boton_actualizar = tk.Button(root, text="Actualizar Registros", command=self.actualizar_registros)
        boton_actualizar.grid(row=4, column=0, pady=5)

        boton_salir = tk.Button(root, text="Salir", command=root.quit)
        boton_salir.grid(row=5, column=0, pady=5)

        self.controller.obtener_registros()

        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)

    def buscar_registros(self):
        criterio = self.criterio_entry.get()
        self.controller.buscar_registros(criterio)

    def generar_dato_random(self):
        self.controller.generar_dato_random()

    def actualizar_registros(self):
        self.controller.obtener_registros()