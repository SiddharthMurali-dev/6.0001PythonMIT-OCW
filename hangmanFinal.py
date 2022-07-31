# Problem Set 2, hangman.py
# Name: Siddharth Murali
# Collaborators: None
# Time spent: 

# Hangman Game
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string 
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for char in secret_word :
        # print(char)
        if char not in letters_guessed :
            return False
             # if a character in the secret word isnt in the letters guessed, the function returns false
             # meaning that the all the letters havent been guessed so the secret word is NOT guessed
    return True # function returns true after checking each character in secret word

##Test for is_word_guessed --
# secret_word = 'apple'
# letters_guessed = ['e', 'p', 'a', 'l']
# print(is_word_guessed(secret_word,letters_guessed))




def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guessed_word = ('_ ') * len(secret_word)
    # recreates the secret word but with blanks. The space is to differentiate between adjacent underscores
    for i in range(0, len(secret_word)) :
        #searches the entire length of the secret_word
        if secret_word[i] in letters_guessed :
            guessed_word = guessed_word[0 : 2*i] + secret_word[i] + guessed_word[2*i + 1 : len(guessed_word)]
            # The above line inserts matching letters into the blanked guessed_word. The 2*i accounts for
            # the space in '_ '
    return guessed_word #returns the final blanked word including the correctly guessed letters e.g (a p p _ e)

##Test for get_guessed_word
# secret_word = 'apple'
# letters_guessed = ['t', 'p', 'h' ]
# print(get_guessed_word(secret_word,letters_guessed))


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    import string
    string_available_letters = string.ascii_lowercase
    n = 0
    for i in range(0,len(string.ascii_lowercase)) :
        ''' The str string_availble_letters gets modified when a new letter is matched with the list of guessed_letters.
        Here, string.ascii_lowercase is constant and consists of all lowercase letters. A variable n is initialised at 0.'''
        if string.ascii_lowercase[i] in letters_guessed :
            string_available_letters = string_available_letters[0:i - n] + string_available_letters[i - n + 1: len(string.ascii_lowercase)]
            n += 1
            ''' everytime the program enters this loop, n gets incremented by 1. This is two map the i'th character in strings.ascii_lowercase
             to the (i - n)'th character in the modified str string_available_letters
              i.e the ith character in the former is the (i-n)th character in the latter '''
    return string_available_letters
    
# print(get_available_letters(['a', 'c']) )

def hangman(secret_word):
    No_guesses = 6
    No_warnings = 3
    letters_guessed = [] #initialises a list with 0 characters.
    print('Lets play Hangman!')
    print('I am thinking of a word that is', len(secret_word), 'letters long.')
    # print('You have', No_warnings,'warnings left')
    while No_guesses > 0  :
        i = 0
        for char in secret_word :
        # this 'for' loop keeps track of the number of letters guessed in the secret_word. It is later used to check if the secret_word has been found.
            if char in letters_guessed :
                i += 1
        if i < len(secret_word) : #checks if the number of letters guessed(i) is less than the number of letters in secret_word.
            print(get_guessed_word(secret_word,letters_guessed)) #calls the get_guessed_word function.
            print('You have', No_guesses ,'guesses left')
            print('You have', No_warnings,'warnings left')
            print('Available letters =',get_available_letters(letters_guessed)) #calls the get_available_letters function with the letters_guessed parameter
            guessed_letter = input('Please guess a letter: ') # takes input from user, asks for a letter.
            guessed_letter = guessed_letter.lower() # makes the input recieved lowercase. Does nothing if input is not a letter.

            if guessed_letter not in string.ascii_lowercase : # if input is not a letter, goes into this loop
                No_warnings -= 1
                print('Oops! That is not a valid letter.')
                if No_warnings == -1 : #checks if no_warnings has gone below 0. If true, goes inside and decrements No_guesses by 1.
                    No_guesses -= 1
                    No_warnings = 3
                    print("You have no warnings left. You lose one guess")
            elif guessed_letter in letters_guessed : # Checks if input(guessed_letter) has previously been input by checking inside 
                No_warnings -= 1 
                print('You have already guessed this letter.')
                if No_warnings == -1 :
                    No_guesses -= 1
                    No_warnings = 3
                    print("You have no warnings left. You lose one guess")
            else : 
                letters_guessed.append(guessed_letter) #concatenates the new input(guessed_letter) to the list lettters_guessed
                if guessed_letter in ['a','e','i','o','u'] and guessed_letter not in secret_word :
                    No_guesses -= 2
                    print('Oops! That vowel is not in my word')
                elif guessed_letter not in secret_word :
                    No_guesses -= 1
                    print('Oops! That consonant is not in my word')
                else :
                    print('Good guess')

        else : # goes into this statement, if number of letters guessed(i) is greater than or equal to length of secret_word. Basically word is guessed.
            print('Congrats! You found the word :', get_guessed_word(secret_word,letters_guessed))
            unique = []
            for letter in secret_word : # for loop calculates number of unique letters in secret_word
                if letter not in unique :
                    unique.append(letter)
            No_of_unique_letters = len(unique)
            print('You\'re total score is', No_guesses * No_of_unique_letters) 
            break
            
    if No_guesses <= 0 and i < len(secret_word) : # ie. if all the guesses are used up, game ends. 
        print('You are out of guesses. The word was', '"',secret_word,'"') 


