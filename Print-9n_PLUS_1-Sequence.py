import sys
import os

sys.set_int_max_str_digits(2147483647)

num = int(sys.argv[1])
sequence_length = int(sys.argv[2])

os.system(f'echo "Number: {num} <br> 항의 개수: {sequence_length} <br><hr>" >> $GITHUB_STEP_SUMMARY')

Hailstone_Num = [num]
temp = num
is_loop = False
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
    os.system(f'echo "<details><summary>{num} :bangbang: </summary><br><code>{str(Hailstone_Num)}</code><br></details>" >> $GITHUB_STEP_SUMMARY')
    break
  elif (temp == 1):
    Hailstone_Num.append(temp)
    print()
    print(Hailstone_Num)
    os.system(f'echo "<details><summary>{num} :ballot_box_with_check: </summary><br><code>{str(Hailstone_Num)}</code><br></details>" >> $GITHUB_STEP_SUMMARY')
    break
  else:
    Hailstone_Num.append(temp)
