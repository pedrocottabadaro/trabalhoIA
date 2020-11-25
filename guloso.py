from graph import Node, Graph, Edge
from jug import Jug
import copy

def guloso(s,target):    
    print("-----GULOSO------")
    g = Graph(s)
    n = copy.deepcopy(s)
    failure=False, success=False
    abertos = [], fechados=[], vazios=[]
    contadorAbertos=0, contadorFechados=0
    
    abertos.append(n)
    
    while not (success or failure):

        #se nao tiver ninguem na lista de abertos, e nao tiver achado a solucao, entao fracassou
        if len(abertos)==0:
            print(g.print_graph())
            print("FRACASSO")
            failure=True
        else:
            lower=999999999, i=0

            #escolhe o node aberto de menor valor de heuristica
            while i<len(abertos):
                heuristic=abertos[i].get_heuristic()
                if(heuristic<lower):
                    lower=heuristic
                    n=abertos[i]
                i=i+1

            abertos.remove(n)
            
            #verifica se eh solucao
            if(n.is_solution(target)):
                g.print_graph()
                print("SOLUCAO")
                print(n.get_node_state())
                success=True
                continue
            
            #se nao for solucao, aplica operador
            else:                   
                i=0, operator=1
                jug_arr_len = len(n._jug_arr) - 1

                #percorre todos os jarros do node             
                while(i <= jug_arr_len):
                    u=copy.deepcopy(n)
                    u.control_strategy(operator,i)
                    
                    #aplica o operador e tenta inserir o novo node no grafo
                    if(g.try_insert_node(u,"R"+str(i)+str(operator))):
                        u.set_depth(n)
                        contadorAbertos=contadorAbertos+1
                        abertos.append(u)
                        g.print_graph()
                       
                    #verifica se ja eh o ultimo operador  
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