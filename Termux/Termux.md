# Termux

## 1. Termux简介

Termux 是一个 Android 下一个高级的终端模拟器，开源且不需要 root，支持 apt 管理软件包，十分方便安装软件包，完美支持 Python、 PHP、 Ruby、 Nodejs、 MySQL 等。随着智能设备的普及和性能的不断提升，如今的手机、平板等的硬件标准已达到了初级桌面计算机的硬件标准，用心去打造 DIY 的话完全可以把手机变成一个强大的极客工具。

- [官网](https://termux.com/)
- [github项目地址](https://github.com/termux/termux-app)

下载

- [F-Droid下载地址](https://f-droid.org/packages/com.termux/)

### 1.1 初始化

第一次启动 Termux 的时候需要从远程服务器加载数据，然而可能会遇到这种问题：

```
Ubable to install
Termux was unable to install the bootstrap packages.
Check your network connection and try again.
```

这里的 Termux 官方远程的服务器地址是: http://termux.net/bootstrap/

解决方案:

- 使用VPN
- 使用运营商流量
- 使用F-Droid版本

## 2. 基本操作

### 2.1 缩放文本

可以使用缩放手势来调整其字体大小。 对就是 「双指放大缩小」照片那样操作。

### 2.2 长按屏幕

长按屏幕会调出显示菜单项（包括复制、粘贴、更多），方便我们进行复制或者粘贴

`more`菜单的说明

```
长按屏幕
├── COPY:    # 复制
├── PASTE:   # 粘贴
├── More:    # 更多
   ├── Select URL:             # 提取屏幕所有网址
   └── Share transcipt:        # 分享命令脚本
   └── Reset:                  # 重置
   └── Kill process:           # 杀掉当前会话进程
   └── Style:                  # 风格配色 需要自行安装
   └── Keep screen on:         # 保持屏幕常亮
   └── Help:                   # 帮助文档
```

### 2.3 会话管理

显示隐藏式导航栏，可以新建、切换、重命名会话 session 和调用弹出输入法

### 2.4 常用按键

常用键是 PC 端常用的按键如: ESC 键、Tab 键、CTR 键、ALT 键，有了这些按键后可以提高我们日常操作的效率，所以 Termux 后面的版本默认都是显示这个扩展功能按键的。

打开和隐藏这个扩展功能按键目前有下面两种方法：

- 方法一
  - 从左向右滑动，显示隐藏式导航栏，长按左角的 `KEYBOARD`
- 方法二
  - 使用 `Termux` 快捷键: `音量+`+`Q` 键 或者 `音量+`+`K` 键

## 3. 基础知识

### 3.1 快捷键表

`Ctrl` 键是终端用户常用的按键，但大多数触摸键盘都没有这个按键，因此 Termux 使用`音量减小按钮`来模拟 `Ctrl` 键。
例如，在触摸键盘上按`音量减小` + `L` 就相当于是键盘上按 `Ctrl + L` 的效果一样，达到清屏的效果。

| 快捷键         | 功能                            |
| -------------- | ------------------------------- |
| Ctrl + A       | 将光标移动到行首                |
| Ctrl + C       | 中止当前进程                    |
| Ctrl + D       | 注销终端会话                    |
| Ctrl + E       | 将光标移动到行尾                |
| Ctrl + K       | 从光标删除到行尾                |
| Ctrl + U       | 从光标删除到行首                |
| Ctrl + L       | 清除终端                        |
| Ctrl + Z       | 挂起（发送 SIGTSTP 到）当前进程 |
| Ctrl + alt + C | 打开新会话（仅适用于 黑客键盘） |

`音量加键`也可以作为产生特定输入的`特殊键`.

| 快捷键     | 功能                                  |
| ---------- | ------------------------------------- |
| 音量加 + E | Esc 键                                |
| 音量加 + T | Tab 键                                |
| 音量加 + 1 | F1（`音量增加 + 2` → F2… 以此类推）   |
| 音量加 + 0 | F10                                   |
| 音量加 + B | Alt + B，使用 readline 时返回一个单词 |
| 音量加 + F | Alt + F，使用 readline 时转发一个单词 |
| 音量加 + X | Alt+X                                 |
| 音量加 + W | 向上箭头键                            |
| 音量加 + A | 向左箭头键                            |
| 音量加 + S | 向下箭头键                            |
| 音量加 + D | 向右箭头键                            |
| 音量加 + L | \|（管道字符）                        |
| 音量加 + H | 〜（波浪号字符）                      |
| 音量加 + U | _ (下划线字符)                        |
| 音量加 + P | 上一页                                |
| 音量加 + N | 下一页                                |
| 音量加 + . | Ctrl + \（SIGQUIT）                   |
| 音量加 + V | 显示音量控制                          |
| 音量加 + Q | 切换显示的功能键视                    |
| 音量加 + K | 切换显示的功能键视图                  |

### 3.2 基本命令

Termux 除了支持 `apt` 命令外，还在此基础上封装了 `pkg` 命令，`pkg` 命令向下兼容 `apt` 命令。`apt` 命令大家应该都比较熟悉了，这里直接简单的介绍下 `pkg` 命令:

```bash
pkg search <query>              # 搜索包
pkg install <package>           # 安装包
pkg uninstall <package>         # 卸载包
pkg reinstall <package>         # 重新安装包
pkg update                      # 更新源
pkg upgrade                     # 升级软件包
pkg list-all                    # 列出可供安装的所有包
pkg list-installed              # 列出已经安装的包
pkg show <package>              # 显示某个包的详细信息
pkg files <package>             # 显示某个包的相关文件夹路径
```

**建议使用 pkg 命令，因为 pkg 命令每次安装的时候自动执行 `apt update` 命令，还是比较方便的。**

### 3.3 软件安装

除了通过上述的 `pkg` 命令安装软件以外，如果我们有 `.deb` 软件包文件，也可以使用 `dpkg` 进行安装。

```bash
dpkg -i ./package.de         # 安装 deb 包
dpkg --remove [package name] # 卸载软件包
dpkg -l                      # 查看已安装的包
man dpkg                     # 查看详细文档
```

### 3.4 目录结构

```bash
echo $HOME
/data/data/com.termux/files/home

echo $PREFIX
/data/data/com.termux/files/usr

echo $TMPPREFIX
/data/data/com.termux/files/usr/tmp/zsh
```

### 3.5 端口查看

**安卓10以下**

```bash
# 查看所有端口
netstat -an

# 查看3306端口的开放情况
netstat -an|grep 3306
```

**安卓10以上**

Andorid 10 版本的 Termux 下无法正常使用 netstat -an 命令，解决方法是安装一个 nmap，然后扫描本地端口（弯道超车）:

```bash
# 安装nmap端口扫描神器
pkg install nmap

# 扫描本地端口
nmap 127.0.0.1
```

## 4. 进阶配置

### 4.1 更换国内源

使用 `pkg update` 更新一下的时候发现默认的官方源网速有点慢，在这个喧嚣浮躁的时代，我们难以静下心等待，这个时候就得更换成国内的 `Termux` 清华大学源了，加快软件包下载速度。

**方法一:自动替换**

```bash
sed -i 's@^\(deb.*stable main\)$@#\1\ndeb https://mirrors.tuna.tsinghua.edu.cn/termux/termux-packages-24 stable main@' $PREFIX/etc/apt/sources.list

sed -i 's@^\(deb.*games stable\)$@#\1\ndeb https://mirrors.tuna.tsinghua.edu.cn/termux/game-packages-24 games stable@' $PREFIX/etc/apt/sources.list.d/game.list

sed -i 's@^\(deb.*science stable\)$@#\1\ndeb https://mirrors.tuna.tsinghua.edu.cn/termux/science-packages-24 science stable@' $PREFIX/etc/apt/sources.list.d/science.list

pkg update
```

**方法二:手动修改**

请使用内置或安装在 Termux 里的文本编辑器，例如 `vi` / `vim` / `nano` 等直接编辑源文件，**不要使用 RE 管理器等其他具有 ROOT 权限的外部 APP** 来修改 Termux 的文件

编辑 `$PREFIX/etc/apt/sources.list` 修改为如下内容

```bash
# The termux repository mirror from TUNA:
deb https://mirrors.tuna.tsinghua.edu.cn/termux/termux-packages-24 stable main
```

编辑 `$PREFIX/etc/apt/sources.list.d/science.list` 修改为如下内容

```bash
# The termux repository mirror from TUNA:
deb https://mirrors.tuna.tsinghua.edu.cn/termux/science-packages-24 science stable
```

编辑 `$PREFIX/etc/apt/sources.list.d/game.list` 修改为如下内容

```bash
# The termux repository mirror from TUNA:
deb https://mirrors.tuna.tsinghua.edu.cn/termux/game-packages-24 games stable
```

**安装基础工具**

```bash
pkg update
pkg install vim curl wget git tree -y
```

### 4.2 终端配色方案

**脚本项目地址**：https://github.com/Cabbagec/termux-ohmyzsh/

该脚本主要使用了 `zsh` 来替代 `bash` 作为默认 shell，并且支持色彩和字体样式，同时也激活了外置存储，可以直接访问 SD 卡下的目录。主题默认为 agnoster，颜色样式默认为 Tango，字体默认为 Ubuntu。

**执行下面这个命令确保已经安装好了 curl 命令**

```bash
sh -c "$(curl -fsSL https://github.com/Cabbagec/termux-ohmyzsh/raw/master/install.sh)"  
```

如果因为不可抗力的原因，出现 `port 443: Connection refused` 网络超时的情况，那么执行下面国光迁移到国内的地址的命令即可：

```bash
sh -c "$(curl -fsSL https://html.sqlsec.com/termux-install.sh)"  
```

手机 App 默认只能访问自己的数据，如果要访问手机的存储，需要请求权限，如果你刚刚不小心点了拒绝的话，那么可以执行以下命令来重新获取访问权限：

```bash
termux-setup-storage
```

脚本允许后先后有如下两个选项:

```bash
Enter a number, leave blank to not to change: 14
Enter a number, leave blank to not to change: 6
```

分别选择`色彩样式`和`字体样式`，重启 Termux app 后生效配置。不满意刚刚的效果，想要继续更改配色方案的话，可以根据下面命令来更改对应的色彩配色方案：

**设置色彩样式**：

输入 `chcolor` 命令更换色彩样式，或者执行 `~/.termux/colors.sh` 命令

**设置字体**

运行 `chfont` 命令更换字体，或者执行 `~/.termux/fonts.sh` 命令

### 4.3 创建目录软连接

执行过上面的一键配置脚本后，并且授予 Termux 文件访问权限的话，会在家目录生成 `storage` 目录，并且生成若干目录，软连接都指向外置存储卡的相应目录：

**创建 QQ 文件夹软连接**

手机上一般经常使用手机 QQ 来接收文件，这里为了方便文件传输，直接在 `storage` 目录下创建软链接.
**QQ**

```bash
ln -s /data/data/com.termux/files/home/storage/shared/tencent/QQfile_recv QQ
```

**TIM**

```bash
ln -s /data/data/com.termux/files/home/storage/shared/tencent/TIMfile_recv TIM
```

这样可以直接在 `home` 目录下去访问 QQ 文件夹，大大提升了文件操作的工作效率。

### 4.4 定制常用按键

在 Termux v0.66 的版本之后我们可以通过 `~/.termux/termux.properties` 文件来定制我们的常用功能按键，默认是不存在这个文件的，我们得自己配置创建一下这个文件。

```bash
# 新建并编辑配置文件
vim ~/.termux/termux.properties
```

内容为:

```bash
extra-keys = [ \
 ['ESC','|','/','HOME','UP','END','PGUP','DEL'], \
 ['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN','BKSP'] \
]
```

**如果无法创建这个文件，那么得首先新建一下这个目录 `mkdir ~/.termux`**

可以直接输入特殊的字符串，例如上面的例子中的 `|` 就是一个字符串，此外 Termux 还有封装了一些特殊按键，入上面例子中的 `ESC` 就是 Termux 自带的按键，完整的特殊按键表如下：

| 按键       | 说明           |
| ---------- | -------------- |
| `CTRL`     | **`特殊按键`** |
| `ALT`      | **`特殊按键`** |
| `FN`       | **`特殊按键`** |
| ESC        | 退出键         |
| TAB        | 表格键         |
| HOME       | 原位键         |
| END        | 结尾键         |
| PGUP       | 上翻页键       |
| PGDN       | 下翻页键       |
| INS        | 插入键         |
| DEL        | 删除键         |
| BKSP       | 退格键         |
| UP         | 方向键 上      |
| LEFT       | 方向键 左      |
| RIGHT      | 方向键 右      |
| DOWN       | 方向键 下      |
| ENTER      | 回车键         |
| BACKSLASH  | 反斜杠 `\`     |
| QUOTE      | 双引号键       |
| APOSTROPHE | 单引号键       |
| F1~F12     | F1-F12 按键    |

上面列出的三个**特殊键**中的每一个最多只能在附加键定义中列出一次，超过次数将会报错。

### 4.5 zsh主题配色

编辑家目录下的`.zshrc` 配置文件

```bash
$ vim .zshrc
```

### 4.6 修改启动问候语(欢迎界面)

编辑问候语文件可以直接修改启动显示的问候语:

```bash
vim $PREFIX/etc/motd
```

### 4.7 SSH

OpenSSH 是 SSH （Secure SHell） 协议的免费开源实现。SSH 协议族可以用来进行远程控制， 或在计算机之间传送文件。Termux 官方已经封装好了，我们安装起来也会很简单：

```bash
pkg install openssh
```

#### 4.7.1 远程连接电脑

```bash
# ssh -p 端口号 用户名@主机名或者IP
ssh -p 22 user@hostname_or_ip

# ssh -i 私钥 用户名@主机名或者IP
ssh -i id_rsa user@hostname_or_ip
```

#### 4.7.2 传输文件

SSH 不仅仅可以远程连接服务器，同样也可以使用 SSH 自带的 `scp` 命令进行文件传输：

**复制文件**

```bash
# scp 本地文件路径 远程主机用户名@远程主机名或IP:远程文件保存的位置路径
scp local_file remote_username@remote_ip:remote_folder
```

**复制目录**

```bash
# scp -r 本地文件夹路径 远程主机用户名@远程主机名或IP:远程文件夹保存的位置路径
scp -r local_folder remote_username@remote_ip:remote_folder
```

#### 4.7.3 电脑 ssh 连接 Termux

实现这个效果有两大种方法：

1. SSH 通过密码认证连接
2. SSH 通过公私钥连接
   - PC 端生成公私钥，然后将 公钥 拷贝到 Termux 中，通过公私钥连接。
   - Termux 端生成公私钥，然后将 私钥拷贝到 PC 中，通过公私钥连接。

##### 4.7.3.1 启动 ssh 服务

安装完成后，`sshd` 服务默认没有启动，所以得手动启动下：

```bash
ssh-keygen -A
sshd
```

因为手机上面低的端口有安全限制，所以这里 openssh 默认的 sshd 默认的服务端口号为 8022

##### 4.7.3.2 通过密码认证链接

Termux 默认是使用密码认证进行连接的，如果要启用密码连接的话要确保你的密码足够安全

Termux 下的 SSH 默认配置文件的路径为 `$PREFIX/etc/ssh/sshd_config`，我们来查看下这个配置文件：

```sshd_config
PrintMotd no
PasswordAuthentication yes
Subsystem sftp /data/data/com.termux/files/usr/libexec/sftp-server
```

`PrintMotd` : 是否显示登录成功的欢迎信息 例如上次登入的时间、地点等

`PasswordAuthentication`: 是否启用密码认证

`Subsystem`: SFTP 服务相关的设定

##### 4.7.3.3 设置新密码

执行 `passwd` 命令可以直接修改密码：

```bash
passwd
```

##### 4.7.3.4 电脑远程连接测试

```bash
ssh 192.168.31.124 -p 8022
```

##### 4.7.3.5 通过公私钥连接

**首先在PC 端生成公私钥**

```bash
ssh-keygen
```

此时会在 `~/.ssh` 目录下生成 3 个文件
`id_rsa`， `id_rsa.pub`，`known_hosts`

然后需要把公钥 `id_rsa.pub` 拷贝到手机的 **data\data\com.termux\files\home.ssh** 文件夹中。然后

**将公钥拷贝到验证文件中**

在 `Termux` 下操作：

```bash
cat id_rsa.pub > authorized_keys
```

**关掉密码登录**

```bash
vim $PREFIX/etc/ssh/sshd_config
```

找到：

```bash
PasswordAuthentication yes 
```

修改为：

```bash
PasswordAuthentication no
```



## 5. 开发环境

Termux 支持的开发环境很强，可以完美的运行 C、Python、Java、PHP、Ruby 等开发环境。

### 5.1 编辑器

#### 5.1.1 Emacs

```bash
pkg install emacs
```

#### 5.1.2 nano

nano 是一个小而美的编辑器。具有如下：打开多个文件，每行滚动，撤消 / 重做，语法着色，行编号等功能

```bash
pkg install nano
```

#### 5.1.3 Vim

Vim 被称为编辑器之神，基本上 Linux 发行版都会自带 Vim，这个在前文基本工具已经安装了，如果你没有安装的话，可以使用如下命令安装

```bash
pkg install vim
```

并且官方也已经封装了 `vim-python`，对 Python 相关的优化。

```bash
pkg install vim-python
```

##### 5.1.3.1 解决汉字乱码

如果你的 Vim 打开汉字出现乱码的话，那么在家目录 (`~`) 下，新建`.vimrc` 文件

```bash
vim .vimrc
```

添加内容如下:

```bash
set fileencodings=utf-8,gb2312,gb18030,gbk,ucs-bom,cp936,latin1
set enc=utf8
set fencs=utf8,gbk,gb2312,gb18030
```

然后 `source` 下变量:

```bash
source .vimrc
```

##### 5.1.3.2 Vim配色

Termux Vim 自带了如下的配色

```bash
ls /data/data/com.termux/files/usr/share/vim/vim82/colors

desert.vim    morning.vim    shine.vim    blue.vim      elflord.vim   murphy.vim     slate.vim    darkblue.vim  evening.vim   pablo.vim      industry.vim  peachpuff.vim  torte.vim    delek.vim     koehler.vim   ron.vim        zellner.vim 
```

配色可以自己一个个尝试一下，还是向上面的汉字乱码那样，编辑家目录下的`.vimrc` 文件

```bash
vim ~/.vimrc
```

新增如下内容

```ini
set nu                " 显示行号
colorscheme desert    " 颜色主题
syntax on             " 打开语法高亮
```

### 5.2 Apache

Apache 是一个开源网页服务器软件，由于其跨平台和安全性，被广泛使用，是最流行的 Web 服务器软件之一。

**安装Apache**

```bash
pkg install apache2
```

**启动Apache**

```bash
apachectl start
```

然后浏览器访问: `http://127.0.0.1:8080` 访问是否成功启动：

Termux 自带的 Apache 的网站默认路径为：

`$PREFIX/share/apache2/default-site/htdocs/index.html`

**停止 Apache**

```bash
apachectl stop
```

**重启 Apache**

```bash
apachectl restart
```

**Apache 解析 PHP**

既然 Apache、PHP、MySQL 都可以成功安装的话，那么现在只要配置好 Apache 解析 PHP 之后就可以打造一个 Android 平台上的 LAMPP 平台了，配置本小节的内容得确保 Termux 已经配置好了 PHP 开发环境，没有配置好的可以参加下面 PHP 小节部分。

**安装 php-apache**

默认的 Apache 是无法解析 PHP 的，我们需要安装相应的包：

```bash
pkg install php-apache
```

**配置 Apache**

Termux 上的 Apache 默认配置文件的路径为:

`$PREFIX/etc/apache2/httpd.conf`

直接编辑配置文件:

```bash
vim /data/data/com.termux/files/usr/etc/apache2/httpd.conf
```

并在刚刚这个语句下方添加解析器，内容如下:

```properties
<FilesMatch \.php$>
  SetHandler application/x-httpd-php
</FilesMatch> 
```

接着继续往下找配置文件里面配置默认首页的地方，我们添加 `index.php` 到默认首页的规则里面:

```properties
<IfModule dir_module>
  DirectoryIndex index.php index.html
</IfModule>
```

这表示网站目录的默认首页是 index.php，如果没有 index.php 系统会自动寻找 index.html 做为默认首页了。

修改完 Apache 的配置文件后，记得使用 `apachectl restart` 重启 Apache 服务，然后这个时候回发现我们重启居然报错了：

```verilog
Apache is running a threaded MPM, but your PHP Module is not compiled to be threadsafe.  You need to recompile PHP.
AH00013: Pre-configuration failed
```

**解决 Apache PHP 报错**

先找到如下行,给他注释掉：

```properties
LoadModule mpm_worker_module libexec/apache2/mod_mpm_worker.so
```

然后找到如下行,取消注释:

```properties
#LoadModule mpm_prefork_module libexec/apache2/mod_mpm_prefork.so
```

**解析 PHP 测试**

在 Apache 的网站根目录下，创建一个 index.php ，测试一下 phpinfo () 函数能否正常运行:

```bash
echo '<?php phpinfo(); ?>' > $PREFIX/share/apache2/default-site/htdocs/index.php
```

然后浏览访问: `http://127.0.0.1:8080` 查看效果：

### 5.3 C语言

Termux 官方封装了 Clang，他是一个 C、C++、Objective-C 和 Objective-C++ 编程语言的编译器前端。

#### 5.3.1 安装 clang

```bash
pkg install clang
```

#### 5.3.2 编译测试

```c
#include <stdio.h>

int main(){
  printf("Hello World")
  return 0;
}
```

编辑完成后，使用 clang 来编译生成 hello 的可执行文件：

```bash
clang hello.c -o hello
```

### 5.4 Java

Termux 早期原生编译 JAVA 只能使用 `ecj` (Eclipse Compiler for Java) 和 `dx` 了，然后使用 Android 自带的 dalvikvm 运行。后面 Termux 官方也封装了 openjdk-17 这样安装起来就更方便了。

还有如果想要完整体验 JAVA 环境的话，另一个方法就是 Termux 里面安装一个完整的 Linux 系统，然后在 Linux 里面运行 Java。

#### 5.4.1 安装Openjdk-17

```bash
pkg update
pkg install openjdk-17
```

#### 5.4.2 安装编译工具

```bash
pkg install ecj dx -y
```

**编译**

```java
public class HelloWorld {
    public static void main(String[] args){
        System.out.println("Hello Termux");
    }
}
```

**编译生成 class 文件**

```bash
ecj HelloWorld.java
```

**编译生成 dex 文件**

```bash
dx --dex --output=hello.dex HelloWorld.class
```

**使用 dalvikvm 运行**

格式规范如下：`dalvikvm -cp dex文件名 类名`

```bash
dalvikvm -cp hello.dex HelloWorld
```

### 5.5 MariaDB (MySQL)

MariaDB 是 MySQL 关系数据库管理系统的一个复刻，由社区开发，有商业支持，旨在继续保持在 GNU GPL 下开源。开发这个分支的原因之一是：甲骨文公司收购了 MySQL 后，有将 MySQL 闭源的潜在风险，因此社区采用分支的方式来避开这个风险。

#### 5.5.1 安装MariaDB 

Termux 官方也封装了 MariaDB，所以安装起来很方便：

```bash
pkg install mariadb
```

这里基本上会安装很顺利，但是早期用户可能出现安装失败的情况，如果安装失败的话，这个时候手动在配置目录下创建 `my.cnf.d` 文件夹即可：

```bash
$ cd /data/data/com.termux/files/usr/etc/
$ mkdir my.cnf.d
```

#### 5.5.2 初始化数据库

早期的 Termux 安装完 MySQL 是需要初始化数据库的，新版本在安装时候就已经初始化了数据库

```bash
mysql_install_db
```

#### 5.5.3 启动 MySQL 服务

因为正常启动完成后，MySQL 这个会话就一直存活，类似与 Debug 调试一样，此时使用 `Ctrl + C` -> 中止当前进程也无济于事，体验式就一点都不优雅，所以这里国光使用 Linux 自带的 `nohup` 命令将其放到后台启动。

```bash
nohup mysqld &
```

#### 5.5.4 停止 MySQL 服务

Termux 下没有好的办法退出 MySQL 服务，只能强制杀掉进程了，使用如下命令格式可以轻松杀掉进程：

```bash
kill -9 `pgrep mysql`
```

### 5.6 Nginx

Nginx 是一个高性能的 Web 和反向代理服务器，Nginx 用的熟悉的话，下面搭建各种网站也就轻而易举了。

#### 5.6.1 安装 Nginx

```bash
pkg install nginx
```

#### 5.6.2 测试 Nginx

测试检查 Nginx 的配置文件是否正常:

```bash
nginx -t
```

#### 5.6.3 启动 Nginx

早期版本的 Termux 需要在 `termux-chroot` 环境下才可以成功启动 Nginx ，新版本的 Termux 可以直接启动，还是很方便的：

```bash
nginx
```

Termux 在 Nginx 上默认运行的端口号是 8080， 使用 `pgrep` 命令也可以查看 Nginx 进程相关的 PID 号。

然后手机本地直接访问 `http://127.0.0.1:8080` 查看 Nginx 是否正常启动：

#### 5.6.4 重启 Nginx

一般当修改完 Nginx 相关的配置文件时，我们需要重启 Nginx，使用如下命令即可重启:

```bash
nginx -s reload
```

#### 5.6.5 停止 Nginx

**方法一 原生停止**

```bash
nginx -s stop
```

或者

```bash
nginx -s quit
```

quit 是一个优雅的关闭方式，Nginx 在退出前完成已经接受的连接请求。Stop 是快速关闭，不管有没有正在处理的请求。

**方法二 杀掉进程**

```bash
kill -9 `pgrep nginx`
```

### 5.7 Nodejs

Node.js 是能够在服务器端运行 JavaScript 的开放源代码、跨平台 JavaScript 运行环境。

#### 5.7.1 安装 Nodejs

`nodejs-lts` 是长期支持版本，如果执行 `pkg install nodejs` 版本后，发现 npm 报如下错误:

```bah
segmentation fault
```

那么这个时候可以尝试卸载当前版本 `pkg uninstall nodejs` 然后执行下面命令安装长期稳定版本：

```bash
pkg install nodejs-lts
```

安装完成后使用如下命令查看版本信息：

```bash
node -V
npm -V
```

#### 5.7.2 http-server

http-server 是一个基于 Node.js 的简单零配置命令行 HTTP 服务器。

```bash
# 安装 http-server
npm install -g http-server

# 运行 http-server
http-server
```

## 6. 网站搭建

### 6.1 DVWA

DVWA 是一个用来搞 Web 安全从业者入门使用的一个练习靶场，用来学习掌握基本的漏洞原理使用的，如果你对 Web 安全不感兴趣的话可以直接跳过这一个小节。

### 6.2 Hexo

Hexo 是一个用 Nodejs 编写的快速、简洁且高效的博客框架。Hexo 使用 Markdown 解析文章，在几秒内，即可利用靓丽的主题生成静态网页。

#### 6.2.1 安装Hexo

Hexo 是用 Nodejs 编写的，所以安装的话得使用 npm 命令来安装：

```bash
npm install hexo-cli -g
```

#### 6.2.2 Hexo 基本部署

我们建立一个目录，然后到这个目录下初始化 Hexo 环境：

```bash
# 手动创建一个目录
mkdir hexo  

# 进入目录下并初始化Hexo环境
cd hexo  
hexo init  

#生成静态文件 启动Hexo
hexo g
hexo s      
```

#### 6.2.3 Hexo 部署到 Nginx

Hexo 是纯静态博客，官方默认把 Hexo 搭建在 Github Pages 仅仅是把 Hexo 根目录的 public 文件夹即 Hexo 生成的纯 HTML 源码部署到上面而已。所以知道这样原理 我们就可以轻而易举地将 Hexo 部署到 Nginx 下面。

##### 6.2.3.1 生成 HTML 纯静态源码

```bash
hexo g
```

##### 6.2.3.2 拷贝源码到 Nginx

现在我们只需要将 public 的文件夹里面的源码 全部拷贝到 Nginx 的网站根目录下：

```bash
# 在 nginx 根目录下新建 hexo 文件夹
mkdir $PREFIX/share/nginx/html/hexo

# 拷贝 源码到 nginx 下
cp -rf public/* $PREFIX/share/nginx/html/hexo
```

浏览器访问:`http://127.0.0.1:8080/hexo/` 即可看到效果：

当然这里网站的 CSS 等样式没有加载出来，这个原因是 Hexo 对网站目录下部署并不友好 ，大概有如下解决方法：

1. Nginx vhosts 配置多域名，这个服务器上常用的操作，但是 Termux 里面实现难度较高
2. 将 Hexo 的源码 直接拷贝到 Nginx 的根目录下，不用拷贝到 html/hexo 目录下了，然后直接访问 `http://127.0.0.1:8080` 即可看到效果

## 7. 系统安装

Termux 可以安装其他 Linux 发行版系统，核心用到的工具是 chroot ，所以我们得确保安装系统的时候 `proot` 这个包你是安装好的，然后因为操作系统店都有官方维护的脚本，所以安装起来甚至比我们前面配置的开发环境还要简单，下面来具体的介绍吧。

### 7.1 实用必备工具

可以在F-Droid 下载

| 软件                          | 下载地址                                     | 说明                       |
| ----------------------------- | -------------------------------------------- | -------------------------- |
| VNC Viewer 3.6.1.42089 汉化版 | [蓝奏云](https://sqlsec.lanzoux.com/ibq43wb) | 远程连接使用               |
| NetHunter KeX 4.0.7-6         | [蓝奏云](https://sqlsec.lanzoux.com/ibq4akb) | Kali 官方 远程连接工具     |
| AnLinux 6.10                  | [蓝奏云](https://sqlsec.lanzoux.com/ibq4iuj) | 提供比较全面的系统安装脚本 |
| AndroNix 4.2                  | Google Play                                  | 提供比较全面的系统安装脚本 |

### 7.2 国光Termux系统安装脚本

**Termux 安装 Linux 系统项目地址**：https://github.com/sqlsec/termux-install-linux

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/8d4a21f6504ccce1055bbdf62e80d8f0.jpg)

**确保 Termux 已经安装了 proot 和 Python3 才可以顺利安装**

```bash
git clone https://github.com/sqlsec/termux-install-linux
cd termux-install-linux
python termux-linux-install.py
```

## 8. 官方插件

### 8.1 TermuxAPI

Termux:API，可用于访问手机硬件实现更多的友情的功能。

#### 8.1.1 安装 Termux:API

**下载地址**

- [Termux:API F-Droid 下载地址](https://f-droid.org/packages/com.termux.api/)

#### 8.1.2 给 app 权限

因为 Termux-api 可以直接操作手机底层，所以我们需要到手机的设置里面给 这个 APP 的权限全部开了，这样下面操作的时候就不会提示权限不允许的情况了。

#### 8.1.3 安装 Termux-api 软件包

手机安装完 Termux-api 的 APP 后，Termux 终端里面必须安装对应的包后才可以与手机底层硬件进行交互。

```bash
pkg install termux-api
```

### 8.2 Termux:Boot

用于将自定义命令开机自启使用，不要每次重启完重复敲命令了。

#### 8.2.1 安装 Termux:Boot

- [Termux:Boot F-Droid 下载地址](https://f-droid.org/packages/com.termux.boot/)

#### 8.2.2 使用方法

安装完成启动这个应用程序后，创建 `~/.termux/boot/` 目录，将需要开机自启的脚本放在这个目录下面，如果有多个文件的话，将他们按照排序顺序执行，如果要确保设备进入睡眠状态，建议脚本前面先运行 `termux-wake-lock` 命令。

下面是一个开机自启 `sshd` 服务的的脚本，文件的完整路径为: `~/.termux/boot/start-sshd` 内容如下：

```bash
#!/data/data/com.termux/files/usr/bin/sh
termux-wake-lock
sshd
```

### 8.3 Termux:Float

可以将 Termux 悬浮窗形式显示，看上去比较酷炫。

#### 8.3.1 安装Termux:Float

**下载地址**

- [Termux: Float F-Droid 下载地址](https://f-droid.org/packages/com.termux.window/)

## 9. 其他

### 9.1 cmatrix

《黑客帝国》的代码雨视觉特效。

```bash
pkg install cmatrix
cmatrix
```

### 9.2 cowsay

cowsay 命令是一个有趣的命令，它会用 ASCII 字符描绘牛，羊和许多其他动物，还可以附带上个自定义文本，很巧的是 Termux 也封装了这个工具。

```bash
pkg intall cowsay
cowsay -f 动物 内容
```

内置如下动物：

```bash
$ cowsay -l list

Cow files in /data/data/com.termux/files/usr/share/cows:
beavis.zen bong bud-frogs bunny cheese cower daemon default dragon
dragon-and-cow elephant elephant-in-snake eyes flaming-sheep ghostbusters
head-in hellokitty kiss kitty koala kosh luke-koala meow milk moofasa moose
mutilated ren sheep skeleton stegosaurus stimpy three-eyes turkey turtle
tux vader vader-koala www
```

### 9.3 figlet

FIGlet 是创建一个简单的命令行实用程序，用于创建 ASCII logo。

```bash
pkg install figlet
figlet -f 字体 '文本内容'
```

内置如下样式：

```bash
ls $PREFIX/share/figlet

646-ca.flc   646-jp.flc   8859-7.flc      circle.tlf    mini.flf       smbraille.tlf
646-ca2.flc  646-kr.flc   8859-8.flc      digital.flf   mnemonic.flf   smmono12.tlf
646-cn.flc   646-no.flc   8859-9.flc      emboss.tlf    mono12.tlf     smmono9.tlf
646-cu.flc   646-no2.flc  ascii12.tlf     emboss2.tlf   mono9.tlf      smscript.flf
646-de.flc   646-pt.flc   ascii9.tlf      frango.flc    moscow.flc     smshadow.flf
646-dk.flc   646-pt2.flc  banner.flf      future.tlf    pagga.tlf      smslant.flf
646-es.flc   646-se.flc   big.flf         hz.flc        script.flf     standard.flf
646-es2.flc  646-se2.flc  bigascii12.tlf  ilhebrew.flc  shadow.flf     term.flf
646-fr.flc   646-yu.flc   bigascii9.tlf   ivrit.flf     slant.flf      upper.flc
646-gb.flc   8859-2.flc   bigmono12.tlf   jis0201.flc   small.flf      ushebrew.flc
646-hu.flc   8859-3.flc   bigmono9.tlf    koi8r.flc     smascii12.tlf  uskata.flc
646-irv.flc  8859-4.flc   block.flf       lean.flf      smascii9.tlf   utf8.flc
646-it.flc   8859-5.flc   bubble.flf      letter.tlf    smblock.tlf    wideterm.tlf
```

### 9.4 hollywood

在 Linux 终端中伪造好莱坞黑客屏幕，假装自己是一名黑客。

```bash
pkg install hollywood
hollywood
```

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/761b6165c40d0585c4bcdf0b65f99d61.png)

### 9.5 neofetch

Neofetch 是一个简单但有用的命令行系统信息工具。它会收集有关系统软硬件的信息，并在终端中显示结果。

```bash
pkg install neofetch
neofetch
```

### 9.6 nyancat

**彩虹貓**（英语： **Nyan Cat**）是在 2011 年 4 月上传在 Youtube 的视频，并且迅速爆红于网络，並在 2011 年 YouTube 浏览量最高的视频中排名第五，B 站这个小猫也很多，主要是 BGM 比较魔性，感兴趣的朋友可以自己去搜索看看。

```bash
pkg install nyancat
nyancat
```

使用 `Ctrl + C` 快捷键退出魔性循环

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/648127a7e49d51324a15d3758f0d21fb.png)

### 9.7 screenfetch

Screenfetch 是一个适用于 Linux 的小工具，用于显示系统信息及 ASCII 化的 Linux 发行版图标。

```bash
pkg install screenfetch
screenfetch
```

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/b8de75ee61695576e4def4fe7d20dd36.png)

显示其他 Linux 发行版的 logo：

```bash
screenfetch -A 发行版
```

现在内置的发行版 logo 有：

```properties
ALDOS, Alpine Linux, Amazon Linux, Antergos, Arch Linux (Old and Current
    Logos), ArcoLinux, Artix Linux, blackPanther OS, BLAG, BunsenLabs, CentOS,
    Chakra, Chapeau, Chrome OS, Chromium OS, CrunchBang, CRUX, Debian, Deepin,
    DesaOS,Devuan, Dragora, elementary OS, EuroLinux, Evolve OS, Sulin, Exherbo,
    Fedora, Frugalware, Fuduntu, Funtoo, Fux, Gentoo, gNewSense, Guix System,
    Hyperbola GNU/Linux-libre, januslinux, Jiyuu Linux, Kali Linux, KaOS, KDE neon,
    Kogaion, Korora, LinuxDeepin, Linux Mint, LMDE, Logos, Mageia,
    Mandriva/Mandrake, Manjaro, Mer, Netrunner, NixOS, OBRevenge, openSUSE, OS
    Elbrus, Oracle Linux, Parabola GNU/Linux-libre, Pardus, Parrot Security,
    PCLinuxOS, PeppermintOS, Proxmox VE, PureOS, Qubes OS, Raspbian, Red Hat
    Enterprise Linux, ROSA, Sabayon, SailfishOS, Scientific Linux, Siduction,
    Slackware, Solus, Source Mage GNU/Linux, SparkyLinux, SteamOS, SUSE Linux
    Enterprise, SwagArch, TinyCore, Trisquel, Ubuntu, Viperr, Void and Zorin OS and
    EndeavourOS
```

内置的操作系统 logo 有：

```bash
Dragonfly/Free/Open/Net BSD, Haiku, Mac OS X, Windows
```

### 9.8 sl

某编程牛人也经常犯把 ls 敲成 sl 的错误，所以他自己编了一个程序娱乐一下，这个程序的作用很简单，就是当你输入 sl 的时候终端会出现一个火车呼啸而过～～

```bash
pkg install sl
sl
```

### 9.9 toilet

toilet 能用字母拼写出更大字母的工具，具体拼出什么字由命令后面的参数决定，不仅如此，它还能打印出各种风格的效果，比如彩色，金属光泽等。

```bash
pkg install toilet
toilet -f 字体 -F 颜色参数 '文本信息'
```

内置如下字体：

```bash
$ ls $PREFIX/share/figlet

ascii12.tlf     bigmono12.tlf  emboss2.tlf  mono9.tlf      smblock.tlf    wideterm.tlf
ascii9.tlf      bigmono9.tlf   future.tlf   pagga.tlf      smbraille.tlf
bigascii12.tlf  circle.tlf     letter.tlf   smascii12.tlf  smmono12.tlf
bigascii9.tlf   emboss.tlf     mono12.tlf   smascii9.tlf   smmono9.tlf
```

内置如下颜色效果：

```bash
$ toilet --filter list

Available filters:
"crop": crop unused blanks
"gay": add a rainbow colour effect
"metal": add a metallic colour effect
"flip": flip horizontally
"flop": flip vertically
"180": rotate 180 degrees
"left": rotate 90 degrees counterclockwise
"right": rotate 90 degrees clockwise
"border": surround text with a border
```

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/e2785afd6b415b6e6a8afd75c60ff9b7.png)

### 9.10 终端二维码

Linux 命令行下的二维码，主要核心是这个网址：`http://qrenco.de/`

```bash
echo "http:www.baidu.com" |curl -F-=\<- qrenco.de
```

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/e263d34d36d55da4f527ed2f60a5b608.png)

