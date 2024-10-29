# app.py
import tkinter as tk
from test import m_regis

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Examen Tema_2")
        self.root.geometry("400x400")
        self.root.resizable(width=False, height=False)

        # Crear botón y área de texto
        self.boton = tk.Button(root, text="Mostrar Registros", command=self.obtener_registros)
        self.boton.pack(pady=10)

        self.resultado_text = tk.Text(root, wrap="word", height=15, width=45)
        self.resultado_text.pack(padx=5, pady=5)

        # Instancia del controlador
        self.controller = m_regis(self.resultado_text)

    def obtener_registros(self):
        self.controller.obtener_registros()

# Ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
