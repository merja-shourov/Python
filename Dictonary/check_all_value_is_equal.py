my_dict     = {} #{"a": 2, "b": 2, "c": 2}
your_dict   = {"a": 1, "b": 3, "c": 7}

# # Method-1:
# my_set = set()
# for val in my_dict.values():
#     my_set.add(val)

# if len(my_set) == 1:
#     print(True)
# elif len(my_set) == 0:
#     print("Empty")
# else:
#     print("False")

# Sortest Method

len_count = len(set(your_dict.values()))
if len_count == 0:
    print("Empty")
else:
    if len_count == 1:
        print(True)
    else:
        print("False")