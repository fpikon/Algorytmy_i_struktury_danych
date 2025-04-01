# OCENA 4.5/5
"""
elif self.length() == 1: --- przejście po całej liście, a wystarczyło sprawdzić jeden warunek (self.head.next == None)
self.__head = None
"""
class NodeDwuKier:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.data)

class ListaDwuKier:
    def __init__(self):
        self.__head = None
        self.__tail = None

    def destroy(self):
        self.__head = None
        self.__tail = None

    def add(self, data) -> None:
        node = NodeDwuKier(data)
        if self.is_empty():
            self.__head = node
            self.__tail = node
        else:
            node.next = self.__head
            self.__head.prev = node
            self.__head = node

    def append(self, data) -> None:
        node = NodeDwuKier(data)
        if self.is_empty():
            self.__head = node
            self.__tail = node
        else:
            node.prev = self.__tail
            self.__tail.next = node
            self.__tail = node

    def remove(self):
        if self.is_empty():
            return None
        elif self.length() == 1:
            self.__head = None
            self.__tail = None
        else:
            self.__head = self.__head.next
            self.__head.prev = None

    def remove_end(self):
        if self.is_empty():
            return None
        elif self.length() == 1:
            self.__head = None
            self.__tail = None
        else:
            self.__tail = self.__tail.prev
            self.__tail.next = None

    def is_empty(self) -> bool:
        if self.__head is None and self.__tail is None:
            return True
        return False

    def length(self) -> int:
        if self.is_empty():
            return 0
        list_len = 1
        current = self.__head
        while current.next is not None:
            list_len += 1
            current = current.next
        return list_len

    def get(self):
        if self.is_empty():
            return None
        return self.__head.data

    def __str__(self):
        if self.is_empty():
            return 'ListaWiazana is empty'
        else:
            str_list = [""]
            current = self.__head
            str_list.append(str(current))
            while current.next is not None:
                current = current.next
                str_list.append(str(current.data))
            return "\n-> ".join(str_list)

    def reversed_print(self):
        if self.is_empty():
            print('ListaWiazana is empty')
        else:
            str_list = [""]
            current = self.__tail
            str_list.append(str(current))
            while current.prev is not None:
                current = current.prev
                str_list.append(str(current.data))
            print('\n-> '.join(str_list))


def main():
    lista_uczelni = [('AGH', 'Kraków', 1919),
                        ('UJ', 'Kraków', 1364),
                        ('PW', 'Warszawa', 1915),
                        ('UW', 'Warszawa', 1915),
                        ('UP', 'Poznań', 1919),
                        ('PG', 'Gdańsk', 1945)]

    uczelnie = ListaDwuKier()
    for i in range(3):
        uczelnie.append(lista_uczelni[i])

    for i in range(3):
        uczelnie.add(lista_uczelni[i+3])

    print(uczelnie)
    uczelnie.reversed_print()
    print(" ")
    print(uczelnie.length())

    print(" ")
    uczelnie.remove()
    print(uczelnie.get())

    uczelnie.remove_end()
    print(uczelnie)
    uczelnie.reversed_print()

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