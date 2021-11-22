# opensoooooource

## 题目描述

听说逆向二进制文件对萌新来说太难了，那——如果直接拿到源码了呢？

## 题目文件

`opensoooooource.py`

## flag

flag{d0_u_know_what_the_SECRET_is_ju5t_534rch_tha7!}

## hint

1.  仔细看每个check的限制条件，一段一段出flag
2. 5个check，五个密码算法（Tea、Okamoto、Vigenere、Enigma、Rijndael），改改调用就能解密
3. 公钥密码Okamoto可以不用算私钥，限定了字符集直接爆破就好

