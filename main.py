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
    
    def setVetorJarros(self,vet):
        self.vetorJarros = vet
        
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
        self.vetorSolucao = []
        self.noAtual=None
        self.arestas = []
        self.vetoresFechados=[]
    def getNoAtual(self):
        return self.noAtual

    def setNoAtual(self,no):
        self.noAtual=no

    def imprimirSolucao(self):

        for i in self.vetorSolucao:
            auxVet=i.getVetorJarros()
            print(str(auxVet[0].getQuantidadeAtual())+"-"+str(auxVet[1].getQuantidadeAtual())+"-"+str(auxVet[2].getQuantidadeAtual()))  
            
    def verificaSeExiste(self, no):
        
        if(self.vetorSolucao==[]):
            print("lista vazia")
            return False

        #PERCORRE A LISTA DE NOS PARA VERIFICAR SE JA EXISTE UM ESTADO IGUAL
        return (no.getVetorJarros() in self.vetoresFechados)
        
    def inserirNoNaSolucao(self, no):
        
        if self.verificaSeExiste(no):
            exit()
        else:
      
            self.vetorSolucao.append(no)
            a = Aresta(self.getNoAtual(), no)
            self.arestas.append(a)
            self.setNoAtual(no)
            self.vetoresFechados.append(no.getVetorJarros())

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
import copy
#BACKTRACKING
def backtracking(vetorJ):    
    #instanciando grafo de estados
    grafoDeEstados = Grafo()
    vetorDeJarros = vetorJ
    
    noOrigem=No(vetorDeJarros,None)
    #insercao do primeiro estado 0-0-0
    grafoDeEstados.inserirNoNaSolucao(noOrigem)
    
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
            
            ##Se for o ultimo indice do vetor, a direita dele é o indice 0
            if(i==(len(vetorDeJarros)-1)):
                indiceDireita=0
            else:
                indiceDireita=i+1

            ###verifica condição pra entrar no primeiro operador (ENCHER JARRO)
            if(vetorDeJarros[i].getQuantidadeAtual() != vetorDeJarros[i].getCapacidade()):
                #Fazer copia do vetorDeJarros do no atual
                auxVet = copy.deepcopy(vetorDeJarros)
                print("entrou p encher jarro")
                ##criar o no auxiliar
                noAux = No(auxVet, grafoDeEstados.getNoAtual())
                #Copiar o jarro que irá sofrer modificacao
                auxJarro = copy.deepcopy(vetorDeJarros[i])
                #Operacao
                auxJarro.encheJarro()
                noAux.vetorJarros[i]=auxJarro
            
            ###Verifica se existe o estado. Se existir, botar no grafo.
                if not (grafoDeEstados.verificaSeExiste(noAux)):
                   
                    grafoDeEstados.inserirNoNaSolucao(noAux)
                    vetorDeJarros = noAux.getVetorJarros()
                    grafoDeEstados.imprimirSolucao()

                    #verificar se o nó é solução
                    break

            ## verifica condição pra entrar no segundo operador (ESVAZIAR JARRO)
            elif(vetorDeJarros[i].getQuantidadeAtual() != 0):
               
                auxVet = copy.deepcopy(vetorDeJarros)
                print("entrou p esvaziar jarro")
              
                noAux = No(auxVet, grafoDeEstados.getNoAtual())
              
                auxJarro = copy.deepcopy(vetorDeJarros[i])
            
                auxJarro.esvaziaJarro()
                noAux.vetorJarros[i]=auxJarro
              
                if not (grafoDeEstados.verificaSeExiste(noAux)):
                   
                    grafoDeEstados.inserirNoNaSolucao(noAux)
                    vetorDeJarros = noAux.getVetorJarros()
                    grafoDeEstados.imprimirSolucao()
                 
                    break

           ##verifica condição pra entrar no Terceiro operador (TRANSFERIR PARA A ESQUERDA)
            elif(vetorDeJarros[i-1].getQuantidadeAtual() != vetorDeJarros[i-1].getCapacidade()):
             
                auxVet = copy.deepcopy(vetorDeJarros)
                print("entrou p transferir jarro ESQUERDA")
            
                noAux = No(auxVet, grafoDeEstados.getNoAtual())
             
                auxJarro = copy.deepcopy(vetorDeJarros[i-1])
           
                auxJarro.setQuantidadeAtual(vetorDeJarros[i].getQuantidadeAtual())
                noAux.vetorJarros[i-1]=auxJarro
                noAux.vetorJarros[i].esvaziaJarro()

                if not (grafoDeEstados.verificaSeExiste(noAux)):
                    
                    grafoDeEstados.inserirNoNaSolucao(noAux)
                    vetorDeJarros = noAux.getVetorJarros()
                    grafoDeEstados.imprimirSolucao()

                    break

            ##verifica condição pra entrar no Quarto operador (TRANSFERIR PARA A Direita)    
            elif(vetorDeJarros[indiceDireita].getQuantidadeAtual() != vetorDeJarros[indiceDireita].getCapacidade()):
              
                auxVet = copy.deepcopy(vetorDeJarros)
                print("entrou p transferir jarro DIREITA")
     
                noAux = No(auxVet, grafoDeEstados.getNoAtual())
          
                auxJarro = copy.deepcopy(vetorDeJarros[indiceDireita])
       
                auxJarro.setQuantidadeAtual(vetorDeJarros[i].getQuantidadeAtual())
                noAux.vetorJarros[indiceDireita]=auxJarro
                noAux.vetorJarros[i].esvaziaJarro()

                if not (grafoDeEstados.verificaSeExiste(noAux)):
                    
                    grafoDeEstados.inserirNoNaSolucao(noAux)
                    vetorDeJarros = noAux.getVetorJarros()
                    grafoDeEstados.imprimirSolucao()

                    
                    break
        break
    sucesso=True
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



