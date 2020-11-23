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
import queue


def profundidade(s,target):
     
    g = Graph(s)
    n = copy.deepcopy(s)

    failure=False
    success=False
    abertos = []
    
    fechados=[]
    vazios=[]
    
    
    abertos.append(n)
    
    while not (success or failure):
        
    
        if len(abertos)==0:
            print(g.print_graph())
            print("FRACASSO")
            failure=True
        else:
            
            n=abertos.pop()
            if(n.is_solution(target)):
                g.print_graph()
                print("SOLUCAO")
                print(n.get_node_state())
                success=True
                continue
            else: 
                              
                i=0
                operator=1
                jug_arr_len = len(n._jug_arr) - 1
             
                while(i <= jug_arr_len):
                    u=copy.deepcopy(n)
                    u.control_strategy(operator,i)
                    ##MUDAR PARA INSERT NODE. PARA PERMITIR NOS IGUAIS NO MESMO NIVEL
                    if(g.try_insert_node(u,"R"+str(i)+str(operator))):
                        
                        abertos.append(u)
                        g.print_graph()
                       
                        operator=1
                        continue 
                      
                    if operator == 4:
                        operator = 0
                        i = i + 1
               
                    operator=operator+1 
                
                                        
                fechados.append(n)
                del n



def largura(s,target):
     
    g = Graph(s)
    n = copy.deepcopy(s)

    failure=False
    success=False
    abertos = queue.Queue()
    
    fechados=[]
    vazios=[]
    
    
    abertos.put(n)
    
    while not (success or failure):
        
    
        if abertos.qsize()==0:
            print(g.print_graph())
            print("FRACASSO")
            failure=True
        else:
            
            n=abertos.get()
            if(n.is_solution(target)):
                g.print_graph()
                print("SOLUCAO")
                print(n.get_node_state())
                success=True
                continue
            else: 
                              
                i=0
                operator=1
                jug_arr_len = len(n._jug_arr) - 1
             
                while(i <= jug_arr_len):
                    u=copy.deepcopy(n)
                    u.control_strategy(operator,i)
                    ##MUDAR PARA INSERT NODE. PARA PERMITIR NOS IGUAIS NO MESMO NIVEL
                    if(g.try_insert_node(u,"R"+str(i)+str(operator))):
                        
                        abertos.put(u)
                        g.print_graph()
                       
                        operator=1
                        continue 
                      
                    if operator == 4:
                        operator = 0
                        i = i + 1
               
                    operator=operator+1 
                
                                        
                fechados.append(n)
                del n





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
                g.print_graph()
                print("SOLUCAO")
                print(new_node.get_node_state())
                

                success=True
            else:
                g.print_graph()
                print()
                
        else:
            if n.get_node_state() == s.get_node_state():
                print("FRACASSO")
                failure=True
            else:
                
                print("BACKTRACKING")  
                print(str(n.get_node_state())+"---->"+str(n.get_parent_node().get_node_state())) 
                n = n.get_parent_node()
            
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
    
    

    # backtracking(Node(None, [Jug(1), Jug(1)]), 2)
    #largura(Node(None, [Jug(4), Jug(5)]), 2)
    profundidade(Node(None, [Jug(4), Jug(5)]), 2)


if __name__ == "__main__":
    main()