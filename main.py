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
from jug import Jug
import copy

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
    jug_array = [Jug(4),Jug(3)]

    jug_array_2 = [Jug(4),Jug(3)]
    jug_array_2[0].fill()

    jug_array_3 = copy.deepcopy(jug_array_2)
    jug_array_3[0].transfer_to(jug_array_3[1])

    jug_array_4 = copy.deepcopy(jug_array_3)
    jug_array_4[1].spill()

    n = Node(None, jug_array)
    n2 = Node(n, jug_array_2)

    g = Graph()
    g.insert_node(n,"begin")
    g.insert_node(n2, "r1")

    g.print_graph()

if __name__ == "__main__":
    main()