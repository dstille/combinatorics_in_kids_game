from permutations import Permutations, PermValue

def frame_build_step(vals, groups):
    permuted, remaining = next(vals)
    num_permuted, num_remaining = permuted.size, groups.k-permuted.size
    out = f'permuted = {permuted}, remaining = {remaining}  number permuted = {num_permuted}, number yet to permute = {num_remaining}'
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