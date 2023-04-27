import os
import time

print('\033[?25l', end="")  # cursor off
# print('\033[?25h', end="")  # cursor on


for i in range(1, 101):
  print(i)
  time.sleep(0.05)
  os.system("clear")