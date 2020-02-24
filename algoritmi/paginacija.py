from math import ceil

from algoritmi.ispis import *

class Paginacija(object):

    def __init__(self, ukupno, po_stranici, trenutna):
        self.ukupno = ukupno
        self.po_stranici = po_stranici
        self.trenutna = trenutna

    def paginacija(self, broj, lista):
        self.po_stranici = broj
        if lista == []:
            print("ne postoji stranica koja ispunjava te zahtjeve")
            exit()
        listaDela = []
        for i in range(0, len(lista), self.po_stranici):
            deo = lista[i:i + self.po_stranici]
            listaDela.append(deo)

        return listaDela

    def ispisiStranu(self, listaDela, recnik):
        ispis = Ispis()
        ispis.prikazRezultata(recnik, listaDela[self.trenutna])


    def ukupan_broj_strana(self):
        return int(ceil(float(self.ukupno) / self.po_stranici))

    def sledeca_strana(self):
        str = self.ukupan_broj_strana()
        if self.trenutna + 1 != str:
            self.trenutna += 1
            return True
        else:
            print("Dosli ste do kraja! Ne postoji naredna stranica.")
            return False

    def prethodna_strana(self):
        if self.trenutna != 0:
            self.trenutna -= 1
            return True
        else:
            print("Na prvoj ste stranici! Ne postoji prethodna.")
            return False
