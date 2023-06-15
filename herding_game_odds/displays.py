import strings as XSTR
from combinations import ComboValue as CV
from players import Players

BORDER = ''.join(['=' for __ in range(120)])

def startup():
    print(BORDER)
    print(XSTR.STORY)

def display_players(aplayers, bplayers, odds_check_names):
    print(BORDER)
    print(f'\n{XSTR.DISPLAY_APLAYERS_NUM_CHOSEN} {aplayers.num_chosen} {XSTR.DISPLAY_APLAYERS}:\n      {XSTR.AND.join(aplayers.players)}')
    print(f'{XSTR.DISPLAY_BPLAYERS_NUM_CHOSEN} {bplayers.num_chosen} {XSTR.DISPLAY_BPLAYERS}:\n      {XSTR.AND.join(bplayers.players)}')
    print(f'{XSTR.DISPLAY_PLAYERS_TO_CHECK_ODDS_FOR}' % XSTR.AND.join(odds_check_names))
    print(BORDER)

def size_explanantion(combos, players):
    return f'we start with {combos.combo_value} and so far we haven chosen {players.num_queried}, {players.queried_set};\nfrom {players.nonqueried_set} we need to choose the remaining {players.num_chosen-players.num_queried}'

def prob_display(combos, players):
    queriedsize = players.num_queried
    qcombo_value = CV(combos.combo_value.n - queriedsize, combos.combo_value.k - queriedsize)
    return f'{qcombo_value}/{combos.combo_value}', f'{qcombo_value.value}/{combos.combo_value.value}', f'{qcombo_value/combos.combo_value:.2f}', qcombo_value.value, combos.combo_value.value

def format_results(odds, prob, msg, allcombos, queried_sets, acombos, bcombos, aqueried_combos, bqueried_combos, aplayers, bplayers):
    l1 = f'{msg}\n\n{XSTR.RESULTS_ODDS} {odds}, {XSTR.RESULTS_PROB} {prob}'
    l2 = f'\n{size_explanantion(acombos, aplayers)}\n{XSTR.DISPLAY_QUERIED_ASETS}{aplayers.remaining_sets.combo_value} =   {aplayers.remaining_sets.combo_value.as_factorials()}  =  {aplayers.remaining_sets.combo_value.value}   {CV.as_formula()}\n{aqueried_combos}'
    l3 = f'\n{XSTR.DISPLAY_ASETS}{acombos.combo_value} =   {acombos.combo_value.as_factorials()}  =  {acombos.combo_value.value}\n{acombos}'
    l4 = f'\n\n{size_explanantion(bcombos, bplayers)}\n{XSTR.DISPLAY_QUERIED_BSETS}{bplayers.remaining_sets.combo_value} =   {bplayers.remaining_sets.combo_value.as_factorials()}  =  {bplayers.remaining_sets.combo_value.value}\n{bqueried_combos}'
    l5 = f'\n{XSTR.DISPLAY_BSETS}{bcombos.combo_value} =   {bcombos.combo_value.as_factorials()}  =  {bcombos.combo_value.value}\n{bcombos}'
    l6 = f'\n\n{XSTR.DISPLAY_QUERIED_COMBINED_SETS}\n{queried_sets}'
    l7 = f'\n{XSTR.DISPLAY_COMINED_SETS}\n{allcombos}'
    return '\n'.join([l1, l2, l3, l4, l5, l6, l7])

def format_math(acombos, bcombos, aplayers, bplayers):
    a1, a2, a3, a4, a5 = prob_display(acombos, aplayers)
    k1, k2, k3, k4, k5 = prob_display(bcombos, bplayers)
    return f'( {a1} = {a2} = {a3} ) * ( {k1} = {k2} = {k3} ) = {a4}/{a5} * {k4}/{k5} = {(a4*k4)/(a5*k5):.2f}'

def display_results(odds, prob, msg, allcombos, queried_sets, acombos, bcombos, aqueried_combos, bqueried_combos, aplayers, bplayers):
    print(format_results(odds, prob, msg, allcombos, queried_sets, acombos, bcombos, aqueried_combos, bqueried_combos, aplayers, bplayers))
    print('\n\n' + format_math(acombos, bcombos, aplayers, bplayers))