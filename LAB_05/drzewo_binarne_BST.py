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


class BinaryTree:
    def __init__(self):
        self.root = None

    def __find_node(self, key, node, path = None):
        if path is None:
            path = []

        if node is None:
            return None, path
        if node.key == key:
            return node, path
        elif node.key < key:
            path.append(node)
            return self.__find_node(key, node.right, path)
        else:
            path.append(node)
            return self.__find_node(key, node.left, path)

    def search(self, key):
        node, path = self.__find_node(key, self.root)
        return node.data if node else None

    def insert(self, key, data):
        self.__insert_it(self.root, key, data)

    def __insert_it(self, node, key, data):
        if self.root is None:
            self.root = Node(key, data)
            return None
        if node is None:
            return Node(key, data)
        if node.key == key:
            node.data = data
            return node
        elif node.key > key:
            node.left = self.__insert_it(node.left, key, data)
            return node
        else:
            node.right = self.__insert_it(node.right, key, data)
            return node

    def delete(self, key):
        node, path = self.__find_node(key, self.root)

        # zły klucz
        if node is None:
            return

        # 0 dzieci
        if node.left is None and node.right is None:
            parent = path.pop()
            if node.key > parent.key:
                parent.right = None
            else:
                parent.left = None
            return

        # 1 dziecko
        # dziecko po prawej
        if node.left is None:
            parent = path.pop()
            if node.key < parent.key:
                parent.left = node.right
            else:
                parent.right = node.right
            return

        # dziecko po lewej
        if node.right is None:
            parent = path.pop()
            if node.key < parent.key:
                parent.left = node.left
            else:
                parent.right = node.left
            return

        # 2 dzieci
        successor_node, successor_parent = self.__successor(node.key)
        node.data = successor_node.data
        node.key = successor_node.key
        if successor_parent == node:
            successor_parent.right = None
            return
        successor_parent.left = None
        return

    def __successor(self, key):
        node, path = self.__find_node(key, self.root)
        if node is None:
            return None
        successor_node = node.right
        while successor_node.left is not None:
            node = successor_node
            successor_node = successor_node.left

        return successor_node, node

    def height(self):
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
    tree = BinaryTree()
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

    tree.print_tree()

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