"""
Celem ćwiczenia jest implementacja dwóch metod sortowania - przez kopcowanie (ang. heapsort) oraz przez wybieranie (ang. selection sort).

1. Możliwym (ale nie wykorzystanym przez nas) sposobem użycia kopca do posortowania tablicy  jest  wstawienie danych z
nieposortowanej tablicy do kopca, a następnie zdejmowanie ich z wierzchołka i wstawianie z powrotem  do tablicy,
która w ten sposób zostanie posortowana.
To podejście wymaga jednak dodatkowej pamięci na kopiec. W tym ćwiczeniu spróbujemy dokonać sortowania kopcowego
w miejscu czyli BEZ dodatkowej pamięci. Do tego wykorzystamy kod napisany w ćwiczeniu dotyczącym kolejki priorytetowej.
Napisane do tej pory metody będą wymagały jedynie niewielkich zmian.

Proszę o skopiowanie rozwiązania sprzed tygodnia. Zaczniemy od uzupełnienia konstruktora klasy reprezentującej kopiec
o parametr zawierający tablicę elementów do posortowania (jako parametr z wartością domyślną None).
Przekazana tablica powinna zostać przypisana do atrybutu przechowującego tablicę z kopcem - na poprzednich zajęciach
była to zapewne pusta lista. Teraz pusta lista ma być przypisywana tylko jeżeli argument konstruktora jest None-m.
W przeciwnym wypadku konstruktor powinien w przekazanej tablicy utworzyć kopiec. Robimy to następująco:

Już powinniśmy dysponować metodą naprawiającą kopiec przesuwającą korzeń w dół drzewa (używaną w dequeue).
Jeżeli, wbrew instrukcji, ktoś nie wydzielił tej metody w zadaniu z kolejką priorytetową, musi to zrobić teraz.
Wydzieloną metodę wystarczy wywołać dla wszystkich węzłów nie będących liśćmi, co spowoduje ich przesunięcie we właściwe
miejsce kopca. Należy jednak zachować kolejność: od ostatniego elementu, który nie jest liściem
(czyli rodzica ostatniego elementu tablicy), aż do korzenia.  Ta metoda działa w czasie O(N).

Sortowanie zostanie wykonane przez 'rozebranie' kopca, czyli usuniecie z niego wszystkich elementów.
W zasadzie już mamy kod, który to realizuje - usuwając korzeń przemieszczamy go na ostatnią pozycję w kopcu
(a ostatni element jest przemieszczany w jego miejsce). Jednakże osoby, które fizycznie usuwały z tablicy ostatni element
(np. metodą pop) muszą teraz przerobić swój program - należy  tak zmodyfikować metodę dequeue, żeby nie usuwała
ostatniego elementu, a rozmiar kopca nie może zależeć od rozmiaru tablicy (musi być 'ręcznie' zwiększany  w enqueue i
zmniejszany w dequeue).
Bez fizycznego usuwania  po 'rozebraniu'  kopca dostaniemy posortowaną tablicę
(jeżeli kopiec był kopcem maksymalnym to uzyskamy tablicę posortowaną rosnąco - na końcu wyląduje element największy,
potem coraz mniejsze).

W main-ie wykonaj 2 osobne testy. Niech main zacznie się od wczytania numeru testu i w zależności od wpisanej wartości
(1 lub 2) wykona się zadany test.

TEST 1:
Niech dana będzie lista z danymi:
 [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]
Stwórz na jej podstawie listę (tablicę), której elementy są obiektami utworzonej na poprzednich zajęciach klasy.
Przykładowo może to być instrukcja:
[ Elem(key, value) for key,value in  [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]]
Przekaż tak utworzoną tablicę jako parametr konstruktora przy tworzeniu kopca.
Wypisz utworzony kopiec jako tablicę i jako drzewo 2D, a następnie, po rozebraniu kopca, wypisz posortowaną tablicę
(tą którą kopiec dostał jako argument przy jego tworzeniu).
Zaobserwuj i wypisz, czy sortowanie jest stabilne, tzn. czy kolejność elementów o tym samym priorytecie zostanie zachowana
(w porównaniu z ich kolejnością w liście z danymi). Wypisane powinno zostać jedno słowo:
STABILNE lub NIESTABILNE


2. Drugim algorytmem do zrealizowania jest sortowanie przez wybieranie.

 Napisz dwie metody sortujące pythonową listę algorytmem przez wybieranie: jedną, wykorzystującą zamianę miejscami
 elementów (swap), i drugą, wykorzystującą przesunięcie elementów (shift).
 W tym drugim wypadku shift można osiągnąć przez pop i insert.


Analogicznie jak w poprzednim punkcie z listy krotek: [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'),
(5,'H'), (1,'I'), (2,'J')] stwórz  tablicę elementów, posortuj ją wariantem 'swap', wypisz postortowaną tablicę.
Zaobserwuj i wypisz, czy sortowanie jest stabilne. Wypisane powinno zostać jedno słowo:
STABILNE lub NIESTABILNE
Stwórz ponownie tablicę elementów (gdyż poprzednia jest już posortowana), posortuj ją wariantem 'shift',
wypisz postortowaną tablicę.   Zaobserwuj i wypisz, czy sortowanie jest stabilne. Wypisane powinno zostać jedno słowo:
STABILNE lub NIESTABILNE


TEST 2:
Wygeneruj losowo 10000 liczb w przedziale od 0 do 99 i wpisz je do tablicy.
Posortuj tę tablicę przez stworzenie i rozebranie kopca. Wypisz czas sortowania takiej tablicy (uwzględniający czas
stworzenia kopca z tablicy). W celu realizacji tego zadania  należy zaimportować moduły random i time.
Do generowania liczb można wykorzystać zapis int(random.random() * 100) powodujący wylosowanie liczby całkowitej z
zakresu 0-99, natomiast do pomiaru czasu można zaadaptować kod:

t_start = time.perf_counter()
# testowana metoda
t_stop = time.perf_counter()
print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))

Powtórz sortowanie dla metody przez wybieranie w waruancie 'swap' i 'shift'. Wypisz czasy obu sortowań.

UWAGA - dla każdego sortowania potrzebna jest osobna kopia tablicy, gdyż są to sortowania 'in situ' i po każdym tablica jest postortowana.

"""
import random
import time


