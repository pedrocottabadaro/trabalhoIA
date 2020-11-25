from graph import Node, Graph, Edge
from jug import Jug
import copy

def profundidade(s,target):
    print("-----PROFUNDIDADE------")
    g = Graph(s)
    n = copy.deepcopy(s)

    failure=False 
    success=False
    abertos = []
    fechados=[]
    contadorAbertos=0
    contadorFechados=0
    profundidade=0
    abertos.append(n)
    
    while not (success or failure):

        #se a pilha de abertos estiver vazia, falhou
        if len(abertos)==0:
            print(g.print_graph())
            print("FRACASSO")
            failure=True

        else:
            n=abertos.pop()

            #verifica se é solucao
            if(n.is_solution(target)):
                g.print_graph()
                print("SOLUCAO")
                print(n.get_node_state())
                success=True
                continue
            
            else:           
                i=0
                operator = 1
                jug_arr_len = len(n._jug_arr) - 1

                #enquanto ainda tiver jarros para alterar
                while(i <= jug_arr_len):
                    u=copy.deepcopy(n)
                    u.control_strategy(operator,i)

                    #tenta inserir o node no grafo
                    if(g.try_insert_node(u,"R"+str(i)+str(operator))):        
                        u.set_depth(n)
                        abertos.append(u)
                        contadorAbertos=contadorAbertos+1
                        g.print_graph()
                        operator=1
                        break 

                    #percorre todos os operadores
                    if operator == 4:
                        operator = 0
                        i = i + 1
               
                    operator=operator+1 

                #adiciona o no que acabou de ser expandido na lista de fechados  
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