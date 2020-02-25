"""U ovom fajlu nalazi se metoda za sortiranje.
   Upotrebljen je quick sort algoriram za sortiranje.
   Prvo smo prebacili recnik u listu ciji kljucevi su rangovi stranica,
   a potom je sortirano na osnovu izracunatog ranga u fajlu rangirana_pretraga."""

def sortiranje(recnik):

    lista = list(recnik.keys())
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] < lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista