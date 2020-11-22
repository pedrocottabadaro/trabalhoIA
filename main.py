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


def backtracking(s, target):  
    g = Graph(s)
    n = copy.deepcopy(s)
   
    failure=False
    success=False
  
    while not (success or failure):       
        new_node = copy.deepcopy(n)
        new_node.set_parent_node(n)

        generation_rule = new_node.try_apply_rule(g)

        if generation_rule != 0:
            n = new_node

            if n.is_solution(target):
                success=True
            else:
                g.print_graph()
                print()
                
        else:
            if n.get_node_state() == s.get_node_state():
                failure=True
            else:
                n = n.get_parent_node()
                print("bt")   
            
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

    backtracking(Node(None, [Jug(4), Jug(3)]), 2)
if __name__ == "__main__":
    main()