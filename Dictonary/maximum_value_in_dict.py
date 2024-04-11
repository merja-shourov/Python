your_dict   = {"a": 10, "b": 3, "c": 7}
my_dict = {}

# max = 0
# for val in your_dict.values():
#     if max < val:
#         max = val
    
# if( max == 0 ):
#     print("none")
# else:
#     print(max)




# # sorted methon
# if your_dict:
#     max_val  = max(set(your_dict.values()))
#     print(max_val)
# else:
#     print("None")


if my_dict:
    max_val = max(list(my_dict.values()))
    print(max_val)
else:
    print("None")