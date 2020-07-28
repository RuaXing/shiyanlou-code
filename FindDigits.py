#!/usr/bin/env python3
fobj = open('/tmp/String.txt')
num = ""
s = fobj.read()
for char in s:
    if char.isdigit():
        num += char
fobj.close()
print(num)
