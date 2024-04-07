
import math
a = [1,2,4]
b = [2,2,3]

addition = (b[0] - b[1]) ** 2 + (b[1]-a[1]) **2 + (b[2]-a[2])**2
# ans = addition **(1/2)
print(math.sqrt(addition))