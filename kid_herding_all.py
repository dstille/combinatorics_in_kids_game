
import random

STORY = """
It turns out that Bear, Leon and Jade's dog, is a herding dog. 
That means that his breed has developed skills to herd animals like sheep.
Bear is excited to see how good of a herder he is and is going to try out his skills out on the Cousins.
The Cousins are divided into two groups: the Adults and the Kids.
The Adults: Sebastian, Brianna, Bailey, Morgan, Bryelle
The Kids: Anya, Leon, Sawyer, Jade, Mia

Bear can pick off and herd a certain number of Adults and a certain number of Kids.

Your job is to figure out the odds of a Cousin or set of Cousins getting herded.
Not all Cousins may participate.
"""

AND = ' and '
NUM_ERROR = 'Not a number. Please try again'
STR_ERROR = 'Error processing input! Please try again'
PERFECT = 'on the nose!'
IN = 'in'
AFFIRM = 'yes'
PODDS1 = 'Enter the odds or probability that'
PODDS2 = 'will be herded.\nFor odds enter __ in __ ; for probability enter 0.__ : '

PUSER_OPTIONS = 'would you like to decide how many cousins to try herding \nand which cousins to finds the odds that they actually got herded, (y/n)? '
PADULTS_TO_PLAY = 'enter the adults that will play, separated by a space: '
PADULTS_CAN_HERD = 'enter the number of adults Bear can herd at once: '
PKIDS_TO_PLAY = 'enter the kids that will play, separated by a space: '
PKIDS_CAN_HERD = 'enter the number of kids Bear can herd at once: '
PCOUSINS = 'enter the cousins to check the odds that they got herded, separated by a space: '

DADULTS_CAN_HERD = 'The number of adults who Bear can catch is'
DADULTS_TO_PLAY = 'and the adult targets are '
DKIDS_CAN_HERD = 'The number of kids who Bear can catch is'
DKIDS_TO_PLAY = 'and the kid targets are'
DCHECK_ODDS1 = 'We are going to check the odds that'
DCHECK_ODDS2 = 'get herded by Bear'

CONGRATS = 'You did it!!!'
TOO_BAD = 'Not quite'
RESULTS_ODDS = 'the odds were'
RESULTS_PROB = 'or a probability of'
SETS = 'sets'
HERDED = 'herded'

COUSINS = ['Leon', 'Jade', 'Sawyer', 'Mia', 'Anya', 'Sebastian', 'Morgan', 'Briana', 'Bailey', 'Bryelle']
ADULTS = COUSINS[5:]
KIDS = COUSINS[:5]
BORDER = ''.join(['=' for __ in range(120)])

def check_guess(guess, isfloat, odds):
    if not isfloat:
        if guess == odds:
            print(PERFECT)
            return True
        else:
            guess = guess[0] / guess[1]
    return close_enough(guess, odds[0] / odds[1])

def close_enough(val1, val2):
    return abs(val1 - val2) <= 0.20

def get_odds(subset, superset):
    return odds(subset, superset)

def get_number_input(prompt):
    while True:
        try:
            raw = input(prompt)
            return (float(raw), True) if '.' in raw else ([int(val.strip()) for val in raw.split(IN)], False)
        except:
            print(NUM_ERROR)

def get_name_input(prompt, cousins):
    while True:
        names = input(prompt).split()
        if set(names).issubset(set(cousins)):
            return names
        print(STR_ERROR)

def get_random_selection(cousins, num_cousins):
    copy_cousins = cousins[::1]
    random.shuffle(copy_cousins)  
    return copy_cousins[:num_cousins]

def get_user_options():
    print(BORDER)
    choice = input(PUSER_OPTIONS)      
    return choice.strip().lower()[0] == AFFIRM[0]

def game():
    print(BORDER)
    print(STORY)
    ask_user = get_user_options()
    atargets, num_herded_adults, ktargets, num_herded_kids, who_to_check_odds_for  = get_selections_from_user() if ask_user else get_random()
    display_players(atargets, num_herded_adults, ktargets, num_herded_kids, who_to_check_odds_for)
    csets = herd(atargets, num_herded_adults, ktargets, num_herded_kids)
    guess, isfloat = get_number_input(f'\n{PODDS1} {AND.join(who_to_check_odds_for)} {PODDS2}')
    odds = get_odds(who_to_check_odds_for, csets)
    wins = check_guess(guess, isfloat, odds)
    herded_csets = elems_in_lists(who_to_check_odds_for, csets)
    display_results(odds, wins, csets, herded_csets)
    display_math(atargets, num_herded_adults, ktargets, num_herded_kids, who_to_check_odds_for)

def get_selections_from_user():
    print(BORDER)
    atargets = get_name_input('\n' + PADULTS_TO_PLAY, ADULTS)
    num_herd_adults = get_number_input(PADULTS_CAN_HERD)[0][0]
    ktargets = get_name_input(DKIDS_TO_PLAY, KIDS)
    num_herd_kids =  get_number_input(PKIDS_CAN_HERD)[0][0]
    who_to_check_the_odds_for = get_name_input(PCOUSINS, atargets + ktargets)
    return atargets, num_herd_adults, ktargets, num_herd_kids, who_to_check_the_odds_for

