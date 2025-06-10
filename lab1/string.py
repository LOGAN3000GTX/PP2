number = 8
text = f"I have more datasets for learning, YOLO {number:.6f}"
print(text.replace('YOLO', 'CHAT GPT'))
print(text.split(","))
print()

txt = "someone said me: \"Can you hear music?\" from the film Oppenheimer"
txt1 = "someone said me: \n\"Can you hear music?\""
print(txt)
print(txt1)
correct_txt = txt.capitalize()
print(correct_txt)

txt2 = "Someone Said Me: \"Can You Hear Music?\" From The Film Oppenheimer"
correct_txt2 = txt2.casefold()
print(correct_txt2)

txt2 = "Someone Said Me: \"Can You Hear Music?\" From The Film Oppenheimer"
correct_txt2 = txt2.count('Someone')
print(correct_txt2)

