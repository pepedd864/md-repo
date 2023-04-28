[TOC]



# 1.简介

## 1.版本控制器

对于代码的管理可以使用版本控制器来控制代码的版本,随意回退代码版本, 进行远程代码托管

常见的版本控制器类型有:

**a. 集中式版本控制工具**

- 集中式版本控制工具，版本库是集中存放在中央服务器的，team里每个人work时从中央服务器下载代码，是必须联网才能工作，局域网或互联网。个人修改后然后提交到中央版本库。
  举例:SVN和CVS

**b. 分布式版本控制工具**

- 分布式版本控制系统没有“中央服务器”，每个人的电脑上都是一个完整的版本库，这样工作的时候，无需要联网了，因为版本库就在你自己的电脑上。多人协作只需要各自的修改推送给对方，就能互相看到对方的修改了。
  举例: Git

## 2. git

git是一个开源的分布式版本控制系统，可以有效、高速地处理从很小到非常大的项目版本管理。Git是LinusTorvalds为了帮助管理Linux内核开发而开发的一个开放源码的版本控制软件。

同生活中的许多伟大事物一样，Git诞生于一个极富纷争大举创新的年代。Linux内核开源项目有着为数众多的参与者。绝大多数的Linux内核维护工作都花在了提交补丁和保存归档的繁琐事务上(1991-2002年间)。到2002年，整个项目组开始启用一个专有的分布式版本控制系统BitKeeper来管理和维护代码。

到了2005年，开发 BitKeeper的商业公司同Linux内核开源社区的合作关系结束，他们收回了Linux内核社区免费使用BitKeeper的权力。这就迫使Linux开源社区（特别是Linux的缔造者Linus Torva7ds）基于使用BitKeeper时的经验教训，开发出自己的版本系统。他们对新的系统制订了若干目标:

- 速度
- 简单的设计
- 对非线性开发模式的强力支持（允许成千上万个并行开发的分支)
- 完全分布式
- 有能力高效管理类似 Linux内核一样的超大规模项目（速度和数据量)

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/fe2d2f4b89747d5fca560161b6a83668.png)

## 3. git工作流程

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/30ccc95fbe8880fe766abc6e94359725.png)

命令如下

1. clone(克隆):从远程仓库中克隆代码到本地仓库
2. checkout(检出) :从本地仓库中检出一个仓库分支然后进行修订
3. add (添加)︰在提交前先将代码提交到暂存区
4. commit(提交)︰提交到本地仓库。本地仓库中保存修改的各个历史版本
5. fetch (抓取)︰从远程库，抓取到本地仓库，不进行任何的合并动作，一般操作比较少。
6. pull (拉取)︰从远程库拉到本地库，自动进行合并(merge)，然后放到到工作区，相当于fetch+merge
7. push(推送):修改完成后，需要和团队成员共享代码时，将代码推送到远程仓库am

# 2. git基本使用

## 2.1 常用linux命令

- `ls/ll` 查看当前目录
- `cat` 查看文件内容
- `touch` 创建文件
- `vi` vi编辑器

## 2.2 git基本配置

### 2.2.1 设置用户信息

- `git config --global user.name "itcast"`
- `git config --global user.email "pepedd@qq.com"`

### 2.2.2 查看配置信息

- `git config --global user.name`
- `git config --global email`

### 2.2.3 给常用指令配置别名

1. 打开用户目录,创建`.bashrc`文件

- `touch ~/.bashrc`

2. 在`.bashrc`文件中输入内容

- `alias git-log='git log --pretty=oneline --all --graph --abbrev-commit'`
- `alias ll='ls-al'`

3. 打开`gitbash` ,执行`source ~/.bashrc`

### 2.2.4 解决gitbash 乱码问题

1. 打开`gitbash`执行下面命令

```
git config --global core.quotepath false
```

2. `${git_home}/etc/bash.bashrc `文件最后加入内容

```
export LANG="zh_CN.UTF-8"
export LC_ALL="zh_CN.UTF-8"
```

## 2.3 获取本地仓库

要使用Git对我们的代码进行版本控制，首先需要获得本地仓库

