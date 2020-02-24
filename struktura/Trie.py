from typing import Tuple

#kad naidje na neku rijec na str ono je dodaje u stablo i na poslednji cvor dodaje rijecnik, na kojoj str je nadjeno i koliko puta
#u add treba da doda pravljenje rijecnika

class TrieNode(object):
    name = ""

    def __init__(self, char):
        self.char = char
        self.children = []
        self.word_finished = False  #zbog toga sto unos za pretragu ne moze biti pomocu prefiksa vec cela rec
        self.recnik = {}    #napravila sam recnik koji je rezultat pretrage, dodacemo ga na kraj cvora i u njemu ce se nalaziti link fajla u kome se rec nalazi i broj ponavljanja te rijeci u fajlu
        self.counter = 1    #ne znam za sta sluzi


def add(root, word, link):      #link str za pars trenutno
    node = root
    for char in word:
        found_in_child = False
        for child in node.children:
            if child.char == char:
                child.counter += 1
                node = child
                found_in_child = True
                break
        if not found_in_child:
            new_node = TrieNode(char)
            node.children.append(new_node)
            node = new_node
    node.word_finished = True

    if link in node.recnik:
        node.recnik[link] += 1
    else:
        node.recnik[link] = 1


def find_prefix(root, prefix: str):
    node = root

    if not root.children:
        return "Nema djece"
    for char in prefix:
        char_not_found = True
        for child in node.children:
            if child.char == char:
                char_not_found = False
                node = child
                break
        if char_not_found:
            return None

    if node.word_finished == False:
        return None

    return node.recnik
