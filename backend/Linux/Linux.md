

## 1. Linux概述

### 1.1 Linux的诞生

Linux的诞生

Linux创始人: 林纳斯托瓦兹

Linux诞生于1991年，作者上大学期间因为创始人在上大学期间经常需要浏览新闻和处理邮件，发现现有的操作系统不好用，于是他决心自己写一个保护模式下的操作系统，这就是Linux的原型，当时他21岁，后来经过全世界网友的支持，现在能够兼容多种硬件，成为最为流行的服务器操作系统之一。

### 1.2 Linux内核

Linux系统的组成如下:

- Linux系统内核
- 系统级应用程序

两部分组成。

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/ff9cd9b5f21336a8169afb4e26b76a0b.png)

- 内核提供系统最核心的功能，如:调度CPU、调度内存、调度文件系统、调度网络通讯、调度lO等。
- 系统级应用程序，可以理解为出厂自带程序，可供用户快速上手操作系统，如:文件管理器、任务管理器、图片查看、音乐播放等。

可以看出，内核是Linux操作系统最核心的所在，系统级应用程序只是锦上添花。Linux内核是免费开源的，任何人都可以下载内核源码并查看且修改。

可以通过:https://www.kernel.org 去下载Linux内核



### 1.3 Linux发行版

内核是免费、开源的，这也就代表了:

- 任何人都可以获得并修改内核，并且自行集成系统级程序
- 提供了内核+系统级程序的完整封装，称之为Linux发行版

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/9798f378072dfe98587511d559945981.png)

任何人都可以封装Linux，目前市面上有非常多的Linux发行版，常见的如下

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/da4bf0b73234ac9bdefe929f5a72a41b.png)



### 1.4 图形化、命令行

对于操作系统的使用，有2种使用形式:

- 图形化页面使用操作系统
- 以命令的形式使用操作系统

不论是Windows还是Linux亦或是MacOS系统，都是支持这两种使用形式。

- 图形化:使用操作系统提供的图形化页面，以获得图形化反馈的形式去使用操作系统。
- 命令行:使用操作系统提供的各类命令，以获得字符反馈的形式去使用操作系统。

无论是企业开发亦或是个人开发，使用Linux操作系统，多数都是使用的:命令行。



### 1.5 远程连接Linux

下载XShell
https://www.xshell.com/zh/free-for-home-school/

1. 新建会话

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/b46d5d1e21aa3a6eb58e52e1195cbab7.png)

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/2f7c08004d64ac34c62c7d87be3e7514.png)

2. 成功连接，输入指令

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/9695ce9c21bced92ce8996fc6a6813a0.png)



### 1.6 WSL(Windows子系统)

WSL:

- Windows Subsystem for Linux，是用于Windows系统之上的Linux子系统。
- 作用很简单，可以在Windows系统中获得Linux系统环境，并完全直连计算机硬件，无需通过虚拟机虚拟硬件。

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/b5f3cd740aa90faa445a8cc3e76fe841.png)

简而言之:

- Windows10的WSL功能，可以无需单独虚拟一套硬件设备就可以直接使用主机的物理硬件，构建Linux操作系统并不会影响windows系统本身的运行

---

微软商店下载安装

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/9f3f39d0086c608b43b089a9c9b6b38f.png)

安装完整打开配置

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/29b3b67a375c2fcda478d2abaf41a7ce.png)

使用Win11自带的Windows Terminal打开ubuntu

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/01e0bb23bfa69c26543c6f546d8432be.png)

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/ba5ce03b5973545d775c7bdb62c43c4e.png)



## 2. Linux目录结构

### 2.1 目录结构

目录结构

- Linux的目录结构是一个树型结构
- Windows系统可以拥有多个盘符，如C盘、D盘、E盘
- Linux没有盘符这个概念,只有一个根目录l,所有文件都在它下面

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/e5ebf24c5d608cef60342b91cd9b62f9.png)

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/c1925e6a30f09b9359b451d8184a41a5.png)

### 2.2 路径描述

路径描述

