from players import Players
import random
import es_strings as XSTR
import displays
from combinatorics import Prob, Odds, Combinatorics
from combinations import Combinations

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

def get_random_selection(players, num_players):
    copy_players = players[::1]
    random.shuffle(copy_players)  
    return copy_players[:num_players]

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
    atargets = get_name_input(BORDER + '\n' + XSTR.PROMPT_APLAYERS_TO_PLAY, XSTR.APLAYERS)
    anum_herded = get_number_input(XSTR.PROMPT_APLAYERS_NUM)[0][0]
    btargets = get_name_input(XSTR.PROMPT_BPLAYERS_TO_PLAY, XSTR.BPLAYERS)
    bnum_herded =  get_number_input(XSTR.PROMPT_BPLAYERS_NUM)[0][0]
    check_odds_names = get_name_input(XSTR.PCOUSINS, atargets + btargets)
    return atargets, anum_herded, btargets, bnum_herded, check_odds_names

def get_random():
    num_atargets = random.randint(1, len(XSTR.APLAYERS)-1)
    atargets = get_random_selection(XSTR.APLAYERS, num_atargets)
    anum_chosen = random.randint(1, num_atargets)
    num_btargets = random.randint(1, len(XSTR.BPLAYERS)-1)
    btargets = get_random_selection(XSTR.BPLAYERS, num_btargets)
    bnum_chosen = random.randint(1, num_btargets)
    check_odds_names = get_random_selection(atargets + btargets, random.randint(1, anum_chosen+bnum_chosen-1))
    return atargets, anum_chosen, btargets, bnum_chosen, check_odds_names

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
    
def get_sets(aplayers, bplayers):
    acombos = Combinations(aplayers.players, aplayers.num_chosen)
    bcombos = Combinations(bplayers.players, bplayers.num_chosen)
    allsets = Combinations.add_sets(acombos.sets, bcombos.sets)
    allcombos = Combinatorics(allsets, aplayers.players+bplayers.players)
    return allcombos, acombos, bcombos

def game(aplayers, bplayers, check_odds_names):
    displays.display_players(aplayers, bplayers, check_odds_names)
    allcombos, acombos, bcombos = get_sets(aplayers, bplayers)
    guess = get_number_input(f'\n{XSTR.PROMPT_ODDS}' % XSTR.AND.join(check_odds_names))
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
    