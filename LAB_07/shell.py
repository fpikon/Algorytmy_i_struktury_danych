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

def selection_sort(tab):
    for i in range(len(tab)-1):
        j_min = i
        for j in range(i+1, len(tab)):
            if tab[j] < tab[j_min]:
                j_min = j
        if j_min != i:
            tab[i], tab[j_min] = tab[j_min], tab[i]

def shell_sort(tab):
    h = len(tab)
    for i in range(len(tab)-1):
        j_min = i
        for j in range(i+1, len(tab)):
            if tab[j] < tab[j_min]:
                j_min = j
        if j_min != i:
            tab[i], tab[j_min] = tab[j_min], tab[i]

def main():
    return 0

if __name__ == "__main__":
    main()