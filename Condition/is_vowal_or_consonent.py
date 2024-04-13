
# txt = "score: 10"

# if not txt:
#     print("Empty")
# else:
#     for char in txt.lower():
#         if char in ('a','e','i','o','u'):
#             print(f"{char} Vowel")
#         elif not char.isalpha():
#             print(f"{char} Not Alphabet")
#         else:
#             print(f"{char} Consonont")

text = "Age: 23"

if text:
    for char in text.lower():
        if( char.isalpha()):
            if char in ('a','e','i','o','u'):
                print(f"{char}: Valuel")
            else:
                print(f"{char} is Consonont")
        else:
            print(f"{char} is Not alphabe")
else:
    print("empty")
