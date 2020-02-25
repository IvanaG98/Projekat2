from algoritmi.paginacija import *
from util.parsiranje import *
from algoritmi.rangirana_pretraga import *
from algoritmi.pretraga_rijeci import *
from algoritmi.sortiranje import *

def main():
    parser = ParsFiles()
    ranger = Rangiranje()
    parser.parseFile()
    reci = input("Unesite rijeci za pretragu:\n")
    (result, broj_reci) = pretraga(reci, parser)
    ranger.rangiranje(result, parser.graph, reci, parser, broj_reci)
    lista = sortiranje(ranger.recnik)

    option = -1
    while option != 0:
        try:
            print("1  - Prikazi konacne rezultate.\n")
            print("2  - Paginacija rezultata.\n")
            print("0  - Izlazak iz programa.\n")
            option = int(input("Unesite opciju koju zelite:\n"))

            if option == 1:
                ispis = Ispis()
                ispis.prikazRezultata(ranger.recnik, lista)

            if option == 2:
                n = int(input("Unesite broj strana za paginaciju:\n"))
                if n <= 0:
                    print("Broj strana za paginaciju mora biti veci od 0.")
                    continue
                else:
                    paginator = Paginacija(len(lista), n, 0)
                    pag = paginator.paginacija(n, lista)
                    paginator.ispisiStranu(pag, ranger.recnik)

                    while True:
                        print("1 -  Prethodna stranica.\n")
                        print("2 -  Naredna stranica.\n")
                        print("3 -  Promjenite broj stranica za paginaciju.\n")
                        print("4 -  Vrati se na prethodni odabir upita.\n")
                        print("0 -  Izlazak.\n")

                        option2 = int(input("Unesite narednu opciju:\n"))

                        if option2 == 1:
                            pag1 = paginator.prethodna_strana()
                            pag = paginator.paginacija(n, lista)
                            if pag1:
                                paginator.ispisiStranu(pag, ranger.recnik)

                        if option2 == 2:
                            pag1 = paginator.sledeca_strana()
                            pag = paginator.paginacija(n, lista)
                            if pag1:
                                paginator.ispisiStranu(pag, ranger.recnik)

                        if option2 == 3:
                            n = int(input("Unesite broj strana za paginaciju:\n"))
                            if n <= 0:
                                print("Broj stranica za paginaciju mora biti veci od 0.")
                                continue
                            pag = paginator.paginacija(n, lista)
                            paginator.ispisiStranu(pag, ranger.recnik)

                        if option2 == 4:
                            break


                        if option2 == 0:
                            exit()
            if option == 0:
                exit()

        except ValueError:
            print("Niste dobro unijeli.\n")

if __name__ == '__main__':
    main()