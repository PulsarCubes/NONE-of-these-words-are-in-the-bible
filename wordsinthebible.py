
def words_in_bible(teststring):
    import string
    translator = str.maketrans('', '', string.punctuation)
    with open("everywordinthebible.txt","r", encoding="utf-8") as f:
        data = f.read()
    teststring = teststring.translate(translator)
    words = teststring.lower().split(" ")
    notinbible = []
    inbible = []
    for word in words:
        if word in data:
            inbible.append(word)
        else:
            notinbible.append(word)
    print(f'the words {inbible} are in the bible')
    print(f'the words {notinbible} are not in the bible')

if __name__ == '__main__':
    words_in_bible("this. is, a! test? string")