#Лаб.3 Рівень 1. Варіант 5.

def power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent > 0:
        return base * power(base, exponent - 1)
    else:
        return 1 / power(base, -exponent)


base_input = input("Введіть число (основу): ")
try:
    base = float(base_input)
except ValueError:
    print("Помилка! Введіть правильне число для основи.")
    exit()

exponent_input = input("Введіть цілий степінь: ")
try:
    exponent = int(exponent_input)  
except ValueError:
    print("Помилка! Введіть правильне ціле число для степеня.")
    exit()


result = power(base, exponent)
print(f"{base} ^ {exponent} = {result}")
