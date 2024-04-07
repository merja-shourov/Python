
color = ["red", "green", "blue", "orange"]
weight = [60, 30, 10, 3]
factor = 2

# #option-1
# for i in range(len(color)):
#     color[i] *= factor
# print(color)

# option-2
for i,element in enumerate(color):
    color[i] = element*factor
print(color)
