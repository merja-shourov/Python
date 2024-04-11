
my_dict = {
    "a": 2,
    "b": 20,
    "c": 5,
    "d": 3,
    "e": 5,
    "f": 3   
}

free_dict = {}
for val in my_dict.values():
    if val in free_dict:
        free_dict[val] += 1
    else:
        free_dict[val] = 1
    
print(free_dict)
