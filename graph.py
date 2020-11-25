import copy
class Graph:

    #construtor
    def __init__(self, root):
        self._root = root
        self._edges = []
        self._vertices = []
        self.try_insert_node(self._root, "root")

    def get_edges(self):
        return self._edges

    def get_vertices(self):
        return self._vertices

    #verifica se o node ja esta no grafo, para realizar a insercao
    def try_insert_node(self, node, generating_rule):

        for v in self._vertices:
            if v.get_node_state() == node.get_node_state():
                return False

        self._vertices.append(node)
        self._edges.append(
            Edge(node.get_parent_node(), node, generating_rule))
        return True
    
    #Insere node sem verificar (pode inserir repetido)
    def insert_node_LP(self, node, generating_rule): 
        self._vertices.append(node)
        self._edges.append(
            Edge(node.get_parent_node(), node, generating_rule))
        
    #verifica se um node esta no grafo
    def check_insert_node(self,node):
        
        for v in self._vertices:
            if v.get_node_state() == node.get_node_state():
                return False
        return True
        
    #imprime o grafo
    def print_graph(self):
        for edge in self._edges:
            print(edge.print_edge())

class Edge:
    #construtor
    def __init__(self, origin, destiny, generating_rule):
        self._origin = origin
        self._destiny = destiny
        self._generating_rule = generating_rule

    def get_origin(self):
        return self._origin

    def get_destiny(self):
        return self._destiny

    def get_generating_rule(self):
        return self._generating_rule

    def print_edge(self):
        if self._origin is None:
            return f"{self._generating_rule}: |-> {self._destiny.get_node_state()}"
        return f"{self._generating_rule}: {self._origin.get_node_state()} -> {self._destiny.get_node_state()} | {self._destiny.get_weight()}"

class Node:
    #construtor
    def __init__(self, parent_node, jug_arr):
        self._parent_node = parent_node
        self._jug_arr = jug_arr
        self._heuristic=0
        self._weight=0
        self._depth=0
        
    def get_heuristic(self):
        self._heuristic=0
        for x in self._jug_arr:
            self._heuristic+=x.get_current_volume()
        return self._heuristic
    
    def get_depth(self):
        return self._depth
    
    def set_depth(self,parentNode):
        self._depth=1+(parentNode.get_depth())
    
    def get_weight(self):
        return self._weight
    
    #o peso utilizado foi o volume total do node
    def set_weight(self,target):
        for x in self._jug_arr:
            self._weight+=x.get_current_volume()
        
        if(self._parent_node!=None):
            self._weight=self._weight+self._parent_node.get_weight()
            self._weight=abs(self._weight-target)
            
        else:
            self._weight=0
        
    def get_parent_node(self):
        return self._parent_node

    def set_parent_node(self, parent_node):
        self._parent_node = parent_node

    def get_jug_arr(self):
        return self._jug_arr

    def set_jug_arr(self, jug_arr):
        self._jug_arr = jug_arr

    def get_node_state(self):
        return [str(j.get_current_volume()) for j in self._jug_arr]

    #chama o operador de transferir, passando como parametro o jarro a esquerda
    def transfer_to_left(self, jug_pos):
        return self.transfer_to(jug_pos, jug_pos-1)

    #chama o operador de transferir, passando como parametro o jarro a direita
    def transfer_to_right(self, jug_pos):
        if jug_pos == (len(self._jug_arr)-1):
            return self.transfer_to(jug_pos, 0)
        else:
            return self.transfer_to(jug_pos, jug_pos+1)

    #operador de transferencia
    def transfer_to(self, source_jug_index, target_jug_index):
        source_jug = self._jug_arr[source_jug_index]
        target_jug = self._jug_arr[target_jug_index]

        if not source_jug.get_current_volume() == 0 and target_jug.get_current_volume() != target_jug.get_total_capacity():
            transfer_volume = target_jug.get_total_capacity() - target_jug.get_current_volume()

            if transfer_volume >= source_jug.get_current_volume():
                transfer_volume = source_jug.get_current_volume()

            source_jug.set_current_volume(
                source_jug.get_current_volume() - transfer_volume)
            target_jug.set_current_volume(
                target_jug.get_current_volume() + transfer_volume)

            self._jug_arr[source_jug_index] = source_jug
            self._jug_arr[target_jug_index] = target_jug
            return True
        return False

    #Tenta aplicar um operador, retornando true (success) ou false
    def control_strategy(self, operator, index):
        if operator == 1:
            return self._jug_arr[index].fill()
        elif operator == 2:
            return self.transfer_to_left(index)
        elif operator == 3:
            return self.transfer_to_right(index)
        elif operator == 4:
            return self._jug_arr[index].spill()

    #verifica se um node é solucao
    def is_solution(self, target_amount):
        if self._jug_arr is None:
            return False

        for x in self._jug_arr:
            if x.get_current_volume() == target_amount:
                return True
        return False

    #tenta aplicar um operador, se conseguir, aplica, tenta inserir no grafo, e retorna a regra aplicada
    def try_apply_rule(self, g):
        i = 0
        operator = 1
        jug_arr_len = len(self._jug_arr) - 1

        while(i <= jug_arr_len):
            nodeAux=copy.deepcopy(self)
            nodeAux.control_strategy(operator, i) 
            
            if g.check_insert_node(nodeAux):
                self.control_strategy(operator, i) 
                g.try_insert_node(self,"R"+str(i)+str(operator))
                self.set_depth(self.get_parent_node())
                return operator

            if operator == 4:
                operator = 0
                i = i + 1

            operator = operator + 1
        return 0