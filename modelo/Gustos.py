from tkinter import StringVar #Para asociar los campos de texto con el compomente texto
from tkinter import IntVar #Para asociar los campos de numero con el compomente radio

class Gustos: #POJO

    def __init__(self):
        self.idNombreGustos = StringVar()
        self.descripcionGustos = StringVar()
        self.idUsuario_TGustos = StringVar()
        self.nombreGustos = StringVar()

    def limpiar(self):
        self.idNombreGustos.set("")
        self.descripcionGustos.set("")
        self.idUsuario_TGustos.set("")
        self.nombreGustos.set("")

    def printInfo(self):
        print(f"idNombre Gustos: {self.idNombreGustos.get()}")
        print(f"Descripcion Gustos: {self.descripcionGustos.get()}")
        print(f"id Usuario Gustos: {self.idUsuario_TGustos.get()}")
        print(f"Nombre Gustos: {self.nombreGustos.get()}")
