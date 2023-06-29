from permutations import Permutations, PermValue
import horse_displays

story1 = 'From %s, %s are going to play a game of horse. How many different shooting orders can we come up with?'
story2 = 'This time %s is going to play too.  How many different shooting orders can we come up with? \nHint: how many different spots can %s be added to the existing lineups?'
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
    playing = players[:3]
    print(story1 % (' and '.join(playing), 3))
    setup(playing, 3)
    print(story2 % (players[3], players[3]))
    setup(players[:4], 4)
