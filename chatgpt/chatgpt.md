# 【技术分享】使用微软Azure服务器配置chatgpt-qq机器人、部署上线网站，Linux环境配置

> #### tag: Azure、ChatGPT、服务器、上线网站、宝塔面板、Tomcat、Linux、技术分享、QQ机器人



> ### Microsoft Azure

1. 为什么不用阿里云、腾讯云之类的，首先这些服务器都是在国内的，如果想部署ChatGPT的QQ机器人是不行的(如果你有其他科学上网手段当我没说)，其次Azure是可以使用学生权益的（100$一年的额度）

2. [Microsoft Azure网站](https://portal.azure.com/)
3. 创建一个虚拟机地区选择中国以外的区域，大小选择B1ms（部署ChatGPT整个项目需要2GB的内存，如果你只是想部署网站的话可以选择B1s），管理员账号随便创建，然后直接创建虚拟机（此处需要保证之前没有创建过其他冲突的虚拟机）
4. 转到资源复制公共IP地址（如果没有就重新创建），打开Windows Termial(命令提示符)，有其他的SSH可以使用其他的。

>### 配置ChatGPT QQ 机器人 

1. 你需要有一个OpenAI的账号，这里就不教怎么注册了

2. 你需要先验证是否能够正常登录（如果你能够保证正常登录可以跳过之后的安装桌面环境、配置远程桌面、安装Chrome步骤）

> ### 在 Linux VM 上安装桌面环境

1. 打开22端口，连接远程服务器

```bash
ssh azureuser@myvm.westus.cloudapp.azure.com
```

2. 安装`xfce`

```bash
sudo apt-get update
sudo DEBIAN_FRONTEND=noninteractive apt-get -y install xfce4
sudo apt install xfce4-session
```

>#### 安装和配置远程桌面服务器

安装桌面环境后，请配置远程桌面服务来侦听传入连接。 [xrdp](http://xrdp.org/) 是大多数 Linux 分发版中提供的开源远程桌面协议 (RDP) 服务器，可与 xfce 完美配合。

```bash
sudo apt-get -y install xrdp
sudo systemctl enable xrdp
```

在 Ubuntu 20 上，需要向 xrdp 用户授予证书访问权限：

```bash
sudo adduser xrdp ssl-cert
```

告诉 xrdp 在启动会话时要使用的桌面环境。 配置 xrdp 以使用 xfce 作为桌面环境，如下所示：

```bash
echo xfce4-session >~/.xsession
```

重新启动 xrdp 服务使更改生效，如下所示：

```bash
sudo service xrdp restart
```

> ### 安装Chrome

1. 下载Chrome安装包

```bash
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
```

2. 安装Chrome浏览器

```bash
sudo dpkg -i google-chrome-stable_current_amd64.deb
sudo apt-get -f install
```

> ### 打开远程桌面

1. 打开Windows的远程桌面（在此之前确保已经打开了3389端口），输入虚拟机的IP，连接远程桌面。
2. 打开Chrome，访问[ChatGPT官网](Chat.openai.com)，如果不能正常登录的话删除虚拟机换其他区域。

> ### chatgpt-mirai-qq-bot项目

[chatgpt-mirai-qq-bot项目地址](https://github.com/lss233/chatgpt-mirai-qq-bot)、[chatgpt-mirai-qq-bot Windows快速部署教程](https://www.bilibili.com/video/av991984534)

1. 你需要准备一个QQ账号作为机器人，并且提前安装`TxCaptchaHelper`来通过QQ登录的滑动验证码[TxCaptchaHelper项目地址](https://github.com/mzdluo123/TxCaptchaHelper)

2. Linux快速部署脚本

```bash
sudo bash -c "$(curl -fsSL https://gist.githubusercontent.com/lss233/54f0f794f2157665768b1bdcbed837fd/raw/chatgpt-mirai-installer-154-16RC3.sh)"
```

3. 填写OpenAI账号密码，QQ机器人账号密码

4. 打开文字转图片功能、角色预设、发送图片等功能
5. 在QQ中验证

> ### 部署上线网站(使用Tomcat服务器)

1. 视频使用Tomcat（会其他的也可以用其他的）部署网站，如果实在不会的，可以使用宝塔面板部署（网上教程很多）
2. 安装jdk

```bash
sudo apt-get install -y openjdk-8-jdk
```

3. 配置环境变量

```bash
sudo vi ~/.bashrc
```

4. 在最后一行加上

```bash
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
export PATH=$JAVA_HOME/bin:$PATH
export CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar
```

5. 测试jdk是否安装成功

```bash
java -version
```

6. 安装Tomcat9

```bash
# 1
sudo apt-get install -y tomcat9-admin
# 2
sudo apt-get install -y tomcat9
```

7. 启动服务

```bash
# 查找Tomacat位置
sudo find / -name *tomcat*
# 转到目录
cd /usr/share/tomcat9/bin
# 启动服务
sudo ./startup.sh
```

8. 上传网站

```bash
# 找到文件夹/var/lib/tomcat9/webapps/ROOT
# 替换其中的文件为你的项目文件
```

9. 打开`你的虚拟机IP:8080`访问网站(确保虚拟机的8080端口是打开的)

10. 提供一个简陋的方案(如果没钱或者没条件用服务器的，可以使用手机Termux配置内网穿透的方案部署网站)



