numbers = [11, 22, 33, None, 55, 66, 77]
numbers[3] = (sum(numbers[:3]) + sum(numbers[4:])) / len(numbers)
print('Исправленный список:', numbers)
