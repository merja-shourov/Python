
# b^2 - 4.a.c = 0 or negatie or positive
import math
a,b,c = map( int , input().split())


discriminent = b**2 - (4*a*c)

if( discriminent == 0 ):
    r = -b/(2*a)
    print(r)
elif discriminent > 0:
        r1 = (-b + math.sqrt(discriminent) )/(2*a)
        r2 = (-b - math.sqrt(discriminent) )/(2*a)
        print(r1, r2, end=" ")
else:
    print("Complex Roots")