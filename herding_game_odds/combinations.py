from combinatorics import Combinatorics

class Combinations(Combinatorics):
    def __init__(self, elems, k):
        sets = self.choose(elems, k)
        self.elements = elems
        super().__init__(sets, self.elements)
        self.combo_value = ComboValue(len(self.elements), k)

    def pascal(self, x, row = [1], n = 1):
        return [row] + self.pascal(x, [1 if k == 0 or n == k else row[k-1] + row[k] for k in range(n+1)], n+1) if n < x else [row]
       
    def choose_r(self, set_in, k, combos = []):
        return [self.choose_r(set_in[idx+1:], k-1, combos + [elem]) for idx, elem in enumerate(set_in)] if k>0 else combos
    
    def choose(self, set_in: list, k: int):
        set_in.sort()
        combos = self.choose_r(set_in, k)   
        return self.flatten(combos)
    
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