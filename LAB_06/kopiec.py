# Ocena 5/5

"""
Celem ćwiczenia jest implementacja kolejki priorytetowej jako kopca (maksymalnego) zrealizowanego w postaci tablicy. Jako tablicę można wykorzystać listę pythonową (albo z natywną obsługą, albo realokowaną  'ręcznie' jak w zadaniu z tablicą cykliczną).

Tym razem implementacja kolejki priorytetowej będzie niezależna od danych w niej przechowywanych. Kolejka będzie tablicą DOWOLNYCH elementów, jedynym wymogiem jest to aby można było te elementy uporządkować (czyli np. muszą być na nich zdefiniowane relacje < i >). W konsekwencji, jeżeli nawet kolejka będzie zawierać obiekty jakiejś klasy to składowe tej klasy nie mają być przez kolejkę znane (w naszym przykładzie będą prywatne).

Element kolejki niech będzie obiektem klasy, której atrybutami będą __dane i __priorytet. Ta klasa powinna mieć zdefiniowane 'magiczne' metody pozwalające na użycie na jej obiektach operatorów < i >  (metody __lt__ i __gt__) oraz wypisanie ich print-em (__repr__ co jest 'lepszą' wersją __str__) w postaci
 priorytet : dane.
Dzięki zastosowaniu operatorów < i > atrybuty __dane i  __priorytet mogą (i powinny być) prywatne.

Klasa reprezentująca kolejkę powinna zawierać pola przechowujące:  tablicę oraz aktualny rozmiar kopca (dopóki koiec będzie rósł to rozmiar tablicy i kopca będą takie same, jednak po dequeue proszę tylko zmniejszyć rozmiar kopca BEZ fizycznego usuwania z tablicy) oraz następujące metody:

    konstruktor tworzący pustą kolejkę
    is_empty - zwracająca True jeżeli kolejka jest pusta
    peek - zwracająca None jeżeli kolejka jest pusta lub element kolejki o najwyższym priorytecie
    dequeue - zwracająca None jeżeli kolejka jest pusta lub element kolejki o najwyższym priorytecie
    (zdejmując go z wierzchołka kopca - ale NIE usuwjąc z tablicy)
    enqueue - otrzymująca dane do wstawienia do kolejki (kopca)  - tym razem będzie to cały obiekt klasy
    implementującej element kolejki (czyli metoda ma mieć tylko jeden parametr oprócz self).
    UWAGA - element początkowo jest dokładany na koniec KOPCA, więc:
        jeżeli rozmiar kopca bedzie taki jak rozmiar tablicy, to będzie oznaczało append,
        a jeżeli będzie mniejszy to będzie to tylko zwiększenie rozmiaru kopca bez powiększania tablicy
        (wpis nastąpi do tablicy zamazując element wcześniej usunięty z kopca)

Kopiec będzie jeszcze przydatny w sortowaniu, dlatego przy jego implementacji warto zadbać aby:
-  metodę deqeue tak zaimplementować, aby nie zmniejszać tablicy a jedynie zapamietywać aktualną 'długość' kopca (chodzi o to aby nie usuwać 'fizycznie' ostatniego elementu)
- z dequeue wydzielić pętlę naprawiającą kopiec jako osobną metodę otrzymującą jako argument indeks węzła od którego zaczynamy naprawę (teraz będzie to 0, ale w sortowaniu pojawią się inne indeksy).

Dodatkowo, aby usprawnić poruszanie się po kopcu, proszę napisać metody left i right,
które otrzymawszy indeks węzła zwracają indeks odpowiednio lewego i prawego potomka,
oraz metodę parent, która na podstawie indeksu węzła zwraca indeks jego rodzica.

Należy także utworzyć funkcje/metody:  wypisująca kolejkę jak słownik (elementy tablicy jako pary priorytet : dane rozdzielone przecinkami, całość w nawiasach { }) i wypisująca kolejkę jak drzewo.
Do wypisania jak słownik  proszę wykorzystać poniższy kod (który należy przerobić celem dostosowania do własnej implementacji):
    def print_tab(self):
        print ('{', end=' ')
        print(*self.tab[:self.heap_size], sep=', ', end = ' ')
        print( '}')

Do wypisania drzewa proszę wykorzystać poniższy kod (który należy przerobić celem dostosowania do własnej implementacji):
    def print_tree(self, idx, lvl):
        if idx<self.size:
            self.print_tree(self.right(idx), lvl+1)
            print(2*lvl*'  ', self.tab[idx] if self.tab[idx] else None)
            self.print_tree(self.left(idx), lvl+1)

Celem wypisania drzewa należałoby tak wywołać powyższą metodę:
    kol_prior.print_tree(0, 0);

UWAGA:
Proszę pamiętać, że w każdej operacji dodania/usunięcia warunek kopca ma zostać zachowany. Przywracanie warunku kopca ma mieć złożoność O(log n),
czyli nie może polegać na przeglądnięciu wszystkich elementów posiadających potomków (to byłaby złożoność O(n)).
Z tego samego powodu nie można używać list.index (złożoność O(n))

W main-ie sprawdź działanie zaimplementowanej kolejki przez:

    utworzenie pustej kolejki
    użycie w pętli enqueue do wpisana do niej elementów których priorytety będą brane z listy [7, 5, 1, 2, 5, 3, 4, 8, 9], a odpowiadające im wartości będą kolejnymi literami z napisu "GRYMOTYLA"
    wypisanie aktualnego stanu kolejki w postaci kopca
    wypisanie aktualnego stanu kolejki w postaci tablicy
    użycie dequeue do odczytu  pierwszej  danej z kolejki, proszę ją zapamiętać
    użycie  peek do odczytu i wypisania kolejnej  danej
    wypisanie aktualnego stanu kolejki w postaci tablicy
    wypisanie zapamiętanej, usuniętej pierwszej danej z kolejki
    opróżnienie kolejki z wypisaniem usuwanych danych (użycie dequeue w pętli dopóki w kolejce będą dane)
    wypisanie opróżnionej kolejki w postaci tablicy (powinno się wypisać { } )
"""

