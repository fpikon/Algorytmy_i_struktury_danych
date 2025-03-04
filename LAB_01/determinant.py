from matrix import *


def determinant(matrix: Matrix):
    det = 1
    size_m = matrix.size()
    if size_m[0] != size_m[1] or size_m[0] < 2:
        raise Exception("Złe wymiary macierzy")
    size_m = size_m[0]
    if size_m == 2:
        det = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
    else:
        if matrix[0][0] == 0:
            for i in range(1, size_m):
                if matrix[i][0] != 0:
                    det *= -1
                    temp_row = matrix[0]
                    matrix[0] = matrix[i]
                    matrix[i] = temp_row
                    break

        reduced_matrix = Matrix((size_m-1, size_m-1))
        for i in range(size_m-1):
            for j in range(size_m-1):
                matrix_2x2 = Matrix([
                        [matrix[0][0], matrix[0][j+1]],
                        [matrix[i+1][0], matrix[i+1][j+1]]
                    ])
                reduced_matrix[i][j] = determinant(matrix_2x2)
        det *= 1 / (matrix[0][0])**(size_m-2) * determinant(reduced_matrix)
    return det


def main():
    m1 = Matrix([
        [5, 1, 1, 2, 3],
        [4, 2, 1, 7, 3],
        [2, 1, 2, 4, 7],
        [9, 1, 0, 7, 0],
        [1, 4, 7, 2, 2]])

    m2 = Matrix([
        [0, 1, 1, 2, 3],
        [4, 2, 1, 7, 3],
        [2, 1, 2, 4, 7],
        [9, 1, 0, 7, 0],
        [1, 4, 7, 2, 2]])

    print(determinant(m1))
    print(determinant(m2))


if __name__ == "__main__":
    main()