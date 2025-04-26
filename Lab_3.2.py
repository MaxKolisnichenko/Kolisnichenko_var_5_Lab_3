#Лаб.3 Рівень 2. Варіант 5.

def count_char_frequency(input_str):

    if len(input_str) == 0:
        print("Помилка! Введений рядок порожній.")
        return {}


    frequency = {}


    for i in range(len(input_str)):
        char = input_str[i] 
        if char in frequency:
            frequency[char] += 1 
            frequency[char] = 1  

    return frequency


input_str = input("Введіть рядок: ")


if not isinstance(input_str, str):
    print("Помилка! Введіть правильний рядок.")
else:
   
    result = count_char_frequency(input_str)


    if result: 
        print("Частота кожного символу в рядку:")
        for char, count in result.items():
            print(f"'{char}': {count}")
