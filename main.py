import random

from matrix_utils import create_matrix, print_matrix
from matrix_math import add_matrices, multiply_matrices


while True:
    print("\nДоступные операции: '+', '*'")
    print("Для выхода введите 'exit'")

    op = input("Введите операцию: ").strip()

    if op.lower() == 'exit':
        print("Программа завершена.")
        break

    try:
        if op == "+":
            print("\nСоздание первой матрицы:")
            A = create_matrix()
            print("\nСоздание второй матрицы:")
            B = create_matrix()

            print_matrix(A, "Матрица A")
            print_matrix(B, "Матрица B")

            result = add_matrices(A, B)
            if result is None:
                print("Ошибка: размеры матриц не совпадают для сложения")
                print("Сложение невозможно. Попробуйте снова.")
            else:
                print_matrix(result, "Результат сложения")
                print("\nОперация выполнена успешно!")

        elif op == "*":
            print("\nСоздание первой матрицы:")
            A = create_matrix()
            print("\nСоздание второй матрицы:")
            B = create_matrix()

            print_matrix(A, "Матрица A")
            print_matrix(B, "Матрица B")

            result = multiply_matrices(A, B)
            if result is None:
                print("Ошибка: число столбцов A не равно числу строк B")
                print("Умножение невозможно. Попробуйте снова.")
            else:
                print_matrix(result, "Результат умножения")
                print("\nОперация выполнена успешно!")
        else:
            print("Ошибка: неверная операция")
            print("Используйте: + или *")

    except ValueError:
        print("Ошибка: введите корректные числа (целые положительные значения)")
    except Exception as e:
        print(f"Непредвиденная ошибка: {e}")
