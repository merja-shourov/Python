
s1 = { 1, 3, 4}
s2 = { 2, 3, 5}

# option 1

intersection = set()
for item in s1:
    if item in s2:
        intersection.add(item)

print(intersection)

print(s1.intersection(s2))