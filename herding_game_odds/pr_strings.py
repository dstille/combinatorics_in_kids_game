STORY = """
Acontece que Bear, o cachorro de Leon e Jade, é um cão pastor.
Isso significa que sua raça desenvolveu habilidades para pastorear animais como ovelhas.
Bear fica animado ao ver o bom pastor que ele é e vai testar suas habilidades nos primos.
Os Primos são divididos em dois grupos: Adultos e Crianças.
Adultos: Sebastian, Brianna, Bailey, Morgan, Bryelle
Filhos: Anya, Leon, Sawyer, Jade, Mia

Bear pode pegar e pastorear um certo número de adultos e um certo número de crianças.

Seu trabalho é descobrir as probabilidades de que um primo ou um conjunto de primos serão agrupados.
Nem todos os primos podem participar.
"""
COUSINS = ['Leon', 'Jade', 'Sawyer', 'Mia', 'Anya', 'Sebastian', 'Morgan', 'Briana', 'Bailey', 'Bryelle']
ADULTS = COUSINS[5:]
KIDS = COUSINS[:5]

AND = ' e '
NUM_ERROR = 'Não é um número. Tenta de novo'
STR_ERROR = 'Erro ao processar entrada! Tenta de novo'
PERFECT = 'NO NARIZ!!!'
IN = 'em'
AFFIRM = 'sim'
PODDS = 'Digite as cotas ou a probabilidade de %s ser pastado.\nPara cotas digite __ em __; para probabilidade digite _.__ : '
PUSER_OPTIONS = 'você gostaria de decidir quantos primos tentariam pastorear \ne quais primos teriam chances de realmente serem pastoreados, (sim/não)? '
PADULTS_TO_PLAY = 'insira os adultos para jogar, separados por um espaço: '
PADULTS_CAN_HERD = 'insira o número de adultos que o urso pode reunir ao mesmo tempo: '
PKIDS_TO_PLAY = 'insira as crianças para brincar, separadas por um espaço: '
PKIDS_CAN_HERD = 'insira o número de crianças que o Urso pode reunir ao mesmo tempo: '
PCOUSINS = 'digite os primos para verificar as probabilidades de terem sido pastoreados, separados por um espaço: '

DADULTS_CAN_HERD = 'O número de adultos que o urso pode pegar é'
DADULTS_TO_PLAY = 'e os alvos adultos são '
DKIDS_CAN_HERD = 'O número de crianças que o Urso pode pegar é'
DKIDS_TO_PLAY = 'e os objetivos das crianças são'
DCHECK_ODDS = 'Vamos verificar as probabilidades de %s ser conduzido pelo Urso'

DQADULTS_SETS = 'subconjuntos adultos consultados: '
DADULTS_SETS = 'conjuntos adultos: '
DQKIDS_SETS = 'subconjuntos filhos consultados: '
DKIDS_SETS = 'conjuntos infantis: '
DQCOMBINED_SETS = 'subconjuntos consultados combinados: '
DCOMINED_SETS = 'conjuntos combinados: '

CONGRATS = 'Você conseguiu!'
TOO_BAD = 'Não é bem assim'
RESULTS_ODDS = 'probabilidades eram'
RESULTS_PROB = 'ou uma probabilidade de'
SETS = 'conjuntos'
HERDED = 'rebanho'
CONTINUE = 'Gostaria de outra chance, (s/n)?: '