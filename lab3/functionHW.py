#В рецепте, 
# который вы читаете, указано, сколько граммов 
# вам нужно для ингредиента. К сожалению, ваш магазин продает 
# товары только в унциях. Создайте функцию для преобразования 
# граммов в унции. ounces = 28.3495231 * grams
"""
grams = float(input())
def Convert():
    ounces = 28.3495231 * grams
    print(ounces)
Convert()
"""
#Чтение при температуре Фаренгейта. 
# Рассчитайте и отобразите эквивалентную температуру по Цельсию.
#  Для преобразования используется следующая формула: C = (5 / 9) * (F – 32)
"""
F = float(input("Farenheit: "))
def ConvertT():
    C = (5 / 9) * (F - 32)
    print(C)
ConvertT()
"""
#Напишите программу для решения классической головоломки: 
# Мы насчитали 35 голов и 94 ноги среди кур и кроликов на ферме. 
# Сколько у нас кроликов и сколько кур? create function: solve(numheads, numlegs):
"""
def solve(numheads, numlegs):
    rabits = numlegs - 2* numheads
    chikens = numheads - rabits
    if chikens > 0 and rabits > 0:
"""

#Вам будет предоставлен список чисел через пробелы. 
# Напишите функцию, которая будет принимать список чисел в 
# качестве агрумента и возвращать только простые числа из списка.
# filter_prime
"""
def is_prime(n):
    # 1, 3, 5
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % 2 == 0:
            return False
    return True
def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]

input = input()
num_list = list(map(int, input.split()))
prime_numbers = filter_prime(num_list)
print(prime_numbers)
"""   
"""
from itertools import permutations
def print_permutations(s):
    perm_set = set(permutations(s))  # множество, чтобы убрать дубликаты
    for p in perm_set:
        print(''.join(p))
user_input = input("Введите строку: ")
print_permutations(user_input)
"""

#Напишите функцию, которая принимает строку от пользователя, 
# взвращает предложение с обратными словами. We are ready -> ready are We
"""
def reverse_words(s):
    words = s.split()
    reverse_words = words[::-1]
    return ' '.join(reverse_words)
input = input()
result = reverse_words(input)
print(result)
"""

"""
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False
input = input()
numbers = list(map(int, input.split()))
result = has_33(numbers)
print(result)
"""

"""
def contains_007(nums):
    code = [0, 0, 7]
    code_index = 0
    for num in nums:
        if num == code[code_index]:
            code_index += 1
        if code_index == len(code):
            return True
    return False

input = input()
numbers = list(map(int, input.split()))
result = contains_007(numbers)
print(result)
"""

"""
r = int(input())
def volumeSphere():
    sphere = 4 * 3.14 * (r ** 3)
    print(sphere)
volumeSphere()
"""

"""
def get_unique_elements(lst):
    unique = []
    for items in lst:
        if items not in unique:
            unique.append(items)
    return unique
input = [9, 3, 3, 5, 6, 2, 9, 7]
print(get_unique_elements(input))
"""
"""

"""
def histogram(items):
    for i in items:
        print('$' * i) # умножаем количество элементов которые мы задаем его кол-во
input = input()
numbers = list(map(int, input.split()))
result = histogram(numbers)
print(result)

