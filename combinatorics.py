class Combinatorics:
    def __init__(self, sets):
        self.sets = sets

    def add_sets(self, set1, set2):
        return self.eliminate_duplicates([(*s1, *s2) for s2 in set2 for s1 in set1])

    def format_as_sets(sets_in):
        return ', '.join(['{' + ', '.join(s) + '}' for s in sets_in])

    def flatten(self, lists):
        def down_1d(outer_l):
            return [elem for inner_l in outer_l for elem in inner_l]
        while type(lists[0][0]) == list:
            lists = down_1d(lists) 
        return lists
    
    def counts(self, sub, lists: list):
        return sum(set(sub).issubset(set(l)) for l in lists)

    def odds(self, event, poss_outcomes):
            event_ct = self.counts(event, poss_outcomes)
            size_outcomes = len(poss_outcomes)
            return event_ct, size_outcomes
    
    def save(self, fname, contents):
        with open(fname, 'w') as f:
            f.write(contents)

    def __str__(self) -> str:
        return Combinatorics.format_as_sets(self.sets)
    
class Combinations(Combinatorics):
    def __init__(self, elements, k):
        self.combos = self.choose(elements, k)
        super().__init__(self.combos)

    def pascal(self, x, row = [1], n = 1):
        return [row] + self.pascal(x, [1 if k == 0 or n == k else row[k-1] + row[k] for k in range(n+1)], n+1) if n < x else [row]
       
    def choose_r(self, set_in, k, combos = []):
        return [self.choose_r(set_in[idx+1:], k-1, combos + [elem]) for idx, elem in enumerate(set_in)] if k>0 else combos
    
    def choose(self, set_in: list, k: int):
        set_in.sort()
        combos = self.choose_r(set_in, k)   
        return self.flatten(combos)


    
class Permutations(Combinatorics):
    def __init__(self, elements, k):
        self.permutations = self.permute(elements, k)
        super().__init__(self.permutations)

    def permute_r(self, set_in, k, combos = []):
        return [self.permute_r(self.remove_at_idx(set_in, idx), k-1, combos + [elem]) for idx, elem in enumerate(set_in)] if k>0 else combos

    def remove_at_idx(self, list_in, idx):
        return list_in[:idx] if idx+1 >= len(list_in) else list_in[:idx] + list_in[idx+1:] 

    def permute(self, set_in: list, k: int):
        permutations = self.permute_r(set_in, k)   
        return self.flatten(permutations)

    def eliminate_duplicates(self, sets_in):
            return [sorted(s) for s in frozenset(frozenset(sorted(set)) for set in sets_in)]

        
COUSINS = ['Leon', 'Jade', 'Sawyer', 'Mia', 'Anya', 'Sebastian', 'Morgan', 'Briana', 'Bailey', 'Bryelle']
ADULTS = COUSINS[5:]
KIDS = COUSINS[:5]
p = Permutations(KIDS, 3)
print(p)
print(p.eliminate_duplicates(p.permutations))


