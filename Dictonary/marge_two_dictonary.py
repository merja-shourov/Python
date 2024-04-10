my_dict1 = {"a": 1, "b": 2, "c": 3}
my_dict2 = {"c": 4, "d": 6, "e": 8}


# # method-1
# final_dict = my_dict1 | my_dict2
# print(final_dict)

# #second method
# final_dict = { **my_dict1, **my_dict2}
# print(final_dict)

# Method-3
final_dict = dict()
final_dict.update(my_dict1)
final_dict.update(my_dict2)
print(final_dict)