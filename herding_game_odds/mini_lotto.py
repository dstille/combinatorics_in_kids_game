from permutations import PermBuild, Permutations
from combinatorics import Set
from combinations import ComboBuild, Combinations, ComboBuild2
from copy import deepcopy

story = '''
Your Uncle Dan wants to run an unlicensed gambling game and he has three games he can offer:
 (a) numbers -- pick a number between 0 and 99
 (b) mini-lotto version 1 -- choose 2 numbers from 0 to 9 (can choose a number only once for any given ticket
            and order matters)
 (c) mini-lotto version 2 -- choose 2 numbers from 0 to 9 (can choose a number only once for any given ticket
            and order doesn't matter)

 Each try costs a dollar and the prize is $95. Just in case there is more than one winning
            ticket, the prize is split evenly. Which game should Uncle Dan offer to make the most money?

            
 '''

def get_input(prompt, options):
    char = input(prompt)
    while True:
        char = input(prompt)
        if char in [options]:
            return char
        else:
            print('Not an option. Please try again')

def check_guess(guess, answer):
    return 'You got it!!!' if guess == answer else f'Not this time, the answer was {answer}'

def explain_math():
    print('**********   SIMULATION    ************')
    digits = [f'{n}' for n in range(10)]
    print('(a) DIFFERENT BAGS: drawing first number from one bag, and second number from another bag')
    for first_digit in range(10):
        second_digits = digits
        print(f'if first number is: {first_digit}, second number chosen from: {Set(second_digits)}')
    print()
    print('(b) ONE BAG, DRAW TWO SLIPS, ONE NUMBER: order matters')
    for first_digit in range(5):
        second_digits = remove_at_idx(digits, first_digit)
        print(f'if first number is: {first_digit}, second number chosen from: {Set(second_digits)}')
    print()
    print('(c) ONE BAG, DRAW TWO SLIPS, SEPARATE NUMBERS: order does not matter')
    groups = Combinations(digits, 3)
    display_builds(groups)
    build = ComboBuild2(digits, 3)
    dicts: list = build.get_build_as_dicts()
    print(dicts)
    for d in dicts:
        for combined, remaining in d.items():
            print(f'if we start with: {combined}, we can choose our next element from: {remaining}')
    print()
    print('what is the difference is size between a and b?')
    print('(a) is a fraction of the size of either (b) or (c), but which one?')
    print('what is that fraction?')
    print('(c) is missing some of the columns in (b). looking at (b), how would you describe that pattern?')

def remove_at_idx(list_in, idx):
    copy = deepcopy(list_in)
    copy[idx] = '{}'
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
        print(f'if we start with {ky}:')
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