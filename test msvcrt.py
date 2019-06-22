import msvcrt
import time


car = "0"
time.sleep(3)
print(car)
print("wait")
time.sleep(3)
check = msvcrt.kbhit()
if check:
    car = msvcrt.getch()
print(car)
input()
