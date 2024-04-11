
n_list = [ ["Danish Rich", 20], ["Stroustrup",56 ], ["linux", 45]]

dict = {}

for item in n_list:
    key = item[0]
    val = item[1]
    dict[key] = val

print(dict)