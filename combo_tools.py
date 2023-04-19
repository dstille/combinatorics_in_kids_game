def choose_r(set_in, k, combos = []):
    return [choose_r(set_in[idx+1:], k-1, combos + [elem]) for idx, elem in enumerate(set_in)] if k>0 else combos
 
def pascal(x, row = [1], n = 1):
    return [row] + pascal(x, [1 if k == 0 or n == k else row[k-1] + row[k] for k in range(n+1)], n+1) if n < x else [row]

def add_sets(set1, set2):
    return [(*s1, *s2) for s2 in set2 for s1 in set1]

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
    combos = choose_r(set_in, k)   
    return flatten(combos)

def counts(sub, lists: list):
    return sum(set(sub).issubset(set(l)) for l in lists)

def odds(event, poss_outcomes):
    event_ct = counts(event, poss_outcomes)
    size_outcomes = len(poss_outcomes)
    return event_ct, size_outcomes

        

