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
print("РЎСѓРјРјР° С‡РёСЃРµР» РѕС‚ 1 РґРѕ 50, РґРµР»СЏС‰РёС…СЃСЏ РЅР° 3:", total)

"""
# 3. Ask the user for the password until they enter admin123.
"""
attempts = 0
while attempts < 3:
    password = input("Р’РІРµРґРёС‚Рµ РїР°СЂРѕР»СЊ: ")
    if password == "admin123":
        print("Р”РѕСЃС‚СѓРї СЂР°Р·СЂРµС€С‘РЅ. Р”РѕР±СЂРѕ РїРѕР¶Р°Р»РѕРІР°С‚СЊ!")
        break
    else:
        print("РќРµРІРµСЂРЅС‹Р№ РїР°СЂРѕР»СЊ.")
        attempts += 1
if attempts == 3:
    print("РџСЂРµРІС‹С€РµРЅРѕ РєРѕР»РёС‡РµСЃС‚РІРѕ РїРѕРїС‹С‚РѕРє. Р”РѕСЃС‚СѓРї Р·Р°РїСЂРµС‰С‘РЅ.")
"""
