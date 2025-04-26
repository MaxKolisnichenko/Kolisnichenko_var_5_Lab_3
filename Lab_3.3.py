#Лаб.3 Рівень 2. Варіант 5.

def matrix_multiply(A, B):
    n = len(A)
    result = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]
    
    return result

def get_matrix_input(n):
    matrix = []
    for i in range(n):
        while True:
            row = input(f"Рядок {i+1}: ").split()
            if len(row) != n:
                print(f"Помилка! Рядок повинен містити {n} елементів.")
                continue
            try:
                matrix.append([int(x) for x in row])
                break
            except ValueError:
                print("Помилка! Введіть тільки числа.")
    return matrix

while True:
    try:
        n = int(input("Введіть розмір матриці (n для матриці n x n): "))
        if n <= 0:
            print("Розмір матриці повинен бути додатним числом.")
            continue
        break
    except ValueError:
        print("Помилка! Введіть ціле число.")

print("Матриця A:")
A = get_matrix_input(n)

print("Матриця B:")
B = get_matrix_input(n)


C = matrix_multiply(A, B)

print("\nРезультат множення матриць A і B:")
for row in C:
    print(row)

