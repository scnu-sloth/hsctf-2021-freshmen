flag = "flag{E1d3sTBrOth3r_CaR0Ilikoule}"
key  = "H4ve_fun_w1th_R3verse_my_friend~"
arr = []
for i in range(len(flag)):
    arr.append(ord(flag[i]) ^ ord(key[i]))
print(arr)