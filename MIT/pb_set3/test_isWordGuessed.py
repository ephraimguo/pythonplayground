def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for l in secretWord:
        if l not in lettersGuessed:
            return False
    return True



word = 'durian'
letter = ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u']
print(isWordGuessed(word, letter))



# def test_try():
#     for l in letter:
#         if l not in word:
#             print('inner loop')
#             return False
#     return True
#
# test_try()