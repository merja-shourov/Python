import itertools
my_list = [1, 2, 3]

# permutations = list(itertools.permutations(my_list))

for permu in itertools.permutations(my_list):
    print(permu)