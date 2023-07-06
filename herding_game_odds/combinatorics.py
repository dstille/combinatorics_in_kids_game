class Sets:
    def __init__(self, sets) -> None:
        self.sets = sets
        self.size = len(sets)
        self.sets_representations = [repr(SetRepr(set)) for set in self.sets]

    @classmethod
    def add_sets(cls, set1, set2):
        return [(*s1, *s2) for s2 in set2 for s1 in set1]

    @staticmethod
    def format_as_sets(sets_in):
        return ', '.join(sets_in) if sets_in else '{}'
    
    def counts(self, subset, supersets):
        return sum(set(subset).issubset(set(sup)) for sup in supersets)
    
    def elems_in_sets(self, elems):
        return Combinatorics([s for s in self.sets if set(elems).issubset(set(s))], elems)
    
    def difference(self, sub, super):
        return [elem for elem in super if elem not in sub]
    
    def __str__(self) -> str:
        return Sets.format_as_sets(self.sets_representations)
    
class Combinatorics(Sets):
    def __init__(self, sets, elements):
        super().__init__(sets)
        self.elements = elements
        self.as_iter = iter(self.sets)

    def flatten(self, lists):
        def down_1d(outer_l):
            return [elem for inner_l in outer_l for elem in inner_l]
        while lists and lists[0] and type(lists[0][0]) == list:
            lists = down_1d(lists) 
        return lists
    
    def factorial(self, n):
        return self.factorial(n-1) * n if n > 1 else 1
    
class Odds(Combinatorics):
    def __init__(self, event, sets) -> None:
        self.omega = sets
        self.sizeomega = len(self.omega)
        self.event = event
        self.counts, self.sizesample = self.get_odds()

    def get_odds(self):
        return self.counts(self.event, self.omega), self.sizeomega

    def __eq__(self, __value: object) -> bool:
        return type(__value) == tuple and self.counts == __value[0] and self.sizesample == __value[1]

    def __str__(self) -> str:
        return f'{self.counts} in {self.sizesample}'    
    
class SetRepr:
    def __init__(self, set) -> None:
        self.set = set
        self.size = len(self.set)

    @staticmethod
    def format_as_set(set_in):
        return '{' + ', '.join([elem for elem in set_in]) + '}' if set_in else '{}'
    
    def __str__(self) -> str:
        return SetRepr.format_as_set(self.set)
    
    def __repr__(self) -> str:
        return SetRepr.format_as_set(self.set)

    
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


    