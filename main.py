

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

"""
class Estado:  #nós do grafo
    def __init__(self, id):
        self.id = id
        #colocar outros atributos
        
    def getId(self):
        return self.id
    
    def setId(self, id):
        self.id = id
                
class Transicao:  #arestas do grafo
    def __init__(self, id):
        self.id = id
        
    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

class Grafo(): #grafo
    def __init__(self):
        self.nos = []
        self.arestas = []
        
    def buscarNo(self, id):
        for i in self.nos:
            if id == i.getId():
                return i
            
    def buscarArestas(self, id):
        for i in self.arestas:
            if id == i.getId():
                return i
    
    def criarNo(self, id):
        if self.buscarNo(id) is None:
            self.nos.append(Estado(id))
            
    def criarAresta(self, id):
        if self.buscarAresta(id) is None:
            self.arestas.append(Transicao(id))
"""

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


i=0
#setando os vizinhos dos jarros
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



