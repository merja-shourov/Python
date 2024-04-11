
# str = "Hello, World"
str = "Excellent"

free_dict = {}
for char in str.lower():
    if char.isalpha():
        if char not in free_dict:
            free_dict[char] = 1
        else:
            free_dict[char] += 1

print(free_dict)

    