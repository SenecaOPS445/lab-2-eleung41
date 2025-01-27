#!/usr/bin/env python3
# Author: Edison Leung

import sys

# Check if exactly 2 additional arguments are provided
if len(sys.argv) != 3:
    print("Usage: " + sys.argv[0] + " name age")
else:
    # Assign command-line arguments to the objects
    name = sys.argv[1]  # First argument is the name
    age = sys.argv[2]   # Second argument is the age

    # Print the greeting message
    print('Hi ' + name + ', you are ' + age + ' years old.')

