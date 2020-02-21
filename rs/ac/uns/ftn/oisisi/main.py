
from rs.ac.uns.ftn.oisisi import zadaci, repositoryUtils


def pickOption(option):     #u zavisnosti koju opciju izaberemo ,odredjena funkcija se izvrsava(varijabla ima pokazivac na funkciju)
    switcher = {
        0: zadaci.exit,
        1: zadaci.directorySelection,
        #2: zadaci.paginacija,
        3: zadaci.wordSearch,
      #  #  5: tasks.printContent,
    }
    func = switcher.get(option, lambda: "pogresna opcija")
    func()
    # Ako smo odabrali izlaz, nasilno izadji i ne pitaj nista
    if option != 0:
        quitOpt = input(" .. press any key to continue ... ")


n = -1  # predefinisana peginacija


def main():
    option = -1
    while option != 0:
        try:
            repositoryUtils.cls()  # brisanje ekrana
            print("[1] Odabir direktorijuma")
            print("[2] Unesi n za paginaciju") #kolio hocemo rezultata
            print("[3] Pretraga reci ")
            print("[4] Ispisi sadrzaj")
            print("[0] Prekid")

            option = int(input())
            pickOption(option)
        except ValueError:
            print("Unesite neku od ponudjenih opcija:")


main()