"""
Zaimplementuj w języku Python drzewo AVL przerabiając program z poprzedniego zadania.
Klasa reprezentująca węzeł drzewa powinna zawierać dodatkowe pole wykorzystywane do  równoważenia drzewa
(może to być pole przechowujące wysokość węzła).
Klasa reprezentująca drzewo powinna mieć zmodyfikowane metody dodawania i usuwania węzłów (szczegóły poniżej).
Po wykonaniu operacji dodawania lub usuwania węzłów odbywa się określona operacja rotacji węzłów,
która przywraca zrównoważenie drzewa binarnego.
Zaimplementuj funkcjonalności takie jak w drzewie BST w poprzednim zadaniu.
Należy jednak tym razem przy dodawaniu i usuwaniu węzłów uwzględnić równoważenie drzewa.

W przypadku braku zrównoważenia drzewa AVL konieczna jest odpowiednia rotacja konkretnych węzłów.

Przykład uwzględniający podwójną rotację RL:


Cyfry pod literami A, B i C są wartościami tzw. współczynnika wyważenia.
Można przyjąć, że jest to różnica wysokości lewego i prawego poddrzewa.

Współczynnik wyważenia korzenia jest mniejszy od zera, więc wymaga rotacji w lewo.
Zanim zostanie wykonana dodatkowo sprawdzany jest współczynnik wyważenia prawego dziecka.
Jeśli dziecko ma współczynnik wyważenia większy od zera (dłuższa lewa gałąź) to wymagana jest rotacja w prawo
względem dziecka. Po niej dopiero następuje rotacja w lewo względem korzenia.
Istnieją 4 przypadki, kiedy konieczna jest rotacja:
LL - Wsp. węzła = -2 i  wsp. prawego potomka <=0
RL - Wsp. węzła = -2 i  wsp. prawego potomka > 0
RR - Wsp. węzła = 2 i  wsp. lewego potomka >= 0
LR - Wsp. węzła = 2 i  wsp. lewego potomka < 0

Działania:
LL - Lewa rotacja
LR - Lewa rotacja + prawa rotacja
RR - Prawa rotacja
RL - Prawa rotacja + lewa rotacja

Należy zaimplementować funkcje, które będą realizować rotację w lewo oraz rotację w prawo (LL i RR).
LR i RL są złożeniami  LL i RR.


Każde dodanie nowego i usunięcie istniejącego węzła powinno spowodować przeliczenie na nowo wysokości jego rodzica
(i dalszych przodków). Korzysta się tu z tego, że wysokość węzła jest o jeden większa od wysokości 'wyższego' potomka.

Każda rotacja  również wymaga przeliczenia rotowanych węzłów (tylko dwóch - proszę się zastanowić których).

W main-ie sprawdź działanie zaimplementowanego drzewa przez:

    utworzenie pustego drzewa BST
    dodanie kolejno elementy klucz:wartość --
    {50:'A', 15:'B', 62:'C', 5:'D', 2:'E', 1:'F', 11:'G', 100:'H', 7:'I', 6:'J', 55:'K', 52:'L', 51:'M', 57:'N', 8:'O',
    9:'P', 10:'R', 99:'S', 12:'T'} tworząc drzewo o podanej strukturze, jak na rysunku:


Dla porównania tak wygląda drzewo niewyważone, czyli drzewo BST:

    wyświetl drzewo 2D
    wyświetl zawartość drzewa jako listę od najmniejszego do największego klucza w formie klucz:wartość
    wyszukaj element o kluczu 10 i wypisz wartość
    usuń element o kluczu 50
    usuń element o kluczu 52
    usuń element o kluczu 11
    usuń element o kluczu 57
    usuń element o kluczu 1
    usuń element o kluczu 12
    dodaj element o kluczu 3:AA
    dodaj element o kluczu 4:BB
    usuń element o kluczu 7
    usuń element o kluczu 8
    wyświetl drzewo 2D
    wyświetl zawartość drzewa jako listę od najmniejszego do największego klucza w formie klucz:wartość

Efekt końcowy:
"""
from time import process_time_ns


class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

    def __str__(self):
        return f"{self.key} {self.data}"


class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node = 0):
        if node == 0:
            node = self.root
        return node.height if node else 0

    def get_balance(self, node = 0):
        if node == 0:
            node = self.root
        return self.height(node.left) - self.height(node.right) if node else 0

    def rotate_right(self, a):
        if a is None or a.left is None:
            return a
        b = a.left
        c = b.right
        b.right = a
        a.left = c

        a.height = max(self.height(a.left), self.height(a.right)) + 1
        b.height = max(self.height(b.left), self.height(b.right)) + 1
        return b

    def rotate_left(self, a):
        if a is None or a.right is None:
            return a
        b = a.right
        c = b.left
        b.left = a
        a.right = c
        a.height = max(self.height(a.left), self.height(a.right)) + 1
        b.height = max(self.height(b.left), self.height(b.right)) + 1
        return b

    def balance(self, node):
        balance_factor = self.get_balance(node)

        if balance_factor > 1:
            if self.get_balance(node.left) < 0:
                node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        if balance_factor < -1:
            if self.get_balance(node.right) > 0:
                node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

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

        node.height = max(self.height(node.left), self.height(node.right)) + 1
        return self.balance(node)

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

        node.height = max(self.height(node.left), self.height(node.right)) + 1
        return self.balance(node)

    def __successor(self, node):
        while node.left is not None:
            node = node.left
        return node

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

def main():
    data_dic = {50:'A', 15:'B', 62:'C', 5:'D', 2:'E', 1:'F', 11:'G', 100:'H', 7:'I', 6:'J', 55:'K', 52:'L', 51:'M', 57:'N', 8:'O', 9:'P', 10:'R', 99:'S', 12:'T'}
    tree = AVLTree()

    for key, value in data_dic.items():
        tree.insert(key, value)

    tree.print_tree()
    print(tree)
    print(tree.search(10))

    to_delete = [50, 52, 11, 57, 1, 12]
    for i in to_delete:
        tree.delete(i)

    tree.insert(3, "AA")
    tree.insert(4, "BB")

    tree.delete(7)
    tree.delete(8)

    tree.print_tree()
    print(tree)


if __name__ == "__main__":
    main()