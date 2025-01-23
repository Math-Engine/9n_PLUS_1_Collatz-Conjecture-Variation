# 구간별 최솟값 그래프 그리기

import sys
import os
import math

import matplotlib.pyplot as plt
import io
import base64

sys.set_int_max_str_digits(2147483647)

def dividing_2(n):
  if (len(str(n)) < 16):
    return n//2
  return int(str((n * 5))[0:len(str(n * 5)) - 1])

num = int(sys.argv[1])
sequence_length = int(sys.argv[2])
section_range = int(sys.argv[3])

os.system(f'echo "Number: {num} <br> 항의 개수: {sequence_length} <br> 구간 범위: {section_range} <br> <hr>" >> $GITHUB_STEP_SUMMARY')

Hailstone_Num = [num]
temp = num
is_loop = False
is_end = False
for i in range(sequence_length - 1):
  # print(temp)
  if (int(str(temp)[-1])%2 == 1):
    temp = (temp * 9) + 1
  else:
    temp = dividing_2(temp)
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
print()

if (is_end == False):
  # os.system(f'echo "<details><summary>{num} :question: </summary><br><code>{str(Hailstone_Num)}</code><br></details>" >> $GITHUB_STEP_SUMMARY')
  os.system(f'echo "question:" >> $GITHUB_STEP_SUMMARY')

minimums_class = [] # 계급
minimums_arr = [] # 계급값
for j in range(0, math.ceil(len(Hailstone_Num)/section_range)):
  minimums_class.append(f"{(section_range * j) + 1} ~ {section_range*(j + 1)}")
  minimums_arr.append(min(Hailstone_Num[(section_range*j):(section_range*(j+1) - 1)]))
os.system(f'echo "구간별 최솟값: {str(minimums_arr)}" >> $GITHUB_STEP_SUMMARY')

plt.plot(minimums_class, minimums_arr)
plt.xlabel('계급')
plt.ylabel('계급값')
plt.title(f'9n + 1 구간별 최솟값 ( n = {num} )')

buffer = io.BytesIO()
plt.savefig(buffer, format='png')
buffer.seek(0)
img_base64 = base64.b64encode(buffer.read()).decode('utf-8')
img_url = f"data:image/png;base64,{img_base64}"

print("==============================================================================================================================")
print(img_url)
print("==============================================================================================================================")
os.system(f'echo "<details><summary>9n + 1 구간별 최솟값 ( n = {num} ) 그래프 Base64 URL</summary><br><br>```{img_url}```<br><br></details>" >> $GITHUB_STEP_SUMMARY')
