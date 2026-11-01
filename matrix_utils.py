import random

def create_matrix():
    rows = int(input("Введите количество строк: "))
    cols = int(input("Введите количество столбцов: "))

    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            value = random.randint(1, 10)
            row.append(value)
        matrix.append(row)

    return matrix

def print_matrix(matrix, name="Матрица"):
    print(f"{name}:")
    for row in matrix:
        line = []
        for value in row:
            line.append(str(value))
        print(" ".join(line))
