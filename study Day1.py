# 1.求1-100的偶数和
import math
sum = 0
for i in range(1,101):
    if i % 2 == 0:
        sum += i
    else:
        continue
print('1-100的偶数和为%d'%sum)

