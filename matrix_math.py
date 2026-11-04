def add_matrices(matrix_a, matrix_b):
    """Return the sum of two matrices, or None if their sizes differ."""
    if not matrix_a or not matrix_b:
        return None

    if len(matrix_a) != len(matrix_b):
        return None

    if any(len(row_a) != len(row_b) for row_a, row_b in zip(matrix_a, matrix_b)):
        return None

    return [
        [value_a + value_b for value_a, value_b in zip(row_a, row_b)]
        for row_a, row_b in zip(matrix_a, matrix_b)
    ]


def multiply_matrices(matrix_a, matrix_b):
    """Return the product of two matrices, or None if multiplication is impossible."""
    if not matrix_a or not matrix_b:
        return None

    if not matrix_a[0] or not matrix_b[0]:
        return None

    columns_a = len(matrix_a[0])
    rows_b = len(matrix_b)

    if any(len(row) != columns_a for row in matrix_a):
        return None

    if any(len(row) != len(matrix_b[0]) for row in matrix_b):
        return None

    if columns_a != rows_b:
        return None

    result = []
    for row_a in matrix_a:
        result_row = []
        for column_index in range(len(matrix_b[0])):
            value = 0
            for index in range(columns_a):
                value += row_a[index] * matrix_b[index][column_index]
            result_row.append(value)
        result.append(result_row)

    return result
