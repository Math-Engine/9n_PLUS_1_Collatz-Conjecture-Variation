# 오직 2의 배수인 자연수만 2로 나눌 수 있습니다.

import sys
sys.set_int_max_str_digits(2147483647)

def algorithm_1(n):
  if (len(str(n)) < 16):
    return n//2
  n = str(n)
  r = 0
  for i in range(len(n) - 1):
    r = r + int(str(int(n[i] + "0")//2) + ("0" * (len(n) - 2 - i)))
  r = r + int(n[-1])//2
  return r
