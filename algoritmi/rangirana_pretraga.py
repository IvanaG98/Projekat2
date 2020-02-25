from algoritmi.pretraga_rijeci import *

class Rangiranje(object):

    def __init__(self):
        self.recnik = {}
        self.par1 = 0      #broj linkova koji ukazuju na nasu stranicu
        self.par2 = 0      #broj rijeci koje se nalaze na stranici
        self.par3 = 0      #broj rijeci na stranici koja ukazuje na nasu
        self.par4 = 1      #koliko se rijeci iz upita pojavljuje na nasoj stranicu

    def rangiranje(self, lista, graph, words, parser, broj_reci):
        rez = {}
        if len(words) > 2:                  #ukoliko je unijet upit sa operatorima
            if words[1] == "and":           #i ukoliko je operator and
                words[1] = "or"             #posmatraj ga kao or
                (rez, b) = pretraga(words, parser)
            elif words[1] == "not":
                (rez, b) = pretraga(words[0], parser)
            else:
                (rez, b) = pretraga(words, parser)
        for str in lista:
            self.par2 = lista[str]           #broj rijeci na stranici
            self.par4 = broj_reci[str]       #koliko reci iz upita se nalazi na nasoj stranici
            for key in graph.graph_dict:
                if str in graph.graph_dict[key]:    #prodjem kroz sve stranice na kojima se pominje unesena rijec
                    self.par1 += 1                  #uvecam broj linkova ka njoj
                    for i in rez:
                        if i == key:
                            self.par3 += rez[key]  #svaki put kad naidje na tu rijec na nekom linku koji ukazuje na nju uveca je za tu vrednost

            #najveci uticaj na rangiranje imace broj rijeci na linku koji pokazuje na nasu stranicu
            #potom broj rijeci na stranici
            #i broj linkova na nju

            rang = (0.5 * self.par3 + 0.3 * self.par2 + 0.2 * self.par1) * self.par4

            self.recnik[rang] = (str, self.par1, self.par2, self.par3, self.par4)
        return self.recnik

