#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = ''
    pos = 0
    for char in str:
        if pos != n:
            new_str += char
        pos += 1
    return new_str
