import sys
sys.set_int_max_str_digits(2147483647)

# a = 2**67
# b = 2**68

# print((a/2) * 2)
# print("\n" * 3)
# print((b/2) * 2)
# print("\n" * 3)
# print((b-2/2) * 2)
# print("\n" * 3)

# print("==============")

# print((2**30/2) * 2)
# print("\n" * 3)
# print((2**31/2) * 2)
# print("\n" * 3)
# print((2**32/2) * 2)
# print("\n" * 3)

# print("==============")

# for i in range(1, 70):
#   ex = ((2**i)/2) * 2
#   print(f'{i}: {ex}')
#   if "e" in str(ex):
#     print("==========")
#     print((((2**i) - 2)/2) * 2)

print((int("9" * 15)/2) * 2)
