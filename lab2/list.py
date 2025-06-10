# 1. Create a list of 5 numbers. Output: 1. the sum of all the numbers, 2. maximum and minimum values
"""
elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = 0
for i in elements:
    sum += i
print(sum)
print(max(elements))
print(min(elements))
"""
# 2. A list of strings. Replace the second element with "updated" and display the final list.
"""
Cars = ['TOYOTA', 'PORSHE', 'BMV', 'JETOUR', 'LADA', 'KAMAZ']
Cars[1]= "Update" + "Update"
print(Cars)
"""
# 3. Create a list of 5 names. Print only those that start with the letter "A"
Names = ['Aaron', 'Uar', 'Ilyas', 'Mom', 'Father', 'Grandmother']
a_names = [name for name in Names if name.startswith('A')]
print(f"Names with start A: {a_names}")
