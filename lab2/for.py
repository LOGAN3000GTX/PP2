# 1. Write a for loop that prints squares of numbers from 1 to 10.
for i in range(1, 10):
    print(f"{i}^2 = {i ** 2}")
# 2. Create a list of 5 words and output the length of each word.
words = ['Easy', 'Medium', 'Hard', 'Hardcor']
for word in words:
    print(f"Length of word: {word}: {len(word)}")
# 3. Use nested loops to output the multiplication table from 1 to 5.
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} * {j} = {i * j}")