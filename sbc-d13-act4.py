#CUSTOM TOKENIZATION

text = "Hello!, Goodbye for Now!"
custom = []
current_word = ''

for char in text:
    if char.isalnum():
        current_word += char
    else:
        if current_word:
            custom.append(current_word)
            current_word = ''
        if char.strip():
            custom.append(char)

if current_word:
    custom.append(current_word)

print(custom)
