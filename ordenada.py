from graph import Node, Graph, Edge
from jug import Jug
import copy

def ordenada(s,target):
    print("-----ORDENADA------")
    g = Graph(s)
    n = copy.deepcopy(s)

    failure=False, success=False, inicio=True
    abertos = [], fechados = []
    contadorAbertos = 0, contadorFechados = 0
    
    abertos.append(n)
    while not (success or failure):
        
        #se nao tiver mais nenhum no aberto, e nao tiver achado a solucao, entao falhou
        if len(abertos)==0:
            print(g.print_graph())
            print("FRACASSO")
            failure=True
        else:
            lower=999999999
            i=0
            
            #seleciona o menor custo da lista de abertos
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
            contadorFechados=contadorFechados+1
            
            #verifica se eh solucao
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

                    #verifica se o node esta na lista de fechados, para nao gerar um repetido
                    for v in fechados:
                        if v.get_node_state() == u.get_node_state():
                            insert=False       
                        
                    if(insert):
                        u.set_weight()
                        u.set_depth(n)
                        g.insert_node_LP(u,"R"+str(i)+str(operator))
                        abertos.append(u)
                        contadorAbertos=contadorAbertos+1
                        g.print_graph()
                    
                    #verifica se ja esta no ultimo operador
                    if operator == 4:
                        operator = 0
                        i = i + 1
               
                    operator=operator+1 
                
        print("---------------------------------")
        print()
        
    print("NOS ABERTOS = "+str(contadorAbertos))
    print("NOS FECHADOS = "+str(contadorFechados))
    maior=0
    for x in g._vertices:
        if(x.get_depth()):
            maior=x.get_depth()
            
        if(x.is_solution(target)):
            custo=x.get_weight()
    
    print("PROFUNDIDADE = "+str(maior))
    print("CUSTO = "+str(custo))