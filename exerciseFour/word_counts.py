# Initialize a dictionary to store word counts
dict_word_counts = {}


# Function to update word counts in the dictionary
def update_word_counts(word):
    if word in dict_word_counts:
        dict_word_counts[word] += 1
    else:
        dict_word_counts[word] = 1


word = input('Please enter word ')

while word != 'Stop':
    update_word_counts(word)
    word = input('Please enter word ')

print(dict_word_counts)