class Combinatorics:
    def __init__(self, sets, elements):
        self.sets = sets
        self.elements = elements
        self.as_iter = iter(self.sets)

    @classmethod
    def add_sets(cls, set1, set2):
        return [(*s1, *s2) for s2 in set2 for s1 in set1]

    @staticmethod
    def format_as_sets(sets_in):
        return ', '.join(['{' + ', '.join(s) + '}' for s in sets_in]) if sets_in else '{}'

    def flatten(self, lists):
        def down_1d(outer_l):
            return [elem for inner_l in outer_l for elem in inner_l]
        while lists and type(lists[0][0]) == list:
            lists = down_1d(lists) 
        return lists
    
    def counts(self, subset, supersets):
        return sum(set(subset).issubset(set(sup)) for sup in supersets)
    
    def elems_in_sets(self, elems):
        return Combinatorics([s for s in self.sets if set(elems).issubset(set(s))], elems)

    def odds(self, event, poss_outcomes):
        return self.counts(event, poss_outcomes), len(poss_outcomes)

    def __str__(self) -> str:
        return Combinatorics.format_as_sets(self.sets)
    
class Combinations(Combinatorics):
    def __init__(self, elems, k):
        self.sets = self.choose(elems, k)
        self.elements = elems
        super().__init__(self.sets, self.elements)
        self.combo_value = ComboValue(len(self.elements), k)

    def pascal(self, x, row = [1], n = 1):
        return [row] + self.pascal(x, [1 if k == 0 or n == k else row[k-1] + row[k] for k in range(n+1)], n+1) if n < x else [row]
       
    def choose_r(self, set_in, k, combos = []):
        return [self.choose_r(set_in[idx+1:], k-1, combos + [elem]) for idx, elem in enumerate(set_in)] if k>0 else combos
    
    def choose(self, set_in: list, k: int):
        set_in.sort()
        combos = self.choose_r(set_in, k)   
        return self.flatten(combos)
    
class Odds(Combinatorics):
    def __init__(self, event, sets) -> None:
        self.omega = sets
        self.sizeomega = len(self.omega)
        self.event = event
        super().__init__(self.omega, event)
        self.counts, self.sizesample = self.odds(self.event, self.omega)

    def get_odds(self):
        return self.counts(self.event, self.omega), self.sizeomega

    def __eq__(self, __value: object) -> bool:
        return type(__value) == tuple and self.counts == __value[0] and self.sizesample == __value[1]

    def __str__(self) -> str:
        return f'{self.counts} in {self.sizesample}'    
    
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

class ComboValue:
    def __init__(self, n, k) -> None:
         self.n = n
         self.k = k
         self.value = self.C(n, k) if k >= 0 else 0
    
    def factorial(self, x):
        return x * self.factorial(x-1) if x>1 else 1

    def C(self, n, k):
        return self.factorial(n) // (self.factorial(n-k)*self.factorial(k))
    
    def as_factorials(self):
        return f'{self.n}! / {self.n -self.k}!{self.k}!'
    
    @staticmethod
    def as_formula():
        return 'C(n,k) = n! / (n-k)!k!'
    
    def __truediv__(self, obj):
        return self.value / obj.value if type(obj) == ComboValue else self.value / obj
    
    def __str__(self) -> str:
        return f'C({self.n},{self.k})'
    

    
class Prob:
    def __init__(self, subsize, supersize) -> None:
        self.subsize = subsize
        self.supersize = supersize
        self.value = self.subsize/self.supersize

    def __eq__(self, __value: object) -> bool:
        return self.value == __value if type(__value) == float else False
    
    def __mul__(self, obj):
        return self.value*obj.value if type(obj) == Prob else self.value*obj
    
    def __truediv__(self, obj):
        return self.value/obj.value if type(obj) == Prob else self.value/obj
    
    def __sub__(self, obj):
        return self.value - obj.value if type(obj) == Prob else self.value - obj

    def __str__(self) -> str:
        return f'{self.value:.2f}'
    
class Factorial:
    def __init__(self, n) -> None:
        self.n = n
        self.value = self.factorial(self.n)

    def factorial(self, n):
        return n * self.factorial(n-1) if n>1 else 1

    def __str__(self) -> str:
        return '*'.join(str(n) for n in range(self.n, 0, -1))
    
cv = ComboValue(5,2)
print(cv)