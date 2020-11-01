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
           
    def is_new_state(self, state):
        return state in self._closed_states
           
    def insert_node(self, node):   
        if not self.is_new_state(node.get_state()):     
            self._vertices.append(node) 
            self._edges.append(Edge(node.get_parent_node(), node))

class Edge:
    """
    Defines an edge which holds references to both origin and destiny of a graph node.

    Args:
        none

    Returns:
        A reference to an edge object containing a node origin and a node destiny
    """
    
    def __init__(self, origin, destiny):
        self._origin = origin
        self._destiny = destiny
    
    def get_origin(self):
        return self._origin
    
    def set_origin(self, n):
        self._origin = n
    
    def get_destiny(self):
        return self._destiny
    
    def set_destiny(self, n):
        self._destiny = n

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
    
    def __init__(self, jug_arr, parent_node):
        self._jug_arr = jug_arr
        self._parent_node = parent_node

    def get_parent_node(self):
        return self._parent_node

    def set_parent_node(self, parent_node):
        self._parent_node = parent_node

    def get_jug_arr(self):
        return self._jug_arr
    
    def set_jug_arr(self, jug_arr):
        self._jug_arr = jug_arr

    def get_state(self):
        self._state = ','.join(_jug_arr)