# OCENA 3.5/5

"""
slot_idx = (slot_idx + self.c1 * i + self.c2 * i**2) % self.size
w wyrażeniu jest calc_hash a nie slot_idx

Wypisywanie niezgodne z instrukcją

Brak wstawiania (mimo istniejącego miejsca)
tab.insert("test", "W")
"""

"""
Zaimplementuj tablicę mieszającą w postaci klasy zawierającej 'tablicę statyczną', np.:
tab = [None for i in range(size)]
gdzie size jest parametrem 'konstruktora'.

Klasa powinna mieć zaimplementowaną metodę realizującą funkcję mieszającą, obliczającą modulo rozmiaru tablicy
oraz metodę rozwiązującą kolizję metodą adresowania otwartego (z próbkowaniem kwadratowym, gdzie c1 i c2 powinny być 4
parametrami konstruktora z domyślnym ustawieniem odpowiednio 1 i 0 - czyli domyślnie mamy próbkowanie liniowe).
Zakładamy, że funkcja mieszająca może otrzymać wprost liczbę, lub napis - wówczas należy go zamienić na liczbę poprzez
zsumowanie kodów ASCII wszystkich jego liter (funkcja ord).

Następnie należy zaimplementować metody:

    konstruktor (z parametrami: rozmiar tablicy oraz c1, c2  jak powyżej) tworzący pustą tablicę (wypełnioną None-ami)
    search - wyszukująca i zwracająca wartość odpowiadającą podanemu kluczowi (lub None w wypadku nieznalezienia)
    insert - wstawiająca daną wg podanego klucza, jeżeli element o takim kluczu istnieje, jego wartość powinna zostać
        nadpisana
    remove - usuwająca daną o podanym kluczu (początkowo zaimplementuj usuwanie przez wpisanie None w  miejsce wskazane
        przez wyliczony indeks).
    __str__ -  wypisującą tablicę w postaci par {klucz:wartość, ...} - tak jak wypisywany jest pythonowy słownik;
        'Puste' miejsce niech będzie wypisywane jako None

W wypadku kolizji należy ograniczyć liczbę prób wyznaczenia kolejnego indeksu do wartości będącej rozmiarem tablicy.
Metody insert i remove powinny w jakiś sposób informować o niepowodzeniu (insert - brak miejsca, remove - brak danej o
 podanym kluczu). Może to być np. wyjątek lub zwracana wartość None. W takim wypadku w miejscu wywołania niech pojawia
 się komunikaty "Brak miejsca" i "Brak danej".


Elementy tablicy również powinny być zaimplementowane jako klasa z dwoma atrybutami przechowującymi: klucz oraz  wartość
(jakąś daną).
Ponadto napisz metodę __str__(self) zwracającą napis przedstawiający  element w postaci klucz:wartość


W main-ie sprawdź działanie zaimplementowanej tablicy przez stworzenie dwóch funkcji testujących.
Niech te funkcje mają takie same parametry jak 'konstruktor' tablicy mieszającej.
Pierwsza niech przetestuje tablicę przez:

    utworzenie pustej tablicy o rozmiarze 13 i próbkowaniem liniowym
    użycie insert do wpisana do niej 15 danych Niech kluczami będą  kolejne liczby od 1
    (ZA WYJĄTKIEM 6 i 7, zamiast których kluczami powinny być 18 i 31), a wartościami - kolejne litery od 'A'.
    wypisanie tablicy
    użycie search do wyszukania (i wypisania) danej o kluczu 5
    użycie search do wyszukania (i wypisania) danej o kluczu 14
    użycie insert do nadpisania wartości dla klucza 5 wartością 'Z'
    użycie search do wyszukania (i wypisania) danej o kluczu 5
    użycie remove do usunięcia danej o kluczu 5
    wypisanie tablicy
    użycie search do wyszukania (i wypisania) danej o kluczu 31

W tym miejscu zaobserwujemy problem z usuwaniem elementów tablic mieszających z adresowaniem otwartym.
Zaproponuj i zrealizuj rozwiązanie tego problemu (w razie trudności zwróć się o podpowiedź do Prowadzącego zajęcia)

Ponownie uruchom program w celu sprawdzenia czy tym razem tablica działa poprawnie.

Wprowadź do tablicy insertem daną o wartości 'W'  z kluczem 'test' i ponownie wypisz tablicę.

Utwórz drugą funkcję testującą wpisującą takie same wartości do tablicy jak poprzednio (kolejne litery), ale niech ich
klucze będą wielokrotnościami wartości 13 (zaczynając od 13). Niech funkcja tylko wypisuje uzyskaną tablicę.
Uruchom funkcję z próbkowaniem liniowym. Zaobserwuj czy wszystkie miejsca w tablicy zostały zajęte.
Ponownie wywołaj drugą funkcję zmieniając próbkowanie na kwadratowe (parametry c konstruktora: 0, 1).
Zaobserwuj zajętość tablicy.
Zawołaj pierwszą funkcję testującą z próbkowaniem kwadratowym (parametrami  c dla konstruktora: 0, 1).
Zaobserwuj zajętość tablicy oraz brak danej  'M'.

"""

