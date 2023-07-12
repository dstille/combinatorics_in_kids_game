import strings as XSTR
from combinations import ComboValue as CV

BORDER = ''.join(['=' for __ in range(120)])

def startup():
    print(BORDER)
    print(XSTR.STORY2 % XSTR.AND.join(XSTR.PETS))

def display_players(players, odds_check_names):
    print(BORDER)
    print(f'\n{XSTR.PDISPLAY_PLAYERS_NUM_CHOSEN} {players.num_chosen} {XSTR.PDISPLAY_PLAYERS}:\n      {XSTR.AND.join(players.players)}')
    print(f'{XSTR.PDISPLAY_PLAYERS_TO_CHECK_ODDS_FOR}' % XSTR.AND.join(odds_check_names))
    print(BORDER)

def hint(combos, players, check_odds_names):
    print(XSTR.SIZE_HINT % (players.num_chosen-players.num_queried, players.nonqueried_set, players.queried_players))  

def size_explanantion(combos, players):
    return XSTR.SIZE_EXPLANATION % (combos.combo_value, players.num_queried, players.queried_set, players.nonqueried_set, players.num_chosen-players.num_queried)

def prob_display(combos, players):
    queriedsize = players.num_queried
    qcombo_value = CV(combos.combo_value.n - queriedsize, combos.combo_value.k - queriedsize)
    return f'{qcombo_value}/{combos.combo_value}', f'{qcombo_value.value}/{combos.combo_value.value}', f'{qcombo_value/combos.combo_value:.2f}', qcombo_value.value, combos.combo_value.value

def format_results(odds, prob, msg, combos, queried_sets, queried_combos, players):
    l1 = f'{msg}\n\n{XSTR.RESULTS_ODDS} {odds}, {XSTR.RESULTS_PROB} {prob}'
    l2 = f'\n{size_explanantion(combos, players)}\n{XSTR.PDISPLAY_QUERIED_SETS}{players.remaining_sets.combo_value} =   {players.remaining_sets.combo_value.as_factorials()}  =  {players.remaining_sets.combo_value.value}   {CV.as_formula()}\n{queried_sets}'
    l3 = f'\n{XSTR.PDISPLAY_SETS}{combos.combo_value} =   {combos.combo_value.as_factorials()}  =  {combos.combo_value.value}\n{combos}'
    l4 = f'\n\n{XSTR.PDISPLAY_QUERIED_SETS}\n{queried_sets}'
    l5 = f'\n{XSTR.PDISPLAY_SETS}\n{combos}'
    return '\n'.join([l1, l2, l3])

def format_math(combos, players):
    a1, a2, a3, a4, a5 = prob_display(combos, players)
    return f' {a1} = {a2} = {a3}'

def display_results(odds, prob, msg, combos, queried_sets, queried_combos, players):
    print(format_results(odds, prob, msg, combos, queried_sets, queried_combos, players))
    print('\n\n' + format_math(combos, players))