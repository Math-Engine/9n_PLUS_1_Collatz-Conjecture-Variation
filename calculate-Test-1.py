import sys
import os

sys.set_int_max_str_digits(2147483647)

num = 2**1000
sequence_length = 1002

Hailstone_Num = [num]
temp = num
is_loop = False
is_end = False
for i in range(sequence_length - 1):
  print(temp, end=" - ")
  if (temp%2 == 1):
    temp = (temp * 9) + 1
  else:
    temp = temp/2
  if temp in Hailstone_Num:
    is_loop = True
    Hailstone_Num.append(temp)
    print()
    print(Hailstone_Num)
    os.system(f'echo "<details><summary>{num} :bangbang:" >> $GITHUB_STEP_SUMMARY')
    is_end = True
    break
  elif (temp == 1):
    Hailstone_Num.append(temp)
    print()
    print(Hailstone_Num)
    os.system(f'echo "<details><summary>{num} :ballot_box_with_check:" >> $GITHUB_STEP_SUMMARY')
    is_end = True
    break
  else:
    Hailstone_Num.append(temp)

if (is_end == False):
  os.system(f'echo "<details><summary>{num} :question:" >> $GITHUB_STEP_SUMMARY')
