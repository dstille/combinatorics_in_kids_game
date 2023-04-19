import random

def assign_prizes():
    doors = [1, 2, 3]
    random.shuffle(doors)
    prize, *goats = doors
    return prize, goats

def get_contestant_guess():
    return random.randint(1, 3)

def choose_reveal_door(guess, goats):
    if guess in goats:
        goats.remove(guess)
    return random.choice(goats) 

def get_switch_door(guess, goat):
    doors = [1, 2, 3]
    doors.remove(guess)
    doors.remove(goat)
    return doors.pop() 

def get_winner(prize, guess, switch):
    return 'stay' if guess == prize else 'switch' if switch == prize else 'error'

def print_game(prize, guess, goat, switch, winner):
    print(f'Contestant guesses door {guess}, is shown a goat behind door {goat} and is offered to switch to door {switch}')
    print(f'Prize is behind door {prize}\n{winner} wins\n')

def game(): 
    prize, goats = assign_prizes() 
    guess = get_contestant_guess()
    goat = choose_reveal_door(guess, goats)
    switch = get_switch_door(guess, goat)
    winner = get_winner(prize, guess, switch)
    print_game(prize, guess, goat, switch, winner)
    return winner

def main():
    results = [game() for __ in range(100)]
    print('Staying wins %s times; switching wins %s times' %(results.count('stay'), results.count('switch')))       

if __name__ == '__main__':
    main()
    
