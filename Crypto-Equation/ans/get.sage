import libnum
import string

a0 = 30188147721117215781129100297502653147720244598096
b0 = 21570432690338300962113223428601821765217196091704
a1 = 2644612157538919571387894485245174170571484040764
b1 = 2439650961154362725659337213967574551053744888261
a2 = 3549540394738386267390659328154240007562582898045
b2 = 3396047733146044072945509494632282291396398974799

# Part 0
nn = lcm(a0, b0)
x0 = nn//a0
y0 = nn//b0

# Part 1
_, x1, y1 = xgcd(a1, b1)
x1 = abs(x1)
y1 = abs(y1)

# Part 2
M = matrix([
  [1, a2],
  [0, b2]
])
L = M.LLL()
w = L[0]

v = M.solve_left(w)
# guess gcd(x2, y2)
for g in range(1, 10000):
  x2 = abs(v[0]) * g
  mx2 = libnum.n2s(int(x2))
  yes = True
  for m in mx2:
    if not chr(m) in string.printable:
      yes = False
      break
  if yes:
    y2 = abs(v[1]) * g
    my2 = libnum.n2s(int(y2))
    yes = True
    for m in my2:
      if not chr(m) in string.printable:
        yes = False
        break
    if yes:
      #print(x2, y2)
      break
else:
  print('more gcd')
  exit(-1)

# get flag
res = [x0, y0, x1, y1, x2, y2]
res = [libnum.n2s(int(x)) for x in res]
flag = ''
for r in res:
  for m in r:
    flag += chr(m)
print(flag)


