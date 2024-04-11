product_info = {
	"description": "shoe",
	"price": 4.56,
	"colors": ["green", "blue", "red"],
}

product_list = []

for key, val in product_info.items():
    product_list.append([key,val])

print(product_list)
