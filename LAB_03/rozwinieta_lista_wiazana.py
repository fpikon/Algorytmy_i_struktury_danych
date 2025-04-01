# OCENA 1.5/2
# odjął 0.5 punktu bo zły main został wysłany a tak to było git

class Node:
    def __init__(self, size):
        self.tab = [None for _ in range(size)]
        self.size = size
        self.count = 0
        self.next = None

    def insert(self, index, value):
        if index > self.count:
            self.tab[self.count] = value
        else:
            self.tab[index+1:] = self.tab[index:-1]
            self.tab[index] = value
        self.count += 1

    def delete(self, index):
        if index >= self.count:
            raise IndexError
        temp = self.tab[index + 1:]
        temp.append(None)
        self.tab[index:] = temp
        self.count -= 1

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
                raise IndexError

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
            size_half = self.__size // 2
            size_half_2 = self.__size - size_half
            new_node = Node(self.__size)
            new_node.next = current.next
            current.next = new_node
            new_node.tab[0:size_half] = current.tab[size_half_2:]
            current.tab[size_half_2:] = [None for _ in range(size_half)]
            current.count = size_half_2
            new_node.count = size_half

            # wybór odpowiedniej listy do dopisania
            if index >= size_half:
                index -= size_half
                current = current.next

        # dodawanie elementu do listy
        current.insert(index, value)


    def delete(self, index):
        current = self.__head
        next_node = current.next
        while index > current.count:
            if current.next is None:
                raise IndexError
            index -= current.count
            current = current.next

        current.delete(index)

        #zmniejszenie ilości tablic w liście
        if current.count <= self.__size//2:
            if current.next is not None:
                for i in range(next_node.count):
                    data = next_node.tab[0]
                    next_node.delete(0)
                    current.insert(current.count, data)
                    if current.count >= self.__size//2 and not next_node.count <= self.__size//2:
                        break
                if next_node.count == 0:
                    current.next = next_node.next



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
    print(l.get(4))

    l.insert(1, 10)
    l.insert(8, 11)
    print(l)

    l.delete(1)
    l.delete(2)
    print(l)



if __name__ == '__main__':
    main()