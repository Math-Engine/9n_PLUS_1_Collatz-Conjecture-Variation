import sys
import os

sys.set_int_max_str_digits(2147483647)

start = int(sys.argv[1])
end = int(sys.argv[2])

for i in range(start, end+1):
  Hailstone_Num = [i]
  temp = i
  while True:
    if (temp%2 == 1):
      temp = (temp * 9) + 1
    else:
      temp = temp/2
    if temp in Hailstone_Num:
      Hailstone_Num.append(temp)
      os.system(f'echo "<details><summary>{i} :bangbang: </summary><br><code>{str(Hailstone_Num)}</code><br></details>" >> $GITHUB_STEP_SUMMARY')
      print(Hailstone_Num)
      break
    elif (temp == 1):
      Hailstone_Num.append(temp)
      os.system(f'echo "<details><summary>{i} :ballot_box_with_check: </summary><br><code>{str(Hailstone_Num)}</code><br></details>" >> $GITHUB_STEP_SUMMARY')
      print(Hailstone_Num)
      break
    else:
      Hailstone_Num.append(temp)