- 在Linux系统中，路径之间的层级关系，使用:`/`来表示
- 在Windows系统中，路径之间的层级关系，使用:`\`来表示

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/c70de4a90fa5cdeb31f7dd1cb5d51dfe.png)

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/d69506eca57630252b58178d137fa3a9.png)



## 3. Linux基础命令

### 3.1 命令

命令与命令行

- 命令行:即Linux终端(Terminal)，是一种命令提示符页面。以纯“字符”的形式操作系统，可以使用各种字符化命令对系统发出操作指令。
- 命令:即Linux程序。一个命令就是一个Linux的程序。命令没有图形化页面,可以在命令行(终端中)提供字符化的反馈。

---

命令基础格式

无论是什么命令，用于什么用途，在Linux中，命令有其通用的格式:

```bash
command [-options] [parameter]
```

- command 命令本身
- -options:命令的一些选项，可以通过选项控制命令的行为细节
- parameter:命令的参数，多数用于命令的指向目标等



### 3.1 ls命令

ls命令的作用是列出目录下的内容，语法细节如下:

```bash
ls [-a -l -h] [Linux路径]
```

- -a -l -h是可选的选项
  - `-a`，可以展示出隐藏的内容（以.开头的文件或文件夹默认被隐藏）
  - `-l`，以列表的形式展示内容，并展示更多细节
  - `-h`，需要和-l搭配使用，以更加人性化的方式显示文件的大小单位

- Linux路径是此命令可选的参数

当不使用选项和参数,直接使用ls命令本体，表示:以平铺形式，列出当前工作目录下的内容

---

ls命令选项的组合使用

写法：

- `ls -l -a`
- `ls -la`
- `ls -al`

上述三种写法，都是一样的，表示同时应用`-l`和`-a`的功能

### 3.2 HOME目录和工作目录

- 当前登录用户的HOME目录作为当前工作目录，所以`ls`命令列出的是HOME目录的内容

- HOME目录:每个Linux操作用户在Linux系统的个人账户目录，路径在:`/home/用户名`

### 3.3 cd  和 pwd 命令

cd切换工作目录

- 当Linux终端（命令行）打开的时候，会默认以用户的`HOME`目录作为当前的工作目录，我们可以通过`cd`命令，更改当前所在的工作目录
- 语法：`cd [Linux路径]`
- cd命令无需选项，只有参数，表示要切换到哪个目录下
- cd命令直接执行，不写参数，表示回到用户的`HOME`目录

---

pwd命令查看当前工作目录

- 我们可以通过`pwd`命令，来查看当前所在的工作目录

### 3.4 相对路径和绝对路径

绝对路径

- 以根目录为起点，描述路径的一种写法，路径描述以`/`开头

相对路径

- 以当前目录为起点，描述路径的一种写法，路径描述无需以`/`开头

### 3.5 特殊路径符

特殊路径符

- `.` 表示当前目录，比如`cd ./Desktop`表示切换到当前目录下的`Desktop`目录内，和`cd Desktop`效果一致
- `..` 表示上一级目录，比如`cd ..`即可切换到上一级目录，`cd ../..`切换到上二级目录
- `~` 表示`HOME`目录，比如 `cd ~`即可切换到`HOME`目录或`cd ~/DeSktop`，切换到`HOME`内的`Desktop`目录

### 3.6 mkdir命令

通过`mkdir`命令可以创建新的目录

语法

- `mkdir [-p] Linux路径`

  - 参数必填，表示Linux路径，即要创建的文件夹的路径，相对路径或绝对路径均可
  - `-p`选项可选，表示自动创建不存在的父目录，使用于创建连续多层级的目录

  

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/3e10b48025b0300dc44a1dff433b5800.png)

### 3.7 touch命令

可以通过`touch`命令创建文件

语法

- `touch Linux路径`
  - `touch`命令无选项，参数必填，表示要创建的文件路径

### 3.8 cat 和 more 命令

通过`cat`命令查看文件内容

语法

- `cat Linux路径`

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/8c060b4437ac435559fd0112f75a3542.png)

---

`more`命令也可以查看文件内容，但是

- `cat`是直接将内容全部显示出来
- `more`支持翻页，如果文件内容过多，可以一页页的展示

语法

- `more Linux路径`

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/64adb03424123fbe38bb98ceb5aafde4.png)

### 3.9 cp mv rm 命令

`cp`命令可以用于复制文件或文件夹

语法

- `cp [-r] 参数1 参数2`
  - `-r`选项，可选，用于复制文件夹使用，表示递归
  - 参数1，Linux路径，表示被复制的文件或文件夹
  - 参数2，Linux路径，表示要复制到的地方

---

`mv`命令可以用于移动文件或文件夹

语法

- `mv 参数1 参数2`
  - 参数1，Linux路径，表示被移动的文件或文件夹
  - 参数2，Linux路径，表示被移动去的路径，如果目标不存在，则进行改名，确保目标存在

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/0059176a3b275b93e16e4c8ad44a124f.png)

---

rm命令可用于删除文件、文件夹

语法

- `rm [-r -f] 参数1 参数2 ... 参数N`
  - 通`cp`命令一样，`-r`选项用于删除文件夹
  - `-f`表示force，强制删除
    - 普通用户删除内容不会弹出提示，只有root管理员用户删除内容会有提示
  - 参数1、参数2、...、参数N表示要删除的文件或文件夹路径，按照空格隔开

通配符

`rm`命令支持通配符`*`,用来做模糊匹配

- 符号`*`表示通配符，级匹配任意内容，例如
  - `test*`，表示匹配任何以test开头的内容
  - `*test`，表示匹配任何以test结尾的内容
  - `*test*`，表示匹配任何包含test的内容

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/4f1ee4a0759ba85885fe8e9e556254ad.png)

### 3.10 which find命令

可以通过`which`命令，查看所使用的一系列命令的程序文件存放在哪里

语法

- `which 要查找的命令`

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/8e3c93f2179923f1ee985e010077c2ca.png)

---

可以通过`find`命令去搜索指定的文件。

语法

- `find 起始位置 -name "被查找文件名"`	按文件名查找
- `find 起始位置 -size +|-n[kMG]`  按文件大小查找
  - `+、-`表示大于和小于
  - `n`表示大小数字
  - `kMG`表示大小单位，k表示kb，M表示Mb，G表示Gb

为了确保后续演示，拥有最大的权限，可以在整个系统完成搜索我们可以切换到root用户以获得管理员权限

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/84cacb9f5da7ff91cdaa46229f8fba68.png)

`find`命令也可以使用通配符进行模糊查找

### 3.11 grep、wc和管道符

可以通过`grep`命令，从文件中通过关键字过滤文件行。

语法:

- `grep [-n]关键字 文件路径`
  - 选项`-n`，可选，表示在结果中显示**匹配的行的行号**。
  - 参数，关键字，必填，**表示过滤的关键字**，带有空格或其它特殊符号，建议使用””将关键字包围起来
  - 参数，文件路径，必填，表示要过滤内容的文件路径，可作为内容输入端口

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/da5f78d7e327d8e47532b5bf2a1198d6.png)

---

可以通过wc命令统计文件的行数、单词数量等

语法: 

- `wc [-c -m -l -w] 文件路径`
  - 选项，`-c`，统计bytes数量
  - 选项，`-m`，统计字符数量
  - 选项，`-l`，统计行数
  - 选项，`-w`，统计单词数量
  - 参数，文件路径，被统计的文件，可作为内容输入端口

---

管道符：`|`

管道符的含义是:**将管道符左边命令的结果，作为右边命令的输入**

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/afabc93066736a4a147b99932b2a5dba.png)

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/2b54b19a316ec2546be2070c03d7f545.png)

### 3.12 echo、反引号`、tail命令、重定向符号

可以使用`echo`命令在命令行内输出指定内容

语法:

