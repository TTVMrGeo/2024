flashcards = []
while True:
    class flashcard():
        def __init__(self, word, definition):
            self.word = word
            self.definition = definition
        def __str__(self):
            return f"{self.word}"
        
    cword = input('Word: ')
    cdef = input('Definition: ')
    flashcardr = flashcard(cword, cdef)
    user_try = input(f'What is the definition of {flashcardr}?: ')
    if user_try == flashcard.definition:
        print('Correct!')
    else:
        print('Incorrect!')