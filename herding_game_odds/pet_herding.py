from players import Players2
import random
import strings as XSTR
import pet_herding_displays
from math_reprs import Prob, Odds
from combinations import Combinations
import numpy as np

CLOSE_ENOUGH = 0.12
BORDER = '='*120

def get_user_option(prompt):
    print(BORDER)
    choice = input(prompt).strip().lower()[0]     
    return choice == XSTR.AFFIRM[0] if choice in ['y', 'n'] else get_user_option(f'not an option\n{prompt}')

def get_number_input(prompt):
    while True:
        try:
            raw = input(prompt)
            return float(raw) if '.' in raw else tuple(int(val.strip()) for val in raw.split(XSTR.IN))
        except:
            print(XSTR.NUM_ERROR)

def get_random_selection(elements, num_elems):
    copy = elements[::1]
    random.shuffle(copy)  
    return copy[:num_elems], copy[num_elems:]

def get_subset_matches(sets, subset):
    return sets.elems_in_sets(subset)

def close_enough(val1, val2):
    return abs(val1 - val2) <= CLOSE_ENOUGH

def get_odds(subset, superset):
    return Odds(subset, superset)

def set_up_player_combos(targets, num_herded, queried_names, nonqueried_names):
    num_nonqueried = num_herded - len(queried_names)
    return Players2(targets, num_herded), Players2(nonqueried_names, num_nonqueried)

def get_random():
    num_targets = get_weighted_randint(1, len(XSTR.PETS))
    targets, __ = get_random_selection(XSTR.PETS, num_targets)
    num_chosen = get_weighted_randint(1, num_targets)
    queried_names, nonqueried_names = get_random_selection(targets, get_weighted_randint(1, num_chosen))
    return targets, num_chosen, queried_names, nonqueried_names

def get_weighted_randint(min, max):
    return int(min + np.random.normal(min+(max-min)/2,1))

def check_guess(guess, player_combos, queried_names):
    odds = Odds(queried_names, player_combos.sets)
    prob = Prob(odds.counts, odds.sizesample)
    if odds == guess or prob == guess:
        msg = XSTR.PERFECT
    else:
        guess_prob = guess if type(guess) == float else 0.0 if guess[0] == 0 else Prob(*guess) 
        msg = f'\n{XSTR.CONGRATS}' if close_enough(prob, guess_prob) else f'\n{XSTR.TOO_BAD}'
    queried_sets = player_combos.elems_in_sets(queried_names)
    return odds, prob, msg, queried_sets


def game(player_combos, nonqueried_player_combos, queried_names):
    pet_herding_displays.display_players(player_combos, queried_names)
    if player_combos.num_chosen - len(queried_names) > 0 and get_user_option('would you like a hint? '):
        pet_herding_displays.hint(player_combos, nonqueried_player_combos, queried_names)
    guess = get_number_input(f'\n{XSTR.PROMPT_ODDS}' % XSTR.AND.join(queried_names))
    results = check_guess(guess, player_combos, queried_names)
    pet_herding_displays.display_results(*results, player_combos, nonqueried_player_combos)

def start():
    targets, num_chosen, queried_names, nonqueried_names = get_random()
    player_combos, nonqueried_player_combos = set_up_player_combos(targets, num_chosen, queried_names, nonqueried_names)
    game(player_combos, nonqueried_player_combos, queried_names)
    start() if get_user_option(XSTR.CONTINUE) else None

if __name__ == '__main__':
    pet_herding_displays.startup()
    start()
    