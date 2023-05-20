STORY = """
Acontece que Bear, o cachorro de Leon e Jade, é um cão pastor.
Isso significa que sua raça desenvolveu habilidades para pastorear animais como ovelhas.
Bear está animado para ver o quão bom pastor ele é e vai testar suas habilidades nos Primos.
Os Primos estão divididos em dois grupos: os Adultos e os Miúdos.
Os adultos: Sebastian, Brianna, Bailey, Morgan, Bryelle
As crianças: Anya, Leon, Sawyer, Jade, Mia

O urso pode apanhar e pastorear um certo número de adultos e um certo número de crianças.

Seu trabalho é descobrir as chances de um primo ou conjunto de primos serem pastoreados.
Nem todos os Primos podem participar.
"""
ALLPLAYERS = ['Leon', 'Jade', 'Sawyer', 'Mia', 'Anya', 'Sebastian', 'Morgan', 'Briana', 'Bailey', 'Bryelle']
APLAYERS = ALLPLAYERS[5:]
BPLAYERS = ALLPLAYERS[:5]

AND = ' e '
NUM_ERROR = 'Não é um número. Por favor, tente novamente'
STR_ERROR = 'Erro ao processar entrada! Por favor, tente novamente'
PERFECT = 'NO NARIZ!!!'
IN = 'em'
AFFIRM = 'sim'
PROMPT_ODDS = 'Digite as probabilidades ou probabilidade de que %s será pastoreado.\nPara probabilidades, insira __ em __ ; para probabilidade digite _.__ : '
PROMPT_USER_OPTIONS = 'você gostaria de decidir quantos primos tentar pastorear \ne quais primos encontrar as chances de que eles realmente foram pastoreados, (s/n)? '
PROMPT_APLAYERS_TO_PLAY = 'insira os adultos que irão jogar, separados por um espaço: '
PROMPT_APLAYERS_NUM = 'digite o número de adultos que o Urso pode reunir de uma vez: '
PROMPT_BPLAYERS_TO_PLAY = 'insira as crianças que irão brincar, separadas por um espaço: '
PROMPT_BPLAYERS_NUM = 'insira o número de cabritos que o Urso pode reunir de uma vez: '
PROMPT_PLAYERS_TO_CHECK_ODDS_FOR = 'digite os primos para verificar as probabilidades de terem sido pastoreados, separados por um espaço: '

DISPLAY_APLAYERS_NUM_CHOSEN = 'O número de adultos que o urso pode pegar é'
DISPLAY_APLAYERS = 'e os alvos adultos são '
DISPLAY_BPLAYERS_NUM_CHOSEN = 'O número de crianças que o Urso pode pegar é'
DISPLAY_BPLAYERS = 'e os alvos infantis são'
DISPLAY_PLAYERS_TO_CHECK_ODDS_FOR = 'Vamos verificar as chances de %s ser pastoreado pelo Urso'

DISPLAY_QUERIED_ASETS= 'subconjuntos adultos consultados: '
DISPLAY_ASETS = 'conjuntos adultos: '
DISPLAY_QUERIED_BSETS = 'subconjuntos infantis consultados: '
DISPLAY_BSETS = 'conjuntos infantis: '
DISPLAY_QUERIED_COMBINED_SETS = 'subconjuntos consultados combinados: '
DISPLAY_COMINED_SETS = 'conjuntos combinados: '

CONGRATSS = 'Você conseguiu!!!'
TOO_BAD = 'Não é bem assim'
RESULTS_ODDS = 'as probabilidades eram'
RESULTS_PROB = 'ou uma probabilidade de'
SETS = 'conjuntos'
CONTINUE = 'Gostaria de tentar outra vez, (s/n)?: '