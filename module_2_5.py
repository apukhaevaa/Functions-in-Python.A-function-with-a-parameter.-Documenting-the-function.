# Пухаева Алина Александровна
# Functions in Python.A function with a parameter. Documenting the function.
# 12.09.2024
# Notes: ctrl+alt+L
def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(value)
        matrix.append(row)
    return matrix
result1 = get_matrix(3, 4, 77)
result2 = get_matrix(2, 5, 3)
result3 = get_matrix(4, 2, 5)
print(result1)
print(result2)
print(result3)