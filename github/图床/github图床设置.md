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

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/f92a9b74be432a3d968e9c3e25bf48d0.png)

2. 获取token

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/be3ae789c57088b8b7ef50c68e335a02.png)

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/1a8bcdae8bd404e067889a308954764b.png)

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/2b046f0496ae828239153150ed3a23d5.png)

3. 选择token有效期，勾选授权仓库权限

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/7a28e607c7b258fbfdc8aed13ce3004f.png)

4. 获得token，**注意，token只会显示一次，刷新后不再显示**

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/98ae13c44760bed7df17da40134d96a3.png)

# 3. picgo设置

按照图示填入信息即可，设定自定义域名使用的是`https://cdn.staticaly.com/gh/用户名/仓库名@分支`，之前使用的`https://www.jsdelivr.com/`被墙失效

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/0ecb7b69b7be6dfbd03ad8dac01b3120.png)

填入信息无误后确认即可

# 4. 上传图片

picgo支持直接使用截切板上传图片

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/cbf0d7569ea56648a920dc2365f74cca.png)

上传成功便可以得到一个图片的链接，如下

`![](https://cdn.staticaly.com/gh/pepedd864/cdn-repos@main/img/20221229225702.png)`

此时可以将图片引入各个项目文件中使用

# 5. 常见问题

截切板没有内容



![截切板没有图片](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/d90475b0c239b78f80cc85a9a3fa6665.png)



开启网络代理工具可能会导致上传时出现证书错误的提示，关闭代理再上传即可

![证书错误](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/9a206d8188bf79332868bb2dbc2183a7.png)

# 6. typora的图片上传功能

成功配置picgo后可以使用typora的图片上传功能，将本地图片转换为线上图片

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/af3217914b300d600ba41eb4cc32bc9e.png)

