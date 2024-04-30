import sys


arrow = []
for x in sys.stdin:
    s = x.strip('\n')
    if s == 'D':
        arrow.append('⮕')
    elif s == 'A':
        arrow.append('⬅')
    elif s == 'S':
        arrow.append('⬇')
    elif s == 'W':
        arrow.append('⬆')
print(arrow)