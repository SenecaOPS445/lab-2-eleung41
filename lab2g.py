#!/usr/bin/env python3
# Author: Edison Leung
# Author ID: 147724231
# Date Created: 2025/01/26

import sys

# Check if a command line argument is provided
if len(sys.argv) == 2:
    # If argument is provided, use it as the timer value
    timer = int(sys.argv[1])
else:
    # If no argument is provided, set the timer to 3
    timer = 3

# Use a while loop to count down from the timer to 1
while timer > 0:
    print(timer)
    timer -= 1  # Decrement the timer by 1

# Print "blast off!" after the countdown ends
print("blast off!")

