# -*- coding: utf-8 -*-
"""
TRABALHO INTELIGENCIA ARTIFICIAL - PROBLEMA DO JOGO DOS JARROS
Inteligência Artificial - DCC014

Discentes: Davi Rezende
           Pedro Cotta Badaro
           Jonas Gabriel
           
Doscente: Saulo Moraes
"""

import numpy as np


class No:  #nós do grafo
    def __init__(self, v):
        self.vetorJarros = v

    def getVetorJarros(self):
        return self.vetorJarros
    
    def setVetorJarros(self, index, q):
        self.vetorJarros[index] = q
                
                
class Aresta:  #arestas do grafo
    def __init__(self, o, d):
        self.origem = o
        self.destino = d
    
    def getOrigem(self):
        return self.origem
    
    def setOrigem(self, n):
        self.origem = n
    
    def getDestino(self):
        return self.destino
    
    def setDestino(self, n):
        self.destino = n

class Grafo(): #grafo
    def __init__(self):
        self.nos = []
        self.arestas = []
        
    def verificaSeExiste(self, x):
        for i in self.nos:
            if i.getVetorJarros() == x :
                return True
            return False
                
    def inserirNoNaSolucao(self, x):
        if self.verificaSeExiste(x):
            exit()
        else:
            n = No(x)
            self.nos.append(n)
            a = Aresta(self.nos[-1], n)
            self.arestas.append(a)


class Jarro:
    def __init__(self, c, q):
        self.capacidade = c
        self.quantidadeAtual = q
        self.vizinhoEsquerda=None 
        self.vizinhoDireita=None 

    def setVizinhoEsquerda(self, j):
        self.vizinhoEsquerda = j

    def setVizinhoDireita(self, j):
        self.vizinhoDireita = j    
    
    def getVizinhoDireita(self):
        return self.vizinhoDireita 

    def getVizinhoEsquerda(self):
        return self.vizinhoEsquerda

    def getCapacidade(self):
        return self.capacidade

    def getQuantidadeAtual(self):
        return self.quantidadeAtual

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def setCapacidade(self, c):
        self.capacidade = c

    def setQuantidadeAtual(self, q):
        self.quantidadeAtual = q

    def esvaziaJarro(self):
        self.quantidadeAtual = 0

    def encheJarro(self):
        self.quantidadeAtual = self.capacidade
    
    def recebeAgua(self, qntd):
        if ((self.quantidadeAtual + qntd) >= self.capacidade):
            self.quantidadeAtual = self.capacidade
        else:
            self.quantidadeAtual += qntd

    def transfereEsquerda(self):
        if self.quantidadeAtual == 0:
            exit()
        else:
            self.vizinhoEsquerda.recebeAgua(self.quantidadeAtual)
            self.setQuantidadeAtual(0)
    
    def transfereDireita(self):
        if self.quantidadeAtual == 0:
            exit()
        else:
            self.vizinhoDireita.recebeAgua(self.quantidadeAtual)
            self.setQuantidadeAtual(0)

#-------------------------------------------------------------------------------------------------------------
#ALGORITMOS

#BACKTRACKING
def backtracking(vetorJ):    
    #instanciando grafo de estados
    grafoDeEstados = Grafo()
    vetorSolucao = []

    vetorDeJarros = vetorJ

    grafoDeEstados.inserirNoNaSolucao(vetorDeJarros)
    sucesso = False
    fracasso = False
    i = 0
    while(sucesso == False and fracasso == False):
        #ESTRATEGIA DE CONTROLE
        #1º -> ENCHE O PRIMEIRO JARRO DISPONIVEL   
        #2º -> ESVAZIA O PRIMEIRO JARRO DISPONIVEL                    
        #3º -> TRANSFERE PRA ESQUERDA DO PRIMEIRO JARRO DISPONIVEL
        #4º -> TRANSFERE PRA DIREITA DO PRIMEIRO JARRO DISPONIVEL

        #SOLUÇÃO: O PRIMEIRO JARRO DEVE TER METADE DE SUA CAPACIDADE

        noAtual = grafoDeEstados.nos[i]
        #verifica se é solução
        if (noAtual.getVetorJarros[0].getQuantidadeAtual() == (noAtual.getVetorJarros[0].getCapacidade()/2)):
            #temos uma solução 
            #ai ve oq faz aqui
            print("a")
        else:
            print("a")
            #escolhe o operador de acordo com a estrategia de controle
            #executa o operador (oq significa criar um novo nó, fazer as alteracoes)
            #adiciona operador excutado no vetorSolucao
        
#--------------------------------------------------------------------------------------------------------------
#INTERFACE
print("*INTELIGÊNCIA ARTIFICIAL - PROBLEMA DO JOGOS DOS JARROS*")
#botar aqui depois pro usuario entrar com o numero de jarros
#TESTANDO INICIALMENTE COM 3 JARROS
qntdJarros = 3
vetorJarros = []
#vamos limitar a 4 operacoes por jarro, encher, esvaziar, transferir pro da frente, transferir pro de tras

i = 0
#instanciando os jarros
while i < qntdJarros:
   
    capacidade = input("Digite a capacidade do jarro"+str(i+1)+":")
    
    while(int(capacidade) <= 0):
        print("capacidade invalida, digite de novo")
        capacidade = input("Digite uma nova capacidade do jarro:")

    vetorJarros.append(Jarro(int(capacidade),0))
    print("Vetor de jarros criado com sucesso!")
    i=i+1


#setando os vizinhos dos jarros
i=0
while i < qntdJarros:    
    if i == 0:
        vetorJarros[i].setVizinhoEsquerda(vetorJarros[qntdJarros-1])
        vetorJarros[i].setVizinhoDireita(vetorJarros[i+1])
    elif i == (qntdJarros - 1):
        vetorJarros[i].setVizinhoEsquerda(vetorJarros[i-1])
        vetorJarros[i].setVizinhoDireita(vetorJarros[0])
    else:
        vetorJarros[i].setVizinhoEsquerda(vetorJarros[i-1])
        vetorJarros[i].setVizinhoDireita(vetorJarros[i+1])
    i=i+1       

backtracking(vetorJarros)



