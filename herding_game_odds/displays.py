import strings as XSTR
from combinatorics import ComboValue as CV

BORDER = ''.join(['=' for __ in range(120)])

def startup():
    print(BORDER)
    print(XSTR.STORY)

def display_players(aplayers, kplayers, who_to_check_odds_for):
    print(BORDER)
    print(f'\n{XSTR.DADULTS_CAN_HERD} {aplayers.num_herded} {XSTR.DADULTS_TO_PLAY}:\n      {XSTR.AND.join(aplayers.players)}')
    print(f'{XSTR.DKIDS_CAN_HERD} {kplayers.num_herded} {XSTR.DKIDS_TO_PLAY}:\n      {XSTR.AND.join(kplayers.players)}')
    print(f'{XSTR.DCHECK_ODDS}' % XSTR.AND.join(who_to_check_odds_for))
    print(BORDER)

def format_results(odds, prob, msg, csets, queried_sets, asets, ksets, aqueried_sets, kqueried_sets, aplayers, kplayers):
    l1 = f'{msg}\n{XSTR.RESULTS_ODDS} {odds}, {XSTR.RESULTS_PROB} {prob}'
    l2 = f'\n{XSTR.DQADULTS_SETS}{aplayers.remaining_sets.combo_value}\n{aqueried_sets}'
    l3 = f'\n{XSTR.DADULTS_SETS}{asets.combo_value}\n{asets}'
    l4 = f'\n{XSTR.DQKIDS_SETS}{aplayers.remaining_sets.combo_value}\n{kqueried_sets}'
    l5 = f'\n{XSTR.DKIDS_SETS}{ksets.combo_value}\n{ksets}'
    l6 = f'\n{XSTR.DQCOMBINED_SETS}\n{queried_sets}'
    l7 = f'\n{XSTR.DCOMINED_SETS}\n{csets}'
    return '\n'.join([l1, l2, l3, l4, l5, l6, l7])

def prob_display(herded, players):
    queriedsize = players.num_queried
    qcombo_value = CV(herded.combo_value.n - queriedsize, herded.combo_value.k - queriedsize)
    return f'{qcombo_value}/{herded.combo_value}', f'{qcombo_value.value}/{herded.combo_value.value}', f'{qcombo_value/herded.combo_value:.2f}', qcombo_value.value, herded.combo_value.value

def format_math(acombos, kcombos, aplayers, kplayers):
    a1, a2, a3, a4, a5 = prob_display(acombos, aplayers)
    k1, k2, k3, k4, k5 = prob_display(kcombos, kplayers)
    return f'( {a1} = {a2} = {a3} ) * ( {k1} = {k2} = {k3} ) = {a4}/{a5} * {k4}/{k5} = {(a4*k4)/(a5*k5):.2f}'

def display_results(odds, prob, msg, csets, queried_sets, asets, ksets, aqueried_sets, kqueried_sets, aplayers, kplayers):
    print(format_results(odds, prob, msg, csets, queried_sets, asets, ksets, aqueried_sets, kqueried_sets, aplayers, kplayers))
    print(format_math(asets, ksets, aplayers, kplayers))