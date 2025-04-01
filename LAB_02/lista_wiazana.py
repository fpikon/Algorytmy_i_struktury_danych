# OCENA 1.5/2

"""
def destroy(self):
    self.__head = None
    self.__tail = None
--- wyciek pamięci, obiekty na które coś wskazuje nie są automatycznie usuwane, a tu elementy wskazują na siebie nawzajem
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

class ListaWiazana:
    def __init__(self):
        self.__head = None

    def destroy(self):
        self.__head = None

    def add(self, data) -> None:
        node = Node(data)
        if self.is_empty():
            self.__head = node
        else:
            node.next = self.__head
            self.__head = node

    def append(self, data) -> None:
        node = Node(data)
        if self.is_empty():
            self.__head = node
        else:
            current = self.__head
            while current.next is not None:
                current = current.next
            current.next = node

    def remove(self):
        if self.is_empty():
            return None
        self.__head = self.__head.next

    def remove_end(self):
        if self.is_empty():
            return None
        elif self.length() == 1:
            self.__head = None
        else:
            current = self.__head
            previous = None
            while current.next is not None:
                previous = current
                current = current.next
            previous.next = None

    def is_empty(self) -> bool:
        if self.__head is None:
            return True
        return False

    def length(self) -> int:
        if self.is_empty():
            return 0
        len = 1
        current = self.__head
        while current.next is not None:
            len += 1
            current = current.next
        return len

    def get(self):
        if self.is_empty():
            return None
        return self.__head.data

    def __str__(self):
        if self.__head is None:
            return 'ListaWiazana is empty'
        else:
            str_list = [""]
            current = self.__head
            str_list.append(str(current))
            while current.next is not None:
                current = current.next
                str_list.append(str(current.data))
            return "\n-> ".join(str_list)

def main():
    lista_uczelni = [('AGH', 'Kraków', 1919),
                        ('UJ', 'Kraków', 1364),
                        ('PW', 'Warszawa', 1915),
                        ('UW', 'Warszawa', 1915),
                        ('UP', 'Poznań', 1919),
                        ('PG', 'Gdańsk', 1945)]

    uczelnie = ListaWiazana()
    for i in range(3):
        uczelnie.append(lista_uczelni[i])

    for i in range(3):
        uczelnie.add(lista_uczelni[i+3])

    print(uczelnie)
    print(" ")
    print(uczelnie.length())

    print(" ")
    uczelnie.remove()
    print(uczelnie.get())

    uczelnie.remove_end()
    print(uczelnie)

    print(" ")
    uczelnie.destroy()
    print(uczelnie.is_empty())

    uczelnie.remove()
    uczelnie.remove_end()
    print(" ")
    uczelnie.add(lista_uczelni[0])
    uczelnie.remove_end()
    print(uczelnie.is_empty())

if __name__ == "__main__":
    main()