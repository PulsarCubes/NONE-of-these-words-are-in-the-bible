with open("everywordinthebible.txt","r", encoding="utf-8") as f:
    data = f.read()
word = ''
wordlist = []
for i,char in enumerate(data):
    try:

        if data[i+1] == " " or data[i+1] == "\n":
            word += char
            if word not in wordlist:
                wordlist.append(word)
            word = ''
        elif char != " " and word != ')' and word != ')':
            if char.isalpha():
                char = char.lower()
            word += char
    except IndexError:
        word += char
        if word not in wordlist:
            wordlist.append(word)

with open("everywordinthebible.txt","w", encoding="utf-8") as f:
    for word in wordlist:
        f.write(word)
