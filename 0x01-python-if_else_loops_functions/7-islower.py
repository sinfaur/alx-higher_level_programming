#!/usr/bin/python3
def islower(c):
    if not c:
        raise ValueError()
    return c.isalpha() and c == c.lower()
