str = "My Love"

word_list = str.split(" ")
new_str = ""

for word in word_list:
    reverse_word = "".join(reversed(word))
    swap_case = reverse_word.swapcase()
    new_str += swap_case + " "
print(new_str)