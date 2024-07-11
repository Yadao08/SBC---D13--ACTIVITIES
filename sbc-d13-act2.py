# character tokenization

text = input("chars: ")
split_text = []
for char in text:
    split_text.append(char.upper())

print("Tokenized Characters: ")
print(split_text)