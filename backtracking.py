from graph import Node, Graph, Edge
from jug import Jug
import copy

def backtracking(s, target):      
    print("-----BACKTRACKING------")
    g = Graph(s)
    n = copy.deepcopy(s)
    contadorPercorridos=0
    failure=False
    success=False
  
    while not (success or failure):  
        new_node = copy.deepcopy(n)
        new_node.set_parent_node(n)
        #aplica uma regra, baseado na estrategia de controle
        generation_rule = new_node.try_apply_rule(g)
        
        if generation_rule != 0:
            contadorPercorridos=contadorPercorridos+1
            n = new_node
            
            #verifica se é solucao
            if n.is_solution(target):
                g.print_graph()
                print("SOLUCAO")
                print(new_node.get_node_state())
                success=True

            else:
                g.print_graph()
                print()
                
        #se nao tiver operadores aplicaveis, verifica se esta na raiz
        else:
            #se estiver na raiz, o algoritmo falhou
            if n.get_node_state() == s.get_node_state():
                print("FRACASSO")
                failure=True

            #se nao for raiz, faz backtracking pro pai
            else:
                print("BACKTRACKING")  
                print(str(n.get_node_state())+"---->"+str(n.get_parent_node().get_node_state())) 
                n = n.get_parent_node()    
        print("---------------------------------")
        print()
    print("NOS VISITADOS = "+str(contadorPercorridos))
    maior=0
    for x in g._vertices:
        if(x.get_depth()):
            maior=x.get_depth()
    
    print("PROFUNDIDADE = "+str(maior))