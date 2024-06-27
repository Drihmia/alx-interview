#!/usr/bin/python3
"""
Main file for testing
"""

validUTF8 = __import__('0-validate_utf8').validUTF8

# 1 byte valid
data = []
print(validUTF8(data))

# 3 bytes valid
data = [228, 189, 160, 229, 165, 189]
print(validUTF8(data))

# Invalid 3 bytes
data = [168]
print(validUTF8(data))

# Invalid 3 bytes
data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))

# 4 bytes valid
data = [229, 65, 127, 254]
print(validUTF8(data))

# Create valid test for 1 to 4 bytes long
data = [229, 65, 127, 254]
for i in range(1, 5):
    print(validUTF8(data[:i]))
