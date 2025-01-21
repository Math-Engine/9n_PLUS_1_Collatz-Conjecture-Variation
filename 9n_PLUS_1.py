import sys
import os

sys.set_int_max_str_digits(2147483647)

def dividing_2(n):
  if (len(str(n)) < 16):
    return n//2
  n = str(n)
  r = 0
  for i in range(len(n) - 1):
    r = r + int(str(int(n[i] + "0")//2) + ("0" * (len(n) - 2 - i)))
  r = r + int(n[-1])//2
  return r

start = int(sys.argv[1])
end = int(sys.argv[2])

for i in range(start, end+1):
  Hailstone_Num = [i]
  temp = i
  while True:
    print(temp)
    if (int(str(temp)[-1])%2 == 1):
      temp = (temp * 9) + 1
    else:
      temp = dividing_2(temp)
    if temp in Hailstone_Num:
      Hailstone_Num.append(temp)
      os.system(f'echo "<details><summary>{i} :bangbang: </summary><br><code>{str(Hailstone_Num)}</code><br></details>" >> $GITHUB_STEP_SUMMARY')
      print()
      print(Hailstone_Num)
      break
    elif (temp == 1):
      Hailstone_Num.append(temp)
      os.system(f'echo "<details><summary>{i} :ballot_box_with_check: </summary><br><code>{str(Hailstone_Num)}</code><br></details>" >> $GITHUB_STEP_SUMMARY')
      print()
      print(Hailstone_Num)
      break
    else:
      Hailstone_Num.append(temp)
