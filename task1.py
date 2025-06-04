# 1. Write a program that outputs all even numbers from 2 to 20.
"""
i = 2
while i < 20:
    i += 2
    print(i)
"""

#Write a program that counts the sum of all the numbers from 1 to 50 that are divisible by 3.
"""
sum = 0
i = 1
for i in range(51):
    if i % 3 == 0:
        sum += i
print(sum)
"""

#Ask the user for the password until they enter admin123.
"""
attemps = 0 
while attemps <= 3:
    password = input("Password: ")
    if password == 'admin123':
        print("Ваш доступ разрешен.")
        break
    else:
        print("Неверный пароль.")
        attemps += 1
        
if(attemps == 3):
    print("Превышенно кол-во попыток.")
"""

