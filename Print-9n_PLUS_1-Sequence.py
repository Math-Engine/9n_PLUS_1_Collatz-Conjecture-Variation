import sys
import os

sys.set_int_max_str_digits(2147483647)

def dividing_2(n):
  if (len(str(n)) < 16):
    return n//2
  return int(str(n * 5)[0:len(str(n * 5)) - 1])

num = int(sys.argv[1])
sequence_length = int(sys.argv[2])

os.system(f'echo "Number: {num} <br> 항의 개수: {sequence_length} <br><hr>" >> $GITHUB_STEP_SUMMARY')

Hailstone_Num = [num]
temp = num
is_loop = False
is_end = False
for i in range(sequence_length - 1):
  print(temp)
  if (int(str(temp)[-1])%2 == 1):
    temp = (temp * 9) + 1
  else:
    temp = dividing_2(temp)
  if temp in Hailstone_Num:
    is_loop = True
    Hailstone_Num.append(temp)
    print()
    print(Hailstone_Num)
    os.system(f'echo "<details><summary>{num} :bangbang: </summary><br><code>{str(Hailstone_Num)}</code><br></details>" >> $GITHUB_STEP_SUMMARY')
    is_end = True
    break
  elif (temp == 1):
    Hailstone_Num.append(temp)
    print()
    print(Hailstone_Num)
    os.system(f'echo "<details><summary>{num} :ballot_box_with_check: </summary><br><code>{str(Hailstone_Num)}</code><br></details>" >> $GITHUB_STEP_SUMMARY')
    is_end = True
    break
  else:
    Hailstone_Num.append(temp)

if (is_end == False):
  os.system(f'echo "<details><summary>{num} :question: </summary><br><code>{str(Hailstone_Num)}</code><br></details>" >> $GITHUB_STEP_SUMMARY')
