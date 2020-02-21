import importlib, importlib.util
import os  # (ugradjeni modul)
#import repositoryUtils as ru


from tkinter import *
from tkinter.filedialog import askopenfilename

from rs.ac.uns.ftn.oisisi import repositoryUtils, htmlpage

#import htmlpage as model
from collections import defaultdict

n = -1
workingDir = "none"


# Metoda za ucitavanja modula
def module_from_file(module_name, file_path):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


trie = module_from_file("TrieNode", "Trie.py")
# G = graph.Graph()
# metoda koja sve radi xd


T = []


def parseFolders(root):
    global T

    for file in os.listdir(root):  # iz fajla koji nam je korijen  izlistavamo direktorijume
        if os.path.isdir(os.path.join(root,file)):  # provjera da li je taj faljl folder (ako jeste udji u njega)
            for subfile,dirs,files  in os.listdir(os.path.join(root, file)):  # provjeri je li html
                if subfile.endswith(".html"):
                    node = parseOnePage(root, os.path.join(root,subfile))  # pozivamo sledecu funkciju(koja ce da parsira sadrzaj jedne srtanice)
                    t = trie.TrieNode('')
                    t.name = node.name
                    for word in node.content:
                        trie.add(t, word.upper())

                    T.append(t)

        if file.endswith(".html"):
            node = parseOnePage(root, file)
            t = trie.TrieNode('')
            t.name = node.name
            for word in node.content:
                trie.add(t, word.upper())
            T.append(t)

        # [1] odabir direktorijuma


def directorySelection():
    Tk().withdraw()  # otvara dijalog za biranje direktorijuma
    filename = askopenfilename()
    repositoryUtils.cls()

    workingDir = repositoryUtils.getDir(filename)
    print("Parsed folder & all subfolders\n")
    # contains all files and subfolders NAMES
    pages = parseFolders(workingDir)


mc = module_from_file("Parser", "parser.py")


# fullpath = path + "\\" + filename
def parseOnePage(path, filename):
    global mc
    parser = mc.Parser()
    [links, words] = parser.parse(path + "\\" + filename)
    page = htmlpage.HTMLpage(filename, path, words, links)
    return page


def searchByWords(words):
    result = defaultdict(set)
    global T

    for t in T:
        for word in words:
            if trie.find_prefix(t, word)[0] == True:
                result[t.name].add(word)

    for key in result:
        print(key, end=" ")
        print(result[key])



def wordSearch():
    print("Unesite upit:")
    line = input()
    operator = ["AND", "OR", "NOT"]

    query = line.upper().split(' ')
    result = []
    # if any(item in operator for item in query):

    #     if len(query) < 2:
    #         result = searchByWords(query)
    #     else:
    #         if not query[1] in operator:
    #             print("Nije dobar upit")
    #         else:
    #             if len(query) != 3:
    #                 print("Nije dobra duzina")
    #             else:
    #                result = searchByQuery(query)
    # else:
    result = searchByWords(query)
    return result


def exit():
    return
