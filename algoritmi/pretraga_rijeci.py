from struktura.set import *
from struktura.Trie import *


def pretraga(words, parser):
    operator = ["and", "or", "not"]
    result = {}
    query=words.lower().split(' ')       #dijelimo unos po razmacima i pravimo listu od toga
    if any(item in operator for item in query):   #da li se unijeti operator nalazi u listi operatora
        if len(query) < 2:
            (result, broj_reci) = pretragaPoRijecima(query, parser)   #posto imamo 2 dijela(nemamo operator) vrsimo potregaPoRijecima
        else:
            if not query[1] in operator:    #sad nas upit ima vise od 2 rijeci i provjeravamo da li je "srednja" rijec operator
                print("Nije dobar upit")
                exit()
            else:
                if len(query) != 3:         #nasa pretraga sa operatorima radi samo ako query ima duzinu 3 i ako jje "srednja rijec" operator
                    print("Nije dobra duzina")
                    exit()
                else:
                    (result, broj_reci) = pretragaSaOperatorima(query, parser)

    else:
        (result, broj_reci) = pretragaPoRijecima(query, parser)  #u ostalim slucajevima koristimo pretragu po rijecima
    return result, broj_reci

def pretragaPoRijecima(query, parser):
    data = []
    set = Set()

    for word in query:
        if find(parser.trie, word) is not None:    #ako rijec pronadjemo u trie-u
            data.append(find(parser.trie, word))    # dodamo u listu data
            set.unija(data)

    return set.recnik, set.broj_reci


def pretragaSaOperatorima(query, parser):
    val1 = query[0]
    op = query[1]    #srednja rijec je operator
    val2 = query[2]
    result = Set()

    prvi = find(parser.trie, val1)
    drugi = find(parser.trie, val2)
    if op == "and":
        if prvi is not None:
            if drugi is not None:
               result.presek(prvi, drugi)

    if op == "or":
        lista = []
        lista.append(prvi)
        lista.append(drugi)
        if prvi is not None:
            if drugi is not None:
               result.unija(lista)

    if op == "not":
        lista = []
        lista.append(prvi)
        lista.append(drugi)
        if query[0] == query[2]:
            print("zahtjev je nemoguce izvrsiti")      #npr. java not java  nema resenje
            exit()
        if prvi is not None:
            if drugi is not None:
                result.komplement(lista)

    return result.recnik, result.broj_reci
