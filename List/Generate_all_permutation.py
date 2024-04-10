import itertools

lst = [1,2,3]
permutations  = list(itertools.permutations(lst))
print(permutations)
for permutation in permutations:
    print(permutation)