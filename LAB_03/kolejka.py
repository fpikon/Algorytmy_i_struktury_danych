class Queue:
    def __init__(self, size) -> None:
        self.__tab = [None for _ in range(size)]
        self.__read_head = 0
        self.__write_head = 0
        self.__size = 0

    def is_empty(self) -> bool:
        if self.__read_head == self.__write_head:
            return True
        return False

    def peek(self):
        if self.is_empty():
            return None
        return self.__tab[self.__read_head]

    def dequeue(self):
        if self.is_empty():
            return None
        data = self.__tab[self.__read_head]
        self.__read_head += 1
        self.__size -= 1

        if self.__read_head == len(self.__tab):
            self.__read_head = 0
        return data

    def enqueue(self, data):
        self.__tab[self.__write_head] = data
        self.__write_head += 1
        self.__size += 1
        if self.__write_head == len(self.__tab):
            self.__write_head = 0
        if self.__write_head == self.__read_head:
            old_length = len(self.__tab)
            new_tab = [None for _ in range(2*old_length)]
            new_tab[0:self.__read_head] = self.__tab[0:self.__read_head]
            new_tab[self.__read_head + old_length:] = self.__tab[self.__read_head:]
            self.__read_head += old_length
            self.__tab = new_tab

    def __str__(self):
        if self.is_empty():
            return "[]"
        str_list = []
        temp_read = self.__read_head
        for i in range(self.__size):
            str_list.append(str(self.__tab[temp_read]))
            temp_read += 1
            if temp_read == len(self.__tab):
                temp_read = 0
            if temp_read == self.__write_head:
                break
        return "[" + ', '.join(str_list) + "]"

    def size(self):
        return self.__size

    def get_tab(self):
        return self.__tab

def main():
    q = Queue(5)
    for i in range(1, 5):
        q.enqueue(i)
    temp = q.dequeue()
    print(temp)

    temp = q.peek()
    print(temp)

    print(q)

    for i in range(5, 9):
        q.enqueue(i)
    print(q)
    print(q.get_tab())

    while not q.is_empty():
        q.dequeue()


    print(q)

if __name__ == '__main__':
    main()