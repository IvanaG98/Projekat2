class Ispis(object):

    def prikazRezultata(self, recnik, lista):
        if lista ==[]:
            print("ne postoji stranica koja ispunjava te zahtjeve")         #posto nemamo rezultata izlazimo iz programa
            exit()

        if lista !=[]:
            prvi = "RANG"
            drugi = "STRANICA"
            treci = "BROJ LINKOVA NA NJU"
            cetvrti = "BROJ RIJECI NA STR"
            peti = "BROJ RIJECI NA LINKU"
            sesti = "POJAVLJIVANJE"
            print(prvi.center(15, " "), drugi.center(90, " "), treci.center(20, " "), cetvrti.center(20," "), peti.center(10, " "), sesti.center(10, " "))

            n = len(lista)
            for i in range(n):
                key = lista[i]
                pomocna = recnik[key]
                print(str(round(key,2)).center(15, " "), pomocna[0].center(90, " "), str(pomocna[1]).center(20, " "), str(pomocna[2]).center(20, " "), str(pomocna[3]).center(15, " "), str(pomocna[4]).center(30, " "))




