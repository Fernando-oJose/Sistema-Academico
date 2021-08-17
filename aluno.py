import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os.path
import pickle
import disciplina as disc

class Aluno:

    def __init__(self, nroMatric, nome, curso):
        self.__nroMatric = nroMatric
        self.__nome = nome
        self.__curso = curso

        self.__historico = []
        
    def getNroMatric(self):
        return self.__nroMatric
    
    def getNome(self):
        return self.__nome
    
    def getHistorico(self):
        return self.__historico

    def getCurso(self):
        return self.__curso

class LimiteInsereAlunos(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('350x300')
        self.title("Aluno")
        self.controle = controle

        self.frameNro = tk.Frame(self)
        self.frameNome = tk.Frame(self)
        self.frameCurso = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNro.pack()
        self.frameNome.pack()
        self.frameCurso.pack()
        self.frameButton.pack()

        self.labelNro = tk.Label(self.frameNro,text="Nro Matrícula: ")
        self.labelNro.pack(side="left")
        self.labelNome = tk.Label(self.frameNome,text="Nome: ")
        self.labelNome.pack(side="left")  
        self.labelCurso = tk.Label(self.frameCurso,text="Curso: ")
        self.labelCurso.pack(side="left")  

        self.inputNro = tk.Entry(self.frameNro, width=20)
        self.inputNro.pack(side="left")
        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputNome.pack(side="left")    
        self.inputCurso = tk.Entry(self.frameCurso, width=20)
        self.inputCurso.pack(side="left")          
      
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

#interface para inserir as disciplinas cursadas no historico do aluno
class LimiteInsereDisciplina(tk.Toplevel):
    def __init__(self, controle, listaNroMatrics, listaCodDiscip):
        tk.Toplevel.__init__(self)
        self.geometry('350x300')
        self.title("Adicionar disciplina no histórico")
        self.controle = controle

        self.frameNro = tk.Frame(self)
        self.frameDiscCursada = tk.Frame(self)
        self.frameAnoSemestre = tk.Frame(self)
        self.frameNota = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameHistorico = tk.Frame(self)
        self.frameNro.pack()
        self.frameDiscCursada.pack()
        self.frameAnoSemestre.pack()
        self.frameNota.pack()
        self.frameButton.pack()

        #combobox para os nros dos alunos
        self.labelNro = tk.Label(self.frameNro,text="Nro Matrícula: ")
        self.labelNro.pack(side="left")
        self.escolhaCombo1 = tk.StringVar()
        self.combobox = ttk.Combobox(self.frameNro, width = 15 , textvariable = self.escolhaCombo1)
        self.combobox.pack(side="left")
        self.combobox['values'] = listaNroMatrics

        #combobox para as disciplinas
        self.labelDiscCursada = tk.Label(self.frameDiscCursada,text="Disciplina: ")
        self.labelDiscCursada.pack(side="left")
        self.escolhaCombo2 = tk.StringVar()
        self.combobox = ttk.Combobox(self.frameDiscCursada, width = 15 , textvariable = self.escolhaCombo2)
        self.combobox.pack(side="left")
        self.combobox['values'] = listaCodDiscip

        #outras informações
        self.labelAnoSemestre = tk.Label(self.frameAnoSemestre,text="Ano.semestre: ")
        self.labelAnoSemestre.pack(side="left")
        self.inputAnoSemestre = tk.Entry(self.frameAnoSemestre, width=20)
        self.inputAnoSemestre.pack(side="left")

        self.labelNota = tk.Label(self.frameNota,text="Nota: ")
        self.labelNota.pack(side="left")  
        self.inputNota = tk.Entry(self.frameNota, width=20)
        self.inputNota.pack(side="left") 

        self.buttonInsere = tk.Button(self.frameButton ,text="Cadastrar")           
        self.buttonInsere.pack(side="left")
        self.buttonInsere.bind("<Button>", controle.insereDiscHist)

        self.buttonFecha = tk.Button(self.frameButton ,text="Concluído")      
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

# interface para consultar o historico do aluno
class LimiteConsultaHistorico(tk.Toplevel):
    def __init__(self, controle, listaNroMatrics):
        tk.Toplevel.__init__(self)
        self.geometry('350x300')
        self.title("Consulta histórico")
        self.controle = controle 

        self.frameConsulta = tk.Frame(self)
        self.frameConsulta.pack()
        self.frameButton = tk.Frame(self)
        self.frameButton.pack()

        self.labelNro = tk.Label(self.frameConsulta,text="Aluno: ")
        self.labelNro.pack(side="left")
        self.escolhaCombo1 = tk.StringVar()
        self.combobox = ttk.Combobox(self.frameConsulta, width = 15 , textvariable = self.escolhaCombo1)
        self.combobox.pack(side="left")
        self.combobox['values'] = listaNroMatrics

        self.buttonInsere = tk.Button(self.frameButton ,text="Consultar")           
        self.buttonInsere.pack(side="left")
        self.buttonInsere.bind("<Button>", controle.consultaHist)

#interface para mostrar historico
class LimiteMostraHistorico():
    def __init__(self, str):
        messagebox.showinfo('Historico', str)

    
class LimiteMostraAlunos():
    def __init__(self, stri):
        messagebox.showinfo('Lista de alunos', stri)

class CtrlAluno():       
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        self.listaNroMatrics = []
        self.__historico = []

        if not os.path.isfile("aluno.pickle"):
            self.listaAlunos =  []
        else:
            with open("aluno.pickle", "rb") as f:
                self.listaAlunos = pickle.load(f)

    def salvaAlunos(self):
        if len(self.listaAlunos) != 0:
            with open("aluno.pickle","wb") as f:
                pickle.dump(self.listaAlunos, f)
    
    def getAluno(self, nroMatric):
        aluRet = None
        for alu in self.listaAlunos:
            if alu.getNroMatric() == nroMatric:
                aluRet = alu
        return aluRet
    
    #pegar o historico do aluno
    def getHistorico(self, codigo):
        codRet = None
        for cod in self.listaAlunos:
            if cod.getNroMatric() == codigo:
                codRet = cod
        return codRet
    
    def getlistaNroMatrics(self):
        listaNroMatrics = []
        for alu in self.listaAlunos:
            listaNroMatrics.append(alu.getNroMatric())
        return listaNroMatrics
    
    def insereAlunos(self):
        self.limiteIns = LimiteInsereAlunos(self)
    
    #chama interface para consultar historico
    def conHistorico(self):
        listaNroMatrics = self.getlistaNroMatrics()
        self.limiteIns = LimiteConsultaHistorico(self, listaNroMatrics) 


    # chama a interface para cadastrar as disciplinas no historico do aluno
    def insereDisciplinas(self):
        listaNroMatrics = self.getlistaNroMatrics()
        listaCodDiscip = self.ctrlPrincipal.ctrlDisciplina.getListaCodDisciplinas()
        self.limiteIns = LimiteInsereDisciplina(self, listaNroMatrics, listaCodDiscip) 

    #insere disciplina no historico do aluno
    def insereDiscHist(self, event):
        nroAluno = self.limiteIns.escolhaCombo1.get()
        codDisc = self.limiteIns.escolhaCombo2.get()
        anoSem = self.limiteIns.inputAnoSemestre.get()
        nota = self.limiteIns.inputNota.get()
        
        #add no historico
        for alu in self.listaAlunos:
            if alu.getNroMatric() == nroAluno:
                alu.getHistorico().append({"Disciplina":codDisc, "Ano.Semestre":anoSem,  "Nota":nota})
        
        self.limiteIns.mostraJanela('Sucesso', 'Disciplina adicionada no histórico')

    
    #mostrar historico
    def consultaHist(self, event):
        nroAluno = self.limiteIns.escolhaCombo1.get()
        #pega dados do aluno
        alunoCon = self.getAluno(nroAluno)
        # cargas horarias do aluno
        cargaObrigat = 0
        cargaElet = 0
        str2 = 'Cod da disciplina e Status: \n'
        
        for alu in self.listaAlunos:
            if alu == alunoCon:
                #percorre todas as disciplinas cursadas do aluno
                for disc in alu.getHistorico():
                    #status
                    if float(disc["Nota"]) >= 6:
                        str2 += disc["Disciplina"] + '    ' + 'aprovado \n'
                    
                        #ver se é obrigatória ou eletiva
                        if self.ctrlPrincipal.ctrlDisciplina.getDisciplina(disc["Disciplina"]).getCurso() == alu.getCurso().getNome():
                            cargaObrigat += int(self.ctrlPrincipal.ctrlDisciplina.getDisciplina(disc["Disciplina"]).getCargaHoraria())
                        else:
                            cargaElet +=  int(self.ctrlPrincipal.ctrlDisciplina.getDisciplina(disc["Disciplina"]).getCargaHoraria())
                    
                    #ver status
                    
                    else:
                        str2 += disc["Disciplina"] + '    ' + 'reprovado \n'
        
        str2 += 'Carga Horária obrigatoria: ' + str(cargaObrigat) + '    ' + 'Carga Horária eletiva: ' + str(cargaElet)
        
        self.limiteLista = LimiteMostraHistorico(str2)


    def mostraAlunos(self):
        str = 'Nro Matric. -- Nome\n'
        for alu in self.listaAlunos:
            stri += alu.getNroMatric() + ' -- ' + alu.getNome() + '\n'       
        self.limiteLista = LimiteMostraAlunos(str)
    
    def enterHandler(self, event):
        nroMatric = self.limiteIns.inputNro.get()
        nome = self.limiteIns.inputNome.get()
        cursoSel = self.limiteIns.inputCurso.get()
        curso = self.ctrlPrincipal.ctrlCurso.getCurso(cursoSel)
        aluno = Aluno(nroMatric, nome, curso)
        #add a matricula na lista de matriculas
        #self.listaNroMatrics.append(nroMatric)
        self.listaAlunos.append(aluno)
        self.limiteIns.mostraJanela('Sucesso', 'Aluno cadastrado com sucesso')
        self.clearHandler(event)

    def clearHandler(self, event):
        self.limiteIns.inputNro.delete(0, len(self.limiteIns.inputNro.get()))
        self.limiteIns.inputNome.delete(0, len(self.limiteIns.inputNome.get()))
        self.limiteIns.inputCurso.delete(0, len(self.limiteIns.inputCurso.get()))
    
    def fechaHandler(self, event):
        self.limiteIns.destroy()