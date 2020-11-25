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
import time
import random



def ordenada(s,target):
    print("-----ORDENADA------")

    g = Graph(s)
    n = copy.deepcopy(s)

    failure=False
    success=False
    abertos = []
    
    fechados=[]
    
    abertos.append(n)
    inicio=True
    while not (success or failure):

        pai=copy.deepcopy(s)
        if len(abertos)==0:
            print(g.print_graph())
            print("FRACASSO")
            failure=True
        else:
            lower=999999999
            i=0
            
            while i<len(abertos):
                parentWeight=0
                x=abertos[i]
                if(n.get_parent_node()!=None):
                    parentWeight=x.get_parent_node().get_weight()
                weight=n.get_weight()+parentWeight
                if(weight<lower):
                    lower=weight
                    n=abertos[i]
                    
                i=i+1
            abertos.remove(n)
            fechados.append(n)
            
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
                    insert=True
                    u=copy.deepcopy(n)
                    u.control_strategy(operator,i)
                    u.set_parent_node(n)

                    for v in fechados:
                        if v.get_node_state() == u.get_node_state():
                            insert=False       
                        
                    if(insert):
                        u.set_weight(n,target)
                        g.insert_node_LP(u,"R"+str(i)+str(operator))
                        abertos.append(u)
                        g.print_graph()
                    
                    if operator == 4:
                        operator = 0
                        i = i + 1
               
                    operator=operator+1 
                
    print("---------------------------------")
    print()



def gulosa(s,target):
    
    print("-----GULOSA------")
  
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
            lower=999999999
            i=0
            while i<len(abertos):
                heuristic=abertos[i].get_heuristic()
                if(heuristic<lower):
                    lower=heuristic
                    n=abertos[i]
                i=i+1
            abertos.remove(n)
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
    print("---------------------------------")
    print()





def profundidade(s,target):
    print("-----PROFUNDIDADE------")
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

    print("---------------------------------")
    print()

def largura(s,target):
    print("-----LARGURA------")
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

    print("---------------------------------")
    print()



def backtracking(s, target):  
    
    print("-----BACKTRACKING------")
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
                
        print("---------------------------------")
        print()

            
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
    f = open("entrada.txt", "r")
    target_amount = int(f.readline())

    for x in f:
        jug_list.append(Jug(int(x.strip())))

    root = Node(None, jug_list)

    backtracking(root, target_amount)
    largura(root, target_amount)
    profundidade(root, target_amount)
    largura(root, target_amount)
    gulosa(root, target_amount)
    ordenada(root, target_amount)


if __name__ == "__main__":
    main()