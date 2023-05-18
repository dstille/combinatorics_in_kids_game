from players import Players, COUSINS, ADULTS, KIDS
import math_representations
import random
import strings as XSTR
import displays
from combinatorics import Combinations, Odds, Prob, Combinatorics

BORDER = ''.join(['=' for __ in range(120)])

def check_guess(guess, csets, queried):
    odds = Odds(queried, csets.sets)
    prob = Prob(odds.counts, odds.sizesample)
    if odds == guess or prob == guess:
        msg = XSTR.PERFECT
    else:
        guess_prob = guess if type(guess) == float else 0.0 if guess[0] == 0 else Prob(*guess) 
        msg = f'\n{XSTR.CONGRATS}' if close_enough(prob, guess_prob) else f'\n{XSTR.TOO_BAD}'
    queried_sets = csets.elems_in_sets(queried)
    return odds, prob, msg, csets, queried_sets

def close_enough(val1, val2):
    return abs(val1 - val2) <= 0.12

def get_odds(subset, superset):
    return Odds(subset, superset)

def get_number_input(prompt):
    while True:
        try:
            raw = input(prompt)
            return float(raw) if '.' in raw else tuple(int(val.strip()) for val in raw.split(XSTR.IN))
        except:
            print(XSTR.NUM_ERROR)

def get_name_input(prompt, cousins):
    while True:
        names = input(prompt).split()
        if set(names).issubset(set(cousins)):
            return names
        print(XSTR.STR_ERROR)

def get_random_selection(cousins, num_cousins):
    copy_cousins = cousins[::1]
    random.shuffle(copy_cousins)  
    return copy_cousins[:num_cousins]

def get_user_option(prompt):
    print(BORDER)
    choice = input(prompt)      
    return choice.strip().lower()[0] == XSTR.AFFIRM[0]

def game():
    ask_user = False #get_user_option(XSTR.PUSER_OPTIONS)
    aplayers, kplayers, who_to_check_odds_for  = set_up_players(*get_selections_from_user() if ask_user else get_random())
    asets, ksets = play(aplayers, kplayers, who_to_check_odds_for)
    displays.display_math(asets, ksets, aplayers, kplayers)
    game() if get_user_option(XSTR.CONTINUE) else None

def play(aplayers, kplayers, who_to_check_odds_for):
    displays.display_players(aplayers, kplayers, who_to_check_odds_for)
    csets, asets, ksets = herd(aplayers, kplayers)
    guess = get_number_input(f'\n{XSTR.PODDS1} {XSTR.AND.join(who_to_check_odds_for)} {XSTR.PODDS2}')
    results = check_guess(guess, csets, who_to_check_odds_for)
    aqueried_sets = get_subset_matches(asets, aplayers.queried_players)
    kqueried_sets = get_subset_matches(ksets, kplayers.queried_players)
    displays.display_results(*results, asets, ksets, aqueried_sets, kqueried_sets, aplayers, kplayers)
    return asets, ksets

def get_subset_matches(sets, subset):
    return sets.elems_in_sets(subset)

def set_up_players(atargets, num_herded_adults, ktargets, num_herded_kids, who_to_check_odds_for):
    aplayers = Players(atargets, num_herded_adults, who_to_check_odds_for)
    kplayers = Players(ktargets, num_herded_kids, who_to_check_odds_for)
    return aplayers, kplayers, who_to_check_odds_for

def get_selections_from_user():
    atargets = get_name_input(BORDER + '\n' + XSTR.PADULTS_TO_PLAY, ADULTS)
    num_herd_adults = get_number_input(XSTR.PADULTS_CAN_HERD)[0][0]
    ktargets = get_name_input(XSTR.DKIDS_TO_PLAY, KIDS)
    num_herd_kids =  get_number_input(XSTR.PKIDS_CAN_HERD)[0][0]
    who_to_check_the_odds_for = get_name_input(XSTR.PCOUSINS, atargets + ktargets)
    return atargets, num_herd_adults, ktargets, num_herd_kids, who_to_check_the_odds_for

def get_random():
    num_atargets = random.randint(1, len(ADULTS)-1)
    atargets = get_random_selection(ADULTS, num_atargets)
    num_herd_adults = random.randint(1, num_atargets)
    num_ktargets = random.randint(1, len(KIDS)-1)
    ktargets = get_random_selection(KIDS, num_ktargets)
    num_herd_kids = random.randint(1, num_ktargets)
    who_to_check_the_odds_for = get_random_selection(atargets + ktargets, random.randint(1, num_herd_adults+num_herd_kids-1))
    return atargets, num_herd_adults, ktargets, num_herd_kids, who_to_check_the_odds_for

def herd(aplayers, kplayers):
    acombos = Combinations(aplayers.players, aplayers.num_herded)
    kcombos = Combinations(kplayers.players, kplayers.num_herded)
    csets = Combinations.add_sets(acombos.sets, kcombos.sets)
    ccombos = Combinatorics(csets, aplayers.players+kplayers.players)
    return ccombos, acombos, kcombos

if __name__ == '__main__':
    displays.startup()
    game()
    