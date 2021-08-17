import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os.path
import pickle

class Disciplina:

    def __init__(self, codigo, nome, curso, carga):
        self.__codigo = codigo
        self.__nome = nome
        self.__curso = curso
        self.__carga = carga

    def getCodigo(self):
        return self.__codigo
    
    def getNome(self):
        return self.__nome
    
    def getCurso(self):
        return self.__curso
    
    def getCargaHoraria(self):
        return self.__carga

class LimiteInsereDisciplinas(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('450x300')
        self.title("Disciplina")
        self.controle = controle

        self.frameNome = tk.Frame(self)
        self.frameCodigo = tk.Frame(self)
        self.frameCurso = tk.Frame(self)
        self.frameCarga = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameCodigo.pack()
        self.frameNome.pack()
        self.frameCurso.pack()
        self.frameCarga.pack()
        self.frameButton.pack()
      
        self.labelCodigo = tk.Label(self.frameCodigo,text="Código: ")
        self.labelNome = tk.Label(self.frameNome,text="Nome: ")
        self.labelCurso = tk.Label(self.frameCurso,text="Curso: ")
        self.labelCarga = tk.Label(self.frameCarga,text="Carga: ")
        self.labelCodigo.pack(side="left")
        self.labelNome.pack(side="left")  
        self.labelCurso.pack(side="left")
        self.labelCarga.pack(side="left")  

        self.inputCodigo = tk.Entry(self.frameCodigo, width=20)
        self.inputCodigo.pack(side="left")
        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputNome.pack(side="left")     
        self.inputCurso = tk.Entry(self.frameCurso, width=20)
        self.inputCurso.pack(side="left")
        self.inputCarga = tk.Entry(self.frameCarga, width=20)
        self.inputCarga.pack(side="left")        
      
        self.buttonSubmit = tk.Button(self.frameButton ,text="Enter")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterHandler)
      
        self.buttonClear = tk.Button(self.frameButton ,text="Clear")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandler)  

        self.buttonFecha = tk.Button(self.frameButton ,text="Concluído")      
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteMostraDisciplinas():
    def __init__(self, str):
        messagebox.showinfo('Lista de disciplinas', str)

      
class CtrlDisciplina():       
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        if not os.path.isfile("disciplina.pickle"):
            self.listaDisciplinas =  []
        else:
            with open("disciplina.pickle", "rb") as f:
                self.listaDisciplinas = pickle.load(f)

    def salvaDisciplinas(self):
        if len(self.listaDisciplinas) != 0:
            with open("disciplina.pickle","wb") as f:
                pickle.dump(self.listaDisciplinas, f)

    def getListaDisciplinas(self):
        return self.listaDisciplinas

    def getDisciplina(self, codDisc):
        discRet = None
        for disc in self.listaDisciplinas:
            if disc.getCodigo() == codDisc:
                discRet = disc
        return discRet

    def getListaCodDisciplinas(self):
        listaCod = []
        for disc in self.listaDisciplinas:
            listaCod.append(disc.getCodigo())
        return listaCod

    def insereDisciplinas(self):
        self.limiteIns = LimiteInsereDisciplinas(self) 

    def mostraDisciplinas(self):
        str = 'Código -- Nome\n'
        for disc in self.listaDisciplinas:
            str += disc.getCodigo() + ' -- ' + disc.getNome() + '\n'
        self.limiteLista = LimiteMostraDisciplinas(str)

    def enterHandler(self, event):
        nroMatric = self.limiteIns.inputCodigo.get()
        nome = self.limiteIns.inputNome.get()
        curso = self.limiteIns.inputCurso.get()
        carga = self.limiteIns.inputCarga.get()
        disciplina = Disciplina(nroMatric, nome, curso, carga)
        self.listaDisciplinas.append(disciplina)
        self.limiteIns.mostraJanela('Sucesso', 'Disciplina cadastrada com sucesso')
        self.clearHandler(event)

    def clearHandler(self, event):
        self.limiteIns.inputCodigo.delete(0, len(self.limiteIns.inputCodigo.get()))
        self.limiteIns.inputNome.delete(0, len(self.limiteIns.inputNome.get()))
        self.limiteIns.inputCurso.delete(0, len(self.limiteIns.inputCurso.get()))
        self.limiteIns.inputCarga.delete(0, len(self.limiteIns.inputCarga.get()))

    def fechaHandler(self, event):
        self.limiteIns.destroy()
    