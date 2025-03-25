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

    def find_place(self, key):
        if self.is_empty():
            return None

        path = []
        node = self.head
        i = -1

        while True:
            if -i > node.level:
                break

            path.append(node)
            next_node = node.tab[i]

            if next_node is None:
                if -i == node.level:
                    break
                i -= 1
            elif next_node.key == key:
                path.append(next_node)
                return path
            elif next_node.key > key:
                i -= 1
            else:
                node = next_node
                i = -1
                path.pop()

        return path

    def insert(self, key, data):
        path = self.find_place(key)

        new_node = Node(key, data, random_level(0.5, self.max_level))
        if path is None:
            self.head.tab[0] = new_node
        if path[-1].key == key:
            path[-1].data = data
        else:
            for i in range(new_node.level):
                new_node.tab[i] = path[-1-i].tab[i]
                path[-1-i].tab[i] = new_node

    def search(self, key):
        path = self.find_place(key)
        if path is None:
            return None
        if path[-1].key == key:
            return path[-1].data
        return None

    def delete(self, key):
        for i in range(self.max_level):
            node = self.head.tab[i]
            if node is None:
                return
            while node.tab[i] is not None and node.tab[i].key != key:
                node = node.tab[i]

            node.tab[i] = node.tab[i].tab[i] if node.tab[i] is not None else None

    def is_empty(self) -> bool:
        if self.head == Node(None, None, self.max_level):
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

    def __str__(self):
        str_tab = []
        node = self.head.tab[0]
        while node is not None:
            str_tab.append(node.data)
            node = node.tab[0]

        return "["+ ", ".join(str_tab) + "]"

def main():
    random.seed(42)
    skip_list = SkipList(4)
    alfabet = "ABCDEFGHIJKLMNOPRSTYVWY"
    for i in range(1, 16):
        skip_list.insert(i, alfabet[i-1])
    skip_list.display_list()

    print(skip_list.search(2))
    skip_list.insert(2, "Z")
    print(skip_list.search(2))

    skip_list.delete(5)
    skip_list.delete(6)
    skip_list.delete(7)

    print(skip_list)

    skip_list.insert(6, "W")

    print(skip_list)


if __name__ == "__main__":
    main()