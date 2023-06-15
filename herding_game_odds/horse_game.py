from permutations import Permutations, PermValue
import horse_displays

story1 = 'from %s, %s are going to play a game of horse. How many different shooting orders can we come up with?'
players = ['Leon', 'Jade', 'Sawyer', 'Mia', "Anya"]

def get_number_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except:
            print('Not a number. Please try again')

def check_guess(guess, answer):
    return 'You got it!!!' if guess == answer else f'Not this time, the answer was {answer}'

def play(groups):
    guess = get_number_input('Enter a number: ')
    result = check_guess(guess, len(groups.permutations))
    print(result)
    display(groups)


def setup(players, k):
    groups = Permutations(players, k)
    play(groups)

def display(groups):
    horse_displays.display_math(groups)
    
if __name__ == '__main__':
    playing = players[:4]
    print(story1 % (' and '.join(playing), 4))
    setup(playing, 4)
