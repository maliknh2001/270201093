# Checking that code is working
print("Hello world")

import time
def count_down(t):
    if t ==0:
        print("Time finished")
        return 0
    else:
        print("time remaining", t)
        time.sleep(1)
        return count_down(t-1)

count_down(5)