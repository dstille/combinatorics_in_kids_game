from combinatorics import Combinatorics, Set

class Combinations(Combinatorics):
    def __init__(self, elements, k):
        sets = self.choose(elements, k)
        super().__init__(sets, elements)
        self.k = k
        self.combo_value = ComboValue(len(elements), k)

    def pascal(self, x, row = [1], n = 1):
        return [row] + self.pascal(x, [1 if k == 0 or n == k else row[k-1] + row[k] for k in range(n+1)], n+1) if n < x else [row]
       
    def choose_r(self, set_in, k, combos = []):
        return [self.choose_r(set_in[idx+1:], k-1, combos + [elem]) for idx, elem in enumerate(set_in)] if k>0 else combos
    
    def choose(self, set_in: list, k: int):
        set_in.sort()
        combos = self.choose_r(set_in, k)   
        return self.flatten(combos)
    
    def get_build_as_dict(self):
        build = ComboBuild(self.elements, self.k)
        return build.get_build_as_dict()
    
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
    
    def __repr__(self) -> str:
        return str(self.value)
    
    def __str__(self) -> str:
        return f'C({self.n},{self.k})'
    
class ComboBuild2(Combinations):
    def __init__(self, elements, k):
        super().__init__(elements, k)

    def get_build_as_dicts(self) -> dict:
        dicts = []
        for idx in range(self.k - 1):
            d = {}
            self.elems_as_key(d, idx)
            self.sort_elems(d)
            dicts += [d]
        return dicts
    
    def elems_as_key(self, d: dict, idx):
        for set in self.sets:
            combined = tuple(set[:idx+1])
            remaining = set[idx+1:]
            if combined in d:
                d[combined] += remaining
            else:
                d[combined] = remaining      

    def sort_elems(self, d: dict):
        for ky, vals in d.items():
            d[ky] = sorted(set(vals))

class ComboBuild(Combinations):
    def __init__(self, elements, k):
        self.elements = elements
        self.k = k
        self.combos = [Combinations(elements, k1) for k1 in range(1, k+1)]

    def get_build_as_dict(self) -> dict:
        d = {}
        self.first_elem_as_key(d)
        self.sort_elems(d)
        self.steps_as_generator(d)
        return d
    
    def first_elem_as_key(self, d: dict):
        for outer in self.combos:
            for inner in outer.sets:
                first_elem = inner[0]
                if first_elem in d:
                    d[first_elem] += [inner]
                else:
                    d[first_elem] = [first_elem]

    def sort_elems(self, d: dict):
        for ky, vals in d.items():
            d[ky] = [[vals[0]]] + (sorted(vals[1:]))

    def steps_as_generator(self, d: dict):
        for ky, vals in d.items():
            d[ky] = ((Set(v), Set([e for e in self.elements if e > v[-1]])) for v in vals)