class Node:
    def __init__(self, data, priorytet):
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
        else:
            self.tab = tab
        self.heap_size = 0

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

        return top

    def fix_dequeue(self, idx):
        if idx < 0 or idx >= self.heap_size:
            return
        if self.left(idx) >= self.heap_size and self.right(idx) >= self.heap_size:
            return

        # jeden potomek (jak jest jeden potomek to jest on lewy)
        if self.left(idx) < self.heap_size <= self.right(idx):
            if self.tab[idx] < self.tab[self.left(idx)]:
                self.tab[idx], self.tab[self.left(idx)] = self.tab[self.left(idx)], self.tab[idx]
                self.fix_dequeue(self.left(idx))
            else:
                return
        # dwoje potomków
        if self.tab[idx] < self.tab[self.right(idx)] or self.tab[idx] < self.tab[self.left(idx)]:
            if self.tab[self.left(idx)] > self.tab[self.right(idx)]:
                self.tab[idx], self.tab[self.left(idx)] = self.tab[self.left(idx)], self.tab[idx]
                self.fix_dequeue(self.left(idx))
            else:
                self.tab[idx], self.tab[self.right(idx)] = self.tab[self.right(idx)], self.tab[idx]
                self.fix_dequeue(self.right(idx))
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


def main():
    kolejka = Kopiec()

    keys = [7, 5, 1, 2, 5, 3, 4, 8, 9]
    data = "GRYMOTYLA"

    for key, d in zip(keys, data):
        new_node = Node(d, key)
        print(new_node)
        kolejka.print_tab()
        kolejka.enqueue(new_node)
        kolejka.print_tab()
        print("\n")


    kolejka.print_tree(0, 0)
    kolejka.print_tab()

    top = kolejka.dequeue()
    print(kolejka.peek())

    kolejka.print_tab()

    print(top)

    while not kolejka.is_empty():
        top = kolejka.dequeue()
        print(top)

    kolejka.print_tab()


if __name__=="__main__":
    main()