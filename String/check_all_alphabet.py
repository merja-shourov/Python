import string

s = "the quick brown fox jumps over the lazy dog"

# print(string.ascii_lowercase)

flag = True
for char in s:
    if( char == " "):
        continue
    if char not in string.ascii_lowercase:
        flag = False
        break

print(flag)
