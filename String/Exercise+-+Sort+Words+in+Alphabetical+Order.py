# ----------------
# Option 1
# ----------------
s = "Hello World"
new_s = ""

words_list = s.split(" ")

for word in words_list:
	lowercase_word = word.lower()
	
	sorted_word = "".join(sorted(lowercase_word))
	new_s += sorted_word + " "

new_s.rstrip()

print(new_s)

# ----------------
# Option 2
# ----------------
s = "Hello World"
new_s = ""

words_list = s.split(" ")

for word in words_list:
	new_s += "".join(sorted(word.lower())) + " "

new_s.rstrip()

print(new_s)