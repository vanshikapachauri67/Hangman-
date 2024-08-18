import random
HANGMAN = [
    '_________________',
    '|                |',
    '|                o',
    '|                |',
    '|             /  |  \\',
    '|                |',
    '|             /     \\',
]

WORDS =  [ 'CASA' , 'CARO' , 'MONO' , 'ESTERNOCLEIDOMASTOIDEO' , 'PYTHON' , 'DJANGO' , 'MILTON'
    , 'LENIS' , 'SWAPPS' , 'LOGIA' , 'UNITTESTING'
]
class hangman():
    def __init__(self,word_to_guess):
        self.failed_atempts = 0
        self.word_to_guess = word_to_guess
        self.game_progress = list('_' *  len(self.word_to_guess))
    def find_indexes(self , letter):
        return [ i for i , char in enumerate(self.word_to_guess)if letter == char]
    def is_invalid__letter(self, input_):
        return input_.isdigit() or (input_.isalpha() and len(input_) > 1)

    
    def print_game_status(self):
        print('\n')
        print('\n'.join(HANGMAN[:self.failed_atempts]))
        print('\n')
        print(''.join(self.game_progress))
    def update_progress(self, letter, indexes):
        for index in indexes:
           self.game_progress[index] = letter


    def get_user_input(self):
       while True:
         user_input = input('\nPlease type a letter: ')
         if not user_input.isalpha() or len(user_input) != 1:
            print('Invalid input. Please enter a single letter.')
         else:
            return user_input



    def play(self):
        while self.failed_atempts < len(HANGMAN):
            self.print_game_status()
            user_input = self.get_user_input()
            if self.is_invalid__letter(user_input):
                print(' ! The input is not a letter')
                continue
            if user_input in self.game_progress:
                print('You already have guessed that letter')
                continue
            if user_input in self.word_to_guess:
                indexes = self.find_indexes(user_input)
                self.update_progress(user_input,indexes)

            if '_' not in self.game_progress:
                print(' \n Yay! You Win! ')
                print(' The word is : {0}'.format(self.word_to_guess))
                quit()
            else:
                self.failed_atempts += 1
                print('\n  OMG! You lost!')

if __name__ == '__main__':
    word_to_guess = random.choice(WORDS)
    hangman = hangman(word_to_guess)
    hangman.play()

        