- `echo输出的内容`
  - 无需选项，只有一个参数，表示要**输出的内容**，复杂内容可以用`””`包围

---

反引号`

被`包围的内容，会被作为命令执行，而非普通字符

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/9666df6711a3c8cbb36f2bb10a4ab5ab.png)

---

重定向符

重定向符

- `>`，将左侧命令的结果，**覆盖**写入到符号右侧指定的文件中
- `>>`，将左侧命令的结果，**追加**写入到符号右侧指定的文件中

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/d4cb8da33a5d19fbb0bb2a0eac04de43.png)

---

tail命令

使用`tail`命令，可以查看文件尾部内容，跟踪文件的最新更改

语法

- `tail [-f -num] Linux路径`
  - 参数，Linux路径，表示被跟踪的文件路径
  - 选项，`-f`，表示**持续跟踪**
  - 选项，`-num`，表示，**查看尾部多少行**，不填默认10行

## 4. vi/vim编辑器

### 4.1 vi/vim编辑器介绍

vi\vim是visual interface的简称，是Linux中最经典的文本编辑器

- 同图形化界面中的文本编辑器一样，vi是命令行下对文本文件进行编辑的绝佳选择
- vim是vi的加强版本，兼容vi的所有指令，不仅能编辑文本，而且还具有shell程序编辑的功能，可以不同颜色的字体来辨别语法的正确性，极大方便了程序的设计和编辑性。

### 4.2 vi/vim的编辑器的三种工作模式

命令模式(Command mode)

- 命令模式下，所敲的按键编辑器都理解为命令，以命令驱动执行不同的功能。此模式下，不能自由进行文本编辑。

输入模式( lnsert mode)

- 也就是所谓的编辑模式、插入模式。
  此模式下，可以对文件内容进行自由编辑。

底线命令模式( Last line mode)

- 以`:`开始，通常用于文件的保存、退出。

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/b81ea81e7bf8075ab03b6d02057693b2.png)

### 4.2 命令模式

如果需要通过vi/vim编辑器编辑文件，请通过如下命令

`vi 文件路径`

`vim 文件路径`

vim兼容全部的vi功能，后续全部使用vim命令

- 如果文件路径表示的文件不存在，那么此命令会用于编辑新文件
- 如果文件路径表示的文件存在，那么此命令用于编辑已有文件

---

命令模式快捷键

| 模式     | 命令             | 描述                                |
| -------- | ---------------- | ----------------------------------- |
| 命令模式 | `i`              | 在当前光标位置进入`输入模式`        |
| 命令模式 | `a`              | 在当前光标位置之后进入`输入模式`    |
| 命令模式 | `I`              | 在当前行的开头，进入`输入模式`      |
| 命令模式 | `A`              | 在当前行的结尾，进入`输入模式`      |
| 命令模式 | `o`              | 在当前光标下一行进入`输入模式`      |
| 命令模式 | `0`              | 在当前光标上一行进入`输入模式`      |
| 输入模式 | `esc`            | 任何情况下输入`esc`都能回到命令模式 |
| 命令模式 | `键盘上、键盘k`  | 向上移动光标                        |
| 命令模式 | `键盘下、键盘j`  | 向下移动光标                        |
| 命令模式 | `键盘左、键盘h`  | 向左移动光标                        |
| 命令模式 | `键盘右、键盘l`  | 向后移动光标                        |
| 命令模式 | `0`              | 移动光标到当前行的开头              |
| 命令模式 | `$`              | 移动光标到当前行的结尾              |
| 命令模式 | `pageup(PgUp)`   | 向上翻页                            |
| 命令模式 | `pageDown(PgDn)` | 向下翻页                            |
| 命令模式 | `/`              | 进入搜索模式                        |
| 命令模式 | `n`              | 向下继续搜索                        |
| 命令模式 | `N`              | 向上继续搜索                        |
| 命令模式 | `dd`             | 删除光标所在行的内容                |
| 命令模式 | `ndd`            | n是数字，表示删除当前光标向下n行    |
| 命令模式 | `yy`             | 复制当前行                          |
| 命令模式 | `nyy`            | n是数字，复制当前行和下面的n行      |
| 命令模式 | `p`              | 粘贴复制的内容                      |
| 命令模式 | `u`              | 撤销修改                            |
| 命令模式 | `ctrl + r`       | 反向撤销修改                        |
| 命令模式 | `gg`             | 跳到首行                            |
| 命令模式 | `G`              | 跳到行尾                            |
| 命令模式 | `dG`             | 从当前行开始，向下全部删除          |
| 命令模式 | `dgg`            | 从当前行开始，向上全部删除          |
| 命令模式 | `d$`             | 从当前光标开始，删除到本行的结尾    |
| 命令模式 | `d0`             | 从当前光标开始，删除到本行的开头    |

### 4.3 底线命令模式

| 模式         | 命令         | 描述         |
| ------------ | ------------ | ------------ |
| 底线命令模式 | `:wq`        | 保存并退出   |
| 底线命令模式 | `:q`         | 仅退出       |
| 底线命令模式 | `:q!`        | 强制退出     |
| 底线命令模式 | `:w`         | 仅保存       |
| 底线命令模式 | `:set nu`    | 显示行号     |
| 底线命令模式 | `:set paste` | 设置粘贴模式 |

 

## 5. Linux用户和权限

### 5.1 root用户

无论是windows、MacOS、Linux均采用多用户的管理模式进行权限管理。。

- 在Linux系统中,拥有最大权限的账户名为: root(超级管理员)，而在前期，我们一直使用的账户是普通的用户: user
- root用户拥有最大的系统操作权限,而普通用户在许多地方的权限是受限的。
- 普通用户的权限，一般在其HOME目录内是不受限的，一旦出了HOME目录,大多数地方，普通用户仅有只读和执行权限,无修改权限

---

su和exit命令

su命令就是用于账户切换的系统命令,其来源英文单词:Switch User

语法: 

su `[-][用户名]`

