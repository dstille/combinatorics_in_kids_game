from permutations import Permutations, PermValue
from combinatorics import SetRepr

story1 = 'Leon has a hook shot, a half court shot and a layup. If he can repeat shots, how many different shots can he make with 2 tries?'
story2 = 'What about with 3 tries?'
story3 = 'From %s, all %s are going to play a game of horse. How many different shooting orders can we come up with?'
story4 = 'This time %s is going to play too.  How many different shooting orders can we come up with? \nHint: how many different spots can %s be added to the existing lineups?'
story5 = 'From %s, only %s are going to play this time. We are going to figure out all the lineups\n and then draw straws to see who is not going to play. How many lineups will we have?' 

def scenario1(shots):
    print(story1)

def scenario2(shots):
    print(story2)

def scenario3(players):
    print(story3 % (SetRepr(players), 3))

def scenario4(players):
    print(story4 % (players[3], players[3]))

def scenario5(players):
    print(story5 % (SetRepr(players), 2))

def frame_build_step(vals, groups):
    permuted, remaining = next(vals)
    rem_display = f'remaining = {remaining},' if str(remaining) == '{}' else f'remaining = {remaining},  '
    num_permuted, num_remaining = permuted.size, groups.k-permuted.size
    out = f'permuted = {permuted}, {rem_display}number permuted = {num_permuted}, number yet to permute = {num_remaining}'
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

def display_values(groups):
    perm_value = PermValue(len(groups.elements), groups.k)
    print(perm_value)
    print(perm_value.as_factorials())
    print(perm_value.as_expanded_factorial())        

def display_math(groups):
    display_builds(groups)
    display_values(groups)