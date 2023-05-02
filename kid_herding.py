import combo_tools
from combination_analysis import CombinationAnalysis
import random
import strings as XSTR

COUSINS = ['Leon', 'Jade', 'Sawyer', 'Mia', 'Anya', 'Sebastian', 'Morgan', 'Briana', 'Bailey', 'Bryelle']
ADULTS = COUSINS[5:]
KIDS = COUSINS[:5]
BORDER = ''.join(['=' for __ in range(120)])

def check_guess(guess, isfloat, odds):
    if not isfloat:
        if guess == odds:
            print(XSTR.PERFECT)
            return True
        else:
            guess = guess[0] / guess[1]
    return close_enough(guess, odds[0] / odds[1])

def close_enough(val1, val2):
    return abs(val1 - val2) <= 0.20

def get_odds(subset, superset):
    return combo_tools.odds(subset, superset)

def get_number_input(prompt):
    while True:
        try:
            raw = input(prompt)
            return (float(raw), True) if '.' in raw else ([int(val.strip()) for val in raw.split(XSTR.IN)], False)
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

def get_user_options():
    print(BORDER)
    choice = input(XSTR.PUSER_OPTIONS)      
    return choice.strip().lower()[0] == XSTR.AFFIRM[0]

def game():
    print(BORDER)
    print(XSTR.STORY)
    ask_user = get_user_options()
    atargets, num_herded_adults, ktargets, num_herded_kids, who_to_check_odds_for  = get_selections_from_user() if ask_user else get_random()
    display_players(atargets, num_herded_adults, ktargets, num_herded_kids, who_to_check_odds_for)
    csets, asets_analysis, ksets_analysis = herd(atargets, num_herded_adults, ktargets, num_herded_kids)
    guess, isfloat = get_number_input(f'\n{XSTR.PODDS1} {XSTR.AND.join(who_to_check_odds_for)} {XSTR.PODDS2}')
    odds = get_odds(who_to_check_odds_for, csets)
    wins = check_guess(guess, isfloat, odds)
    herded_csets = elems_in_lists(who_to_check_odds_for, csets)
    display_results(odds, wins, csets, herded_csets)

def get_selections_from_user():
    print(BORDER)
    atargets = get_name_input('\n' + XSTR.PADULTS_TO_PLAY, ADULTS)
    num_herd_adults = get_number_input(XSTR.PADULTS_CAN_HERD)[0][0]
    ktargets = get_name_input(XSTR.DKIDS_TO_PLAY, KIDS)
    num_herd_kids =  get_number_input(XSTR.PKIDS_CAN_HERD)[0][0]
    who_to_check_the_odds_for = get_name_input(XSTR.PCOUSINS, atargets + ktargets)
    return atargets, num_herd_adults, ktargets, num_herd_kids, who_to_check_the_odds_for

def get_random():
    num_atargets = random.randint(1, len(ADULTS))
    atargets = get_random_selection(ADULTS, num_atargets)
    num_herd_adults = random.randint(1, num_atargets)
    num_ktargets = random.randint(1, len(KIDS))
    ktargets = get_random_selection(KIDS, num_ktargets)
    num_herd_kids = random.randint(1, num_ktargets)
    who_to_check_the_odds_for = get_random_selection(atargets + ktargets, random.randint(1, len(atargets + ktargets)))
    return atargets, num_herd_adults, ktargets, num_herd_kids, who_to_check_the_odds_for

def display_players(atargets, num_herded_adults, ktargets, num_herded_kids, who_took_check_odds_for):
    print(BORDER)
    print(f'\n{XSTR.DADULTS_CAN_HERD} {num_herded_adults} {XSTR.DADULTS_TO_PLAY}:\n {XSTR.AND.join(atargets)}')
    print(f'{XSTR.DKIDS_CAN_HERD} {num_herded_kids} {XSTR.DKIDS_TO_PLAY}:\n {XSTR.AND.join(ktargets)}')
    print(f'{XSTR.DCHECK_ODDS1} {XSTR.AND.join(who_took_check_odds_for)} {XSTR.DCHECK_ODDS2}')

def display_results(odds, wins, csets, herded):
    print(BORDER)
    result = f'\n{XSTR.CONGRATS}' if wins else f'\n{XSTR.TOO_BAD}'
    print(f'{result}\n{XSTR.RESULTS_ODDS} {odds[0]} {XSTR.IN} {odds[1]}, {XSTR.RESULTS_PROB} {odds[0]/odds[1]}')
    print(f'\n{XSTR.SETS}:\n{combo_tools.format_as_set(csets)}')
    print(f'{XSTR.HERDED}:\n{combo_tools.format_as_set(herded)}')

def herd(atargets, num_herded_adults, ktargets, num_herded_kids):
    asets = combo_tools.choose(atargets, num_herded_adults)
    asets_analysis = CombinationAnalysis(asets)
    ksets = combo_tools.choose(ktargets, num_herded_kids)
    ksets_analysis = CombinationAnalysis(ksets)
    return combo_tools.add_sets(asets, ksets), asets_analysis, ksets_analysis

def elems_in_lists(elems, lists: list):
    return [l for l in lists if set(elems).issubset(set(l))]

if __name__ == '__main__':
    game()
    print(BORDER)
    