class Data:
    def __init__(self, key, data):
        self.key = key
        self.data = data



    def __str__(self):
        return str(self.key) + ": " + str(self.data)

class TabMiesz:
    def __init__(self, size,c1 = 1, c2 = 0):
        self.__tab = [None for i in range(size)]
        self.size = size
        self.c1 = c1
        self.c2 = c2

    def calc_hash(self, key):
        if type(key) == int:
            return key % self.size
        if type(key) == str:
            suma = 0
            for character in key:
                suma += ord(character)
            return suma % self.size

    def find_slot(self, key, ignore_removed = False):
        slot_idx = self.calc_hash(key)
        for i in range(self.size):
            if self.__tab[slot_idx] is None or (ignore_removed and isinstance(self.__tab[slot_idx], Removed)):
                return slot_idx
            if not isinstance(self.__tab[slot_idx], Removed):
                if self.__tab[slot_idx].key == key:
                    return slot_idx
            slot_idx = (slot_idx + self.c1 * i + self.c2 * i**2) % self.size
        return None

    def search(self, key):
        slot_idx = self.find_slot(key)
        if slot_idx is None:
            return None

        if self.__tab[slot_idx] is None or isinstance(self.__tab[slot_idx], Removed):
            return None

        return self.__tab[slot_idx].data

    def insert(self, key, data):
        slot_idx = self.find_slot(key, ignore_removed = True)
        if slot_idx is None:
            raise BrakMiejsca
        self.__tab[slot_idx] = Data(key, data)


    def remove(self, key):
        slot_idx = self.find_slot(key)
        if slot_idx is None:
            raise BrakDanej

        self.__tab[slot_idx] = Removed()

    def __str__(self):
        str_tab = []
        for i in range(self.size):
            str_tab.append(str(self.__tab[i]))
        return "{" + "\n".join(str_tab) + "}"

class BrakMiejsca(Exception):
    pass

class BrakDanej(Exception):
    pass

class Removed:
    def __str__(self):
        return "Removed"

def test1(size, c1 = 1, c2 = 0):
    tab = TabMiesz(size, c1, c2)
    keys = [i for i in range(1, 16)]
    keys[5] = 18
    keys[6] = 31
    alfabet = "ABCDEFGHIJKLMNOPRTSU"
    for i in range(15):
        try:
            tab.insert(keys[i], alfabet[i])
        except BrakMiejsca:
            print("Brak miejsca")

    print(tab)
    print(tab.search(5))
    print(tab.search(14))
    tab.insert(5, "Z")
    print(tab.search(5))
    tab.remove(5)
    print(tab)
    print(tab.search(31))
    try:
        tab.insert("test", "W")
    except BrakMiejsca:
        print("Brak miejsca")

def test2(size, c1 = 1, c2 = 0):
    tab = TabMiesz(size, c1, c2)
    keys = [13*i for i in range(1, 16)]
    alfabet = "ABCDEFGHIJKLMNOPRTSU"

    for i in range(len(keys)):
        try:
            tab.insert(keys[i], alfabet[i])
        except BrakMiejsca:
            print("Brak miejsca")
    print(tab)


def main():
    test1(13, 1, 0)
    test2(13, 1, 0)
    test2(13, 0, 1)
    test1(13, 0, 1)

if __name__ == "__main__":
    main()