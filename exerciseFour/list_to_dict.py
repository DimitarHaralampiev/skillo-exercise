def create_dict(list_words):
    return {word: len(word) for word in list_words}


word = input('Please enter word ')
lst_words = []

while word != 'Stop':
    lst_words.append(word)
    word = input('Please enter word ')

print(create_dict(lst_words))