1. 在电脑的任意位置创建一个空目录(例如test)作为我们的本地Git仓库
2. 进入这个目录中，点击右键打开`Git bash`窗口
3. 执行命令`git init`
4. 如果创建成功后可在文件夹下看到隐藏的`.git`目录。

## 2.4 git常用指令

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/34cad4cc1b61f466690395d7b5ba8d4f.png)

### 2.4.1 查看修改的状态(status)

- 作用:查看的修改的状态(暂存区、工作区)
- 命令形式:` git status`

### 2.4.2 添加工作区到暂存区(add)

- 作用:添加工作区一个或多个文件的修改到暂存区
- 命令形式:`git add`单个文件名|通配符
  - 将所有修改加入暂存区: `git add` .

### 2.4.3 提交暂存区到本地仓库(commit)

- 作用:提交暂存区内容到本地仓库的当前分支
- 命令形式: `git commit -m '注释内容’`

### 2.4.4 查看提交日志(log)

**在 1.2.3 中配置的别名`git-log`就包含了这些参数，所以后续可以直接使用指令`git-log`**

- 作用:查看提交记录
- ·命令形式: `git log [option]`
  - `options`
    -  `--all` 显示所有分支
    - `--pretty=oneline` 将提交信息显示为一行
    - `--abbrev-commit` 使得输出的`commitld`更简短
    - `--graph `以图的形式显示

### 2.4.5 版本回退

- 作用:版本切换

- 命令形式:` git reset --hard commitlD`

  - `commitlD`可以使用`git-log`或`git log`指令查看

- 如何查看已经删除的记录?
  - `git reflog`
  - 这个指令可以看到已经删除的提交记录

# 3. 分支

几乎所有的版本控制系统都以某种形式支持分支
使用分支意味着**你可以把你的工作从开发主线上分离开来进行重大的Bug修改、开发新的功能**，以免影响开发主线

## 3.1 查看本地分支

```bash
git branch
```

## 3.2 创建本地分支

```bash
git branch 分支名
```

## 3.3 切换分支

```bash
git checkout 分支名
```

还可以切换到一个不存在的分支(创建并切换)

```bash
git checkout -b 分支名
```

## 3.4 合并分支

一个分支上的提交可以合并到另一个分支

```bash
git merge 分支名称
```

## 3.5 删除分支

**不能删除当前分支，只能删除其他分支**

```bash
git branch -d b1 删除分支时，需要做各种检查
```

```bash
git branch -D b1不做任何检查，强制删除
```

## 3.6 解决冲突

当两个分支上对文件的修改可能会存在冲突，例如同时修改了同一个文件的同一行，这时就需要手动解决冲突，解决冲突步骤如下:

1. 处理文件中冲突的地方
2. 将解决完冲突的文件加入暂存区(add)
3. 提交到仓库(commit)

## 3.7 开发中分支使用原则与流程

在开发中，一般有如下分支使用原则与流程:

- master(生产)分支
线上分支，主分支，中小规模项目作为线上运行的应用对应的分支;
- develop(开发)分支
是从master创建的分支，一般作为开发部门的主要开发分支，如果没有其他并行开发不同期上线要求，都可以在此版本进行开发，阶段开发完成后，需要是合并到master分支,准备上线。
- feature/xxxx分支
从develop创建的分支，一般是同期并行开发，但不同期上线时创建的分支，分支上的研发任务完成后合并到develop分支
-  hotfix/xxxx分支
从master派生的分支，一般作为线上bug修复使用，修复完成后需要合并到master、test、develop分支
- 还有一些其他分支，例如test分支(用于代码测试)、pre分支(预上线分支)等等

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/cd706b6fecfea47722cf0a3db13dc940.png)

# 4. git远程仓库

互联网上提供的一些代码托管服务来实现git远程仓库，其中比较常用的有GitHub、码云、GitLab等。

