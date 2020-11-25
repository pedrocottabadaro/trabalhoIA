from graph import Node, Graph, Edge
from jug import Jug
import copy
import queue
import time
import random


def largura(s,target):
    print("-----LARGURA------")
    g = Graph(s)
    n = copy.deepcopy(s)
    contadorAbertos=0
    contadorFechados=0


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
                        u.set_depth(n)
                        abertos.put(u)
                        contadorAbertos=contadorAbertos+1
                        g.print_graph()
                       
                      
                    if operator == 4:
                        operator = 0
                        i = i + 1
               
                    operator=operator+1 
                
                                        
                fechados.append(n)
                contadorFechados=contadorFechados+1
                del n

        print("---------------------------------")
        print()
    print("NOS ABERTOS = "+str(contadorAbertos))
    print("NOS FECHADOS = "+str(contadorFechados))
    maior=0
    for x in g._vertices:
        if(x.get_depth()):
            maior=x.get_depth()
    
    print("PROFUNDIDADE = "+str(maior))