class Node:
    def __init__(self, priorytet ,data):
        self.__dane = data
        self.__priorytet = priorytet

    def __lt__(self, other):
        return self.__priorytet < other.__priorytet

    def __gt__(self, other):
        return self.__priorytet > other.__priorytet

    def __repr__(self):
        return f"{self.__priorytet}: {self.__dane}"


class Kopiec:
    def __init__(self, tab = None):
        if tab is None:
            self.tab = []
            self.heap_size = 0
        else:
            self.tab = tab
            self.heap_size = len(tab)
            i = self.parent(self.heap_size - 1)
            while i >= 0:
                self.fix_dequeue(i)
                i -= 1

    def is_empty(self):
        return True if self.heap_size <= 0 else False

    def peek(self):
        if self.is_empty():
            return None
        return self.tab[0]

    def enqueue(self, new_node):
        if len(self.tab) > self.heap_size:
            self.tab[self.heap_size] = new_node
        else:
            self.tab.append(new_node)

        i = self.heap_size
        self.heap_size += 1

        # warunek kopca
        self.fix_enqueue(i)

    def fix_enqueue(self, idx):
        if idx <= 0 or idx >= len(self.tab):
            return
        if self.tab[idx] > self.tab[self.parent(idx)]:
            self.tab[idx], self.tab[self.parent(idx)] = self.tab[self.parent(idx)], self.tab[idx]
            self.fix_enqueue(self.parent(idx))
        else:
            return

    def dequeue(self):
        if self.is_empty():
            return None

        top = self.tab[0]
        last_idx = self.heap_size - 1
        self.tab[0], self.tab[last_idx] = self.tab[last_idx], self.tab[0]

        self.heap_size -= 1
        i = 0

        self.fix_dequeue(i)
        # warunek kopca
        return top

    def fix_dequeue(self, idx):
        if idx < 0 or idx >= self.heap_size:
            return
        child_left = self.left(idx)
        child_right = self.right(idx)

        # brak potomków
        if child_left >= self.heap_size and child_right >= self.heap_size:
            return
        # jeden potomek (jak jest jeden potomek to jest on lewy)
        if child_left < self.heap_size <= child_right:
            if self.tab[idx] < self.tab[child_left]:
                self.tab[idx], self.tab[child_left] = self.tab[child_left], self.tab[idx]
                self.fix_dequeue(child_left)
                return
            else:
                return
        # dwoje potomków
        if self.tab[idx] < self.tab[child_right] or self.tab[idx] < self.tab[child_left]:
            if self.tab[child_left] > self.tab[child_right]:
                self.tab[idx], self.tab[child_left] = self.tab[child_left], self.tab[idx]
                self.fix_dequeue(child_left)
                return
            else:
                self.tab[idx], self.tab[child_right] = self.tab[child_right], self.tab[idx]
                self.fix_dequeue(child_right)
                return
        else:
            return

    def left(self, idx):
        return 2 * idx + 1

    def right(self, idx):
        return 2 * idx + 2

    def parent(self, idx):
        return (idx - 1) // 2

    def print_tab(self):
        print ('{', end=' ')
        print(*self.tab[:self.heap_size], sep=', ', end = ' ')
        print( '}')

    def print_tree(self, idx, lvl):
        if idx<len(self.tab):
            self.print_tree(self.right(idx), lvl+1)
            print(2*lvl*'  ', self.tab[idx] if self.tab[idx] else None)
            self.print_tree(self.left(idx), lvl+1)

    def __str__(self):
        return f'{self.tab}'

