def choose_r(set_in, k, combos = []):
    return [choose_r(set_in[idx+1:], k-1, combos + [elem]) for idx, elem in enumerate(set_in)] if k>0 else combos

def permute_r(set_in, k, combos = []):
    return [permute_r(remove_at_idx(set_in, idx), k-1, combos + [elem]) for idx, elem in enumerate(set_in)] if k>0 else combos

def remove_at_idx(list_in, idx):
    return list_in[:idx] if idx+1 >= len(list_in) else list_in[:idx] + list_in[idx+1:] 

def pascal(x, row = [1], n = 1):
    return [row] + pascal(x, [1 if k == 0 or n == k else row[k-1] + row[k] for k in range(n+1)], n+1) if n < x else [row]

def add_sets(set1, set2):
    return eliminate_duplicates([(*s1, *s2) for s2 in set2 for s1 in set1])

def format_as_set(iterables):
    return ', '.join(['{' + ', '.join(itr) + '}' for itr in iterables])

def flatten(lists):
    def down_1d(outer_l):
        return [elem for inner_l in outer_l for elem in inner_l]
    while type(lists[0][0]) == list:
        lists = down_1d(lists) 
    return lists

def save(fname, contents):
    with open(fname, 'w') as f:
        f.write(contents)

def choose(set_in: list, k: int):
    set_in.sort()
    combos = choose_r(set_in, k)   
    return flatten(combos)

def permute(set_in: list, k: int):
    set_in.sort()
    permutations = permute_r(set_in, k)   
    return flatten(permutations)

def counts(sub, super):
    return sum(set(sub).issubset(set(sup)) for sup in super)

def odds(event, poss_outcomes):
    event_ct = counts(event, poss_outcomes)
    size_outcomes = len(poss_outcomes)
    return event_ct, size_outcomes

def eliminate_duplicates(sets_in):
    return [sorted(s) for s in frozenset(frozenset(sorted(set)) for set in sets_in)]

def format_combos(n, k):
    return f'C({n},{k})'

def format_prob(n1, k1, n2, k2):
    return f'{format_combos(n2, k2)} / {format_combos(n1, k1)}'

def factorial(x):
    return x * factorial(x-1) if x>1 else 1

def C(n, k):
    return factorial(n) // (factorial(n-k)*factorial(k))

def p(event, size):
    return event/size

# after much labor, it gets the dimensions right
def choose_alt(elements, k, nth=0, set=[], combos=[]):
    if nth == k:
        combos.append(set)
    else:      
        for idx, elem in enumerate(elements):
            choose_alt(elements[idx+1:], k, nth+1, set+[elem], combos)
        return combos   