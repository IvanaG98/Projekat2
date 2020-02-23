from rs.ac.uns.ftn.oisisi.set import *
from rs.ac.uns.ftn.oisisi.Trie import *

def searchByWords(query, parser):
    data = []
    set = Set()
    for word in query:
        if find_prefix(parser.trie, word) is not None:
            data.append(find_prefix(parser.trie, word))
            set.unija(data)
    #print(set.recnik)
    return set.recnik, set.broj_reci


def wordSearch(words, parser):
    operator = ["and", "or", "not"]
    result = {}
    query=words.lower().split(' ')
    if any(item in operator for item in query):
        if len(query) < 2:
            (result, broj_reci) = searchByWords(query, parser)
        else:
            if not query[1] in operator:
                print("Nije dobar upit")
            else:
                if len(query) != 3:
                    print("Nije dobra duzina")
                else:
                    (result, broj_reci) = searchByQuery(query,parser)
    else:
        (result, broj_reci) = searchByWords(query, parser)
    return result, broj_reci


def searchByQuery(query, parser):
    val1 = query[0]
    op = query[1]
    val2 = query[2]
    result = Set()

    prvi = find_prefix(parser.trie, val1)
    drugi = find_prefix(parser.trie, val2)
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
        if prvi is not None:
            if drugi is not None:
                result.komplement(lista)

    return result.recnik, result.broj_reci


