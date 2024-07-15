#Countdown timer

import time

time_is = int(input("Enter seconds: "))

for x in reversed(range(0, time_is)):
    seconds = (x % 60)
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    time.sleep(1)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")

print("Time is UP!!!")