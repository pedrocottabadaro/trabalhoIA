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



