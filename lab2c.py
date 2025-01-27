#!/usr/bin/env python3
# Author: Edison Leung

import sys

# Assign command-line arguments to the objects
name = sys.argv[1]  # First argument is the name
age = int(sys.argv[2])  # Second argument is the age (converted to an integer)

# Print the greeting message
print('Hi ' + name + ', you are ' + str(age) + ' years old.')

