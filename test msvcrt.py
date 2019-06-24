import msvcrt
import time

car = "0"
print("wait 5")
time.sleep(5)


count = 1

while msvcrt.kbhit():
    car = msvcrt.getch()
    print("caractere {}, tour de boucle {}".format(car, count))
    count += 1
print ("SORTIE de boucle")


input()
