import strings as XSTR
from combinatorics import ComboValue as CV

BORDER = ''.join(['=' for __ in range(120)])

def startup():
    print(BORDER)
    print(XSTR.STORY)

def display_players(aplayers, bplayers, odds_check_names):
    print(BORDER)
    print(f'\n{XSTR.DADULTS_CAN_HERD} {aplayers.num_herded} {XSTR.DADULTS_TO_PLAY}:\n      {XSTR.AND.join(aplayers.players)}')
    print(f'{XSTR.DKIDS_CAN_HERD} {bplayers.num_herded} {XSTR.DKIDS_TO_PLAY}:\n      {XSTR.AND.join(bplayers.players)}')
    print(f'{XSTR.DCHECK_ODDS}' % XSTR.AND.join(odds_check_names))
    print(BORDER)

def format_results(odds, prob, msg, allcombos, queried_sets, acombos, bcombos, aqueried_combos, bqueried_combos, aplayers, bplayers):
    l1 = f'{msg}\n{XSTR.RESULTS_ODDS} {odds}, {XSTR.RESULTS_PROB} {prob}'
    l2 = f'\n{XSTR.DQADULTS_SETS}{aplayers.remaining_sets.combo_value}\n{aqueried_combos}'
    l3 = f'\n{XSTR.DADULTS_SETS}{acombos.combo_value}\n{acombos}'
    l4 = f'\n{XSTR.DQKIDS_SETS}{bplayers.remaining_sets.combo_value}\n{bqueried_combos}'
    l5 = f'\n{XSTR.DKIDS_SETS}{bcombos.combo_value}\n{bcombos}'
    l6 = f'\n{XSTR.DQCOMBINED_SETS}\n{queried_sets}'
    l7 = f'\n{XSTR.DCOMINED_SETS}\n{allcombos}'
    return '\n'.join([l1, l2, l3, l4, l5, l6, l7])

def prob_display(combos, players):
    queriedsize = players.num_queried
    qcombo_value = CV(combos.combo_value.n - queriedsize, combos.combo_value.k - queriedsize)
    return f'{qcombo_value}/{combos.combo_value}', f'{qcombo_value.value}/{combos.combo_value.value}', f'{qcombo_value/combos.combo_value:.2f}', qcombo_value.value, combos.combo_value.value

def format_math(acombos, bcombos, aplayers, bplayers):
    a1, a2, a3, a4, a5 = prob_display(acombos, aplayers)
    k1, k2, k3, k4, k5 = prob_display(bcombos, bplayers)
    return f'( {a1} = {a2} = {a3} ) * ( {k1} = {k2} = {k3} ) = {a4}/{a5} * {k4}/{k5} = {(a4*k4)/(a5*k5):.2f}'

def display_results(odds, prob, msg, allcombos, queried_sets, acombos, bcombos, aqueried_combos, bqueried_combos, aplayers, bplayers):
    print(format_results(odds, prob, msg, allcombos, queried_sets, acombos, bcombos, aqueried_combos, bqueried_combos, aplayers, bplayers))
    print(format_math(acombos, bcombos, aplayers, bplayers))