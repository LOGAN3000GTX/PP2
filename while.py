# 1. Write a program that outputs all even numbers from 2 to 20.
"""
i = 0
while i < 20:
    i += 2
    print(i)
"""
# 2. Write a program that counts the sum of all the numbers from 1 to 50 that are divisible by 3.
"""
total = 0
for i in range(1, 51):
    if i % 3 == 0:
        total += i
print("Сумма чисел от 1 до 50, делящихся на 3:", total)

"""
# 3. Ask the user for the password until they enter admin123.
"""
attempts = 0
while attempts < 3:
    password = input("Введите пароль: ")
    if password == "admin123":
        print("Доступ разрешён. Добро пожаловать!")
        break
    else:
        print("Неверный пароль.")
        attempts += 1
if attempts == 3:
    print("Превышено количество попыток. Доступ запрещён.")
"""
