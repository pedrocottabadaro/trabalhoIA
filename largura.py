from graph import Node, Graph, Edge
from jug import Jug
import copy
import queue

def largura(s,target):
    print("-----LARGURA------")
    g = Graph(s)
    n = copy.deepcopy(s)
    contadorAbertos=0, contadorFechados=0
    failure=False, success=False
    abertos = queue.Queue() #fila de abertos
    fechados=[]#lista de fechados
    
    abertos.put(n)
    
    while not (success or failure):

        #se nao tiver mais nenhum no aberto, e nao tiver achado a solucao, entao falhou
        if abertos.qsize()==0:
            print(g.print_graph())
            print("FRACASSO")
            failure=True
        
        else:    
            n=abertos.get()#seleciona na lista de abertos
            
            #verifica se eh solucao
            if(n.is_solution(target)):
                g.print_graph()
                print("SOLUCAO")
                print(n.get_node_state())
                success=True
                continue
            
            else: #se nao for solucao, vamos expandir esse no 
                i=0, operator=1
                jug_arr_len = len(n._jug_arr) - 1
             
                #enquanto ainda tiver jarros para modificar
                while(i <= jug_arr_len):
                    u=copy.deepcopy(n)
                    u.control_strategy(operator,i)
                    
                    if(g.try_insert_node(u,"R"+str(i)+str(operator))):
                        u.set_depth(n)
                        abertos.put(u)
                        contadorAbertos=contadorAbertos+1
                        g.print_graph()
                         
                    if operator == 4:
                        operator = 0
                        i = i + 1
               
                    operator=operator+1 

                #adiciona o no expandido na lista de fechados                 
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