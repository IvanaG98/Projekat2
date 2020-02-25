class Set(object):

    def __init__(self):
        self.recnik = {}
        self.broj_reci = {}

    def unija(self, lista):

        for rec in lista:                   #prolazim kroz recnike koji su rezultat pretrage
            for link in rec:                #prolazim kroz prvi i uzimam njegove kljuceve
                if link not in self.recnik:
                    self.recnik[link] = rec[link]   #ako se rec nije uneta u recnik, dodaj je
                    self.broj_reci[link] = 1    #koliko se rijeci iz upita nalazi na nasoj stranici
                else:
                    self.recnik[link] += rec[link]  #ukoliko je rec pronadjena vec u recniku uvecaj broj ponavljanja za broj ponavljanja te rijeci u recniku kroz koji iteriramo
                    self.broj_reci[link] += 1

    def presek(self, listaA, listaB):
        """Proci ce kroz kljuceve i vrednosti dva recnika ciji presek trazimo i ukoliko pronadje iste reci u oba recnika
         upisacemo ih u novi."""
        self.recnik = {}
        for elA in listaA:
            for elB in listaB:
                if elA == elB:
                    self.recnik[elA] = listaA[elA] + listaB[elB]
                    self.broj_reci[elA] = 2    #uvijek ce biti unijete obe rijeci iz upita


    def komplement(self, lista):
        """Komplement ce dati samo one vrijednosti koje se nalaze u jednom rijecniku a ne nalaze se u drugom"""
        self.recnik = lista[0]
        for key in self.recnik:
            self.broj_reci[key] = 1     #broj rijeci iz upita koje se nalaze na stranici
        for link1 in lista[1]:          #prolazim kroz rijecnik koji je rezultat pretrage
            if link1 in self.recnik:    #ako je rec vec u nasem recniku
                del self.recnik[link1]  #izbrisi je