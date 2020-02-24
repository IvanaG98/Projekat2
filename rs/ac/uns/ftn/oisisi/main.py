from rs.ac.uns.ftn.oisisi.ispis import *
from rs.ac.uns.ftn.oisisi.paginacija import *
from rs.ac.uns.ftn.oisisi.parsiranje import *
from rs.ac.uns.ftn.oisisi.rangirana_pretraga import *
from rs.ac.uns.ftn.oisisi.pretraga_rijeci import *

def pickOption(option):
    parser = ParsFiles()
    ranger = Rangiranje()


    if option == 1:
        parser.parseFile()
        print("Parsiranje je zavrseno.\n")
        return

    if option == 2:
        parser.parseFile()
        reci = input("Unesite rijeci za pretragu:")
        (result, broj_reci) = wordSearch(reci, parser)
        for keys, values in result.items():
            print(keys, values)
        return

    if option == 3:
        parser.parseFile()
        reci = input("Unesite rijeci za pretragu:")
        (result, broj_reci) = wordSearch(reci, parser)
        ranger.rangiranje(result, parser.graph, reci, parser, broj_reci)
        print(result)
        return

    if option == 4:
        parser.parseFile()
        reci = input("Unesite rijeci za pretragu:")
        (result, broj_reci) = wordSearch(reci, parser)
        ranger.rangiranje(result, parser.graph, reci, parser, broj_reci)
        lista = sortiranje(ranger.recnik)
        ispis = Ispis()
        ispis.prikazRezultata(ranger.recnik, lista)
        return

    if option == 5:
        parser.parseFile()
        reci = input("Unesite rijeci za pretragu:")
        (result, broj_reci) = wordSearch(reci, parser)
        ranger.rangiranje(result, parser.graph, reci, parser, broj_reci)
        lista = sortiranje(ranger.recnik)
        paginator = Paginacija(len(lista), 5, 0)
        pag = paginator.paginacija(5, lista)
        paginator.ispisiStranu(pag, ranger.recnik)
        return

    if option == 0:
        exit()

    if option != 0:
        quitOpt = input("Pritisnite bilo sta da nastavite.")

def main():

    option = -1
    while option != 0:
        try:
            print("[1] Unesite putanju do fajla za parsiranje:")
            print("[2] Pretraga rijeci:")
            print("[3] Rangiranje stranica:")
            print("[4] Prikazi konacne rezultate:")
            print("[5] Paginacija rezultata:")
            print("[0] Prekid:")

            option = int(input())
            pickOption(option)
        except ValueError:
            print("Please enter an integer")

if __name__ == '__main__':
    main()