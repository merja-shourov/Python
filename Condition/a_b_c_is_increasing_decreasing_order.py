
a,b,c = map(int, input().split())

if a > b and b > c :
    print("Decreasing order")
elif a < b and b < c:
    print("Increasing order")
else:
    print("None")