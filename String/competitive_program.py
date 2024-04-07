import sys
input = lambda: sys.stdin.readline().rstrip()

ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 998244353
 
 
def solve():
    ans = 'YES'
    n = ii()
    if n != 5:
        ans = 'NO'
    s = input()
 
    if sorted(s) != sorted('Timur'):
        ans = 'NO'
    print(ans)
 
for _ in range(ii()):
    solve()