# hangman(choose_word(wordlist))
# hangman('orange')

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word = my_word.replace(' ','')
    n = 0
    if len(my_word) == len(other_word) :
        for i in range(0,len(my_word)) :
            if my_word[i] == other_word[i] or my_word[i] == '_' :
                n += 1
            if my_word[i] == '_' :
                for char in my_word :
                    if char == other_word[i] :
                        return False
    if n == len(my_word) :
        return True
    else :
        return False

# my_word = get_guessed_word(secret_word,letters_guessed)
# print(my_word)
# print(match_with_gaps(my_word,'apple'))

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    i = 0
    matched_words = ''
    for other_word in wordlist :
        if match_with_gaps(my_word,other_word) == True :
            matched_words = other_word + ' ' + matched_words[:]
            i += 1
    if i == 0 :
        print('No matches found')
    else :
        return matched_words

# show_possible_matches('a _ _ _ e')

def hangman_with_hints(secret_word):
    No_guesses = 6
    No_warnings = 3
    letters_guessed = [] #initialises a list with 0 characters.
    print('Lets play Hangman!')
    print('I am thinking of a word that is', len(secret_word), 'letters long.')
    # print('You have', No_warnings,'warnings left')
    while No_guesses > 0  :
        i = 0
        for char in secret_word :
        # this 'for' loop keeps track of the number of letters guessed in the secret_word. It is later used to check if the secret_word has been found.
            if char in letters_guessed :
                i += 1
        if i < len(secret_word) : #checks if the number of letters guessed(i) is less than the number of letters in secret_word.
            print(get_guessed_word(secret_word,letters_guessed)) #calls the get_guessed_word function.
            print('You have', No_guesses ,'guesses left')
            print('You have', No_warnings,'warnings left')
            print('Available letters =',get_available_letters(letters_guessed)) #calls the get_available_letters function with the letters_guessed parameter
            guessed_letter = input('Please guess a letter: ') # takes input from user, asks for a letter.
            guessed_letter = guessed_letter.lower() # makes the input recieved lowercase. Does nothing if input is not a letter.

            if guessed_letter not in string.ascii_lowercase and guessed_letter != '*' : # if input is not a letter, goes into this loop
                No_warnings -= 1
                print('Oops! That is not a valid letter.')
                if No_warnings == -1 : #checks if no_warnings has gone below 0. If true, goes inside and decrements No_guesses by 1.
                    No_guesses -= 1
                    No_warnings = 3
                    print("You have no warnings left. You lose one guess")
            elif guessed_letter == '*' :
                matched_words = show_possible_matches(get_guessed_word(secret_word,letters_guessed))
                print('The possible matches are: ')
                print(matched_words.upper())
            elif guessed_letter in letters_guessed : # Checks if input(guessed_letter) has previously been input by checking inside 
                No_warnings -= 1 
                print('You have already guessed this letter.')
                if No_warnings == -1 :
                    No_guesses -= 1
                    No_warnings = 3
                    print("You have no warnings left. You lose one guess")
            else : 
                letters_guessed.append(guessed_letter) #concatenates the new input(guessed_letter) to the list lettters_guessed
                if guessed_letter in ['a','e','i','o','u'] and guessed_letter not in secret_word :
                    No_guesses -= 2
                    print('Oops! That vowel is not in my word')
                elif guessed_letter not in secret_word :
                    No_guesses -= 1
                    print('Oops! That consonant is not in my word')
                else :
                    print('Good guess')

        else : # goes into this statement, if number of letters guessed(i) is greater than or equal to length of secret_word. Basically word is guessed.
            print('Congrats! You found the word :', get_guessed_word(secret_word,letters_guessed))
            unique = []
            for letter in secret_word : # for loop calculates number of unique letters in secret_word
                if letter not in unique :
                    unique.append(letter)
            No_of_unique_letters = len(unique)
            print('You\'re total score is', No_guesses * No_of_unique_letters) 
            break
            
    if No_guesses <= 0 and i < len(secret_word) : # ie. if all the guesses are used up, game ends. 
        print('You are out of guesses. The word was', '"',secret_word,'"') 



secret_word = choose_word(wordlist)
hangman_with_hints(secret_word)