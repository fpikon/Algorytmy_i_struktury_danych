"""
Zaimplementuj w języku Python drzewo binarne BST. Niech będzie zaimplementowane za pomocą dwóch klas: pierwsza klasa
zawiera pole root wskazujące na korzeń drzewa (ang. root node), druga klasa reprezentuje węzeł drzewa i zawiera cztery
pola: klucz, wartość oraz wskaźniki na dwa węzły dzieci (ang. child node) - prawe i lewe rozgałęzienie.

Zaimplementuj poniższe funkcjonalności:

    konstruktor - tworzy obiekt reprezentujący drzewo z polem root ustawionym na None
    search - wyszukująca i zwracająca wartość odpowiadającą podanemu kluczowi (lub None)
    insert - wstawiająca daną wg podanego klucza, jeżeli element o takim kluczu istnieje, jego wartość powinna zostać
        nadpisana (funkcja pamięta poprzednika, patrz wykład)
    delete -  usuwająca daną o podanym kluczu
    print - wypisująca zawartość drzewa jako listę elementów ułożonych od najmniejszego do największego
        klucza wypisanych tak jak pokazano w przykładzie poniżej
    height - metoda zwracająca maksymalną wysokość od korzenia do węzła nieposiadającego kolejnych potomków (leaf node)
        - najdłuższa ścieżka w drzewie


Funkcja search wykonuje wyszukiwanie elementu w drzewie na podstawie klucza w wersji rekurencyjnej
    (może to być funkcja, która zawiera tylko wywołanie pomocniczej funkcji rekurencyjnej)
Funkcja insert tworzy kolejne elementy drzewa na podstawie podanego klucza, prawe rozgałęzienie zawiera klucze większe
    niż klucz w węźle rodzic (parent node), lewe rozgałęzenie zawiera klucze mniejsze niż klucz w węźle rodzic.

Funkcja delete usuwa element drzewa na podstawie podanego klucza. Należy uwzględnić trzy przypadki:

    usunięcie węzła, który nie posiada węzłów dzieci (child nodes)
    usunięcie węzła z jednym dzieckiem
    usunięcie węzła, który posiada dwa węzły dzieci - usuwany węzeł zastępujemy minimalnym kluczem z prawego poddrzewa
        (ang. right subtree) - successor node

Funkcja print_tree wypisująca całą strukturę drzewa w formie 2D (UWAGA: tak wypisywane drzewo jest przekręcone o 90 stopni
    - 'leży na lewym boku'):

    def print_tree(self):
        print("==============")
        self.__print_tree(self.root, 0)
        print("==============")

    def __print_tree(self, node, lvl):
        if node!=None:
            self.__print_tree(node.right, lvl+5)

            print()
            print(lvl*" ", node.key, node.data)

            self.__print_tree(node.left, lvl+5)
"""

class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return f"{self.key} {self.data}"


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def search(self, key):
        node = self.__search_it(self.root, key)
        return node.data if node else None

    def __search_it(self, node, key):
        if node is None:
            return None
        if node.key == key:
            return node
        elif node.key < key:
            return self.__search_it(node.right, key)
        else:
            return self.__search_it(node.left, key)

    def insert(self, key, data):
        self.root = self.__insert_it(self.root ,key, data)

    def __insert_it(self, node, key, data):
        if node is None:
            return Node(key, data)

        if node.key == key:
            node.data = data
        elif node.key > key:
            node.left = self.__insert_it(node.left, key, data)
        else:
            node.right = self.__insert_it(node.right, key, data)

        return node

    def delete(self, key):
        self.root = self.__delete_it(self.root, key)

    def __delete_it(self, node, key):
        if node is None:
            return node

        if key < node.key:
            node.left = self.__delete_it(node.left, key)
        elif key > node.key:
            node.right = self.__delete_it(node.right, key)
        else:
            if node.left is None and node.right is None:
                return None
            if node.left is None or node.right is None:
                temp = node.left if node.left else node.right
                return temp

            successor_node = self.__successor(node.right)
            node.key = successor_node.key
            node.data = successor_node.data
            node.right = self.__delete_it(node.right, successor_node.key)

        return node

    def __successor(self, node):
        while node.left is not None:
            node = node.left
        return node

    def height(self):
        if self.root is None:
            return -1
        return self.__height_it(self.root)

    def __height_it(self, node):
        if node is None:
            return 0

        left_height = self.__height_it(node.left)
        right_height = self.__height_it(node.right)

        return 1 + max(left_height, right_height)

    def print_tree(self):
        print("==============")
        self.__print_tree(self.root, 0)
        print("==============")

    def __print_tree(self, node, lvl):
        if node is not None:
            self.__print_tree(node.right, lvl + 5)

            print()
            print(lvl * " ", node.key, node.data)

            self.__print_tree(node.left, lvl + 5)

    def visit_str(self, node, visit_tab=None):
        if visit_tab is None:
            visit_tab = []
        if node is None:
            return node
        self.visit_str(node.left, visit_tab)
        visit_tab.append(str(node))
        self.visit_str(node.right, visit_tab)
        return visit_tab

    def __str__(self):
        if self.root is None:
            return "Empty tree"
        visit_tab = self.visit_str(self.root)
        return ", ".join(visit_tab)

"""
W main-ie sprawdź działanie zaimplementowanego drzewa przez:

    utworzenie pustego drzewa BST
    dodanie kolejno elementy klucz:wartość -- 
    {50:'A', 15:'B', 62:'C', 5:'D', 20:'E', 58:'F', 91:'G', 3:'H', 8:'I', 37:'J', 60:'K', 24:'L'}, 
    tworząc drzewo o podanej strukturze, jak na rysunku: 


    wypisz drzewo 2D (funkcją print_tree)
    wyświetl zawartość drzewa jako listę elementów ułożonych od najmniejszego do największego klucza wypisanych 
    w postaci klucz wartość - przykładowo powyższe drzewo powinno być wypisane tak:

    3 H,5 D,8 I,15 B,20 E,24 L,37 J,50 A,58 F,60 K,62 C,91 G,

    znajdź klucz 24 i wypisz wartość
    zaktualizuj wartość "AA" dla klucza 20
    dodaj element 6:M
    usuń element o kluczu 62
    dodaj element 59:N
    dodaj element 100:P
    usuń element o kluczu 8
    usuń element o kluczu 15
    wstaw element 55:R
    usuń element o kluczu 50
    usuń element o kluczu 5
    usuń element o kluczu 24
    wypisz wysokość drzewa
    wyświetl zawartość drzewa jako listę elementów
    wyświetl drzewo 2D
"""


def main():
    tree = BinarySearchTree()
    data_dic = {50:'A', 15:'B', 62:'C', 5:'D', 20:'E', 58:'F', 91:'G', 3:'H', 8:'I', 37:'J', 60:'K', 24:'L'}

    for key, data in data_dic.items():
        tree.insert(key, data)

    tree.print_tree()
    print(tree)

    print(tree.search(24))
    tree.insert(20, "AA")
    tree.insert(6, "M")
    tree.delete(62)
    tree.insert(59, "N")
    tree.insert(100, "P")
    tree.delete(8)
    tree.delete(15)
    tree.insert(55, "R")
    tree.delete(50)
    tree.delete(5)
    tree.delete(24)

    print(tree.height())
    print(tree)
    tree.print_tree()


if __name__ == "__main__":
    main()