# Ocena 2/2

"""
Sortowanie metodą Shella to w pewnym sensie uogólniona metoda sortowania przez wstawianie (ang. insertion sort).
W wersji "zwykłej" elementy przesuwane są o 1 pozycję aż trafią na odpowiednie miejsce.

W metodzie Shella możliwe jest przesuwanie elementów położonych dalej od siebie, co zmniejsza liczbę operacji i
zwiększa efektywność działania. Zamiast przesuwania elementów lepiej może się sprawdzić swapowanie.
Zamiast sprawdzania i przesuwania o 1 element poruszamy się co h elementów.
Taka operacja powinna być powtórzona h razy (czyli startujemy po kolei z pierwszych h elementów,
rozpatrując za każdym razem co h-ty element). Po wykonaniu wszystkich h przebiegów wartość h jest
zmniejszana i cały proces powtarzany, aż do momentu, gdy h osiągnie wartość 1 (to będzie ostatnie powtórzenie).

Istotnym czynnikiem, świadczącym o efektywności metody Shella, jest dobór odpowiednich odstępów h.
Niestety, znalezienie optymalnych wartości jest bardzo trudnym zadaniem. W pierwotnej propozycji shella h
zaczynało od wartości N//2 i było zmniejszane również dwukrotnie - zacznij od tej implementacji.

Lepszym wyborem początkowej wartości h może być największa wartość (3k-1)/2, mniejsza od N/3,
gdzie N to liczba elementów w zbiorze. Mniejsze odstępy h otrzymujemy poprzez całkowitoliczbowe dzielenie
poprzedniej wartości h przez 3.

Zaimplementuj 'zwykłe' sortowanie przez wstawianie oraz metodę Shella.

Dla listy: [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]
sprawdź działanie obu metod sortowania przez wstawianie i porównaj wyniki (stwórz z listy tablicę elementów
jak w poprzednim zadaniu). Zaobserwuj i wypisz stabilność obu wersji algorytmu sortującego.

Wygeneruj 10000 losowych elementów (o wartościach od 0 do 99), którymi wypełnisz wejściową tablicę.
Posortuj ją obiema metodami i porównaj  czas ich wykonania Porównaj także ten czas  z czasem wykonania
sortowania kopcowego z poprzedniego ćwiczenia.
UWAGA - dla każdego sortowania potrzebna jest osobna kopia tablicy, gdyż są to sortowania 'in situ'!
"""
import time
import random


def insertion_sort(tab):
    for i in range(1, len(tab)):
        j = i
        while j > 0 and tab[j-1] > tab[j]:
            tab[j], tab[j-1] = tab[j-1], tab[j]
            j -= 1


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

def main():
    tab = [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]
    shell_sort(tab)
    print(tab)

    tab = [(5, 'A'), (5, 'B'), (7, 'C'), (2, 'D'), (5, 'E'), (1, 'F'), (7, 'G'), (5, 'H'), (1, 'I'), (2, 'J')]
    insertion_sort(tab)
    print(tab)

    tab_size = 10000
    random_tab = [int(random.random() * 100) for i in range(tab_size)]
    t_start = time.perf_counter()
    shell_sort(random_tab)
    t_stop = time.perf_counter()
    print("Shell sort:")
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))

    random_tab = [int(random.random() * 100) for i in range(tab_size)]
    t_start = time.perf_counter()
    insertion_sort(random_tab)
    t_stop = time.perf_counter()
    print("Insertion sort:")
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))


if __name__ == "__main__":
    main()