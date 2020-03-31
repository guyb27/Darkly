import os

list_char = ''
i = 32
while i < 127:
    list_char+=chr(i)
    i +=1
max_char=11

def generate(l, d):
    if d < 1:
        return
    for c in l:
        if d == 1:
            yield (c)
        else:
            for k in generate(l, d-1):
                yield c+k

for d in range(1, max_char):
    for c in generate(list_char, d):
        print(c + "\n")