def selection_sort_swap(tab):
    for i in range(len(tab)-1):
        j_min = i
        for j in range(i+1, len(tab)):
            if tab[j] < tab[j_min]:
                j_min = j
        if j_min != i:
            tab[i], tab[j_min] = tab[j_min], tab[i]

def selection_sort_shift(tab):
    for i in range(len(tab)-1):
        j_min = i
        for j in range(i+1, len(tab)):
            if tab[j] < tab[j_min]:
                j_min = j
        if j_min != i:
            item = tab.pop(j_min)
            tab.insert(i, item)

def shell_sort(tab):
    k = 1
    h = ((3**k)-1) // 2
    while ((3 ** k) - 1) // 2 < len(tab) / 3:
        h = ((3 ** k) - 1) // 2
        k += 1

    insertion_sort_shell(tab, h)

def insertion_sort_shell(tab, h):
    if h < 1:
        return
    for a in range(h):
        for i in range(a-1, len(tab), h):
            j = i
            while j > 0 and tab[j-h] > tab[j]:
                tab[j], tab[j - h] = tab[j - 1], tab[j]
                j -= h
    insertion_sort_shell(tab, h // 3)

def test_1():
    data_tab =  [ Node(key, value) for key,value in  [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]]

    kopiec = Kopiec(data_tab)

    kopiec.print_tab()
    kopiec.print_tree(0, 0)
    while not kopiec.is_empty():
        kopiec.dequeue()
    print(data_tab)
    print("NIESTABILNE")

    data_tab =  [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]
    selection_sort_swap(data_tab)
    print(data_tab)
    print("STABILNE")

    data_tab =  [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]
    selection_sort_shift(data_tab)
    print(data_tab)
    print("STABILNE")

def test_2():
    tab_size = 10000
    random_tab = [int(random.random() * 100) for i in range(tab_size)]
    random_tab_2 = random_tab.copy()
    t_start = time.perf_counter()
    kopiec = Kopiec(random_tab)
    while not kopiec.is_empty():
        kopiec.dequeue()
    t_stop = time.perf_counter()
    print("Heap sort:")
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))


    t_start = time.perf_counter()
    shell_sort(random_tab_2)
    t_stop = time.perf_counter()
    print("Selection sort swap:")
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))

    """random_tab = [int(random.random() * 100) for i in range(tab_size)]
    t_start = time.perf_counter()
    selection_sort_swap(random_tab)
    t_stop = time.perf_counter()
    print("Selection sort swap:")
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))

    random_tab = [int(random.random() * 100) for i in range(tab_size)]
    t_start = time.perf_counter()
    selection_sort_shift(random_tab)
    t_stop = time.perf_counter()
    print("Selection sort shift:")
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))"""

def main():
    #aaa = input("Numer testu: ")
    aaa = ('2')
    if aaa == '1':
        test_1()
    elif aaa == '2':
        test_2()
    else:
        print("Zły numer testu")

if __name__=="__main__":
    main()