- gitHub (地址: https://github.com/ )是一个面向开源及私有软件项目的托管平台，因为只支持Git作为唯一的版本库格式进行托管，故名gitHub
- 码云（地址: https://gitee.com/)是国内的一个代码托管平台，由于服务器在国内，所以相比于GitHub，码云速度会更快
- GitLab（地址: https://about.gitlab.com/ )是一个用于仓库管理系统的开源项目，使用Git作为代码管理工具，并在此基础上搭建起来的web服务，一般用于在企业、学校等内部网络搭建git私服。

## 4.1 创建仓库

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/6ee9c06fc81a46d62f6d842717d53644.png)

## 4.2 配置ssh公钥

1. 生成ssh公钥

```bash
1. ssh-keygen -t rsa
2. 直接全部回车确认
```

2. Gitee设置账户公钥
   - 获取公钥

```bash
cat ~/.ssh/id_rsa.pub	
```

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/4e95f666806abb0697489996bf519ed7.png)

- 
  - 验证是否配置成功

```bash
ssh -T git@gitee.com
```

## 4.3 添加、查看、推送远程仓库

1. 复制仓库地址

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/993cf73e90068bc07464e45ac1e028de.png)

2. 指定本地仓库的远程仓库`git remote add <远端名称> <仓库路径>`
   - 远端名称，默认是origin，取决于远端服务器设置
   - 仓库路径，从远端服务器获取此URL

```bash
git remote add origin git@gitee.com:pepedd864/git_test01.git
```

3. 查看仓库`git remote`

```bash
git remote
```

4. 推送本地仓库到远程仓库`git push [-f] [--set-upstream] [远端名称] [本地分支名]:[远端分支名]`
   - 如果远端分支名和本地分支名相同，可以只写本地分支
     - `git push origin master`
   - `-f`表示强制覆盖
   - `--set-upstream`推送到远端的同时并且**建立起和远端分支的关联关系**，之后可以省略`git push`后的参数直接推送
     - `git push --set-upstream origin master`
   - 如果**当前分支已经和远端分支关联**，则可以省略分支名和远端名。
     - ` git push`将master分支推送到已关联的远端分支。

## 4.4 操作远程仓库

### 4.4.1 本地分支与远程分支的关联关系

- 查看关联关系使用`git branch -vv` 命令

### 4.4.2 从远程仓库克隆

如果已经有一个远端仓库，我们可以直接`clone`到本地

- 命令: `git clone <仓库路径>[本地目录]`
  - 本地目录可以省略，会自动生成一个目录

### 4.4.3 从远程仓库中抓取和拉取

远程分支和本地的分支一样，我们可以进行`merge`操作，只是需要先把远端仓库里的更新都下载到本地，再进行操作。

- 抓取命令: `git fetch [remote name] [branch name]`
  - **抓取指令就是将仓库里的更新都抓取到本地，不会进行合并**
  - 如果不指定远端名称和分支名，则抓取所有分支
- 拉取命令: `git pull [remote name] [branch name]`
  - **拉取指令就是将远端仓库的修改拉到本地并自动进行合并，等同于`fetch+merge`**
  - 如果不指定远端名称和分支名，则抓取所有并更新当前分支。

### 4.4.4 解决合并冲突

在一段时间，A、B用户修改了同一个文件，且修改了同一行位置的代码，此时会发生合并冲突。

A用户在本地修改代码后优先推送到远程仓库，此时B用户在本地修订代码，提交到本地仓库后，也需要推送到远程仓库，此时B用户晚于A用户，**故需要先拉取远程仓库的提交，经过合并后才能推送到远端分支**,如下图所示。

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/4420d82e1f1c2d5defc10bcd1ed58b6b.png)

在B用户拉取代码时，因为A、B用户同一段时间修改了同一个文件的相同位置代码，故会发生合并冲突。

**远程分支也是分支，所以合并时冲突的解决方式也和解决本地分支冲突相同相同。**

## 4.5 通过VSCode提交远程仓库

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/c4cea441fa4fdda2e53a38ee695fab46.png)

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/f674361e6a81e02acda553e87d262409.png)

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/12139140593b385937494672f407372f.png)

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/f999a13f9a30c4af28bfe3ec3231fb38.png)

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/09d49932e48119ca82d63c7a26e2f32a.png)

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/c8cafd2dee0a384f6dd1682e90695472.png)

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/60addb4d58d098bb0d34e99b9a4785ff.png)