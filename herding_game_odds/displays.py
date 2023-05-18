import strings as XSTR
import math_representations

BORDER = ''.join(['=' for __ in range(120)])

def startup():
    print(BORDER)
    print(XSTR.STORY)

def display_players(aplayers, kplayers, who_to_check_odds_for):
    print(BORDER)
    print(f'\n{XSTR.DADULTS_CAN_HERD} {aplayers.num_herded} {XSTR.DADULTS_TO_PLAY}:\n      {XSTR.AND.join(aplayers.players)}')
    print(f'{XSTR.DKIDS_CAN_HERD} {kplayers.num_herded} {XSTR.DKIDS_TO_PLAY}:\n      {XSTR.AND.join(kplayers.players)}')
    print(f'{XSTR.DCHECK_ODDS1} {XSTR.AND.join(who_to_check_odds_for)} {XSTR.DCHECK_ODDS2}')
    print(BORDER)

def format_results(odds, prob, msg, csets, queried_sets, asets, ksets, aqueried_sets, kqueried_sets, aplayers, kplayers):
    l1 = f'{msg}\n{XSTR.RESULTS_ODDS} {odds}, {XSTR.RESULTS_PROB} {prob}'
    l2 = f'\nqueried adults subsets:   {aplayers.remaining_sets.combo_value}\n{aqueried_sets}'
    l3 = f'\nadult sets:               {asets.combo_value}\n{asets}'
    l4 = f'\nqueried kids subsets:     {aplayers.remaining_sets.combo_value}\n{kqueried_sets}'
    l5 = f'\nkid sets:                 {ksets.combo_value}\n{ksets}'
    l6 = f'\ncombined sets:\n{csets}'
    l7 = f'\n{XSTR.HERDED}:\n{queried_sets}'
    return '\n'.join([l1, l2, l3, l4, l5, l6, l7])

def display_results(odds, prob, msg, csets, queried_sets, asets, ksets, aqueried_sets, kqueried_sets, aplayers, kplayers):
    print(format_results(odds, prob, msg, csets, queried_sets, asets, ksets, aqueried_sets, kqueried_sets, aplayers, kplayers))

def display_math(asets, ksets, aplayers, kplayers):
    print(math_representations.display_math(asets, ksets, aplayers, kplayers))
    print(BORDER)