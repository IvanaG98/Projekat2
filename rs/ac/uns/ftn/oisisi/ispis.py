class Ispis(object):

    def prikazRezultata(self, recnik):
        print("LEGENDA:\n")
        print("Rang - R\nLink stranice - L\nBroj linkova ka njoj - BRL\nBroj rijeci na njoj - BRR\nBroj rijeci na stranicama koje ukazuju na nju - BRLR\nBroj rijeci iz pretrage koje se pojavljuju na toj stranici - BRPR\n")
        print("                 R                              L                                             BRL    BRR   BRLR   BRPR\n")

        lista = list(recnik.keys())
        n = len(lista)
        for i in range(n):
            for j in range(0, n - i - 1):
                if lista[j] < lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
        for i in range(n):
            key = lista[i]
            pomocna = recnik[key]
            print(round(key,2), pomocna[0], pomocna[1], pomocna[2], pomocna[3], pomocna[4])



