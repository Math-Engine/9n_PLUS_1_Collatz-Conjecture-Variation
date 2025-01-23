# 오직 2의 배수인 자연수만 2로 나눌 수 있습니다.

import sys
sys.set_int_max_str_digits(2147483647)

def dividing_2(n):
  if (len(str(n)) < 16):
    return n//2
  return int(str((n * 5))[0:len(str(n * 5)) - 1])
