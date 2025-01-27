#!/usr/bin/env python3
# Author: Edison Leung
# Author ID: 147724231
# Date Created: 2025/01/26

import sys

# Assign the value of the first command line argument to timer, converting it to an integer
timer = int(sys.argv[1])

# Use a while loop to count down from the timer to 1
while timer > 0:
    print(timer)
    timer -= 1  # Decrement the timer by 1

# Print "blast off!" after the countdown ends
print("blast off!")