- `-`符号是可选的，表示是否在切换用户后加载环境变量，建议带上
- 参数:用户名，表示要切换的用户，用户名也可以省略,省略表示切换到root
- 切换用户后，可以通过exit命令退回上一个用户，也可以使用快捷键: ctrl + d
- 使用普通用户，切换到其它用户需要输入密码，如切换到root用户
- 使用root用户切换到其它用户，无需密码,可以直接切换



### 5.2 sudo命令

可以通过`sudo`命令，为普通的命令授权，临时以`root`身份授权

语法

- `sudo 其他命令`
  - 在其它命令之前，带上sudo,即可为这一条命令临时赋予root授权
  - 但是并不是所有的用户，都有权利使用sudo，我们需要为普通用户配置sudo认证

---

为普通用户配置sudo认证

- 切换到root用户,执行`visudo`命令,会自动通过vi编辑器打开`/etc/sudoers`

- 在文件的最后添加

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/70ffbccc4eb78bbdea7f19636f60a295.png)

- 切换普通用户 使用`sudo 其他命令`

### 5.3 用户、用户组

用户、用户组

Linux系统中可以

- 配置多个用户
- 配置多个用户组
- 用户可以加入多个用户组

Linux中关于权限的管控级别分别由2个

- 针对用户的权限控制
- 针对用户组的权限控制

比如,针对某文件，可以控制用户的权限，也可以控制用户组的权限。

---

用户组管理

- 创建用户组
  - `groupadd 用户组名`
- 删除用户组
  - `groupdel 用户组名`

---

用户管理

- 创建用户
  - `useradd [-g -d] 用户名`
    - 选项：`-g`指定用户的组，不指定`-g`，会创建同名组并自动加入，指定`-g`需要组已经存在，如已经存在同名组，必须用`-g`
    - 选项：`-d`指定用户HOME路径，不指定美国，HOME目录默认在` /home/用户名`

- 删除用户
  - `userdel [-r] 用户名`
    - 选项：`-r`，删除用户的HOME目录，不使用`-r`，删除用户时，HOME目录保留
- 查看用户所属组
  - `id [用户名]`
    - 参数：用户名，被查看的用户，如果不提供则查看自身
- 修改用户所属组
  - `usermod -aG 用户组 用户组`将指定用户加入用户组 
- 查看当前系统又那些用户
  - `getent passwd`

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/3e87fa04e90844967f5c5c34562c076b.png)

显示有七份信息

用户名：密码(x):用户ID:组ID:描述信息(无用):HOME目录:执行终端(默认bash)

### 5.4 权限信息

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/7b74c2bdb6d40a160b6af01d597639c4.png)

- 序号1,表示文件、文件夹的权限控制信息
- 序号2,表示文件、文件夹所属用户
- 序号3,表示文件、文件夹所属用户组

---

认识权限信息

权限细节总共分为10个槽位

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/6d955e2df3192c99361c275a9be5a41d.png)

例如：drwxr-xr-x

- 这是一个文件夹，首字母d表示
- 所属用户（u）(右上角图序号2)的权限是:有r有w有x, rwx
- 所属用户组（g）(右上角图序号3)的权限是:有r无w有x, r-x( -表示无此权限)
- 其它用户（o)的权限是:有r无w有x, r-x

rwx

- r表示读权限
- w表示写权限
- x表示执行权限

### 5.5 修改权限控制

chmod

通过`chmod`命令，修改文件、文件夹的权限信息

注意，只有文件、文件夹的所属用户或root用户可以修改。

语法: 

- `chmod [-R] 权限 文件或文件夹`
  - 选项: `-R`，对文件夹内的全部内容应用同样的操作

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/c9868de4472477ac906fe1fb1e28bc63.png)

---

权限的数字序号

权限可以用3位数字来代表,第一位数字表示用户权限
，第二位表示用户组权限，第三位表示其它用户权限。
数字的细节如下:r记为4, w记为2,x记为1，可以有:

- 0:无任何权限，即---
- 1:仅有x权限，即--x
- 2:仅有w权限，即-w-
- 3:有w和x权限，即–wx
- 4:仅有r权限，即r--
- 5:有r和x权限,即r-x
- 6:有r和w权限即rw-
- 7:有全部权限即rwx

所以上面的命令可以写成

- `chmod 751 test.txt`

---

chown命令

使用chown命令，可以修改文件、文件夹的所属用户和用户组
普通用户无法修改所属为其它用户或组,所以此命令只适用于root用户执行

语法

- `chown [-R] [用户][:][用户组] 文件或文件夹`
  - 选项，-R，同chmod,对文件夹内全部内容应用相同规则
  - 选项，用户，修改所属用户
  - 选项，用户组,修改所属用户组
  - `:`用于分隔用户和用户组



## 6. Linux常用操作

### 6.1 各类操作

1. `ctrl + c` 强制停止

2. `ctrl + d` 退出账户的登录，或者退出某些特定程序的专属界面
3. 通过`history`命令，查看历史输入过的命令

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/2771a96f69447ad33769286527b4e2b1.png)

4. 通过`!`命令前缀，自动执行上一次匹配前缀的命令

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/eb421fc3828ef91158c3c8ac02a0f958.png)

5. 通过快捷键`ctrl + r`输入内容去匹配历史命令

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/d892c73844d3f8f2e89eacc6497b4814.png)

6. 光标移动
   1. `ctrl + a`，跳到命令开头
   2. `ctrl + e`，跳到命令结尾
   3. `ctrl + 方向左键`，向左跳一个单词
   4. `strl + 方向右键`，向右跳一个单词
7. 清屏
   1. 快捷键`ctrl + l`
   2. 命令`clear`

### 6.2 软件安装

Linux系统”应用商店“`yum`

---

yum命令

yum:

- RPM包软件管理器，用于自动化安装配置Linux软件，并可以自动解决依赖问题。
- 语法：`yum [-y] [install | remove | search] 软件名称`
  - 选项：`-y`，自动确认，无需手动确认安装或卸载
  - `install`：安装
  - `remove`：卸载
  - `search`：搜索
