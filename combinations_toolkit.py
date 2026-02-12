def save(fname, contents):
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(contents)

def get_combos_formatted(elements, k):
    return format_as_set(choose(elements, k))        

def format_as_set(iterables):
    return '{\n' + ',\n'.join([' {' + ', '.join(itr) + '}' for itr in iterables]) + '\n}'        

def flatten(lists):
    def down_1d(outer_l):
        return [elem for inner_l in outer_l for elem in inner_l]
    while type(lists[0][0]) == list:
        lists = down_1d(lists) 
    return lists        

def choose_r(elements, k, combos = []):
    return [choose_r(elements[idx+1:], k-1, combos + [elem]) for idx, elem in enumerate(elements)] if k>0 else combos        

def choose_orig(elements: list, k: int):
    combos = choose_r(elements, k)   
    return flatten(combos)

def choose(elements, k, nth=0, set=[], combos=[]):
    if nth == k:
        combos.append(set)
    else:      
        for idx, elem in enumerate(elements):
            choose(elements[idx+1:], k, nth+1, set+[elem], combos)
        return combos   



if __name__ == '__main__':
    elements = ['a','b','c','d','e','f', 'g']
    print(choose(elements, 5))
