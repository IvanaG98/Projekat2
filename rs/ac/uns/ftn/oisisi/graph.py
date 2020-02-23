#uvezati
class Graph(object):

    def __init__(self, graph_dict=None):        #self uvijek pisem kod klase
        """ initializes a graph object          graf je rijecnik, gdje je kljuc link str na kojoj se nalazimo
            If no dictionary or None is given,  a vrijednost je lista linkova na koje ta str pokazuje, koji imaj u toj stranici
            an empty dictionary will be used    Tuple je niz u pythonu, i predstavlja vezu
        """
        if graph_dict == None:
            graph_dict = {}
        self.graph_dict = graph_dict

    def vertices(self):                 #cvorovi
        """ returns the vertices of a graph """
        return list(self.graph_dict.keys())

    def edges(self):                    #veze
        """ returns the edges of a graph """
        return self.__generate_edges()

    def add_vertex(self, vertex):
        """ If the vertex "vertex" is not in
            self.__graph_dict, a key "vertex" with an empty
            list as a value is added to the dictionary.
            Otherwise nothing has to be done.
        """
        if vertex not in self.__graph_dict:
            self.graph_dict[vertex] = []          #dodaje kljuc koji nema vred u ovom trenutku

    def add_edge(self, edge):
        """ assumes that edge is of type set, tuple or list;
            between two vertices can be multiple edges!
        """
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict:
            self.graph_dict[vertex1].append(vertex2)
        else:
            self.graph_dict[vertex1] = [vertex2]

    def __generate_edges(self):
        """ A static method generating the edges of the
            graph "graph". Edges are represented as sets
            with one (a loop back to the vertex) or two
            vertices
        """
        edges = []
        for vertex in self.graph_dict:            #ovako se prolazi kroz kljuceve
            for neighbour in self.graph_dict[vertex]: #ovako kroz vrijednosti
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})   #dodavanje na kraj liste
        return edges

    def __str__(self):
        res = "vertices: "
        for k in self.graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res
