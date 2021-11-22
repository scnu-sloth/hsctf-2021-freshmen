from base64 import b64decode

part1 = b'ZmxhZ3tEb191X2g0dmVfYQ=='
part2 = b'X2wxdmVseV9ucHlfaGFofQ=='
flag = b64decode(part1) + b64decode(part2)

print(flag)
# b'flag{Do_u_h4ve_a_l1vely_npy_hah}'