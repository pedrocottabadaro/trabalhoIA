class Graph:
    """
    Represents a collection of a network of edges of connected nodes

    Args:
        none

    Returns:
        An graph representation containung the edges and vertices containing nodes

    """

    def __init__(self):
        self._edges = []
        self._vertices = []

    def get_edges(self):
        return self._edges

    def get_vertices(self):
        return self._vertices

    def insert_node(self, node, generating_rule):   
        if not node in self._vertices:     
            self._vertices.append(node) 
            self._edges.append(Edge(node.get_parent_node(), node, generating_rule))

    def print_graph(self):
        for edge in self._edges:
            print(edge.print_edge())


class Edge:
    """
    Defines an edge which holds references to both origin and destiny of a graph node.

    Args:
        none

    Returns:
        A reference to an edge object containing a node origin and a node destiny
    """
    
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
            return f"{self._generating_rule}: |-> {self._destiny.print_node()}"
        return f"{self._generating_rule}: {self._origin.print_node()} -> {self._destiny.print_node()}"

        
class Node:
    """
    Defines a node which contains a jug array.
    It also contains a parent node reference.

    Args:
        none

    Returns:
        A node instance containing a jug array and 
        a parent node reference.
    """
    
    def __init__(self, parent_node, jug_arr):
        self._parent_node = parent_node
        self._jug_arr = jug_arr
        
    def get_parent_node(self):
        return self._parent_node

    def set_parent_node(self, parent_node):
        self._parent_node = parent_node

    def get_jug_arr(self):
        return self._jug_arr
    
    def set_jug_arr(self, jug_arr):
        self._jug_arr = jug_arr

    def print_node(self):
        return [str(j.get_current_volume()) for j in self._jug_arr]