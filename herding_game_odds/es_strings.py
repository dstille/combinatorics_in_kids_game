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
COUSINS = ['Leon', 'Jade', 'Sawyer', 'Mia', 'Anya', 'Sebastian', 'Morgan', 'Briana', 'Bailey', 'Bryelle']
ADULTS = COUSINS[5:]
KIDS = COUSINS[:5]

AND = ' y '
NUM_ERROR = 'No es un número. Inténtalo de nuevo'
STR_ERROR = '¡Error al procesar la entrada! Inténtalo de nuevo'
PERFECT = 'EN LA NARIZ!!!'
IN = 'en'
AFFIRM = 'sí'
PODDS = 'Ingrese las cuotas o probabilidad de que %s sea pastoreado.\nPara cuotas ingrese __ en __; para probabilidad ingrese _.__ : '
PUSER_OPTIONS = '¿le gustaría decidir cuántos primos tratarían de arrear \ny qué primos encontrarían las probabilidades de que realmente fueran arreados, (sí/no)? '
PADULTS_TO_PLAY = 'ingrese los adultos que jugarán, separados por un espacio: '
PADULTS_CAN_HERD = 'ingrese el número de adultos que el oso puede arrear a la vez: '
PKIDS_TO_PLAY = 'ingrese los niños que jugarán, separados por un espacio: '
PKIDS_CAN_HERD = 'ingrese el número de niños que Bear puede pastorear a la vez: '
PCOUSINS = 'ingrese los primos para comprobar las probabilidades de que hayan sido arreados, separados por un espacio: '

DADULTS_CAN_HERD = 'El número de adultos que Bear puede atrapar es'
DADULTS_TO_PLAY = 'y los objetivos adultos son '
DKIDS_CAN_HERD = 'El número de niños que Bear puede atrapar es'
DKIDS_TO_PLAY = 'y los objetivos de los niños son'
DCHECK_ODDS = 'Vamos a comprobar las probabilidades de que %s sea arreado por Bear'

DQADULTS_SETS = 'subconjuntos de adultos consultados: '
DADULTS_SETS = 'conjuntos adultos: '
DQKIDS_SETS = 'subconjuntos de niños consultados: '
DKIDS_SETS = 'conjuntos de niños: '
DQCOMBINED_SETS = 'subconjuntos consultados combinados: '
DCOMINED_SETS = 'conjuntos combinados: '

CONGRATS = '¡Lo hiciste!'
TOO_BAD = 'No del todo'
RESULTS_ODDS = 'las probabilidades eran'
RESULTS_PROB = 'o una probabilidad de'
SETS = 'conjuntos'
HERDED = 'rebaño'
CONTINUE = '¿Te gustaría otra oportunidad, (s/n)?: '