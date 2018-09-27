#detect englissh module for using this import this code e.g import detectEnglsih
#detecting.isEnglish(someString) # return True or False
#there must be the dictionary.txt file exists

upperletters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letters_And_space = upperletters + upperletters.lower() + ' \t\n'

def laod_dictionary():
    dict_file = open('dictionary.txt')
    eng_word = {}
    for word in dict_file.read().split('\n'):
        eng_word[word] = None#this will take word as key and None stored for that key
    dict_file.close()
    return eng_word

english_word = laod_dictionary()#store the dictionary value in the variabel called dictionary word

def get_eng_count(mesage):
    mesage = message.upper()
    message = remove_non_letters(mesage)
    possible_words = message.split()
    if possible_words == []:#means the lsit is empty after passing to the function remove_non_letters
        return 0.0 # take one argument and returning the cloat value ,this indicate that none of word in message are english word
    
    matches = 0
    for word in possible_words:
        if word in english_word:
            match += 1
    return float(matches) / len(possible_words)

def removal_non_letters(message):
    lettersonly = []
    for symbol in message:
        if symbol in letters_And_space:
            lettersonly.append(symbol)
    return ''.join(lettersonly)

def isEnglish(message, wordPercentage =20, letterPercentage=85):

    wordsMatch = getEnglishCount(message) * 100 >= wordPercentage
    numLetters = len(removeNonLetters(message))
    messageLettersPercentage = float(numLetters) / len(message) * 100
    lettersMatch = messageLettersPercentage >= letterPercentage
    return wordsMatch and lettersMatch