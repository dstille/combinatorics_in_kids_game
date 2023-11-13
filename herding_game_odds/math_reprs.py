class Fraction:
    def __init__(self, *args) -> None:
        self.numer, self.denom = self.parseargs(args)

    def parseargs(self, args):
        if type(args[0]) == str:
            return args[0].split('/')
        return (args[0].counts, args[0].sizesample) if type(args[0]) == Odds else args 

    def reduce(self):
        numer_factors = Factors(self.numer).elements
        print(numer_factors)
        denom_factors = Factors(self.denom).elements
        print(denom_factors)
        numer_copy = numer_factors[::1]
        for f in numer_copy:
            if f in denom_factors:
                numer_factors.remove(f)
                print(numer_factors)
                denom_factors.remove(f)
                print(denom_factors)
        return Fraction(Product(numer_factors).value, Product(denom_factors).value)
        
    def __eq__(self, obj):
        return self.numer == obj.numer and self.denom == obj.denom

    def __mul__(self, fract2):
        return f'{self} * {fract2} = {Fraction(self.numer * fract2.numer, self.denom * fract2.denom)}'

    def __repr__(self) -> str:
        return f'{int(self.numer)} / {int(self.denom)}' 
    
    def __str__(self) -> str:
        return f'{self.numer} / {self.denom}'

class Product:
    def __init__(self, elements):
        self.value = self.get_product(elements)

    def get_product(self, elements):
        return elements[0] * self.get_product(elements[1:]) if elements else 1  

class Factors:
    def __init__(self, number):
        self.elements = self.get_prime_factors(number)

    def get_prime_factors(self, number):
        if self.is_prime(numbers):
            return [1, number]
        factors = []
        for fac in range(2, int(num**.5)):
            quot, rem = divmod()
            if rem == 0:
                while True:
                    nquot, nrem = qu

        

    def is_prime(self, num):
        for fac in range(2, int(num**.5)):
            if num % fac == 0:
                return False
        return True                           
    

class Odds:
    def __init__(self, event, sets) -> None:
        self.omega = sets
        self.event = event
        self.counts, self.sizesample = self.get_odds()

    def get_odds(self):
        return sum(set(self.event).issubset(set(sup)) for sup in self.omega), len(self.omega)

    def __eq__(self, __value: object) -> bool:
        return type(__value) == tuple and self.counts == __value[0] and self.sizesample == __value[1]

    def __str__(self) -> str:
        return f'{self.counts} in {self.sizesample}'    
    
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
    
    def __mul__(self, fac2):
        return f'{self.n}!{fac2.n}!' if type(fac2) == Factorial else  f'{self.n}!{fac2}'
    
    def __truediv__(self, fac2):
        return f'{self.n}! / {fac2.n}!' if type(fac2) == Factorial else f'{self.n}! / {fac2}'
    
    def reversed(self):
        return str(self)[::-1]
    
    def __repr__(self) -> str:
        return str(self.value)

    def __str__(self) -> str:
        return '*'.join(str(n) for n in range(self.n, 0, -1))

