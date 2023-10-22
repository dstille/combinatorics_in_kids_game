def to_binary(n):
    return n%2 + 10*to_binary(n//2) if n>0 else 0


print(to_binary(10))

'''
n = 10
sum = 0
while n>0:
'''
