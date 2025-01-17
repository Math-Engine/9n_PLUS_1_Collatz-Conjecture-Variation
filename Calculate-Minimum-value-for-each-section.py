# 구간별 최솟값 찾기

import sys
import os
import math

sys.set_int_max_str_digits(2147483647)

num = int(sys.argv[1])
sequence_length = int(sys.argv[2])
section_range = int(sys.argv[3])

os.system(f'echo "Number: {num} <br> 항의 개수: {sequence_length} <br> 구간 범위: {section_range} <br> <hr>" >> $GITHUB_STEP_SUMMARY')

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
    # os.system(f'echo "<details><summary>{num} :bangbang: </summary><br><code>{str(Hailstone_Num)}</code><br></details>" >> $GITHUB_STEP_SUMMARY')
    os.system(f'echo ":bangbang:" >> $GITHUB_STEP_SUMMARY')
    is_end = True
    break
  elif (temp == 1):
    Hailstone_Num.append(temp)
    print()
    print(Hailstone_Num)
    # os.system(f'echo "<details><summary>{num} :ballot_box_with_check: </summary><br><code>{str(Hailstone_Num)}</code><br></details>" >> $GITHUB_STEP_SUMMARY')
    os.system(f'echo ":ballot_box_with_check:" >> $GITHUB_STEP_SUMMARY')
    is_end = True
    break
  else:
    Hailstone_Num.append(temp)

if (is_end == False):
  # os.system(f'echo "<details><summary>{num} :question: </summary><br><code>{str(Hailstone_Num)}</code><br></details>" >> $GITHUB_STEP_SUMMARY')
  os.system(f'echo "question:" >> $GITHUB_STEP_SUMMARY')

minimuns_arr = []
for j in range(0, math.ceil(len(Hailstone_Num)/section_range)):
  minimuns_arr.append(min(Hailstone_Num[(section_range*j):(section_range*(j-1) + 1)]))
os.system(f'echo "구간별 최솟값: {str(minimuns_arr)}" >> $GITHUB_STEP_SUMMARY')
