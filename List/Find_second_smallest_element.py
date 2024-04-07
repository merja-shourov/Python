arr = [1, 22, 5, 11, 11, 3]
unique_arr = list(set(arr)) #set automatic sort this

unique_arr.sort(reverse=True)

print(unique_arr)

print(f"Second smallest value is - {unique_arr[1]}")

# option-2

max_element = max(unique_arr)
unique_arr.remove(max_element)
second_max = max(unique_arr)
print("Second Max Element: ", second_max)