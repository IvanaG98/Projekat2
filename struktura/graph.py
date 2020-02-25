class Graph(object):

    """Graf je usmeren."""

    def __init__(self, graph_dict = None):
        """graf je rijecnik, gdje je kljuc link str na kojoj se nalazimo
           a vrijednost je lista linkova na koje ta stranica pokazuje.
        """
        if graph_dict == None:
            graph_dict = {}
        self.graph_dict = graph_dict

    def vertices(self):
        """Metoda vraca cvorove grafa koji predstavljaju kljuceve."""
        return list(self.graph_dict.keys())

    def edges(self):
        """Metoda vraca veze u grafu."""
        return self.__generate_edges()

    def add_vertex(self, vertex):
        """Ukoliko cvorovi ne postoje u recniku grafa, kljuc sa praznom listom za vrijednost je dodat u rijecnik."""

        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = []          #dodaje kljuc koji nema vrednost u ovom trenutku

    def add_edge(self, edge):
        """Metoda koja dodaje veze izmedju cvorova, veza moze biti vise."""
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.graph_dict:
            self.graph_dict[vertex1].append(vertex2)
        else:
            self.graph_dict[vertex1] = [vertex2]

    def __generate_edges(self):
        edges = []
        for vertex in self.graph_dict:                      #prolazimo kroz kljuceve
            for neighbour in self.graph_dict[vertex]:       #prolazimo kroz vrijednosti
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})       #dodavanje na kraj liste
        return edges

    def __str__(self):
        res = "cvorovi: "
        for k in self.graph_dict:
            res += str(k) + " "
        res += "\nveze: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res
