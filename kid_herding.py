import combo_tools
from combination_analysis import CombinationAnalysis
import random

COUSINS = ['Leon', 'Jade', 'Sawyer', 'Mia', 'Anya', 'Sebastian', 'Morgan', 'Briana', 'Bailey', 'Bryelle']
ADULTS = COUSINS[5:]
KIDS = COUSINS[:5]

story = """
It turns out that Bear, Leon and Jade's dog, is a herding dog. 
That means that his breed has developed skills to herd animals like sheep.
Bear is excited to see how good of a herder he is and is going to try out his skills out on the cousins.
The cousins are divided into two groups: the Adults and the Kids.
The Adults: Sebastian, Brianna, Bailey, Morgan, Bryelle
The Kids: Anya, Leon, Sawyer, Jade, Mia

Bear can pick off and herd a certain number of Adults and a certain number of Kids.

Your job is to figure out the odds of a cousin or set of cousins getting herded.
Not all cousins may participate.
"""

def check_guess(guess, isfloat, odds):
    if not isfloat:
        if guess == odds:
            print('on the nose!')
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
            return (float(raw), True) if '.' in raw else ([int(val.strip()) for val in raw.split('in')], False)
        except:
            print('Not a number. Please try again')

def get_name_input(prompt, cousins):
    while True:
        names = input(prompt).split()
        if set(names).issubset(set(cousins)):
            return names
        print('Error processing input! Please try again')

def get_random_selection(cousins, num_cousins):
    copy_cousins = cousins[::1]
    random.shuffle(copy_cousins)  
    return copy_cousins[:num_cousins]

def get_user_options():
    choice = input('would you like to decide how many cousins to try herding and which cousins to finds the odds that they actually got herded, (y/n)? ')      
    return choice.strip().lower()[0] == 'y'

def game():
    print(story)
    ask_user = get_user_options()
    atargets, num_herded_adults, ktargets, num_herded_kids, who_to_check_odds_for  = get_selections_from_user() if ask_user else get_random()
    display_players(atargets, num_herded_adults, ktargets, num_herded_kids, who_to_check_odds_for)
    csets, asets_analysis, ksets_analysis = herd(atargets, num_herded_adults, ktargets, num_herded_kids)
    guess, isfloat = get_number_input(f'\nEnter the odds or probability that {" and ".join(who_to_check_odds_for)} will be herded.\nFor odds enter __ in __ ; for probability enter 0.__ : ')
    odds = get_odds(who_to_check_odds_for, csets)
    wins = check_guess(guess, isfloat, odds)
    herded_csets = elems_in_lists(who_to_check_odds_for, csets)
    display_results(odds, wins, csets, herded_csets)

def get_selections_from_user():
    atargets = get_name_input(f'\nenter the adults that will play, separated by a space: ', ADULTS)
    num_herd_adults = get_number_input('enter the number of adults Bear can herd at once: ')[0][0]
    ktargets = get_name_input('enter the kids that will play, separated by a space: ', KIDS)
    num_herd_kids =  get_number_input('enter the number of kids Bear can herd at once: ')[0][0]
    who_to_check_the_odds_for = get_name_input('enter the cousins to check the odds that the got herded, separated by a space: ', atargets + ktargets)
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
    print(f'\nThe number of adults who Bear can catch is {num_herded_adults} and the adult targets are {" and ".join(atargets)}')
    print(f'The number of kids who Bear can catch is {num_herded_kids} and the kid targets are {" and ".join(ktargets)}')
    print(f'We are going to check the odds that {" and ".join(who_took_check_odds_for)} get herded by Bear')

def display_results(odds, wins, csets, herded):
    result = '\nYou did it!!!' if wins else '\nNot quite'
    print(f'{result}\nthe odds were {odds[0]} in {odds[1]}, or a probability of {odds[0]/odds[1]}')
    print(f'\nsets:\n{combo_tools.format_as_set(csets)}')
    print(f'herded:\n{combo_tools.format_as_set(herded)}')

def herd(atargets, num_herded_adults, ktargets, num_herded_kids):
    asets = combo_tools.choose(atargets, num_herded_adults)
    asets_analysis = CombinationAnalysis(asets)
    ksets = combo_tools.choose(ktargets, num_herded_kids)
    ksets_analysis = CombinationAnalysis(ksets)
    return combo_tools.add_sets(asets, ksets), asets_analysis, ksets_analysis

def elems_in_lists(elems, lists: list):
    return [l for l in lists if set(elems).issubset(set(l))]

if __name__ == '__main__':
    #game()
    c4_3 = combo_tools.choose(KIDS[:4], 3)
    print(combo_tools.format_as_set(c4_3))
    c3_2 = combo_tools.choose(KIDS[:3], 2)
    print(combo_tools.format_as_set(c3_2))
    c3_3 = combo_tools.choose(KIDS[:3], 3)
    print(combo_tools.format_as_set(c3_3))
    c3_2and3 = combo_tools.add_sets(c3_2, c3_3)
    print(combo_tools.format_as_set(c3_2and3))