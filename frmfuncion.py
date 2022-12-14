import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkFont
import tkinter.messagebox as tkMsgBox
import bll.peliculas as movies
import bll.funciones as sesiones

class Funcion(tk.Toplevel):
    def __init__(self, master=None, isAdmin = False, id_funcion = None):
        super().__init__(master)
        self.master = master 
        self.id_funcion = id_funcion 
        #setting title
        self.title("Función")
        #setting window size
        width=280
        height=258
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        GLabel_131=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_131["font"] = ft
        GLabel_131["fg"] = "#333333"
        GLabel_131["justify"] = "right"
        GLabel_131["text"] = "Película:"
        GLabel_131.place(x=10,y=20,width=70,height=25)

        peli = dict(sesiones.listar_peliculas())

        cb_Peliculas = ttk.Combobox(self, state="readonly", values=list(peli.values()), name="cbPelicula")
        cb_Peliculas.set(peli[4])
        cb_Peliculas.place(x=90,y=30,width=140,height=30)

        GLabel_358=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_358["font"] = ft
        GLabel_358["fg"] = "#333333"
        GLabel_358["justify"] = "right"
        GLabel_358["text"] = "Sala:"
        GLabel_358.place(x=10,y=60,width=70,height=25)

        sala = dict(sesiones.listar_salas())

        cb_Salas = ttk.Combobox(self, state="readonly", values=list(sala.values()), name="cbSala")
        cb_Salas.set(sala[4])
        cb_Salas.place(x=90,y=65,width=140,height=30)

        GLabel_861=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_861["font"] = ft
        GLabel_861["fg"] = "#333333"
        GLabel_861["justify"] = "right"
        GLabel_861["text"] = "Fecha:"
        GLabel_861.place(x=10,y=95,width=70,height=25)

        GLabel_357=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_357["font"] = ft
        GLabel_357["fg"] = "#333333"
        GLabel_357["justify"] = "right"
        GLabel_357["text"] = "Hora:"
        GLabel_357.place(x=10,y=140,width=70,height=25)

        GLineEdit_125=tk.Entry(self)
        GLineEdit_125["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_125["font"] = ft
        GLineEdit_125["fg"] = "#333333"
        GLineEdit_125["justify"] = "left"
        GLineEdit_125["text"] = ""
        GLineEdit_125.place(x=90,y=100,width=140,height=30)

        GLineEdit_765=tk.Entry(self)
        GLineEdit_765["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_765["font"] = ft
        GLineEdit_765["fg"] = "#333333"
        GLineEdit_765["justify"] = "left"
        GLineEdit_765["text"] = ""
        GLineEdit_765.place(x=90,y=140,width=140,height=30)

        GButton_812=tk.Button(self)
        GButton_812["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_812["font"] = ft
        GButton_812["fg"] = "#000000"
        GButton_812["justify"] = "center"
        GButton_812["text"] = "Cancelar"
        GButton_812.place(x=190,y=210,width=70,height=25)
        GButton_812["command"] = self.aceptar

        GButton_420=tk.Button(self)
        GButton_420["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_420["font"] = ft
        GButton_420["fg"] = "#000000"
        GButton_420["justify"] = "center"
        GButton_420["text"] = "Aceptar"
        GButton_420.place(x=100,y=210,width=70,height=25)
        GButton_420["command"] = self.cancelar

    def aceptar(self):
        print("command")


    def cancelar(self):
        self.destroy()


