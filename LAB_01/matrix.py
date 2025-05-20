# OCENA 5/5

class Matrix:
    def __init__(self, matrix, value=0):
        if isinstance(matrix, tuple):
            a = [[value] * matrix[1] for i in range(matrix[0])]
            self.__matrix = a
        else:
            self.__matrix = matrix

    def __getitem__(self, item):
        return self.__matrix[item]

    def __setitem__(self, item, value):
        self.__matrix[item] = value

    def size(self):
        return len(self.__matrix), len(self.__matrix[0])

    def __add__(self, other):
        if self.size() != other.size():
            raise Exception("Złe wymiary macierzy")
        else:
            row_s, col_s = self.size()
            new_matrix = Matrix((row_s, col_s))

            for i in range(row_s):
                for j in range(col_s):
                    new_matrix[i][j] = self[i][j] + other[i][j]
            return new_matrix

    def __mul__(self, other):
        if self.size()[1] != other.size()[0]:
            raise Exception("Złe wymiary macierzy")
        else:
            row_s, col_s = self.size()
            row_o, col_o = other.size()
            new_matrix = Matrix((row_s, col_o))

            for i in range(row_s):
                for j in range(col_o):
                    for k in range(col_s):
                        new_matrix[i][j] += self[i][k] * other[k][j]

            return new_matrix

    def __str__(self):
        a = []
        for i in range(self.size()[0]):
            a.append("\n|")
            for j in range(self.size()[1]):
                a.append(str(self.__matrix[i][j]))
            a.append("|")
        return " ".join(a)


def transpose(matrix):
    new_matrix = Matrix((matrix.size()[1], matrix.size()[0]))

    for i in range(matrix.size()[0]):
        for j in range(matrix.size()[1]):
            new_matrix[j][i] = matrix[i][j]
    return new_matrix


def main():
    m1 = Matrix(
        [[1, 0, 2],
         [-1, 3, 1],
         ])
    m2 = Matrix((2, 3), 1)
    m3 = Matrix(
        [[3, 1],
         [2, 1],
         [1, 0]
         ])
    print(transpose(m1))
    print(m1 + m2)
    print(m1 * m3)


if __name__ == '__main__':
    main()
