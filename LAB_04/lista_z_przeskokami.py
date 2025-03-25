"""Zaimplementuj listę z przeskokami (skip-list) poprzez stworzenie klasy zawierającej atrybut reprezentujący głowę listy (np. head) oraz metody:

    konstruktor z parametrem określającym maksymalną 'wysokość' elementu listy - powinien tworzyć pusty element listy,
    którego tablica wskazań na następne elementy będzie reprezentowała tablicę głów list na poszczególnych poziomach,
    ten element ma zostać przypisany do atrybutu head
    search - wyszukująca i zwracająca wartość odpowiadającą podanemu kluczowi (lub None)
    insert - wstawiająca daną wg podanego klucza - podczas szukania miejsca do wstawienia klucza powinna tu być tworzona
    lista  (tablica) zawierająca poprzedniki  znalezionego elementu  na każdym poziomie
    (znaleziony element to ten, którego klucz jest większy od klucza wstawianego elementu);
    dla poziomów, których znaleziony element nie posiada  w tablicy poprzedników powinna być wpisana głowa listy (np. head).
    remove - usuwająca daną o podanym kluczu
    __str__ -  wypisującą listę jako tablicę w postaci par (klucz:wartość) (należy wypisać 'poziom 0' listy)

Elementy listy również powinny być zaimplementowane jako klasa z atrybutami przechowującymi: klucz,  wartość (jakąś daną),
liczbę poziomów oraz listę (tablicę) ze wskazaniami na następny element o rozmiarze równym liczbie poziomów.
Do tworzenia elementów listy będzie przydatna funkcja/metoda losująca liczbę poziomów
(jako metoda nie musi mieć parametru maxLevel, p zaś będziemy ustawiali na 0.5):
def randomLevel(p, maxLevel):
  lvl = 1
  while random.random() < p and lvl <maxLevel:
        lvl = lvl + 1
  return lvl

W celach testowych przydatna  też będzie funkcja/metoda:
wypisująca całą listę (wszystkie poziomy) przez wypisanie kluczy i danych na każdym z poziomów .
Proszę w tym celu zaadoptować poniższą funkcję:
    def displayList_(self):
        node = self.head.tab[0]  # pierwszy element na poziomie 0
        keys = [ ]                        # lista kluczy na tym poziomie
        while node is not None:
            keys.append(node.key)
            node = node.tab[0]

        for lvl in range(self.max_level - 1, -1, -1):
            print(f"{lvl}  ", end=" ")
            node = self.head.tab[lvl]
            idx = 0
            while node is not None:
                while node.key > keys[idx]:
                    print(end=5*" ")
                    idx += 1
                idx += 1
                print(f"{node.key:2d}:{node.data:2s}", end="")
                node = node.tab[lvl]
            print()



W main-ie zainicjuj generator liczb pseudolosowych wartością 42 (random.seed(42))
Następnie sprawdź działanie zaimplementowanej listy przez:

    utworzenie pustej listy
    użycie insert do wpisana do niej 15 danych (niech kluczami będą  kolejne liczby od 1, a wartościami - kolejne litery),
    wypisanie listy
    użycie search do wyszukania (i wypisania) danej o kluczu 2
    użycie insert do nadpisania wartości dla klucza 2 literą 'Z'
    użycie search do wyszukania (i wypisania) danej o kluczu 2
    użycie delete do usunięcia danych o kluczach 5, 6, 7
    wypisanie tablicy (poziom 0 listy)
    użycie insert do wstawienia  danej 'W' o kluczu 6
    wypisanie tablicy (poziom 0 listy)


Dla końcowego sprawdzenia ponownie wykonaj powyższe operacje, ale tym razem wpisując 15 wartości w odwrotnej kolejności - od 15 do 1."""
import random


class Node:
    def __init__(self, key, data, level):
        self.key = key
        self.data = data
        self.tab = [None for _ in range(level)]
        self.level = level

    def __str__(self):
        return str(self.data)


def random_level(p, max_level):
    lvl = 1
    while random.random() < p and lvl < max_level:
        lvl = lvl + 1
    return lvl


class SkipList:
    def __init__(self, max_level):
        self.head = Node(None, None, max_level)
        self.max_level = max_level
        self.length = 0

    def find_key(self, key): # chujowe nie działa kompletnie inaczej trza zrobić
        if self.is_empty():
            return None

        node = self.head
        next_ = self.head.tab[-1]

        for j in range(self.length):
            for i in range(-1, -node.level, -1):
                next_ = node.tab[i]
                if next_ is not None:
                    break

            while next_.data < key:
                next_ = next_.tab[0]




    def is_empty(self) -> bool:
        if self.head is Node(None, None, self.max_level):
            return True
        return False

    def display_list(self):
        node = self.head.tab[0]  # pierwszy element na poziomie 0
        keys = [ ]                        # lista kluczy na tym poziomie
        while node is not None:
            keys.append(node.key)
            node = node.tab[0]

        for lvl in range(self.max_level - 1, -1, -1):
            print(f"{lvl}  ", end=" ")
            node = self.head.tab[lvl]
            idx = 0
            while node is not None:
                while node.key > keys[idx]:
                    print(end=5*" ")
                    idx += 1
                idx += 1
                print(f"{node.key:2d}:{node.data:2s}", end="")
                node = node.tab[lvl]
            print()

def main():
    random.seed(42)

if __name__ == "__main__":
    main()