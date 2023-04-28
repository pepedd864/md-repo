---
title: "github图床设置"
data: "2022-12-29 23:03:00"
description: "github图床设置，常见问题解答"
---



图床

- 是一种在网络上存储图片的服务
- 使用图床即可在移动本地项目时图片仍然保持正常的方法

# 1. picgo图床工具

github官网:https://github.com/Molunerfinn/PicGo

下载对应版本工具即可

# 2. github仓库设置

1. 创建图床仓库

![](https://cdn.staticaly.com/gh/pepedd864/cdn-repos@main/img/20221229224311.png)

2. 获取token

![](https://cdn.staticaly.com/gh/pepedd864/cdn-repos@main/img/20221229224448.png)

![](https://cdn.staticaly.com/gh/pepedd864/cdn-repos@main/img/20221229224621.png)

![](https://cdn.staticaly.com/gh/pepedd864/cdn-repos@main/img/20221229224741.png)

3. 选择token有效期，勾选授权仓库权限

![](https://cdn.staticaly.com/gh/pepedd864/cdn-repos@main/img/20221229224924.png)

4. 获得token，**注意，token只会显示一次，刷新后不再显示**

![](https://cdn.staticaly.com/gh/pepedd864/cdn-repos@main/img/20221229225123.png)

# 3. picgo设置

按照图示填入信息即可，设定自定义域名使用的是`https://cdn.staticaly.com/gh/用户名/仓库名@分支`，之前使用的`https://www.jsdelivr.com/`被墙失效

![](https://cdn.staticaly.com/gh/pepedd864/cdn-repos@main/img/20221229225252.png)

填入信息无误后确认即可

# 4. 上传图片

picgo支持直接使用截切板上传图片

![](https://cdn.staticaly.com/gh/pepedd864/cdn-repos@main/img/20221229225702.png)

上传成功便可以得到一个图片的链接，如下

`![](https://cdn.staticaly.com/gh/pepedd864/cdn-repos@main/img/20221229225702.png)`

此时可以将图片引入各个项目文件中使用

# 5. 常见问题

截切板没有内容



![截切板没有图片](https://cdn.staticaly.com/gh/pepedd864/cdn-repos@main/img/20221229225956.png)



开启网络代理工具可能会导致上传时出现证书错误的提示，关闭代理再上传即可

![证书错误](https://cdn.staticaly.com/gh/pepedd864/cdn-repos@main/img/20221229230110.png)

# 6. typora的图片上传功能

成功配置picgo后可以使用typora的图片上传功能，将本地图片转换为线上图片

![](https://cdn.staticaly.com/gh/pepedd864/cdn-repos@main/img/image-20221229234058890.png)

