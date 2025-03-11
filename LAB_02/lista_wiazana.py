#!/usr/bin/python
# -*- coding: utf-8 -*-

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

class ListaWiazana:
    def __init__(self):
        self.head = None

    def destroy(self):
        self.head = None

    def add(self, data) -> None:
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def append(self, data) -> None:
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node

    def remove(self):
        if self.head is None:
            return None
        self.head = self.head.next

    def remove_end(self):
        if self.head is None:
            return None
        elif self.head.next is None:
            self.head = None
        else:
            current = self.head
            previous = None
            while current.next is not None:
                previous = current
                current = current.next
            previous.next = None

    def is_empty(self) -> bool:
        if self.head is None:
            return True
        return False

    def length(self) -> int:
        if self.head is None:
            return 0
        len = 1
        current = self.head
        while current.next is not None:
            len += 1
            current = current.next
        return len

    def get(self):
        if self.head is None:
            return None
        return self.head.data

    def __str__(self):
        if self.head is None:
            return 'ListaWiazana is empty'
        else:
            str_list = [""]
            current = self.head
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