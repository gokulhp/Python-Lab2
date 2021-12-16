from itertools import permutations


x =  (''.join(p) for p in permutations('aeiou'))

print(list(x))






