class Node:
    def __init__(self, size):
        self.tab = [None for _ in range(size)]
        self.size = size
        self.count = 0
        self.next = None

    def __str__(self):
        return str(self.tab)
        # return str(self.tab[:self.count])

class ULL:
    def __init__(self, size):
        self.__head = Node(size)
        self.__size = size

    def get(self, index):
        current = self.__head
        while index > current.count:
            if current.next is None:
                raise Exception("Index out of range")

            index -= current.count
            current = current.next
        return current.tab[index]

    def insert(self, index, value):
        current = self.__head
        # przejście do odpowiedniej listy
        while index > current.count:
            if current.next is None:

                break
            index -= current.count
            current = current.next

        # powiększenie listy jak jest pełna
        if current.count == self.__size:
            half_size = self.__size // 2
            new_node = Node(self.__size)
            new_node.next = current.next
            current.next = new_node
            new_node.tab[0:half_size] = current.tab[half_size:]
            current.tab[half_size:] = [None for _ in range(half_size)]
            current.count = half_size
            new_node.count = half_size

            # wybór odpowiedniej listy do dopisania
            if index >= half_size:
                index -= half_size
                current = current.next

        # dodawanie elementu do listy
        if index > current.count:
            current.tab[current.count] = value
        else:
            current.tab[index+1:] = current.tab[index:-1]
            current.tab[index] = value

        current.count += 1

    def delete(self, index):
        current = self.__head
        while index > current.count:
            if current.next is None:
                raise Exception("Index out of range")
            index -= current.count
            current = current.next

        temp = current.tab[index+1:]
        temp.append(None)
        current.tab[index:] = temp

        current.count -= 1



    def __str__(self):
        if self.__head is None:
            return 'List is empty'
        else:
            str_list = [""]
            current = self.__head
            str_list.append(str(current))
            while current.next is not None:
                current = current.next
                str_list.append(str(current.tab))
            return "\n-> ".join(str_list)


def main():
    l = ULL(6)
    for i in range(9):
        l.insert(i+1, i+1)
        print(l)
    print(l.get(4))

    l.insert(1, 10)
    print(l)
    l.insert(8, 11)
    print(l)



if __name__ == '__main__':
    main()