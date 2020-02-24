from typing import Tuple

#kad naidje na neku rijec dodaje je  u stablo i rijecnik, na kojoj str je nadjeno i koliko puta


class TrieNode(object):
    name = ""

    def __init__(self, char):
        self.char = char
        self.children = []
        self.word_finished = False  #zbog toga sto unos za pretragu ne moze biti pomocu prefiksa vec cela rec
        self.recnik = {}   #u njemu ce se nalaziti link fajla u kome se rec nalazi i broj ponavljanja te rijeci u fajlu


def add(root, word, link):      #link str za pars trenutno
    node = root
    for char in word:       #prolazimo karakter po karakter kroz rijec
        found_in_child = False
        for child in node.children:    #prolazimo kroz sve cvorove trie-a
            if child.char == char:
                node = child
                found_in_child = True
                break
        if not found_in_child:        #nismo pronasli u trie-u
            new_node = TrieNode(char)
            node.children.append(new_node)   #pravimo novi cvor
            node = new_node
    node.word_finished = True

    if link in node.recnik:
        node.recnik[link] += 1    #povecavamo brojac rijeci
    else:
        node.recnik[link] = 1


def find(root, wordss: str):
    node = root

    if not root.children:
        return "Nema djece"
    for char in wordss:
        char_not_found = True
        for child in node.children:
            if child.char == char:
                char_not_found = False   #gdje pronadjemo rijec stavljamo da je nas "korijen" i prosledjujemo kao informaciju iz funkcije
                node = child
                break
        if char_not_found:
            return None

    if node.word_finished == False:
        return None

    return node.recnik
