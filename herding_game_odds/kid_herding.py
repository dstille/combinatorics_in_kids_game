from players import Players
import random
import strings as XSTR
import displays
from combinatorics import Combinations, Odds, Prob, Combinatorics

CLOSE_ENOUGH = 0.12
BORDER = ''.join(['=' for __ in range(120)])

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

def get_random_selection(cousins, num_cousins):
    copy_cousins = cousins[::1]
    random.shuffle(copy_cousins)  
    return copy_cousins[:num_cousins]

def get_user_option(prompt):
    print(BORDER)
    choice = input(prompt)      
    return choice.strip().lower()[0] == XSTR.AFFIRM[0]

def get_subset_matches(sets, subset):
    return sets.elems_in_sets(subset)

def close_enough(val1, val2):
    return abs(val1 - val2) <= CLOSE_ENOUGH

def get_odds(subset, superset):
    return Odds(subset, superset)

def set_up_players(atargets, anum_herded, btargets, bnum_herded, check_odds_names):
    aplayers = Players(atargets, anum_herded, check_odds_names)
    bplayers = Players(btargets, bnum_herded, check_odds_names)
    return aplayers, bplayers, check_odds_names

def get_selections_from_user():
    atargets = get_name_input(BORDER + '\n' + XSTR.PADULTS_TO_PLAY, XSTR.ADULTS)
    anum_herded = get_number_input(XSTR.PADULTS_CAN_HERD)[0][0]
    btargets = get_name_input(XSTR.DKIDS_TO_PLAY, XSTR.KIDS)
    bnum_herded =  get_number_input(XSTR.PKIDS_CAN_HERD)[0][0]
    check_odds_names = get_name_input(XSTR.PCOUSINS, atargets + btargets)
    return atargets, anum_herded, btargets, bnum_herded, check_odds_names

def get_random():
    num_atargets = random.randint(1, len(XSTR.ADULTS)-1)
    atargets = get_random_selection(XSTR.ADULTS, num_atargets)
    anum_herded = random.randint(1, num_atargets)
    num_btargets = random.randint(1, len(XSTR.KIDS)-1)
    btargets = get_random_selection(XSTR.KIDS, num_btargets)
    bnum_herded = random.randint(1, num_btargets)
    check_odds_names = get_random_selection(atargets + btargets, random.randint(1, anum_herded+bnum_herded-1))
    return atargets, anum_herded, btargets, bnum_herded, check_odds_names

def check_guess(guess, allcombos, queried):
    odds = Odds(queried, allcombos.sets)
    prob = Prob(odds.counts, odds.sizesample)
    if odds == guess or prob == guess:
        msg = XSTR.PERFECT
    else:
        guess_prob = guess if type(guess) == float else 0.0 if guess[0] == 0 else Prob(*guess) 
        msg = f'\n{XSTR.CONGRATS}' if close_enough(prob, guess_prob) else f'\n{XSTR.TOO_BAD}'
    queried_sets = allcombos.elems_in_sets(queried)
    return odds, prob, msg, allcombos, queried_sets
    
def play(aplayers, bplayers):
    acombos = Combinations(aplayers.players, aplayers.num_herded)
    bcombos = Combinations(bplayers.players, bplayers.num_herded)
    allsets = Combinations.add_sets(acombos.sets, bcombos.sets)
    allcombos = Combinatorics(allsets, aplayers.players+bplayers.players)
    return allcombos, acombos, bcombos

def game(aplayers, bplayers, check_odds_names):
    displays.display_players(aplayers, bplayers, check_odds_names)
    allcombos, acombos, bcombos = play(aplayers, bplayers)
    guess = get_number_input(f'\n{XSTR.PODDS}' % XSTR.AND.join(check_odds_names))
    results = check_guess(guess, allcombos, check_odds_names)
    aqueried_sets = get_subset_matches(acombos, aplayers.queried_players)
    bqueried_sets = get_subset_matches(bcombos, bplayers.queried_players)
    displays.display_results(*results, acombos, bcombos, aqueried_sets, bqueried_sets, aplayers, bplayers)

def start():
    ask_user = False #get_user_option(XSTR.PUSER_OPTIONS)
    aplayers, bplayers, check_odds_names  = set_up_players(*get_selections_from_user() if ask_user else get_random())
    game(aplayers, bplayers, check_odds_names)
    start() if get_user_option(XSTR.CONTINUE) else None

if __name__ == '__main__':
    displays.startup()
    start()
    