from algoritmi.pretraga_rijeci import *

class Rangiranje(object):

    def __init__(self):
        self.recnik = {}
        self.par1 = 0
        self.par2 = 0
        self.par3 = 0   # broj rijeci na stranici koja ukazuje na nasu
        self.par4 = 1
       # self.listaRangova = []

    def rangiranje(self, lista, graph, words, parser, broj_reci):
        rez = {}
        if len(words) > 2 :
            if words[1] == "and":
                words[1] = "or"
                (rez,b) = wordSearch(words, parser)
            elif words[1] == "not":
                (rez, b) = wordSearch(words[0], parser)
            else:
                (rez, b) = wordSearch(words, parser)
        for str in lista:
            self.par2 = lista[str] #broj rijeci na stranici
            self.par4 = broj_reci[str] #koliko reci iz upita se nalazi na nasoj stranici
            for key in graph.graph_dict:
                if str in graph.graph_dict[key]:
                    self.par1 += 1
                    for i in rez:
                        if i == key:
                            self.par3 += rez[key]

            rang = (0.8 * self.par1 + 0.6 * self.par3 + 0.4 * self.par2) * self.par4
            self.recnik[rang] = (str, self.par1, self.par2, self.par3, self.par4)
        return self.recnik

