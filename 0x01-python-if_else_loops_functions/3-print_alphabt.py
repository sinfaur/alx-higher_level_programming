#!/usr/bin/python3
for alphabt in range(ord('a'), ord('z')+1):
    if alphabt not in [101, 113]:
        print("{:c}".format(alphabt), end="")