def get_random():
    num_atargets = random.randint(1, len(ADULTS)-1)
    atargets = get_random_selection(ADULTS, num_atargets)
    num_herd_adults = random.randint(1, num_atargets)
    num_ktargets = random.randint(1, len(KIDS)-1)
    ktargets = get_random_selection(KIDS, num_ktargets)
    num_herd_kids = random.randint(1, num_ktargets)
    who_to_check_the_odds_for = get_random_selection(atargets + ktargets, random.randint(1, len(atargets + ktargets)-1))
    return atargets, num_herd_adults, ktargets, num_herd_kids, who_to_check_the_odds_for

def display_players(atargets, num_herded_adults, ktargets, num_herded_kids, who_took_check_odds_for):
    print(BORDER)
    print(f'\n{DADULTS_CAN_HERD} {num_herded_adults} {DADULTS_TO_PLAY}:\n {AND.join(atargets)}')
    print(f'{DKIDS_CAN_HERD} {num_herded_kids} {DKIDS_TO_PLAY}:\n {AND.join(ktargets)}')
    print(f'{DCHECK_ODDS1} {AND.join(who_took_check_odds_for)} {DCHECK_ODDS2}')

def display_results(odds, wins, csets, herded):
    print(BORDER)
    result = f'\n{CONGRATS}' if wins else f'\n{TOO_BAD}'
    print(f'{result}\n{RESULTS_ODDS} {odds[0]} {IN} {odds[1]}, {RESULTS_PROB} {odds[0]/odds[1]}')
    print(f'\n{SETS}:\n{format_as_set(csets)}')
    print(f'{HERDED}:\n{format_as_set(herded)}')

def display_math(atargets, num_herded_adults, ktargets, num_herded_kids, who_to_check_odds_for):
    aprob = prob_display(len(atargets), num_herded_adults, num_herded_adults, sum(cousin in atargets for cousin in who_to_check_odds_for))
    kprob = prob_display(len(ktargets), num_herded_kids, num_herded_kids, sum(cousin in ktargets for cousin in who_to_check_odds_for))
    print(f'{aprob} * {kprob}')

def herd(atargets, num_herded_adults, ktargets, num_herded_kids):
    asets = choose(atargets, num_herded_adults)
    ksets = choose(ktargets, num_herded_kids)
    return add_sets(asets, ksets)

def elems_in_lists(elems, lists: list):
    return [l for l in lists if set(elems).issubset(set(l))]

def choose_r(set_in, k, combos = []):
    return [choose_r(set_in[idx+1:], k-1, combos + [elem]) for idx, elem in enumerate(set_in)] if k>0 else combos

def permute_r(set_in, k, combos = []):
    return [permute_r(remove_at_idx(set_in, idx), k-1, combos + [elem]) for idx, elem in enumerate(set_in)] if k>0 else combos

def remove_at_idx(list_in, idx):
    return list_in[:idx] if idx+1 >= len(list_in) else list_in[:idx] + list_in[idx+1:] 

def pascal(x, row = [1], n = 1):
    return [row] + pascal(x, [1 if k == 0 or n == k else row[k-1] + row[k] for k in range(n+1)], n+1) if n < x else [row]

def add_sets(set1, set2):
    return eliminate_duplicates([(*s1, *s2) for s2 in set2 for s1 in set1])

def format_as_set(iterables):
    return ', '.join(['{' + ', '.join(itr) + '}' for itr in iterables])

def flatten(lists):
    def down_1d(outer_l):
        return [elem for inner_l in outer_l for elem in inner_l]
    while type(lists[0][0]) == list:
        lists = down_1d(lists) 
    return lists

def save(fname, contents):
    with open(fname, 'w') as f:
        f.write(contents)

def choose(set_in: list, k: int):
    set_in.sort()
    combos = choose_r(set_in, k)   
    return flatten(combos)

def permute(set_in: list, k: int):
    set_in.sort()
    permutations = permute_r(set_in, k)   
    return flatten(permutations)

def counts(sub, lists: list):
    return sum(set(sub).issubset(set(l)) for l in lists)

def odds(event, poss_outcomes):
    event_ct = counts(event, poss_outcomes)
    size_outcomes = len(poss_outcomes)
    return event_ct, size_outcomes

def eliminate_duplicates(sets_in):
    return [sorted(s) for s in frozenset(frozenset(sorted(set)) for set in sets_in)]

def format_combos(n, k):
    return f'C({n},{k})'

def format_prob(n1, k1, n2, k2):
    return f'{format_combos(n1, k1)} / {format_combos(n2, k2)}'

def factorial(x):
    return x * factorial(x-1) if x>1 else 1

def C(n, k):
    return factorial(n) // (factorial(n-k)*factorial(k))

def p(event_ct, size_outcomes):
    return event_ct/size_outcomes

def prob_display(n1, k1, n2, k2):
    event_ct = C(n1, k1)
    size_outcomes = C(n2, k2)
    return f'{format_prob(n1, k1, n2, k2)}  =  {event_ct} / {size_outcomes}  =  {p(event_ct, size_outcomes)}'








if __name__ == '__main__':
    game()
    print(BORDER)
    