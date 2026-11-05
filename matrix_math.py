def add_matrices(A, B):
    if len(A) != len(B):
        return None
    if len(A[0]) != len(B[0]):
        return None

    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            value = A[i][j] + B[i][j]
            row.append(value)
        result.append(row)

    return result


def multiply_matrices(A, B):
    if len(A[0]) != len(B):
        return None

    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            total = 0
            for k in range(len(B)):
                total += A[i][k] * B[k][j]
            row.append(total)
        result.append(row)

    return result

