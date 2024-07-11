# Sub Word tokenization

texts = ["unhappy","unaware", "unwanted","unable","beautiful"]
sub_words = []

for char in texts:
    for word in char.split():
        if word == " ":
            sub_words.append( word[:6] + '#' * 3)  # prefix ni
            sub_words.append(word[-3:]) # suffix ni
        elif len(word) > 3:
            sub_words.append(word[:2])
            sub_words.append('##' + word[2:])
        elif len(word) > 2:
            sub_words.append(word[:1])
            sub_words.append('##' + word[1:])
        else:
            sub_words.append(word)

print("Sub words:", sub_words)