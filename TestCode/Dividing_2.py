# 오직 2의 배수인 자연수만 2로 나눌 수 있습니다.

import math
import sys
sys.set_int_max_str_digits(2147483647)

def algorithm_1(n):
  if (len(str(n)) < 16):
    return math.ceil(n/2)
  n = str(n)
  r = 0
  for i in range(len(n) - 2):
    r = r + int(str(math.ceil(int(n[i] + "0")/2)) + ("0" * (len(n) - 2 - i)))
  r = r + math.ceil(int(n[-1])/2)
  return r

## Test

k = 2**100000
print(k)

print("================")
test_result = k
for i in range(100000):
  k = algorithm_1(k)
print(k)
