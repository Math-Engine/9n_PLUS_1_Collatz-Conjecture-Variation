import sys
sys.set_int_max_str_digits(2147483647)

def ExponentialNotaion_To_StandardNotation(temp):
  return int(str(temp)[0] + str(temp)[(str(temp).find(".") + 1):str(temp).find("e")] + ("0" * (int(str(temp)[((str(temp).find("+")) + 1):(len(str(temp)) + 1)]) - len(str(temp)[(str(temp).find(".") + 1):str(temp).find("e")]))))

print(ExponentialNotaion_To_StandardNotation("7.649670160387128e+16"))
print(ExponentialNotaion_To_StandardNotation(7.649670160387128e+16))
