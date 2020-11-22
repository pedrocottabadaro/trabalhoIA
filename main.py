# -*- coding: utf-8 -*-
"""
TRABALHO INTELIGENCIA ARTIFICIAL - PROBLEMA DO JOGO DOS JARROS
Inteligência Artificial - DCC014

Discentes: Davi Rezende
           Pedro Cotta Badaro
           Jonas Gabriel
           
Doscente: Saulo Moraes
"""
#from backtracking import Backtracking
from graph import Node, Graph, Edge
from jug import Jug
import copy


def backtracking(root):
   
  
    fracasso=False
    sucesso=False
    S=root
    N = copy.deepcopy(S)
    
    000
    while not (sucesso or fracasso):
        newNode=copy.deepcopy(N)
        
        if newNode.try_apply_rule()!=0:
            
            if newNode.is_solution():
                sucesso=True
                
        else:
            if newNode==S:
                fracasso=True
            else:
                N=newNode.get_parent_node()
        
            
                
            
    # início
    # S := estado inicial; N := S;
    # fracasso := F; sucesso := F;
    # enquanto não (sucesso ou fracasso) faça
    # se R(N) ≠ vazio então
    # selecione o operador r de R(N);
    # N := r(N);
    # se N é solução então
    # sucesso := T;
    # fim-se;
    # senão
    # se N = S então
    # fracasso := T;
    # senão
    # N := pai(N);
    # fim-se;
    # fim-se;
    # fim-enquanto;
    # fim.



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
    
    g=Graph(node)
    i=0
    
    while(i<=4):
        newNode=copy.deepcopy(node)
        
        x=newNode.try_apply_rule()
        
        if(x!=0):
            g.insert_node(newNode,"r"+str(x))
        
        i=i+1
        
        node=newNode
    
    print(node.operadores)
    
    
    g.print_graph()
    

    


if __name__ == "__main__":
    main()