- yum命令需要root权限，可以su切换到root,或使用sudo提权。
- yum命令需要联网

---

通过回滚事务卸载应用

> 一般安装软件会安装一系列的依赖项，通过事务回滚可以直接全部删除

1. 查看yum操作（事务）应用

```bash
sudo yum history list
```

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/53f1f2140545b5cdb4b1b1487c5dc429.png)

2. 查看某个事务的详细信息

```bash
sudo yum history info 子命令
```

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/3118ae773e1ca8c278eaaa640b6af126.png)

3. 回滚事务（删除）

```bash
yum history undo 子命令
```

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/4c8b5c4154d55592e060c5474ce7e4d7.png)

---

apt命令

- CentOS使用yum管理器,ubuntu使用apt管理器
- 语法
  - `apt [-y] [install | remove |search] 软件名称`
  - 用法与`yum`一致

### 6.3 systemctl 命令控制软件启动关闭

Linux系统很多软件(内置或第三方)均支持使用systemctl命令控制:启动、停止、开机自启

能够被systemctl管理的软件，一般也称之为:服务

语法

- `systemctl start | stop | status | enable | disable 服务名`

常见的系统内置服务

- NetworkManager,主网络服务
- network，副网络服务
- firewalld，防火墙服务
- sshd，ssh服务

### 6.4 软连接

在系统中创建软链接，可以将文件、文件夹链接到其它位置。类似Windows系统的快捷方式

语法

- `ln -s 参数1 参数2`
  - `-s`选项，创建软连接
  - 参数1：被连接的文件或文件夹
  - 参数2：要连接去的路径

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/fc7d8af060a72b3394a9d48d68475dc8.png)

### 6.5 日期和时区

date命令

- 通过date命令可以在命令行中查看系统的时间
- 语法
  - `date [-d] [格式化字符串]`
  - `-d` 按照给定的字符串显示七日，一般用于日期计算
  - 格式化字符串：通过特定的字符串标记，来控制显示的日期格式
    - `%Y`年
    - `%y` 年份后两位数字
    - `%d`月份
    - `%d`日
    - `%H`小时
    - `%M`分钟
    - `%S`秒
    - `%s`自1970-01-01 00:00:00 UTC到现在的秒数

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/19e4335ece3df324450a3b557d7dfa99.png)

---

date命令进行日期加减

- `-d`，可以按照给定的字符串显示日期
- 其中支持的时间表示为
  - year
  - month
  - day
  - hour
  - minute
  - second
- 可以和格式化字符串一起使用

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/4a654bad078c93f4b855850fb970b8f8.png)

---

修改Linux时区

使用root权限，执行如下命令，修改时区为东八区

```bash
rm -f /etc/localtime
sudo ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
```

将系统自带的localtime文件删除,并将/usr/share/zoneinfo/Asia/Shanghai文件链接为localtime文件即可

---

ntp程序

可以通过ntp程序自动校准系统时间

安装ntp，启动并设置开启自启

- `systemctl start ntpd`
- `systemctl enable ntpd`

当ntpd启动后会定期的帮助我们联网校准系统时间

也可以手动校准`ntpdate -u ntp.aliyun.com`

### 6.6 IP地址和主机名

- 每一台联网的电脑都会有一个地址，用于和其它计算机进行通讯
- IP地址主要有2个版本,V4版本和V6版本
- IPv4版本的地址格式是: a.b.c.d,其中abcd表示0~255的数字，如192.168.88.101就是一个标准的IP地址
- 可以通过命令:` ifconfig`,查看本机的ip地址，如无法使用`ifconfig`命令,可以安装: `yum -y install net-tools`

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/0ab8f625aa0eeb99caea5b70a34c6aa1.png)

---

特殊的IP地址

- 127.0.0.1，这个IP地址用于代指本机
- 0.0.0.0，特殊IP地址
  - 可以用于指代本机
  - 可以在端口绑定中用来确定绑定关系
  - 在一些IP地址限制中,表示所有IP的意思，如放行规则设置为0.0.0.0，表示允许任意IP访问

---

主机名

每一台电脑除了对外联络地址（IP地址)以外，也可以有
一个名字，称之为主机名，无论是Windows或Linux系统,都可以给系统设置主机名

- Windows

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/4ed2c778c7cf61222bfc176ac380f1f3.png)

- Linux

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/67a3fe4f584bac9e9c2adec9daf24636.png)

修改主机名`hostnamectl set-hostname 主机名`

---

域名解析

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/39f8ba200a92c915fa8b68037da7725c.png)

配置主机名映射

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/50e884cc49b980aefcfbc660e1bb22a7.png)

---

配置固定IP

当前我们虚拟机的Linux操作系统,其IP地址是通过DHCP服务获取的。
DHCP

- 动态获取IP地址，即每次重启设备后都会获取一次,可能导致IP地址频繁变更

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/e00b92ccbeaa222022dcaf562748c5af.png)

### 6.7 网络请求和下载

可以通过ping命令,检查指定的网络服务器是否是可联通状态

语法: 

- `ping [-c num] ip或主机名`
  - 选项: `-c`,检查的次数，不使用-c选项,将无限次数持续检查
  - 参数: ip或主机名，被检查的服务器的ip地址或主机名地址

---

wget命令

wget是非交互式的文件下载器，可以在命令行内下载网络文件

语法: 

- `wget [-b] url`
  - 选项:`-b`,可选，后台下载，会将日志写入到当前工作目录的wget-log文件
  - 参数: `url`，下载链接

---

curl命令

curl可以发送http网络请求,可用于:下载文件、获取信息等

语法: 

- `curl [-O] url`
  - 选项:`-О`，用于下载文件，当url是下载链接时，可以使用此选项保存文件
  - 参数: `url`，要发起请求的网络地址

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/fed4a0c4d2e16f4d133708263fbb5cc6.png)

