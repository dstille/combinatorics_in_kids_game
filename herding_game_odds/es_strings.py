STORY = """
Resulta que Bear, el perro de Leon y Jade, es un perro pastor.
Eso significa que su raza ha desarrollado habilidades para pastorear animales como ovejas.
Bear está emocionado de ver lo buen pastor que es y va a probar sus habilidades con los primos.
Los Primos se dividen en dos grupos: los Adultos y los Niños.
Los adultos: Sebastian, Brianna, Bailey, Morgan, Bryelle
Los niños: Anya, Leon, Sawyer, Jade, Mia

Bear puede recoger y arrear un cierto número de adultos y un cierto número de niños.

Tu trabajo es averiguar las probabilidades de que un primo o un conjunto de primos sean arreados.
No todos los primos pueden participar.
"""
ALLPLAYERS = ['Leon', 'Jade', 'Sawyer', 'Mia', 'Anya', 'Sebastian', 'Morgan', 'Briana', 'Bailey', 'Bryelle']
APLAYERS = ALLPLAYERS[5:]
BPLAYERS = ALLPLAYERS[:5]

AND = ' y '
NUM_ERROR = 'No es un número. Inténtalo de nuevo'
STR_ERROR = '¡Error al procesar la entrada! Inténtalo de nuevo'
PERFECT = 'EN LA NARIZ!!!'
IN = 'en'
AFFIRM = 'sí'
PROMPT_ODDS = 'Ingrese las cuotas o probabilidad de que %s sea pastoreado.\nPara cuotas ingrese __ en __; para probabilidad ingrese _.__ : '
PROMPT_USER_OPTIONS = '¿le gustaría decidir cuántos primos tratar de arrear \ny qué primos encontrar las probabilidades de que realmente los arrearan, (sí/no)? '
PROMPT_APLAYERS_TO_PLAY = 'ingrese los adultos que jugarán, separados por un espacio: '
PROMPT_APLAYERS_NUM = 'ingrese el número de adultos que Bear puede arrear a la vez: '
PROMPT_BPLAYERS_TO_PLAY = 'ingrese los niños que jugarán, separados por un espacio: '
PROMPT_BPLAYERS_NUM = 'ingrese el número de niños que Bear puede reunir a la vez: '
PROMPT_PLAYERS_TO_CHECK_ODDS_FOR = 'ingrese los primos para comprobar las probabilidades de que hayan sido arreados, separados por un espacio: '

DISPLAY_APLAYERS_NUM_CHOSEN = 'El número de adultos que Bear puede atrapar es'
DISPLAY_APLAYERS = 'y los objetivos adultos son '
DISPLAY_BPLAYERS_NUM_CHOSEN = 'El número de niños que Bear puede atrapar es'
DISPLAY_BPLAYERS = 'y los objetivos de los niños son'
DISPLAY_PLAYERS_TO_CHECK_ODDS_FOR = 'Vamos a comprobar las probabilidades de que %s sea arreado por Bear'

DISPLAY_QUERIED_ASETS= 'subconjuntos de adultos consultados: '
DISPLAY_ASETS = 'juegos para adultos: '
DISPLAY_QUERIED_BSETS = 'subconjuntos de niños consultados: '
DISPLAY_BSETS = 'conjuntos para niños: '
DISPLAY_QUERIED_COMBINED_SETS = 'subconjuntos consultados combinados: '
DISPLAY_COMINED_SETS = 'conjuntos combinados: '

CONGRATS = '¡Lo hiciste!'
TOO_BAD = 'No del todo'
RESULTS_ODDS = 'las probabilidades eran'
RESULTS_PROB = 'o una probabilidad de'
SETS = 'conjuntos'
CONTINUE = '¿Te gustaría otra oportunidad, (s/n)?: '