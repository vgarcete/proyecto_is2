import tkinter as tk
from tkinter.messagebox import askyesno
from tkinter import messagebox

class BotonApp(tk.Button):
    """clase personalizada para crear botones de la app"""
    def __init__(self,parent = None,**config):
        tk.Button.__init__(self,parent,**config)
        self.pack()

class VentanaApp(tk.Tk):
    """clase para generar nuevas ventanas en donde se crean botones"""
    def __init__(self,**config):
        tk.Tk.__init__(self,**config)
        self.geometry('800x600')

class VentanaSec(tk.Toplevel):
    """ventana secundaria"""
    def __init__(self,parent = None,**config):
        tk.Toplevel.__init__(self,parent,**config)
        self.geometry('800x600')

class CuadroApp(tk.Entry):
    """cuadro donde se toman los datos del teclado en las ventanas"""
    def __init__(self,parent = None,**config):
        tk.Entry.__init__(self,parent,**config)
        self.pack()

class EtiquetaApp(tk.Label):
    """clase para colocar etiquetas o cuadros de texto en las ventanas"""
    def __init__(self,parent = None,**config):
        tk.Label.__init__(self,parent,**config)
        self.pack()

class CasillaBoton(tk.Radiobutton):

    """clase para colocar un selector de botones en las ventanas"""
    def __init__(self,parent = None,**config):
        tk.Radiobutton.__init__(self,parent,**config)
        self.pack()
