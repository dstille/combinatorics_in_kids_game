from permutations import Permutations, PermValue
from sequence import Sequences
import horse_displays

allplayers = ['Leon', 'Jade', 'Sawyer', 'Mia', "Anya"]
shots = ['hook',  'half court shot', 'layup']

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
    result = check_guess(guess, groups.size)
    print(result)
    display(groups)


def setup(players, k):
    groups = Permutations(players, k)
    play(groups)

def display(groups):
    horse_displays.display_math(groups)

def game1():
    groups = Sequences(shots, 2)
    horse_displays.scenario1(shots)
    play(groups)

def game2():
    groups = Sequences(shots, 3)
    horse_displays.scenario2(shots)
    play(groups)

def game3():
    players = allplayers[:3]
    horse_displays.scenario3(players)
    setup(players, 3)
       
def game4():
    players = allplayers[:4]
    horse_displays.scenario4(players)
    setup(players, 4)

def game5():
    players = allplayers[:4]
    horse_displays.scenario5(players)
    setup(players, 2)

if __name__ == '__main__':
    #game1()
    #game2()
    game3()
    game4()
    game5()
