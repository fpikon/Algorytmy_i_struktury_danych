class Node:
    def __init__(self, size):
        self.tab = [None for _ in range(size)]
        self.size = size
        self.count = 0
        self.next = None

    def __str__(self):
        return str(self.tab[:self.count])

class ULL:
    def __init__(self, size):
        self.__head = Node(size)
        self.__size = size

    def get(self, index):
        current = self.__head
        while index > self.__size:
            index -= current.count
            if current.next is None:
                raise Exception("Index out of range")
            current = current.next
        return current.tab[index]

    def insert(self, index, value):
        current = self.__head
        while index > self.__size:
            index -= current.count
            if current.next is None:
                raise Exception("Index out of range")
            current = current.next

        return value

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
    l = ULL(5)

    print(l)

if __name__ == '__main__':
    main()