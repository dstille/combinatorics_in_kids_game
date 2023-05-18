from combinatorics import ComboValue as CV

def prob_display(herded, players):
    queriedsize = players.num_queried
    qcombo_value = CV(herded.combo_value.n - queriedsize, herded.combo_value.k - queriedsize)
    return f'{qcombo_value}/{herded.combo_value}', f'{qcombo_value.value}/{herded.combo_value.value}', f'{qcombo_value/herded.combo_value:.2f}', qcombo_value.value, herded.combo_value.value

def display_math(acombos, kcombos, aplayers, kplayers):
    a1, a2, a3, a4, a5 = prob_display(acombos, aplayers)
    k1, k2, k3, k4, k5 = prob_display(kcombos, kplayers)
    return f'( {a1} = {a2} = {a3} ) * ( {k1} = {k2} = {k3} ) = {a4}/{a5} * {k4}/{k5} = {(a4*k4)/(a5*k5):.2f}'
