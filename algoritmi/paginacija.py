from math import ceil

from algoritmi.ispis import *

class Paginacija(object):

    def __init__(self, ukupno, po_stranici, trenutna):
        self.ukupno = ukupno                #ukupan broj stranica
        self.po_stranici = po_stranici      #podjela po stranicama
        self.trenutna = trenutna            #na kojoj smo trenutno stranici

    def paginacija(self, broj, lista):
        """Metoda koja ce u zavisnosti od prosledjenog broja na paginaciju ispisati toliko stranica"""

        self.po_stranici = broj

        if lista == []:
            print("Ne postoji stranica koja ispunjava te zahtjeve.\n")
            exit()

        listaDela = []           #podijelicemo listu na dijelove da bi nam u zavisnosti od unijetog broja strana koji zelimo ispisao te strane

        for i in range(0, len(lista), self.po_stranici):
            deo = lista[i:i + self.po_stranici]
            listaDela.append(deo)

        return listaDela

    def ispisiStranu(self, listaDela, recnik):          #ispis trenutne stranice na kojoj se nalazimo
        ispis = Ispis()
        ispis.prikazRezultata(recnik, listaDela[self.trenutna])

    def ukupan_broj_strana(self):                       #racuna ukupan broj strana kako bismo znali da li mozemo da se pomerimo na naredmu
        return int(ceil(float(self.ukupno) / self.po_stranici))

    def sledeca_strana(self):                           #preci ce na narednu stranu ukoliko takva postoji
        str = self.ukupan_broj_strana()
        if self.trenutna + 1 != str:
            self.trenutna += 1
            return True
        else:
            print("Dosli ste do kraja! Ne postoji naredna stranica.\n")
            return False

    def prethodna_strana(self):                         #vratice se na prethodnu stranu ukoliko se ne nalazi na prvoj stranici
        if self.trenutna > 0:
            self.trenutna -= 1
            return True
        else:
            print("Na prvoj ste stranici! Ne postoji prethodna.\n")     #inace ce ispisati da nije moguce
            return False