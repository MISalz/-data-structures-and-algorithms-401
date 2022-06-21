class Graph:
    """
    The graph should be represented as an adjacency list, and should include the following methods:

add node
    Arguments: value
    Returns: The added node
    Add a node to the graph
add edge
    Arguments: 2 nodes to be connected by the edge, weight (optional)
    Returns: nothing
    Adds a new edge between two nodes in the graph
    If specified, assign a weight to the edge
    Both nodes should already be in the Graph
get nodes
    Arguments: none
    Returns all of the nodes in the graph as a collection (set, list, or similar)
get neighbors
    Arguments: node
    Returns a collection of edges connected to the given node
    Include the weight of the connection in the returned collection
size
    Arguments: none
    Returns the total number of nodes in the graph
    """

    def __init__(self):
        self._adjacency_list = {}

    def add_node(self, value):
        vertex =  Vertex(value)
        #sets vertex as the key with a blank value in adj list
        self._adjacency_list[vertex]=[]
        return vertex

    def size(self):
        return len(self._adjacency_list)

    def get_nodes(self):
        return self._adjacency_list.keys()

    def add_edge(self, start_vertex, end_vertex, weight=0):
        if start_vertex not in self._adjacency_list or end_vertex not in self._adjacency_list:
            raise KeyError

        edge = Edge(end_vertex, weight)

        self._adjacency_list[start_vertex].append(edge)

    def get_neighbors(self, vertex):
        return self._adjacency_list[vertex]

    def breadth_first(self, vertex):
        '''
        Arguments: Node
        Return: A collection of nodes in the order they were visited.
        Display the collection
        '''

        pass


class Vertex:
    def __init__(self,value):
        self.value = value

class Edge:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight
