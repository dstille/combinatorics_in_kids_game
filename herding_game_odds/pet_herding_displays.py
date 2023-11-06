import strings as XSTR
from combinations import ComboValue as CV
from combinatorics import Set
from math_reprs import Fraction

BORDER = 120*'='

def startup():
    print(BORDER)
    print(XSTR.STORY2 % XSTR.AND.join(XSTR.PETS))

def display_players(players, odds_check_names):
    print(BORDER)
    print(f'\n{XSTR.PDISPLAY_PLAYERS_NUM_CHOSEN} {players.num_chosen} {XSTR.PDISPLAY_PLAYERS}:\n      {players.names}')
    print(f'{XSTR.PDISPLAY_PLAYERS_TO_CHECK_ODDS_FOR}' % XSTR.AND.join(odds_check_names))
    print(BORDER)

def hint(players, nonqueried, queried_names):
    print(XSTR.SIZE_HINT % (players.num_chosen-len(queried_names), nonqueried.names, Set(queried_names)))  

def size_explanantion(players, nonqueried_players, queried_sets):
    return XSTR.SIZE_EXPLANATION % (players.combo_value, queried_sets.elements, nonqueried_players.names, nonqueried_players.num_chosen)

def prob_display(players, queried_sets):
    queriedsize = len(queried_sets.elements)
    qcombo_value = CV(players.combo_value.n - queriedsize, players.combo_value.k - queriedsize)
    return f'{qcombo_value}/{players.combo_value}', f'{qcombo_value.value}/{players.combo_value.value}', f'{qcombo_value/players.combo_value:.2f}'

def format_results(odds, prob, msg, players, queried_sets, nonqueried_players):
    l1 = f'{msg}\n\n{XSTR.RESULTS_ODDS} {odds}, {XSTR.RESULTS_PROB} {prob}'
    l2 = f'\n{size_explanantion(players, nonqueried_players, queried_sets)}\n{XSTR.PDISPLAY_QUERIED_SETS}{nonqueried_players.combo_value} =   {nonqueried_players.combo_value.as_factorials()}  =  {nonqueried_players.combo_value.value}   {CV.as_formula()}\n{queried_sets}'
    l3 = f'\n{XSTR.PDISPLAY_SETS}{players.combo_value} =   {players.combo_value.as_factorials()}  =  {players.combo_value.value}\n{players}'
    return '\n'.join([l1, l2, l3])

def format_math(players, queried_sets):
    a1, a2, a3 = prob_display(players, queried_sets)
    return f' {a1} = {a2} = {a3}'

def display_results(odds, prob, msg, queried_sets, players, nonqueried_players):
    print(format_results(odds, prob, msg, players, queried_sets, nonqueried_players))
    print('\n\n' + format_math(players, queried_sets))