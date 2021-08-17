import tkinter as tk
from tkinter import messagebox
import aluno as alu
import disciplina as disc
import curso as cur

class LimitePrincipal():
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry('400x350')
        self.menubar = tk.Menu(self.root)
        self.alunoMenu = tk.Menu(self.menubar)
        self.disciplinaMenu = tk.Menu(self.menubar)
        self.cursoMenu = tk.Menu(self.menubar)
        self.sairMenu = tk.Menu(self.menubar)

        self.alunoMenu.add_command(label="Cadastrar Aluno", \
                    command=self.controle.insereAlunos)
        self.alunoMenu.add_command(label="Cadastrar Disciplina Cursada", \
                    command=self.controle.cadastrarDiscipCursada)
        self.alunoMenu.add_command(label="Consultar", \
                    command=self.controle.consultarHistorico)
        self.menubar.add_cascade(label="Aluno", \
                    menu=self.alunoMenu)

        self.cursoMenu.add_command(label="Cadastrar Curso", \
                    command=self.controle.insereCursos)
        self.cursoMenu.add_command(label="Consultar Curso", \
                    command=self.controle.mostraCursos)     
        self.menubar.add_cascade(label="Curso", \
                    menu=self.cursoMenu)

        self.disciplinaMenu.add_command(label="Cadastrar Disciplina", \
                    command=self.controle.insereDisciplinas)
        self.menubar.add_cascade(label="Disciplina", \
                    menu=self.disciplinaMenu)

        self.sairMenu.add_command(label="Salvar", \
                    command=self.controle.salvaDados)
        self.menubar.add_cascade(label="Sair", \
                    menu=self.sairMenu)

        self.root.config(menu=self.menubar)

class ControlePrincipal():       
    def __init__(self):
        self.root = tk.Tk()

        self.ctrlAluno = alu.CtrlAluno(self)
        self.ctrlCurso = cur.CtrlCurso(self)
        self.ctrlDisciplina = disc.CtrlDisciplina(self)

        self.limite = LimitePrincipal(self.root, self) 

        self.root.title("Trabalho 11")
        # Inicia o mainloop
        self.root.mainloop()

    def insereAlunos(self):
        self.ctrlAluno.insereAlunos()
    
    def cadastrarDiscipCursada(self):
        self.ctrlAluno.insereDisciplinas()

    def consultarHistorico(self):
        self.ctrlAluno.conHistorico()

    def insereCursos(self):
        self.ctrlCurso.insereCursos()

    def mostraCursos(self):
        self.ctrlCurso.mostraCurso()

    def insereDisciplinas(self):
        self.ctrlDisciplina.insereDisciplinas()

    def salvaDados(self):
        self.ctrlAluno.salvaAlunos()
        self.ctrlDisciplina.salvaDisciplinas()
        self.ctrlCurso.salvaCursos()

        self.root.destroy()

if __name__ == '__main__':
    c = ControlePrincipal()

