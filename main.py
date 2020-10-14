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
    def __init__(self, vetorDeJarros,noPai):
        
        self.vetorJarros = vetorDeJarros
        self.noPai=noPai

    def getNoPai(self):
        return self.getNoPai

    def setNoPai(self,noPai):
        self.noPai=noPai

    def getVetorJarros(self):
        return self.vetorJarros
    
    def setVetorJarros(self,vetorDeJarros):
        self.vetorJarros = vetorDeJarros
                
                
class Aresta:  #arestas do grafo
    def __init__(self, origem, destino):
        self.estadoOrigem = origem
        self.estadoDestino = destino
    
    def getOrigem(self):
        return self.estadoOrigem
    
    def setOrigem(self, n):
        self.estadoOrigem = n
    
    def getDestino(self):
        return self.estadoDestino
    
    def setDestino(self, n):
        self.estadoDestino = n

class Grafo(): #grafo
    def __init__(self):
        self.nos = []
        self.noAtual=None
        self.arestas = []
    
    def getNoAtual(self):
        return self.noAtual

    def setNoAtual(self,no):
        self.noAtual=no

    def imprimirSolucao(self):

        for i in self.nos:
            auxVet=i.getVetorJarros()
            print(str(auxVet[0].getQuantidadeAtual())+"-"+str(auxVet[1].getQuantidadeAtual())+"-"+str(auxVet[2].getQuantidadeAtual()))  
            
    def verificaSeExiste(self, no):
        
        if(self.nos==[]):
            print("lista vazia")
            return False

        #PERCORRE A LISTA DE NOS PARA VERIFICAR SE JA EXISTE UM ESTADO IGUAL
        for i in self.nos:
            if(i.getVetorJarros() == no.getVetorJarros()):
                return True

        return False

    def inserirNoNaSolucao(self, no):
        print("entrou funcao inserir no")
        if self.verificaSeExiste(no):
            print("JA EXISTE")
            exit()
        else:
            print("NAO EXISTE")
            self.nos.append(no)
            a = Aresta(self.getNoAtual(), no)
            self.arestas.append(a)
            self.setNoAtual(no)

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
    vetorDeJarros = vetorJ
    
    #insercao do primeiro estado 0-0-0
    grafoDeEstados.inserirNoNaSolucao(vetorDeJarros)
    
    sucesso = False
    fracasso = False
    
    #PREPARA FORMATO DA SOLUÇÃO
    if(vetorDeJarros[0].getCapacidade()%2==0):
        objetivoPrimeiroJarro=vetorDeJarros[0].getCapacidade()/2
    else:
        objetivoPrimeiroJarro=((vetorDeJarros[0].getCapacidade()+1)/2)

    while(sucesso == False and fracasso == False):
        #ESTRATEGIA DE CONTROLE
        #0º -> ENCHE O JARRO    
        #1º -> ESVAZIA O  JARRO                     
        #2º -> TRANSFERE PRA ESQUERDA DO JARRO 
        #3º -> TRANSFERE PRA DIREITA DO JARRO 
        #SOLUÇÃO: O PRIMEIRO JARRO DEVE TER METADE DE SUA CAPACIDADE SE FOR PAR
        #O PRIMEIRO JARRO DEVE TER METADE DE SUA CAPACIDADE +1 SE FOR IMPAR 
        for i in range(len(vetorDeJarros)):

            #verifica condição pra entrar no primeiro operador (ENCHER JARRO)
            if(vetorDeJarros[i].getQuantidadeAtual() != vetorDeJarros[i].getCapacidade()):
                print("entrou p encher jarro")
                noAux = No(vetorDeJarros, grafoDeEstados.getNoAtual())
                auxVetJarros = vetorDeJarros
                auxVetJarros[i].encheJarro()
                noAux.setVetorJarros(auxVetJarros)

                if (grafoDeEstados.verificaSeExiste(noAux) == False):
                    print("if de inserir no")
                    grafoDeEstados.inserirNoNaSolucao(noAux.getVetorJarros())
                    vetorDeJarros = noAux.getVetorJarros()

                    #verificar se o nó é solução
                    break
     
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



