from struktura.graph import *
from struktura.Trie import *
from util.parser import *

class ParsFiles(object) :
    def __init__(self):
        self.recnik = {}
        self.graph = Graph()
        self.trie = TrieNode(-1)

    def parseFile(self):
        print("Unesite putanju:\n")

        rootdir = input()

        if not os.path.exists(rootdir):
            print("Putanja koju ste unijeli je pogresna.\n")
            exit()

        parser = Parser()
        for subdir, dirs, files in os.walk(rootdir):
            for file in files:
                file1 = os.path.join(subdir, file)      #putanja do svakog fajla

                if file1.endswith(".html"):
                    parser.parse(file1)

                    for word in parser.words:
                        add(self.trie, word.lower(), file1)

                    self.graph.add_vertex(file1)
                    for link in parser.links:
                        self.graph.add_edge((file1, link))



