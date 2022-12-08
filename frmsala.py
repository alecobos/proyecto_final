import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkFont
import tkinter.messagebox as tkMsgBox

class Sala(tk.Toplevel):
    def __init__(self, master=None, isAdmin = False, id_sala = None):
        super().__init__(master)
        self.master = master    
        #setting title
        self.title("Sala")
        #setting window size
        width=280
        height=240
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        GLabel_696=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_696["font"] = ft
        GLabel_696["fg"] = "#333333"
        GLabel_696["justify"] = "right"
        GLabel_696["text"] = "Nombre de la Sala:"
        GLabel_696.place(x=40,y=40,width=110,height=30)

        GLineEdit_335=tk.Entry(self)
        GLineEdit_335["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_335["font"] = ft
        GLineEdit_335["fg"] = "#333333"
        GLineEdit_335["justify"] = "center"
        GLineEdit_335["text"] = ""
        GLineEdit_335.place(x=160,y=40,width=80,height=30)

        GLabel_455=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_455["font"] = ft
        GLabel_455["fg"] = "#333333"
        GLabel_455["justify"] = "right"
        GLabel_455["text"] = "Capacidad:"
        GLabel_455.place(x=80,y=80,width=70,height=30)

        GLineEdit_621=tk.Entry(self)
        GLineEdit_621["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_621["font"] = ft
        GLineEdit_621["fg"] = "#333333"
        GLineEdit_621["justify"] = "center"
        GLineEdit_621["text"] = ""
        GLineEdit_621.place(x=160,y=80,width=80,height=30)

        GLabel_829=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_829["font"] = ft
        GLabel_829["fg"] = "#333333"
        GLabel_829["justify"] = "right"
        GLabel_829["text"] = "Tipo:"
        GLabel_829.place(x=95,y=120,width=70,height=30)

        cb_roles = ttk.Combobox(self, state="readonly", values=["2D", "3D", "4D", "IMAX"])
        cb_roles.place(x=160,y=120,width=80,height=30)

        GButton_989=tk.Button(self)
        GButton_989["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_989["font"] = ft
        GButton_989["fg"] = "#000000"
        GButton_989["justify"] = "center"
        GButton_989["text"] = "Aceptar"
        GButton_989.place(x=90,y=190,width=70,height=25)
        GButton_989["command"] = self.GButton_989_command

        GButton_820=tk.Button(self)
        GButton_820["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_820["font"] = ft
        GButton_820["fg"] = "#000000"
        GButton_820["justify"] = "center"
        GButton_820["text"] = "Cancelar"
        GButton_820.place(x=180,y=190,width=70,height=25)
        GButton_820["command"] = self.GButton_820_command

    def GButton_989_command(self):
        print("command")


    def GButton_820_command(self):
        print("command")

