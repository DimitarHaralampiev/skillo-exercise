
def words_len(lst_words):
    return {word: len(word) for word in lst_words}


lst_elements = [x for x in input('Please enter word ').split() if x != 'Stop' and x.isalpha()]
print(words_len(lst_elements))