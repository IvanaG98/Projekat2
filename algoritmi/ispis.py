class Ispis(object):

    """Klasa sadrzi metodu prikazRezultata koja ispisuje rezultate na osnovu prethodno odredjenog ranga.
       U fajlu sortiranje izvrsen je quick sort algoritam za sortiranje
       i prikazani su rangovi svih stranica, zatim link stranice, broj linkova koji pokazuju na tu stranicu
       broj rijeci na stranici, broj rijeci na linku koji pokazuje na nasu stranicu i pojavljivanje rijeci iz upita na stranici.
       Ispis je formatiran, a rang je zaokruzen na 2 decimale.
    """

    def prikazRezultata(self, recnik, lista):

        if lista == []:
            print("Ne postoji stranica koja ispunjava te zahtjeve")         #posto nemamo rezultata izlazimo iz programa
            exit()

        if lista != []:
            prvi = "RANG"
            drugi = "STRANICA"
            treci = "BROJ LINKOVA NA NJU"
            cetvrti = "BROJ RIJECI NA STR"
            peti = "BROJ RIJECI NA LINKU"
            sesti = "POJAVLJIVANJE"
            print(prvi.center(15, " "), drugi.center(90, " "), treci.center(20, " "), cetvrti.center(20," "), peti.center(10, " "), sesti.center(15, " "))

            n = len(lista)
            for i in range(n):
                key = lista[i]
                pomocna = recnik[key]
                print(str(round(key,2)).center(15, " "), pomocna[0].center(90, " "), str(pomocna[1]).center(20, " "), str(pomocna[2]).center(20, " "), str(pomocna[3]).center(15, " "), str(pomocna[4]).center(30, " "))




