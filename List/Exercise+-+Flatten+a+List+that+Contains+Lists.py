

my_list = [10, 22,  [1, 2, 3], [4, 5, 6], [7, 8, 9]]

plane_list = []

for i in my_list:
    if( isinstance(i, list )):
        plane_list.extend(i)
    else:
        plane_list.append(i)

print(plane_list)
# my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# flat_list = []

# for elem in my_list:
# 	if isinstance(elem, list):
# 		for nested_elem in elem:
# 			flat_list.append(nested_elem)
# 	else:
# 		flat_list.append(elem)

# print(flat_list)