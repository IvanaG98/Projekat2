
from rs.ac.uns.ftn.oisisi.pretraga_rijeci import *

class Rangiranje(object):

    def __init__(self):
        self.recnik = {}
        self.par1 = 0
        self.par2 = 0
        self.par3 = 0   # broj rijeci na stranici koja ukazuje na nasu
        self.par4 = 1
        self.N=0
        self.listaRangova = []
        self.listaPar1=[]

    def rangiranje(self, lista, graph, words, parser, broj_reci):
        for str in lista:
            self.par2 = lista[str] #broj rijeci na stranici
            self.par4 = broj_reci[str] #koliko reci iz upita se nalazi na nasoj stranici
            for key in graph.graph_dict:
                if str in graph.graph_dict[key]:
                    self.par1 += 1
                    rez = wordSearch(words, parser)
                    if key in rez:
                        self.par3 += rez[key]
            rang = (0.8 * self.par1 + 0.6 * self.par3 + 0.4 * self.par2) * self.par4
            self.recnik[rang] = str
       # print(self.recnik)

        listaRangova = list(self.recnik.keys())

        #print(listaRangova)

        n = len(listaRangova)
        for i in range(n):
            for j in range(0, n - i - 1):
                 if listaRangova[j] < listaRangova[j + 1]:
                   listaRangova[j], listaRangova[j + 1] = listaRangova[j + 1], listaRangova[j]
        for i in range(n):
            key = listaRangova[i]
            pomocna = self.recnik[key]
            print(key, pomocna)

      #  print(listaRangova)
        return self.recnik, self.N,listaRangova


