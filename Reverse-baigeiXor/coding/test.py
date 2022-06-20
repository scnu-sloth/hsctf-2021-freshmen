flag = "flag{b4igei_baig3il3_zhenba1ge1}"
flag = list(map(ord, flag))
print(flag)

s = [0, 0, 0]
s[0]   = "really_really_ezzzzzzzzz_reverse"
s[1]   = "keep_going_and_you_will_get_it~!"
s[2]   = "!workHardAndYouWillBeSuccessful!"
for i in range(3):
    s[i] = list(map(ord, s[i]))
    flag = [flag[j] ^ s[i][j] for j in range(len(flag))]

print(flag)