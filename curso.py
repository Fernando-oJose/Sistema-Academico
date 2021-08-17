import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os.path
import pickle

class Curso:
    def __init__(self, nome, grade):
        self.__nome = nome
        self.__grade = grade

        #self.__listaAlunos = []

    def getNome(self):
        return self.__nome

    def getGrade(self):
        return self.__grade
    
    #def getlistaAlunos(self):
    #    return self.__listaAlunos
    
    #def addAluno(self, aluno):
    #    self.__listaAlunos.append(aluno)

class LimiteInsereCursos(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('350x300')
        self.title("Curso")
        self.controle = controle

        self.frameNro = tk.Frame(self)
        #self.frameNome = tk.Frame(self)
        #self.frameAluno = tk.Frame(self)
        self.frameGrade = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNro.pack()
        #self.frameNome.pack()
        #self.frameAluno.pack()
        self.frameGrade.pack()
        self.frameButton.pack()

        self.labelNro = tk.Label(self.frameNro,text="Nome: ")
        self.labelNome = tk.Label(self.frameGrade,text="Grade: ")
        #self.labelAluno = tk.Label(self.frameAluno,text="Alunos: ")
        self.labelNro.pack(side="left")
        self.labelNome.pack(side="left")  
        #self.labelAluno.pack(side="left")  

        self.inputNro = tk.Entry(self.frameNro, width=20)
        self.inputNro.pack(side="left")
        self.inputNome = tk.Entry(self.frameGrade, width=20)
        self.inputNome.pack(side="left")            

        self.buttonFecha = tk.Button(self.frameButton ,text="Enter")      
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.criaCurso)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteMostraCursos():
    def __init__(self, str):
        messagebox.showinfo('Lista de Cursos', str)

class LimiteConsultaCurso(tk.Toplevel):
    def __init__(self, controle):
        
        tk.Toplevel.__init__(self)
        self.geometry('350x300')
        self.title("Curso")
        self.controle = controle

        self.frameCurso = tk.Frame(self)
        self.frameCurso.pack()
        self.frameButton = tk.Frame(self)
        self.frameButton.pack()

        self.labelCurso = tk.Label(self.frameCurso, text="Curso: ")
        self.labelCurso.pack(side="left")
        self.inputCurso = tk.Entry(self.frameCurso, width=20)
        self.inputCurso.pack(side="left")

        self.buttonSubmit = tk.Button(self.frameButton ,text="Enter")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.consultaCurso)

class LimiteMostraCurso():
    def __init__(self, str):
        messagebox.showinfo('Grade', str)

class CtrlCurso():       
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        #self.listaGrade = []

        if not os.path.isfile("curso.pickle"):
            self.listaCursos =  []
        else:
            with open("curso.pickle", "rb") as f:
                self.listaCursos = pickle.load(f)

    def salvaCursos(self):
        if len(self.listaCursos) != 0:
            with open("curso.pickle","wb") as f:
                pickle.dump(self.listaCursos, f)
    
    def getCurso(self, nome):
        curRet = None
        for cur in self.listaCursos:
            if cur.getNome() == nome:
                curRet = cur
        return curRet
    
    def insereCursos(self):
        self.limiteIns = LimiteInsereCursos(self) 
    
    #cahama interface para consultar curso
    def mostraCurso(self):
        self.limiteIns = LimiteConsultaCurso(self)
    
    def criaCurso(self, event):
        nomeCurso = self.limiteIns.inputNro.get()
        gradeCurso = self.limiteIns.inputNome.get()
        curso = Curso(nomeCurso, gradeCurso)
        self.listaCursos.append(curso)
        self.limiteIns.mostraJanela('Sucesso', 'Curso criado com sucesso')
    
    def consultaCurso(self, event):
        curso2 = self.limiteIns.inputCurso.get()
        curso = self.getCurso(curso2)
        str = 'Grade ' + curso.getGrade() + '\n'
        listaDiscip = self.ctrlPrincipal.ctrlDisciplina.getListaDisciplinas()
        
        for disc in listaDiscip:
            if disc.getCurso() == curso.getNome():
                str += 'Nome: ' + disc.getNome() + '    Código: ' + disc.getCodigo() + '     Curso: ' + disc.getCurso() + '     Carga horária: ' + disc.getCargaHoraria() + '\n'
        self.limiteLista = LimiteMostraCurso(str)

    
