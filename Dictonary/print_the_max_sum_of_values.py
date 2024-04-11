my_dict = {
	"a": [1, 2, 3],
	"b": [4, 0, -4],
	"c": [3, 5, 9],
	"d": [45, 12, 100]
}

max_sum = None
for val in my_dict.values():
    max_sum = max(max_sum, sum(val))

print(max_sum)