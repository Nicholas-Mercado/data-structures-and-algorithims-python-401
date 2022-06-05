class Graph:
    '''Implement Graph data structure with following methods

    Methods:

        add_node(self, value)
        size(self)
        get_nodes(self)
        add_edge(self, start_vertex, end_vertex, weight=0)
        get_neighbors(self, vertex)
        
    '''

    def __init__(self):
        self._adjacency_list = {}

    def add_node(self, value):
        ''' Adds node to graph returns vertex

        Arg: value
        '''
        vertex = Vertex(value)
        self._adjacency_list[vertex] = []
        return vertex

    def size(self):

        return len(self._adjacency_list)

    def get_nodes(self):
        """
        Description of get_nodes

        Args: None

        """
        return self._adjacency_list.keys()

    def add_edge(self, start_vertex, end_vertex, weight=0):
        if start_vertex not in self._adjacency_list or end_vertex not in self._adjacency_list:
            raise KeyError()

        edge = Edge(end_vertex, weight)
        # appending to the list of _adjacency_list[start_vertex] not the Dict _adjacency_list
        self._adjacency_list[start_vertex].append(edge)

    def get_neighbors(self, vertex):
        return self._adjacency_list[vertex]

print(Graph.__doc__)

class Vertex:
    def __init__(self, value):
        self.value = value


class Edge:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight


