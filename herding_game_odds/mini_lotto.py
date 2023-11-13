from permutations import PermBuild, Permutations
from combinatorics import Set
from combinations import ComboBuild, Combinations, ComboBuild2
from math_reprs import *
from copy import deepcopy

story = '''
Your Uncle Dan wants to run an unlicensed gambling game and he has three games he can offer:
 (a) numbers -- pick a number between 0 and 99
 (b) mini-lotto version 1 -- choose 2 numbers from 0 to 9 (can choose a number only once for any given ticket
            and order matters)
 (c) mini-lotto version 2 -- choose 2 numbers from 0 to 9 (can choose a number only once for any given ticket
            and order doesn't matter)

 Each try costs a dollar and the prize is $75. Just in case there is more than one winning
            ticket, the prize is split evenly. Which game should Uncle Dan offer to make the most money?

            
 '''

def get_input(prompt, options = []):
    char = input(prompt)
    return char if True else get_input('Not an option. Please try again\n' + prompt, options)
    return char if char in [options] else get_input('Not an option. Please try again\n' + prompt, options)

def check_guess(guess, answer):
    return 'You got it!!!' if guess == answer else f'Not this time, the answer was {answer}'

def explain_math():
    print('**********   SIMULATION    ************')
    digits = [f'{n}' for n in range(10)]
    print('(a) DIFFERENT BAGS: drawing first number from one bag, and second number from another bag')
    for first_digit in range(10):
        second_digits = digits
        print(f'if the set is: {first_digit}, next number chosen from: {Set(second_digits)}')
    print()
    print('(b) ONE BAG, DRAW TWO SLIPS, ONE NUMBER: order matters')
    for first_digit in range(10):
        second_digits = remove_at_idx(digits, first_digit)
        print(f'if the set is: {first_digit}, next element chosen from: {Set(second_digits)}')
    print()
    print('(c) ONE BAG, DRAW TWO SLIPS, SEPARATE NUMBERS: order does not matter')
    groups = Combinations(digits, 2)
    #display_builds(groups)
    build = ComboBuild2(digits[:5], 3)
    dicts: list = build.get_build_as_dicts()
    for d in dicts:
        for combined, remaining in d.items():
            print(f'if the set is: {Set(combined)}, next number chosen from: {Set(remaining)}')
    print()
    guess = get_input('what is the difference is size between a and b? ')
    print(check_guess(Fraction(guess), Fraction('9/10')))
    guess = get_input('(c) is a fraction of the size of either (a) or (b), but which one? ')
    print(check_guess(guess, 'b'))
    guess = get_input('what is that fraction? ')
    print(check_guess(Fraction(guess), Fraction('1/2')))
    guess = get_input('(c) is missing some of the columns in (b). looking at (b), how would you describe that pattern? ')

def remove_at_idx(list_in, idx):
    copy = deepcopy(list_in)
    copy[idx] = '_'
    return copy

def frame_build_step(vals, groups):
    combined, remaining = next(vals)
    rem_display = f'remaining = {remaining},' if str(remaining) == '{}' else f'remaining = {remaining},  '
    num_combined, num_remaining = combined.size, groups.k-combined.size
    out = f'combined = {combined}, {rem_display}number combined = {num_combined}, number yet to combine = {num_remaining}'
    return out + '  +1' if num_remaining == 0 else out

def display_builds(groups):
    build = groups.get_build_as_dict()
    for ky, vals in build.items():
        print(f'if we start with {Set(ky)}:')
        try:
            while True:
                print(frame_build_step(vals, groups))
        except StopIteration:
            continue

def main():
    print(story)
    explain_math()    


if __name__ == '__main__':
    main()