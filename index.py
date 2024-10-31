import tkinter as tk
from tkinter import ttk
import requests
import random

def obtener_registros(treeview):
    try:
        url = "https://671be43c2c842d92c381a619.mockapi.io/test"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        for i in treeview.get_children():
            treeview.delete(i)

        if data:
            for registro in data:
                mostrar_registro(treeview, registro)
        else:
            treeview.insert("", "end", values=("No se encontraron registros.",))
    except requests.exceptions.RequestException as e:
        treeview.insert("", "end", values=(f"Error: {e}",))

def mostrar_registro(treeview, registro):
    treeview.insert("", "end", values=(
        registro['id'],
        registro['Titulo'],
        registro['Autor'],
        registro['Fecha_Publicacion'],
        registro['Ciudad_Publicacion'],
        registro['Ejemplares_Disponibles']
    ))

def generar_dato_random(treeview):
    try:
        url = "https://671be43c2c842d92c381a619.mockapi.io/test"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if data:
            registro_aleatorio = random.choice(data)

            for i in treeview.get_children():
                treeview.delete(i)
            mostrar_registro(treeview, registro_aleatorio)
        else:
            treeview.insert("", "end", values=("No se encontraron registros.",))
    except requests.exceptions.RequestException as e:
        treeview.insert("", "end", values=(f"Error: {e}",))

def buscar_registros(treeview, criterio):
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

        for i in treeview.get_children():
            treeview.delete(i)

        if registros_encontrados:
            for registro in registros_encontrados:
                mostrar_registro(treeview, registro)
        else:
            treeview.insert("", "end", values=("No se encontraron registros con ese criterio.",))
    except requests.exceptions.RequestException as e:
        treeview.insert("", "end", values=(f"Error: {e}",))

def iniciar_app():
    root = tk.Tk()
    root.title("Examen Tema_2")
    root.geometry("750x420")
    root.resizable(width=False, height=False)

    treeview = ttk.Treeview(root, columns=("ID", "Titulo", "Autor", "Fecha", "Ciudad", "Ejemplares"), show="headings")
    treeview.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    for col in treeview["columns"]:
        treeview.heading(col, text=col)
        treeview.column(col, anchor="center", width=100)

    scrollbar = ttk.Scrollbar(root, orient="vertical", command=treeview.yview)
    treeview.configure(yscrollcommand=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky="ns")

    criterio_entry = tk.Entry(root)
    criterio_entry.grid(row=1, column=0, pady=5)
    boton_buscar = tk.Button(root, text="Buscar Registros", command=lambda: buscar_registros(treeview, criterio_entry.get()))
    boton_buscar.grid(row=2, column=0, pady=5)

    boton_random = tk.Button(root, text="Generar Registro Aleatorio", command=lambda: generar_dato_random(treeview))
    boton_random.grid(row=3, column=0, pady=5)

    boton_actualizar = tk.Button(root, text="Actualizar Registros", command=lambda: obtener_registros(treeview))
    boton_actualizar.grid(row=4, column=0, pady=5)

    boton_salir = tk.Button(root, text="Salir", command=root.quit)
    boton_salir.grid(row=5, column=0, pady=5)

    obtener_registros(treeview)

    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.mainloop()

iniciar_app()
