def personal_sum(numbers):
    result = 0
    incorrect_data = 0

    for num in numbers:
        try:
            result += num
        except TypeError:
            incorrect_data += 1

    return result, incorrect_data


def calculate_average(numbers):
    try:
        if not isinstance(numbers, (list, tuple, set)):
            raise TypeError

        result, incorrect_data = personal_sum(numbers)

        average = result / (len(numbers) - incorrect_data)
        return average
    except ZeroDivisionError:
        return 0
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None

print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Некорректный тип данных (строка)
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только числа
print(f'Результат 3: {calculate_average(567)}')  # Некорректный тип данных (число вместо коллекции)
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Все элементы корректные, среднее арифметическое