### 6.8 端口

端口

- 是设备与外界通讯交流的出入口。端口可以分为:物理端口和虚拟端口两类
- 物理端口:又可称之为接口，是可见的端口，如USB接口，RJ45网口，HDMI端口等
- 虚拟端口:是指计算机内部的端口，是不可见的，是用来操作系统和外部进行交互使用的

虚拟端口

- Linux系统，可以支持65535个端口,这6万多个端口分为3类进行使用:
- 公认端口:1~1023,通常用于一些系统内置或知名程序的预留使用，如SSH服务的22端口，HTTPS服务的443端口非特殊需要，不要占用这个范围的端口
- 注册端口:1024~49151,通常可以随意使用，用于松散的绑定一些程序或服务
- 动态端口:49152~65535,通常不会固定绑定程序,而是当程序对外进行网络链接时,用于临时使用。

查看端口占用

- 可以通过Linux命令去查看端口的占用情况
- 使用nmap命令,安装`nmap: yum -y install nmap`
- 语法  `nmap 被查看的IP地址`

netstat

- 可以通过netstat命令,查看指定端口的占用情况
- 语法:`netstat -anp | grep 端口号`，安装netstat: `yum -y install net-tools`

### 6.9 进程

查看进程

- 可以通过ps命令查看Linux系统中的进程信息
- 语法: `ps [-e -f]`
  - 选项:`-e`，显示出全部的进程
  - 选项:`-f`,以完全格式化的形式展示信息	（展示全部信息)
  - 一般来说，固定用法就是:`ps -ef`列出全部进程的全部信息

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/48fbc2533a7249729e344fd03cc7e0b6.png)

从左到右分别是∶

- UID︰进程所属的用户ID
- PID∶进程的进程号ID
- PPID︰进程的父D(启动此进程的其它进程)
- c︰此进程的CPU占用率（百分比)
- STIME︰进程的启动时间
- TTY︰启动此进程的终端序号，如显示?，表示非终端启动
- TIME:进程占用CPU的时间
- CMD：进程对应的名称或启动路径或启动命令

关闭进程

可以通过`kill`命令关闭进程

语法

- `kill [-9] 进程ID`
- 选项：-9，表示强制关闭进程。不适用此选项会向进程发送信号

### 6.10 主机状态监测

查看系统资源占用

- 可以通过`top`命令查看CPU、内存使用情况，类似Windows的任务管理器，默认5秒刷新一次
  - `-p`只显示某个进程的信息
  - `-d`设置刷新时间，默认是5s
  - `-c`显示产生进程的完整命令，默认是进程名
  - `-n`指定刷新次数，比top -n 3，刷新输出3次后退出
  - `-b`以非交互非全屏模式运行，以批次的方式执行top，一般配合`-n`指定输出几次统计信息，将输出重定向到指定文件，比如 top -b -n 3 > /tmp/top .tmp
  - `-i`不显示任何闲置(idle)或无用(zombie)的进程
  - `-u`查找特定用户启动的进程

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/73663c0c2cc215b19becf58b8b2bf546.png)

top 命令解析

- 第一行

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/04cacc9457349e5ad4275e9281ef96d1.png)

top:命令名称，14:39:58:当前系统时间, up 6 min:启动了6分钟, 2 users:2个用户登录, load:1、5、15分钟负载

- 第二行

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/ca09c57ee577893eea0e595c24c5f98d.png)

Tasks:175个进程，1 running:1个进程子在运行，174 sleeping:174个进程睡眠,O个停止进程,0个僵尸进程

- 第三行

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/a64c4779fe163d8d6ee026867fd453f9.png)

%Cpu(s):CPU使用率，us:用户CPU使用率， sy:系统CPU使用率, ni:高优先级进程占用CPU时间百分比, id:空闲CPU率，wa: IO等待CPU占用率, hi: CPU硬件中断率, si:CPU软件中断率，st:强制等待占用CPU率

- 第四、五行

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/6582d0d8ec4f71ef237c0b821f72ee05.png)

Kib Mem:物理内存, total:总量, free:空闲, used:使用, buff/cache: buff和cache占用
Kib Swap:虚拟内存(交换空间) , total:总量, free:空闲,used:使用, buff/cache: buff和cache占用

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/7711f39ada2884299e85a0aca29f3149.png)

- PID:进程id
- USER:进程所属用户
- PR:进程优先级，越小越高
- NI:负值表示高优先级，正表示低优先级
- VIRT:进程使用虚拟内存，单位KB
- RES:进程使用物理内存，单位KBSHR:进程使用共享内存，单位KB
- S:进程状态(S休眠,R运行,Z僵死状态,N负数优先级,l空闲状态)
- %CPU:进程占用CPU率
- %MEM:进程占用内存率
- TIME+:进程使用CPU时间总计，单位10毫秒
- COMMAND:进程的命令或名称或程序文件路径

top交互式选项

| 按键 | 功能                                                         |
| ---- | ------------------------------------------------------------ |
| h键  | 按下h键，会显示帮助画面                                      |
| c键  | 按下c键，会显示产生进程的完整命令，等同于-c参数，再次按下c键，变为默认显示 |
| f键  | 按下f键，可以选择需要展示的项目                              |
| M键  | 按下M键，根据驻留内存大小（RES）排序                         |
| P键  | 按下P键，根据CPU使用百分比大小进行排序                       |
| T键  | 按下T键，根据时间/累计时间进行排序                           |
| E键  | 按下E键，切换顶部内存显示单位                                |
| e键  | 按下e键，切换进程内存显示单位                                |
| l键  | 按下l键，切换显示平均负载和启动时间信息。                    |
| i键  | 按下i键，不显示闲置或无用的进程，等同于-i参数，再次按下，变为默认显示 |
| t键  | 按下t键，切换显示CPU状态信息                                 |
| m键  | 按下m键，切换显示内存信息                                    |

---

磁盘信息监测

