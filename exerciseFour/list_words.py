
def len_words(list_words):
    new_list = []

    for word in list_words:
        new_list.append(len(word))

    return new_list


lst_words = []

name = input('Please enter name ')

while name != 'Stop':

    lst_words.append(name)

    name = input('Please enter name ')

print(len_words(lst_words))

