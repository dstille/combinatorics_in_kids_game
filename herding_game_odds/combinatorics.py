class Set:
    def __init__(self, elems) -> None:
        self.elems = elems
        self.size = len(elems)

    def format_as_set(self):
        return '{' + ', '.join([elem for elem in self.elems]) + '}' if self.elems else '{}'
    
    def sort(self):
        return sorted(self.elems)

    def __str__(self) -> str:
        return self.format_as_set()
        
class Sets(Set):
    def __init__(self, sets, elements) -> None:
        self.sets = sets
        self.size = len(sets)
        self.elements = Set(elements)
        self.elements = elements

    @classmethod
    def add_sets(cls, set1, set2):
        return [(*s1, *s2) for s2 in set2 for s1 in set1]

    @staticmethod
    def format_as_sets(sets_in):
        return ', '.join(str(Set(s)) for s in sets_in) if sets_in else '{}'
    
    def counts(self, subset, supersets):
        return sum(set(subset).issubset(set(sup)) for sup in supersets)
    
    def elems_in_sets(self, elems):
        return Combinatorics([s for s in self.sets if set(elems).issubset(set(s))], elems)
    
    def difference(self, sub, super):
        return [elem for elem in super if elem not in sub]
    
    def __str__(self) -> str:
        return self.format_as_sets(self.sets)
    
class Combinatorics(Sets):
    def __init__(self, sets, elements):
        super().__init__(sets, elements)
        self.as_iter = iter(self.sets)

    def flatten(self, lists):
        def down_1d(outer_l):
            return [elem for inner_l in outer_l for elem in inner_l]
        while lists and lists[0] and type(lists[0][0]) == list:
            lists = down_1d(lists) 
        return lists