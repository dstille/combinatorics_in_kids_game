import itertools
from timeit import default_timer as timer

elements = ('a', 'b', 'c', 'd', 'e', 'f')
k = 3

start = timer()
combinations = list(itertools.combinations(elements, k))
end = timer()

print("Approach 1 (itertools.combinations) - Time taken: {:.6f} seconds".format(end - start))

def combinations_recursive(elements, k):
    if k == 0:
        return [[]]
    
    if not elements:
        return []
    
    first, rest = elements[0], elements[1:]
    
    combinations_without_first = combinations_recursive(rest, k)
    combinations_with_first = [[first] + rest_com for rest_com in combinations_without_first]
    
    return combinations_without_first + combinations_with_first

start = timer()
combinations = combinations_recursive(elements, k)
end = timer()

print("Approach 2 (Recursive Function) - Time taken: {:.6f} seconds".format(end - start))

def combinations_bitwise(elements, k):
    n = len(elements)
    result = []
    
    for i in range(2 ** n):
        if bin(i).count('1') == k:
            new_combination = [elements[j] for j in range(n) if i & (1 << j)]
            result.append(new_combination)
    
    return result

start = timer()
combinations = combinations_bitwise(elements, k)
end = timer()

print("Approach 3 (Bit Manipulation) - Time taken: {:.6f} seconds".format(end - start))

def choose(elements, k, nth=0, set=[], combos=[]):
    if nth == k:
        combos += set
    else:      
        for idx, elem in enumerate(elements):
            choose(elements[idx+1:], k, nth+1, set+[elem], combos)
        return combos 

start = timer()
combinations = dan_recursive(elements, k)
end = timer()

print("Approach 4 (Dan-recursive) - Time taken: {:.6f} seconds".format(end - start)) 

def flatten(lists):
    def down_1d(outer_l):
        return [elem for inner_l in outer_l for elem in inner_l]
    while type(lists[0][0]) == list:
        lists = down_1d(lists) 
    return lists        

def choose_r(elements, k, combos = []):
    return [choose_r(elements[idx+1:], k-1, combos + [elem]) for idx, elem in enumerate(elements)] if k>0 else combos        

def dan_recursive_resize(elements: list, k: int):
    combos = choose_r(elements, k)   
    return flatten(combos)


start = timer()
combinations = dan_recursive_resize(elements, k)
end = timer()

print("Approach 5 (Dan-recursive with resizing) - Time taken: {:.6f} seconds".format(end - start)) 


