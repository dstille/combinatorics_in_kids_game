from combinatorics import Sets, Combinatorics, SetRepr

class Permutations(Combinatorics):
    def __init__(self, elements, k):
        self.k = k
        self.permutations = self.permute(elements, k)
        self.size = len(self.permutations)
        super().__init__(self.permutations, elements)
        self.as_iter = iter(self.permute_r(elements, k))

    def permute_r(self, set_in, k, combos = []):
        return [self.permute_r(self.remove_at_idx(set_in, idx), k-1, combos + [elem]) for idx, elem in enumerate(set_in)] if k>0 else combos

    def remove_at_idx(self, list_in, idx):
        return list_in[:idx] if idx+1 >= len(list_in) else list_in[:idx] + list_in[idx+1:] 

    def permute(self, set_in: list, k: int):
        permutations = self.permute_r(set_in, k)   
        return self.flatten(permutations)
    
    def get_build_as_dict(self):
        build = PermBuild(self.elements, self.k)
        return build.get_build_as_dict()

class PermBuild(Permutations):
    def __init__(self, elements, k):
        self.elements = elements
        self.k = k
        self.perms = [Permutations(elements, k1) for k1 in range(1, k+1)]

    def get_build_as_dict(self) -> dict:
        d = {}
        self.first_elem_as_key(d)
        self.sort_elems(d)
        self.steps_as_generator(d)
        return d
    
    def first_elem_as_key(self, d: dict):
        for outer in self.perms:
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
            d[ky] = ((SetRepr(v), SetRepr(self.difference(v, self.elements))) for v in vals)

class PermValue:
    def __init__(self, n, k) -> None:
         self.n = n
         self.k = k
         self.value = self.P() if k >= 0 else 0
    
    def factorial(self, x):
        return x * self.factorial(x-1) if x>1 else 1

    def P(self):
        return self.factorial(self.n) // self.factorial(self.k)
    
    def as_factorials(self):
        return f'{self.n}! / ({self.n}-{self.k})!'
    
    def as_expanded_factorial(self):
        numerator = '*'.join([str(i) for i in range(self.n, 0, -1)])
        denominator = '*'.join([str(i) for i in range(self.n - self.k, 1, -1)] + ['1'])
        return f'{numerator} / {denominator}'

    
    @staticmethod
    def as_formula():
        return 'P(n,k) = n! / n-k!'
    
    def __truediv__(self, obj):
        return self.value / obj.value if type(obj) == PermValue else self.value / obj
    
    def __str__(self) -> str:
        return f'P({self.n},{self.k})'
    

