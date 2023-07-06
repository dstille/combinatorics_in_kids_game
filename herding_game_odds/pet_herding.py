from players import Players
import random
import strings as XSTR
import pet_herding_displays
from combinatorics import Prob, Odds, Combinatorics
from combinations import Combinations

CLOSE_ENOUGH = 0.12
BORDER = ''.join(['=' for __ in range(120)])

def get_user_option(prompt):
    print(BORDER)
    choice = input(prompt)      
    return choice.strip().lower()[0] == XSTR.AFFIRM[0]

def get_number_input(prompt):
    while True:
        try:
            raw = input(prompt)
            return float(raw) if '.' in raw else tuple(int(val.strip()) for val in raw.split(XSTR.IN))
        except:
            print(XSTR.NUM_ERROR)

def get_name_input(prompt, all_names):
    while True:
        names = input(prompt).split()
        if set(names).issubset(set(all_names)):
            return names
        print(XSTR.STR_ERROR)

def get_random_selection(players, num_players):
    copy_players = players[::1]
    random.shuffle(copy_players)  
    return copy_players[:num_players]

def get_subset_matches(sets, subset):
    return sets.elems_in_sets(subset)

def close_enough(val1, val2):
    return abs(val1 - val2) <= CLOSE_ENOUGH

def get_odds(subset, superset):
    return Odds(subset, superset)

def set_up_players(targets, num_herded, check_odds_names):
    return Players(targets, num_herded, check_odds_names), check_odds_names

def get_random():
    num_targets = random.randint(1, len(XSTR.PETS)-1)
    targets = get_random_selection(XSTR.PETS, num_targets)
    num_chosen = random.randint(1, num_targets)
    check_odds_names = get_random_selection(targets, random.randint(1, num_chosen))
    return targets, num_chosen, check_odds_names

def check_guess(guess, combos, queried):
    odds = Odds(queried, combos.sets)
    prob = Prob(odds.counts, odds.sizesample)
    if odds == guess or prob == guess:
        msg = XSTR.PERFECT
    else:
        guess_prob = guess if type(guess) == float else 0.0 if guess[0] == 0 else Prob(*guess) 
        msg = f'\n{XSTR.CONGRATS}' if close_enough(prob, guess_prob) else f'\n{XSTR.TOO_BAD}'
    queried_sets = combos.elems_in_sets(queried)
    return odds, prob, msg, combos, queried_sets
    
def get_sets(players):
    return Combinations(players.players, players.num_chosen)

def game(players, check_odds_names):
    pet_herding_displays.display_players(players, check_odds_names)
    combos = get_sets(players)
    guess = get_number_input(f'\n{XSTR.PROMPT_ODDS}' % XSTR.AND.join(check_odds_names))
    results = check_guess(guess, combos, check_odds_names)
    queried_sets = get_subset_matches(combos, players.queried_players)
    pet_herding_displays.display_results(*results, combos, players)

def start():
    players, check_odds_names  = set_up_players(*get_random())
    game(players, check_odds_names)
    start() if get_user_option(XSTR.CONTINUE) else None

if __name__ == '__main__':
    pet_herding_displays.startup()
    start()
    