- 使用`df`命令，查看硬盘使用情况

语法

- `df [-h]`
- 选项：`-h`，以更加人性化的单位显示

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/724e351f4382342e270ee400897e4629.png)

- 可以使用`iostat`查看CPU、硬盘的相关信息

语法

- `iostat [-x][num1][num2]`
- 选项：`-x`，显示更多信息
- num1；数字，刷新间隔，num2，数字，刷新几次

---

网络状态监测

- 可以使用sar命令查看网络的相关统计

语法

- `sar -n DEV num1 num2`
- 选项：`-n`，查看网络，DEV表示查看网络接口
- num1；数字，刷新间隔，num2，数字，刷新几次

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/00502eed06afb0b56c064ea17d11a23d.png)

---

内存管理

-  free命令

```bash
free -h	# 查看内存
```

- 清理缓存

```bash
sync # 清理缓存前先使用
echo 3 > /proc/sys/vm/drop_caches	# 释放内存命令
```



### 6.11 环境变量

环境变量

- 操作系统（Windows、Linux、Mac)在运行的时候，记录的一些关键性信息,用以辅助系统运行。在Linux系统中执行:`env`命令即可查看当前系统中记录的环境变量
- 环境变量是一种KeyValue型结构，即名称和值，如下图:

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/37f2afdae2c303f28d70c7de268e88a1.png)

环境变量PATH

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/d83939126f8be7c552668ca83cba6803.png)

- PATH记录了系统执行任何命令的搜索路径

---

`$`符号

- 在Linux系统中，`$`符号被用于取”变量“的值

- 环境变量记录的信息，除了给操作系统自己使用外，如果我们想要取用，也可以使用。取得环境变量的值就可以通过语法:`$环境变量名`来取得比如: `echo $PATH`

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/51dfcbc95ead46bd78825b628258409a.png)

---

自行设置环境变量

用户自行设置方法

- 临时设置，语法`export 变量名=变量值`

- 永久生效
  - 针对当前用户生效，配置在当前用户的`~/.bashrc`文件中
  - 针对所有用户生效，配置在系统的`/etc/profile`文件中
  - 并通过语法`source 配置文件`，进行立即生效，或者重新登录

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/1855924f7c02c36f59199aea9b9a1836.png)

### 6.12 上传、下载

rz、sz命令

可以通过rz、sz命令进行文件传输，安装命令`yum install lrzsz`

- `rz`命令，进行上传
- `sz`命令，进行下载

### 6.13 压缩、解压

tar压缩解压命令

- Linux和Mac系统常用有2种压缩格式,后缀名分别是:
  - `.tar`,称之为tarball,归档文件,即简单的将文件组装到一个.tar的文件内，并没有太多文件体积的减少，仅仅是简单的封装
  - `.gz`，也常见为.tar.gz, gzip格式压缩文件,即使用gzip压缩算法将文件压缩到一个文件内，可以极大的减少压缩后的体积

- 针对这两种格式,使用`tar`命令均可以进行压缩和解压缩的操作
- 语法: `tar [-c -v -x -f -z -C]参数1 参数2 ... 参数N`
  - -c,创建压缩文件，用于压缩模式
  - -v，显示压缩、解压过程，用于查看进度
  - -x，解压模式
  - -f，,要创建的文件，或要解压的文件，-f选项必须在所有选项中**位置处于最后一个**
  - -z,gzip模式，不使用-z就是普通的tarball格式
  - -C，选择解压的目的地，用于解压模式

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/5d825414a7478a22c357eae257266cc5.png)

tar解压

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/d55a7ec804ec8488313ac00696e69e43.png)

---

zip压缩命令

- 可以使用zip命令，压缩文件为zip压缩包
- 语法: `zip [-r] 参数1 参数2 ..．参数N`
  - -r，被压缩的包含文件夹的时候，需要使用-r选项，和rm
    cp等命令的-r效果一致

unzip 解压命令

- 使用unzip命令，可以方便的解压zip压缩包
- 语法:`unzip [-d] 参数`
  - -d,指定要解压去的位置，同tar的-C选项。
  - 参数，被解压的zip压缩包文件

### 6.14 screen命令

1. 查看screen 是否安装

```bash
screen -v
```

2. 创建screen 终端

```bash
screen	# 创建匿名对话
screen -S yoursreenname
```

3. 离开screen视窗

```
Ctrl + A + D
```

4. 查看现有的screen会话

```bash
screen -ls
```

5. 返回离开的screen 视窗

```bash
screen -r 6952
```

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/502de6db8244d6ea81ce36e0d9cc1444.png)

6. 关闭screen 窗口

```bash
exit
```

### 6.15 Ubuntu防火墙

Ubuntu20.04一般都默认安装了UFW（Uncomplicated Firewall），它是一款轻量化的工具，主要用于对输入输出的流量进行监控。如果没有安装，请用下面的命令安装：

1. 安装

```bash
sudo apt install ufw
```

2. 启用

```bash
sudo ufw enable
sudo ufw default deny # 默认拒绝
```

3. 查看端口放行情况

```bash
sudo ufw status verbose
```

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/d9a56935136ef648a2d0519b00c2ebc7.png)

4. 开启/禁止端口

```bash
# 开启
sudo ufw allow 端口
# 禁止
sudo ufw deny 端口
# 删除规则
sudo ufw delete allow smtp
```



### 6.16 安装zsh和oh-my-zsh

1. 安装必要软件

```bash
sudo apt install wget git curl vim -y
```

2. 安装zsh

```bash
sudo apt install zsh -y
```

2. 设为默认shell，需要输入密码

```bash
chsh -s /bin/zsh
```

3. 重启终端，输入下面命令，查看是否为zsh

```bash
echo $SHELL
```

4. 安装oh-my-zsh

