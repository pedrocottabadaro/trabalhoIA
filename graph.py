class Graph:
    """
    Represents a collection of a network of edges of connected nodes

    Args:
        none

    Returns:
        An graph representation containung the edges and vertices containing nodes

    """

    def __init__(self, root):
        self._root = root
        self._edges = []
        self._vertices = []
        self.try_insert_node(self._root, "root")

    def get_edges(self):
        return self._edges

    def get_vertices(self):
        return self._vertices

    def try_insert_node(self, node, generating_rule):
        if not node in self._vertices:
            self._vertices.append(node)
            self._edges.append(
                Edge(node.get_parent_node(), node, generating_rule))
            return True
        return False

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
            return f"{self._generating_rule}: |-> {self._destiny.get_node_state()}"
        return f"{self._generating_rule}: {self._origin.get_node_state()} -> {self._destiny.get_node_state()}"


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
        self._operator = 0

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

    def transfer_to_left(self, jug_pos):
        left_jug = self._jug_arr[jug_pos-1]
        return self._jug_arr[jug_pos].transfer_to(left_jug)

    def transfer_to_right(self, jug_pos):
        if jug_pos == (len(self._jug_arr)-1):
            return self._jug_arr[jug_pos].transfer_to(self._jug_arr[0])
        else:
            return self._jug_arr[jug_pos].transfer_to(self._jug_arr[jug_pos+1])

    def control_strategy(self, operator, index):
        """
        Try to apply the given operation.
        Returns True for success and False for failure
        """
        if operator == 1:
            return self._jug_arr[index].fill()
        elif operator == 2:
            return self.transfer_to_left(index)
        elif operator == 3:
            return self.transfer_to_right(index)
        elif operator == 4:
            return self._jug_arr[index].spill()

    def is_solution(self, target_amount):
        """
        Checks if given Node has the target amount in one of its jugs
        Returns true for success, false otherwise
        """
        if self._jug_arr is None:
            return False

        for x in self._jug_arr:
            if x.get_current_volume() == target_amount:
                return True
        return False

    def try_apply_rule(self, g):
        """
        Retrieves which rule was applied to this Node
        The rule applied is binded to the control strategy
        If no rules were applied, returns 0
        """

        i = 0
        operator = 1
        jug_arr_len = len(self._jug_arr) - 1

        while(i <= jug_arr_len):
            if operator > self._jug_arr[i].get_operator() and self.control_strategy(operator, i) and g.try_insert_node(self, "r"+ str(operator)):
                self._jug_arr[i].set_operator(operator)
                return operator                 

            if operator == 4:
                operator = 0
                i = i + 1
            
            operator = operator + 1
       
        return 0
