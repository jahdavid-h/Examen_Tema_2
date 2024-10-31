import requests
import random


class Registros:
    def __init__(self, treeview):
        self.treeview = treeview

    def obtener_registros(self):
        try:
            url = "https://671be43c2c842d92c381a619.mockapi.io/test"
            response = requests.get(url)
            response.raise_for_status()

            data = response.json()

            for i in self.treeview.get_children():
                self.treeview.delete(i)

            if data:
                for registro in data:
                    self.mostrar_registro(registro)
            else:
                self.treeview.insert("", "end", values=("No se encontraron registros.",))
        except requests.exceptions.RequestException as e:
            self.treeview.insert("", "end", values=(f"Error: {e}",))

    def mostrar_registro(self, registro):
        self.treeview.insert("", "end", values=(
            registro['id'],
            registro['Titulo'],
            registro['Autor'],
            registro['Fecha_Publicacion'],
            registro['Ciudad_Publicacion'],
            registro['Ejemplares_Disponibles']
        ))

    def generar_dato_random(self):
        try:
            url = "https://671be43c2c842d92c381a619.mockapi.io/test"
            response = requests.get(url)
            response.raise_for_status()

            data = response.json()
            if data:

                registro_aleatorio = random.choice(data)

                for i in self.treeview.get_children():
                    self.treeview.delete(i)
                self.mostrar_registro(registro_aleatorio)
            else:
                self.treeview.insert("", "end", values=("No se encontraron registros.",))
        except requests.exceptions.RequestException as e:
            self.treeview.insert("", "end", values=(f"Error: {e}",))

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

            for i in self.treeview.get_children():
                self.treeview.delete(i)

            if registros_encontrados:
                for registro in registros_encontrados:
                    self.mostrar_registro(registro)
            else:
                self.treeview.insert("", "end", values=("No se encontraron registros con ese criterio.",))
        except requests.exceptions.RequestException as e:
            self.treeview.insert("", "end", values=(f"Error: {e}",))