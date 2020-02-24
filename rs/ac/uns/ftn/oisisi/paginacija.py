from math import ceil

from rs.ac.uns.ftn.oisisi.ispis import *


class Paginator(object):

    def __init__(self, total=None, per_page=100, current_page=1):
        """init with total number of items in your set, how many you want per_page, and set the current_page you are on"""
        self.total = total
        self.per_page = per_page
        self.current_page = current_page


    def repr__(self):
        return str(self.__dict__)

    def total_pages(self, lista):
        """The number of pages this pagination can have due to the total and per_page, e.g. total 10, per_page 5 = 2 total_pages
        Cast to float so result is float, round up, then back to int
        """
        ispis = Ispis()
        input("Unesite koliko stranica zelite za paginaciju:\n")
        if self.total > len(lista):
            print("Unos nije moguc!Broj stranica je veci nego sto treba.")

        #ispis.prikazRezultata()

        return int(ceil(float(self.total) / self.per_page))

    def pages(self):
        """Returns list of integers of pages e.g. for 3 pages [1,2,3]"""
        return range(1, self.total_pages + 1)

    def next_page(self):
        """The page number after the current_page or None"""
        if self.current_page == self.total:
            print("Dosli ste do poslednje stranice.\n")


        return self._get_page_offset(+1)

    def prev_page(self):
        """The page number before the current_page or None"""

        return self._get_page_offset(-1)


    def _get_page_offset(self, offset):
        """Give an offset, +1 or -1 and the page number around the current_page will be returned
        So if we are on current_page 2 and pass +1 we get 3, if we pass -1 we get 1.  Or None if not valid
        """
        try:
            return self.pages[self.pages.index(self.current_page + offset)]
        except ValueError:
            return None


    def start(self):
        """The starting offset used when querying"""
        return self.current_page * self.per_page - self.per_page