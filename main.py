# -*- coding: utf-8 -*-
"""
TRABALHO INTELIGENCIA ARTIFICIAL - PROBLEMA DO JOGO DOS JARROS
Inteligência Artificial - DCC014

Discentes: Davi Rezende
           Pedro Cotta Badaro
           Jonas Gabriel
           
Doscente: Saulo Moraes
"""
from graph import Node, Graph, Edge
from largura import largura
from profundidade import profundidade
from ordenada import ordenada
from guloso import guloso
from backtracking import backtracking
from jug import Jug
import copy
import queue
import time
import random

            
def main():
    """
    Main function of application
    """

    """
        OPERACOES
        r1=ENCHER JARRO
        r2=ESVAZIAR JARRO
        r3=TRANSFERIR ESQUERDA
        r4= TRANSFERIR DIREITA
    """
    
    jug_list = []
    """
    Primeira linha do arquivo = objetivo do problema
    Demais linhas = capacidade total do jarro
    """
    f = open("entrada.txt", "r")
    target_amount = int(f.readline())

    for x in f:
        jug_list.append(Jug(int(x.strip())))

    root = Node(None, jug_list)

   
    
    
    start = time.time()
    backtracking(root, target_amount)
    end = time.time()
    timeBT=end-start
    print()

    start = time.time()
    profundidade(root, target_amount)
    end = time.time()
    timeProf=end-start
    print()

    start = time.time()
    largura(root, target_amount)
    end = time.time()
    timeLarg=end-start
    print()

    start = time.time()
    guloso(root, target_amount)
    end = time.time()
    timeGul=end-start
    print()

    start = time.time()
    ordenada(root, target_amount)
    end = time.time()
    timeOrd=end-start
    print()

    print("-----------------TEMPO DE EXECUCAO ALGORITMOS-----------------------------")
    print("-----------------BACKTRACKING:"+str(timeBT)+"------------------------------")
    print("-----------------PROFUNDIDADE:"+str(timeProf)+"------------------------------")
    print("-----------------LARGURA:"+str(timeLarg)+"------------------------------")
    print("-----------------GULOSO:"+str(timeGul)+"------------------------------")
    print("-----------------ORDENADA:"+str(timeOrd)+"------------------------------")

    


if __name__ == "__main__":
    main()