with open('map.txt', 'r') as f:
    s = ""
    for l in f.readlines():
        s += l.strip()
print(s)

data = []
for x in s:
    if x == '*':
        data.append(0)
    elif x == '.':
        data.append(1)
    elif x == 'x':
        data.append(2)
    elif x == 'y':
        data.append(3)
    else:
        print("?")
print(data)

# h左
# j下
# k上
# l右