def choose_r(set_in, k, combos = []):
    return [choose_r(set_in[idx+1:], k-1, combos + [elem]) for idx, elem in enumerate(set_in)] if k>0 else combos

def flatten(lists):
    def down_1d(outer_l):
        return [elem for inner_l in outer_l for elem in inner_l]
    while type(lists[0][0]) == list:
        lists = down_1d(lists) 
    return lists

def choose(set_in: list, k: int):
    set_in.sort()
    combos = choose_r(set_in, k)   
    return flatten(combos)

def print_sets(itr_outer):
    while True:
        try:
            print(next(itr_outer))
        except StopIteration:
            print_sets(next(itr_outer))

COUSINS = ['Leon', 'Jade', 'Sawyer', 'Mia', 'Anya', 'Sebastian', 'Morgan', 'Briana', 'Bailey', 'Bryelle']
ADULTS = COUSINS[5:]
KIDS = COUSINS[:5]
sets = choose(ADULTS, 3)
print(sets)
itr_outer = iter(sets)
print_sets(itr_outer)