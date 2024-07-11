# Sentence tokenization

text = "Live your life to the fullest. coz theres no rewind! laag samtang dili pa efficacent ang perfume!"

sentence_delimiters = '.!?'
sentences = []
current_sentence = []

for char in text:
    current_sentence.append(char)
    if char in sentence_delimiters:
        sentences.append(''.join(current_sentence).strip())
        current_sentence = []

# Append the last sentence if there's any remaining
if current_sentence:
    sentences.append(''.join(current_sentence).strip())

print("Tokenized Sentences:")
print(sentences)
