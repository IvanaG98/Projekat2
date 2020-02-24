class Set(object):

    def __init__(self):
        self.recnik = {}
        self.broj_reci = {}

    def unija(self, lista):
        for rec in lista:       #prolazim kroz sve recnike
            for link in rec:    #prolazim kroz prvi i uzimam njegove kljuceve
                if link not in self.recnik:   #ubacujem u svoj
                    self.recnik[link] = rec[link] #dodajem kljuc i vrednost
                    self.broj_reci[link] = 1
                else:
                    self.recnik[link] += rec[link]
                    self.broj_reci[link] += 1

    def presek(self, listaA, listaB):
        self.recnik = {}
        for elA in listaA:
            for elB in listaB:
                if elA == elB:
                    self.recnik[elA] = listaA[elA] + listaB[elB]
                    self.broj_reci[elA] = 2


    def komplement(self, lista):
        self.recnik = lista[0]
        for key in self.recnik:
            self.broj_reci[key] = 1
        for link1 in lista[1]:
            if link1 in self.recnik:
                del self.recnik[link1]