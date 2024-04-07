num = [1, 3, 4, 6, 10, 3, 1, 4 ]

match = 1

if len(num) == 0:
    print("Empty List")
elif match not in num:
    print("Dont find")
else:
    for i in num:
        if i == match:
            num.remove(i)
    print(num)