```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

5. 选择主题

```bash
ls .oh-my-zsh/themes
```

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/04b270712fc0b4f97aed37b81ea1944e.png)

6. 修改`./zshrc`

```bash
vim ~/.zshrc
# 修改 ZSH_THEME="YOUR_THEME" 并保存退出
source ~/.zshrc
```

---

安装插件

1. 下载主题PowerLevel10k

```bash
git clone https://github.com/romkatv/powerlevel10k.git $ZSH_CUSTOM/themes/powerlevel10k
```

2. 插件zsh-autosuggestions

```bash
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
```

3. 插件zsh-syntax-highlighting

```bash
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
```

启动插件

1. 修改主题

```bash
vi ~/.zshrc
ZSH_THEME="powerlevel10k/powerlevel10k"
```

2. 新增插件

```bash
plugins=(git zsh-autosuggestions zsh-syntax-highlighting)
```

3. 应用修改

```bash
source ~/.zshrc
```



## 7. 在Linux上部署各类软件

### 7.1 MySQL 数据库在Centos安装部署

MySQL数据库管理系统（后续简称MySQL)，是一款知名的数据库系统，其特点是:轻量、简单、功能丰富。

1. 配置yum仓库

```bash
# 更新密钥
rpm --import https://repo.mysql.com/RPM-GPG-KEY-mysql-2022

# 安装Mysql yum库
rpm -Uvh http://repo.mysql.com//mysql57-community-release-el7-7.noarch.rpm
```

>由于MySQL并不在Centos的官方仓库中，可以使用上述rpm命令
>
>- 导入MySQL仓库的密钥
>- 配置MySQL的yum仓库

2. 安装

```bash
sudo yum install -y mysql-community-server
```

3. 启动并配置开启自启动

```bash
systemctl start mysqld 
systemctl enable mysqld
```

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/a9d3c316bed8c67cb8d079d4b8f3bead.png)

4. 查看服务状态

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/da298d3b2b07d7c088fcf5b3d9a0fdd2.png)

---

配置mysql

   1. 获取MySQL的初始密码

```bash
#通过grep命令，在/var/log/mysqld.log文件中，过滤temporary passWord关键字，得到初始密码\
grep "temporary password" /var/log/mysqld.log
```

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/79e60e969bd764c74432e661a458734b.png)

2. 登录管理系统

```bash
mysql -uroot -p
```

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/2384129b996b9ac6cde944ef2c1c9ae9.png)

3. 修改root用户密码

```sql
#在MySQL控制台内执行
ALTER USER 'root'@'localhost' IDENTIFIED BY '密码';
#密码需要符合:大于8位，有大写字母，有特殊符号，不能是连续的简单语句如123，abc
```

4. 设置root用户简单密码

>此配置仅用于册数环境或学习环境，不要在生产环境中使用

```sql
#如果你想设置简单密码，需要降低Nysql的密码安全级别
set global validate_password_policy=LOW;#密码安全级别低
set global validate_password_length=4;#密码长度最低4位即可

#然后就可以用简单密码了（课程中使用简单密码，为了方便，生产中不要这样)
ALTER USER 'root'@'localhost' IDENTIFIED BY '简单密码';
```

5. 配置root远程登录

>默认情况下，root用户是不允许远程登录的，可以通过配置来实现远程登录

```sql
# 授权root远程登录
grant all privileges on *.* to root@"IP地址" identified by '密码' with grant option;
# IP地址即允许登陆的IP地址，也可以填写%，表示允许任何地址
# 密码表示给远程登录独立设置密码，和本地登陆的密码可以不同

# 刷新权限，生效
flush privileges;
```

6. 检查端口

>MySQL默认绑定了3306端口，可以通过端口占用检查MySQL的网络状态

```bash
netstat -anp | grep 3306
```

### 7.2 MySQL 数据库在Ubuntu安装部署

1. 下载apt仓库文件

```bash
#下载apt仓库的安装包，Ubuntu的安装包是.deb文件
wget https://dev.mysql.com/get/mysql-apt-config_0.8.12-1_all.deb
```

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/3fcdd9e8fab222b7bb4d8a1a78d6d169.png)

2. 配置apt仓库

```bash
# 使用dpkg命令安装仓库
dpkg -i mysql-apt-config_0.8.12-1_all.deb
```

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/127d2b156bb64d4a0ed20802d0cfcc58.png)

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/67dd46d162a7ee583aa902d66ae0258d.png)

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/2c9cb90f2258212a950ca012ba446221.png)

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/3cc977139fd4d6fe1a5df0b4700e816a.png)

3. 更新apt仓库信息

```bash
#首先导入仓库的密钥信息
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 467B942D3A79BD29
#更新仓库信息
apt update
```

4. 检查是否成功配置MySQL5.7仓库

```bash
apt-cache policy mysql-server
```

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/9391dce4ca07057804d6b2cef60223c1.png)

5. 安装MySQL5.7

```bash
#使用apt安装mysql客户端和mysql服务端
apt install -f -y mysql-client=5.7* mysql-community-server=5.7*
```

填写密码

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/4bf078cd6d8a03c34618994e19b62d90.png)

6. 启动MySQL

```bash
/etc/init.d/mysql start	#启动
/etc/init.d/mysql stop	#停止
/etc/init.d/mysql status  #查看状态
```

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/12a3c83352c92af8545a21f366f75765.png)

7. 初始化

```bash
#执行如下命令，此命令是MySQL安装后自带的配置程序
mysql_secure_installation
#可以通过which命令查看到这个自带程序所在的位置
root@DESKTOP-Q89USRE:~# which mysql_secure_installation
/usr/bin/mysql_secure_installation
```

8. 登录

```bash
mysql -uroot -p
```

### 7.3 Tomcat安装部署

Tomcat是由 Apache 开发的一个Servlet 容器，实现了对Servlet和JSP的支持，并提供了作为lWeb服务器的一些特有功能，如Tomcat管理和控制平台、安全域管理和Tomcat阀等。

> 简单来说，Tomcat是一个WEB应用程序的托管平台，可以让用户编写的WEB应用程序，被Tomcat所托管，并提供网站服务。

