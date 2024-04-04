

s = '_0000_15 studio 230194 1'

s1 = s[6:]
print(s1)
ind = s1.find(' ')

t = f'test_{s1[:ind]}'
print(t)