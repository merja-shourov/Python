

list1 = [10, 20, 30, 40]
list2 = [10, 20,30, 40]

new_list = []

for i in list1:
    if i not in list2:
        new_list.append(i)

print(new_list)