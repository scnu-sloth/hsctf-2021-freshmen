## 运行题目代码

1. 安装Python，这个应该没疑问吧？
2. 查看代码的`import`部分，需要的第三方库只有`Crypto`。网上很多文章会让你安装pyCrypto，个人认为不靠谱。pyCrypto早就没人维护了，现在应该用pycryptodome。用`pip install pycryptodome`就可以安装了。
3. 由于`secret.py`文件不提供，查看`game.py`代码可知：`secret.py`里需要一个`aes_key`的变量。所以可以自己创建一个，这样代码就可以在自己的电脑上运行起来了。

## 理解题目

其实本题并不需要选手自己把代码运行起来。因为`aes_key`不同的话，得到的加密文件是不一样的，而正确的`aes_key`只有出题人知道。运行代码只是为了了解一下题目，也方便本地验证自己的做题想法。

首先，注意到代码中使用的是AES的ECB模式。即使不懂这个，也可以搜一下“AES ECB”这样的关键词，网上有超级多文章介绍这个。这里出题人随便选取了[一篇文章](https://www.cnblogs.com/xzj8023tp/p/12970790.html)。

然后，注意到`game.py`代码是对一个文件进行加密，而题目已经给出了三个文件。其中，`passwd_list1.txt_enc`看起来就是`passwd_list1.txt`的加密结果，而`passwd_list2.txt_enc`则没有对应的`passwd_list2.txt`。再结合题目要求：解出door密码。就明白了，题目中的文件是这样得到的：

```bash
> python game.py
where is the file: passwd_list1.txt
finish （得到passwd_list1.txt_enc）
> python game.py
where is the file: passwd_list2.txt
finish （得到passwd_list2.txt_enc）
```

最后，需要了解一下python中`hexlify`和`unhexlify`的意义。`hexlify`就是把所有字符都转成16进制，`unhexlify`当然就是反过来啦。举个栗子：

```
hexlify(b'abcd') = b'61626364'
unhexlify(b'61626364') = b'abcd'
```

注意到`hexlify`之后，字符串会变成两倍长度了。而AES加密的输入是16个字节（字符串长度为16），输出的密文是16个字节。本题中对明文和密文都`hexlify`了，所以加密的字符串长度是8个字符，得到的密文的长度就是32个字节。

## 开始解题

[前面提到的文章](https://www.cnblogs.com/xzj8023tp/p/12970790.html)中对于ECB模式的介绍，就有一张图可以参考。可以注意到该模式下相同的明文对应相同的密文。这个特点基本每篇讲ECB的文章都会说到，甚至有些文章会直接告诉你它就是不安全的，然后介绍如何攻击它。搜到那种文章，那本题直接就解出来了哇。

好了，没搜到，那就往下看。

既然AES-ECB有上述特点，那我们就可以尝试着检查一下`passwd_list1.txt_enc`和`passwd_list2.txt_enc`的内容了。如果它们有什么密文是相同的，那说明对应的明文也相同。

这里要检查的量很小，用肉眼也可以发现第一个：

```
sina:860b5620db25fd291e3165a5cdedca668e1dc11a2d1d07d9d3fa25cc37c38e54
door:860b5620db25fd291e3165a5cdedca6653615145df2517d82f8ab2ab5ac764e92f738b6d550cc80b108c563a1eada0df7c7b7743e2467b75d13775fb5fd5aec5
```

这两个密文的前面有一段是相同的！再看看相同部分的长度，就是32！一块密文的长度就是32！那说明！door密码的密文的第一块，和sina密码的第一块是相同的！所以door密码的明文的前面一段是sina密码的前面一段！也就是`this_is_`！

WOW！竟然如此顺利！那再找找第二段吧！WOW！第二段在这儿：

```
google:53615145df2517d82f8ab2ab5ac764e998276ed81ecb35efab5c851115aa4503e642f04071757a7034389ace7b0519c3ccd531eeb3f4aa7a6c23cb730972c25b
door:860b5620db25fd291e3165a5cdedca66 | 53615145df2517d82f8ab2ab5ac764e92f738b6d550cc80b108c563a1eada0df7c7b7743e2467b75d13775fb5fd5aec5
```

从536151开始！那说明第二段明文是`a_very_s`！

以此类推，就可以得到door密码的明文，也就是flag。

解题时可以用眼睛找每一段，也可以写个代码读取这三个文件的内容，一段一段地匹配。出题人已经用Python实现了一个了，可以自行查看参考。

好了就是这么简单。。。里面还有ICBC密码，~~解出来了就去银行把我的钱拿走吧，本场比赛最丰厚的奖励~~。