# =================
# Option 1
# =================

my_list = [1, 11, 30, 2, 2, 3]
count = 0

for elem in my_list:
	if elem > 3:
		count += 1

print(count)

# =================
# Option 2
# =================

count = sum(1 for elem in my_list if elem > 3)


print(count)

