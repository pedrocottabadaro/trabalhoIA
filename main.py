# -*- coding: utf-8 -*-
"""
TRABALHO INTELIGENCIA ARTIFICIAL - PROBLEMA DO JOGO DOS JARROS
Inteligência Artificial - DCC014

Discentes: Davi Rezende
           Pedro Cotta Badaro
           Jonas Gabriel
           
Doscente: Saulo Moraes
"""
from backtracking import Backtracking
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
    jug_array = [Jug(4),Jug(3), Jug(5)]

    node = Node(None, jug_array)

    node.control_strategy(1, 0)

    print(node.get_node_state())

if __name__ == "__main__":
    main()