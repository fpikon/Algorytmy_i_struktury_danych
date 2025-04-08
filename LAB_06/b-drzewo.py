"""
Zaimplementuj w języku Python uproszczoną wersję b-drzewa. Należy zaimplementować jedynie funkcję insert dodającą element do drzewa. Ponadto dla uproszczenia założymy, że:

    maksymalna liczba elementów w węźle jest nieparzysta (a więc pełny węzeł ma parzystą liczbę potomków).
    dodawanymi elementami będą same klucze (pomijamy dane, które zazwyczaj towarzyszą kluczom)
    w wypadku, gdy węzeł, do którego ma być dodany element, jest pełny następuje jego podział
    (nie ma próby przesunięcia elementów do sąsiednich węzłów)
    nie sprawdzamy czy próbujemy wstawić już istniejący klucz

Możliwa implementacja - dwie klasy:

    pierwsza klasa zawiera pole  wskazujące na korzeń drzewa, pole zawierające maksymalną liczbę potomków
    (lub maksymalną liczbę elementów w węźle) ustawiane przy tworzeniu obiektu tej klasy oraz metodę insert
    dodającą klucz i metodę wypisującą drzewo
    druga klasa zawiera dwa pola: keys (lista kluczy), children (lista potomków).

W omawianej tu implementacji metoda insert zwraca informację czy wstawianie klucza spowodowało podział potomka
(parę - element środkowy z podziału i utworzony w jego trakcie węzeł)
Metoda insert zaczyna od przeszukania aktualnego węzła w poszukiwaniu klucza większego od wstawianego.
Po znalezieniu sprawdza czy aktualny węzeł jest liściem :
 - jeżeli tak dodaje klucz (warto tu zrobić osobną funkcję dodającą do węzła - jest ona opisana poniżej),
 - jeżeli nie - woła się rekurencyjnie dla 'lewego potomka' znalezionego klucza
 (w wypadku gdy wstawiany klucz jest większy od wszystkich w węźle to będzie to ostatni potomek)
Po powrocie z rekurencji może się okazać, że potomek do którego przeszliśmy został podzielony -  tak więc należy dodać
do aktualnego węzła środkowy klucz z podziału i wskazanie na nowo-utworzony węzeł (ta sama funkcja dodająca do węzła co
w poprzednim przypadku)
Funkcja dodająca do węzła otrzymuje jako parametry dodawany klucz oraz ewentualne wskazanie na nowo-utworzony węzeł ze
swego poprzedniego wywołania. Musi ona sprawdzić, czy węzeł nie jest pełny (jeżeli tak to podzielić go przepisując
zarówno keys jak i children) i wpisać w odpowiednie miejsce klucz (do listy keys) oraz ewentualne wskazanie na potomka
(do listy children). Jeżeli nastąpił podział funkcja zwraca środkowy klucz z podziału i wskazanie na utworzony w nowy
węzeł. Jeżeli podziału nie było - można zwrócić None.

Na koniec metody insert należy sprawdzić, czy nie nastąpiło podzielenie root-a - wtedy trzeba utworzyć nowego roota
z jednym elementem (środkiem podziału) i wskazaniami na węzeł utworzony w podziale i na 'starego' root-a.


Poniższe funkcje mogą się przydać w tworzeniu metody wypisującej drzewo. Założono tu, że struktura danych opisująca
węzeł to klasa zawierająca pola:
keys - tablica (lista) kluczy
children -  tablica (lista) potomków
size - liczba elementów w tablicy keys
oraz, że liście też posiadają listę dzieci (wszystkie==None)

    def print_tree(self):
        print("==============")
        self._print_tree(self.root, 0)
        print("==============")

    def _print_tree(self, node, lvl):
        if node!=None:
            for i in range(node.size+1):
                self._print_tree(node.children[i], lvl+1)
                if i<node.size:
                    print(lvl*'  ', node.keys[i])

Oczywiście powyższe metody trzeba dostosować do własnej implementacji.

W main-ie:

    utwórz puste drzewo o maksymalnej liczbie potomków równej 4
    dodaj do niego elementy (będące jednocześnie kluczami) po kolei z listy: [5, 17, 2, 14, 7, 4, 12, 1, 16, 8, 11, 9, 6, 13, 0, 3, 18 , 15, 10, 19]
    wyświetl drzewo
    utwórz drugie puste drzewo, dodaj do niego 20 kolejnych liczb od 0 do 19 (będą to te same liczby co w liście ale dodane w kolejności rosnącej)
    wyświetl stworzone drzewo (zauważ jak różni się od poprzedniego)
    dodaj do drugiego drzewa kolejne liczby od 20 do 199, wyświetl drzewo (zauważ jak wzrosła jego wysokość)
    utwórz trzecie puste drzewo o maksymalnej liczbie potomków równej 6, dodaj do niego te same liczby co do drugiego drzewa (od 0 do 199) i wyświetl go (zauważ jak zmalała jego wysokość)
"""


class Node:
    def __init__(self, max_children):
        self.keys = []
        self.children = []
        self.max_children = max_children

    def is_leaf(self):
        return len(self.children) == 0

    def size(self):
        return len(self.keys)

    def insert(self, key, new_child = None):
        i = 0

        while i < self.size() and key > self.keys[i]:
            i += 1

        self.keys.insert(i, key)
        if new_child:
            self.children.insert(i + 1, new_child)

        if len(self.keys) > self.max_children - 1:
            return self.split()

        return None

    def split(self):
        mid_idx = self.size() // 2
        mid_key = self.keys[mid_idx]

        new_node = Node(self.max_children)
        new_node.keys = self.keys[mid_idx + 1:]
        self.keys = self.keys[:mid_idx]

        if not self.is_leaf():
            new_node.children = self.children[mid_idx + 1:]
            self.children = self.children[:mid_idx+1]

        return mid_key, new_node

    def __str__(self):
        return str(self.keys)

class BTree:
    def __init__(self, max_children):
        self.root = Node(max_children)
        self.max_children = max_children

    def insert(self, key):
        result = self.__insert(self.root, key)
        if result:
            mid_key, new_node = result
            new_root = Node(self.max_children)
            new_root.keys = [mid_key]
            new_root.children = [self.root, new_node]
            self.root = new_root

    def __insert(self, node, key):
        i = 0
        while i < node.size() and key > node.keys[i]:
            i += 1

        if node.is_leaf():
            return node.insert(key)

        result = self.__insert(node.children[i], key)
        if result:
            mid_key, new_node = result
            return node.insert(mid_key, new_node)
        return None

    def print_tree(self):
        print("==============")
        self._print_tree(self.root, 0)
        print("==============")

    def _print_tree(self, node, lvl):
        if node is not None:
            for i in range(node.size() + 1):
                if not node.is_leaf() and i < len(node.children):
                    self._print_tree(node.children[i], lvl + 1)
                if i < node.size():
                    print(' ' * (lvl * 2), node.keys[i])




def main():
    tree = BTree(4)
    data = [5, 17, 2, 14, 7, 4, 12, 1, 16, 8, 11, 9, 6, 13, 0, 3, 18 , 15, 10, 19]
    for i in data:
        tree.insert(i)
    tree.print_tree()

    tree_2 = BTree(4)
    for i in range(20):
        tree_2.insert(i)
    tree_2.print_tree()
    for i in range(20, 200):
        tree_2.insert(i)
    tree_2.print_tree()

    tree_3 = BTree(6)
    for i in range(200):
        tree_3.insert(i)
    tree_3.print_tree()



if __name__ == "__main__":
    main()