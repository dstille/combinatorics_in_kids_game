STORY = '''
It turns out that Bear, Leon and Jade's dog, is a herding dog. 
That means that his breed has developed skills to herd animals like sheep.
Bear is excited to see how good of a herder he is and is going to try out his skills out on the Cousins.
The Cousins are divided into two groups: the Adults and the Kids.
The Adults: Sebastian, Brianna, Bailey, Morgan, Bryelle
The Kids: Anya, Leon, Sawyer, Jade, Mia

Bear can pick off and herd a certain number of Adults and a certain number of Kids.

Your job is to figure out the odds of a Cousin or set of Cousins getting herded.
Not all Cousins may participate.
'''
STORY2 = '''
It's a Stille Family Reunion at Uncle Pete's house and a reunion for the Stille Family Pets as well.
It turns out that Bear, Leon and Jade's dog, is a herding dog. 
That means that his breed has developed skills to herd animals like sheep.
We're counting on Bear to round up his pet cousins for family photos
  and the pets over at Uncle Pete's house are \n  %s.
Some of the pets are inside and some of the pets are outside.
We are going to see if we can get Bear to round up a subset of the ones outside.  
'''
ALLPLAYERS = ['Leon', 'Jade', 'Sawyer', 'Mia', 'Anya', 'Sebastian', 'Morgan', 'Briana', 'Bailey', 'Bryelle']
APLAYERS = ALLPLAYERS[5:]
BPLAYERS = ALLPLAYERS[:5]

PETS = ['Bentley', 'Winnie', 'Luna', 'Obie', 'Mocha', 'Willow', 'Rex']

AND = ' and '
NUM_ERROR = 'Not a number. Please try again'
STR_ERROR = 'Error processing input! Please try again'
PERFECT = 'ON THE NOSE!!!'
IN = 'in'
AFFIRM = 'yes'
PROMPT_ODDS = 'Enter the odds or probability that %s will be herded.\nFor odds enter __ in __ ; for probability enter _.__ : '
PROMPT_USER_OPTIONS = 'would you like to decide how many cousins to try herding \nand which cousins to finds the odds that they actually got herded, (y/n)? '
PROMPT_APLAYERS_TO_PLAY = 'enter the adults that will play, separated by a space: '
PROMPT_APLAYERS_NUM = 'enter the number of adults Bear can herd at once: '
PROMPT_BPLAYERS_TO_PLAY = 'enter the kids that will play, separated by a space: '
PROMPT_BPLAYERS_NUM = 'enter the number of kids Bear can herd at once: '
PROMPT_PLAYERS_TO_CHECK_ODDS_FOR = 'enter the cousins to check the odds that they got herded, separated by a space: '

DISPLAY_APLAYERS_NUM_CHOSEN = 'The number of adults who Bear can catch is'
DISPLAY_APLAYERS = 'and the adult targets are '
DISPLAY_BPLAYERS_NUM_CHOSEN = 'The number of kids who Bear can catch is'
DISPLAY_BPLAYERS = 'and the kid targets are'
DISPLAY_PLAYERS_TO_CHECK_ODDS_FOR = 'We are going to check the odds that %s get herded by Bear\n'

SIZE_EXPLANATION = 'we start with %s and so far we haven chosen %s\nfrom %s we need to choose the remaining %s'
SIZE_HINT = 'if we can choose %s from %s, how many sets can we make by combining with %s'
DISPLAY_QUERIED_ASETS= 'queried adults subsets:   '
DISPLAY_ASETS = 'adult sets:               '
DISPLAY_QUERIED_BSETS = 'queried kids subsets:     '
DISPLAY_BSETS = 'kid sets:                 '
DISPLAY_QUERIED_COMBINED_SETS = 'combined queried subsets:  '
DISPLAY_COMINED_SETS = 'combined sets:'

PDISPLAY_PLAYERS_NUM_CHOSEN = 'The number of pets who Bear can catch is'
PDISPLAY_PLAYERS = 'and out in the yard are '
PDISPLAY_PLAYERS_TO_CHECK_ODDS_FOR = 'Bear has seen a Wanted poster for %s with a Reward of a Milkbone.\nWe are going to figure out the odds that Bear gets that reward.'

PDISPLAY_QUERIED_SETS= 'queried subsets:   '
PDISPLAY_SETS = 'sets of pets:      '




CONGRATS = 'You did it!!!'
TOO_BAD = 'Not quite'
RESULTS_ODDS = 'the odds were'
RESULTS_PROB = 'or a probability of'
SETS = 'sets'
CONTINUE = 'Would you like another go, (y/n)?: '