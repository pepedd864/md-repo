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

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/fe2d2f4b89747d5fca560161b6a83668.png)

## 3. git工作流程

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/30ccc95fbe8880fe766abc6e94359725.png)

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

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/34cad4cc1b61f466690395d7b5ba8d4f.png)

### 2.4.1 查看修改的状态(status)

- 作用:查看的修改的状态(暂存区、工作区)
- 命令形式:` git status`

### 2.4.2 添加工作区到暂存区(add)

- 作用:添加工作区一个或多个文件的修改到暂存区
- 命令形式:`git add`单个文件名|通配符
  - 将所有修改加入暂存区: `git add .`

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

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/cd706b6fecfea47722cf0a3db13dc940.png)

# 4. git远程仓库

互联网上提供的一些代码托管服务来实现git远程仓库，其中比较常用的有GitHub、码云、GitLab等。

- gitHub (地址: https://github.com/ )是一个面向开源及私有软件项目的托管平台，因为只支持Git作为唯一的版本库格式进行托管，故名gitHub
- 码云（地址: https://gitee.com/)是国内的一个代码托管平台，由于服务器在国内，所以相比于GitHub，码云速度会更快
- GitLab（地址: https://about.gitlab.com/ )是一个用于仓库管理系统的开源项目，使用Git作为代码管理工具，并在此基础上搭建起来的web服务，一般用于在企业、学校等内部网络搭建git私服。

## 4.1 创建仓库

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/6ee9c06fc81a46d62f6d842717d53644.png)

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

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/4e95f666806abb0697489996bf519ed7.png)

- 
  - 验证是否配置成功

```bash
ssh -T git@gitee.com
```

## 4.3 添加、查看、推送远程仓库

1. 复制仓库地址

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/993cf73e90068bc07464e45ac1e028de.png)

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

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/4420d82e1f1c2d5defc10bcd1ed58b6b.png)

在B用户拉取代码时，因为A、B用户同一段时间修改了同一个文件的相同位置代码，故会发生合并冲突。

**远程分支也是分支，所以合并时冲突的解决方式也和解决本地分支冲突相同相同。**

## 4.5 通过VSCode提交远程仓库

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/c4cea441fa4fdda2e53a38ee695fab46.png)

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/f674361e6a81e02acda553e87d262409.png)

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/12139140593b385937494672f407372f.png)

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/f999a13f9a30c4af28bfe3ec3231fb38.png)

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/09d49932e48119ca82d63c7a26e2f32a.png)

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/c8cafd2dee0a384f6dd1682e90695472.png)

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/60addb4d58d098bb0d34e99b9a4785ff.png)



# 5. commit规范-约定式规范

官网：https://www.conventionalcommits.org/zh-hans/v1.0.0/

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/51464fa2c7de20eecdf4057d6ced1eb3.png)

**commit message格式**

```text
<type>(<scope>): <subject>
```

**type(必须)**

用于说明git commit的类别，只允许使用下面的标识。

feat：新功能（feature）。

fix/to：修复bug，可以是QA发现的BUG，也可以是研发自己发现的BUG。

- fix：产生diff并自动修复此问题。适合于一次提交直接修复问题
- to：只产生diff不自动修复此问题。适合于多次提交。最终修复问题提交时使用fix

docs：文档（documentation）。

style：格式（不影响代码运行的变动）。

refactor：重构（即不是新增功能，也不是修改bug的代码变动）。

perf：优化相关，比如提升性能、体验。

test：增加测试。

chore：构建过程或辅助工具的变动。

revert：回滚到上一个版本。

merge：代码合并。

sync：同步主线或分支的Bug。

**scope(可选)**

scope用于说明 commit 影响的范围，比如数据层、控制层、视图层等等，视项目不同而不同。

例如在Angular，可以是location，browser，compile，compile，rootScope， ngHref，ngClick，ngView等。如果你的修改影响了不止一个scope，你可以使用*代替。

**subject(必须)**

subject是commit目的的简短描述，不超过50个字符。

建议使用中文（感觉中国人用中文描述问题能更清楚一些）。

- 结尾不加句号或其他标点符号。
- 根据以上规范git commit message将是如下的格式：

```text
fix(DAO):用户查询缺少username属性 
feat(Controller):用户查询接口开发
```



# 6. git进阶用法

## 6.1 filter-repo

filter-repo是git官方指定的历史记录重写和过滤操作工具，它可以用于各种场景，包括：

1. 仓库裁剪：当你想要从一个Git仓库中提取出特定的目录或文件时，`git filter-repo`可以帮助你快速创建一个新的仓库，只包含你感兴趣的部分。这对于从大型仓库中提取子项目或者将仓库拆分为更小的模块非常有用。
2. 敏感数据删除：当你在Git仓库中不小心提交了包含敏感信息的文件（如密码、API密钥等），你可以使用`git filter-repo`来完全删除这些敏感数据的历史记录，以确保不会再有人能够访问到这些信息。
3. 历史记录重写：`git filter-repo`提供了强大的历史记录重写功能，可以帮助你修改提交的内容、合并提交、修改提交顺序等。这对于修复错误、重新组织提交历史或准备干净的发布版本非常有用。
4. 仓库转换：如果你想要将一个Git仓库转换为另一种版本控制系统（如Mercurial），或者将一个仓库迁移到另一个托管平台（如从GitHub迁移到GitLab），`git filter-repo`可以帮助你转换和重构仓库的历史记录，以满足目标系统的要求。

安装

```bash
pip install git-filter-repo
```

删除文件或文件夹

> 首先执行垃圾回收


```bash
git gc
```

```bash
git filter-repo --path <file or folder> --invert-paths --force
```



## 6.2 sparse clone

使用`sparse`系列命令可以让你在从一个大型git仓库中下载特定文件或者文件夹时得心应手

> 使用sparse clone 命令可以下载仓库的元数据，然后根据需要下载文件或文件夹

```bash
# 下载元数据
git clone --filter=blob:none --sparse https://github.com/pepedd864/code-repo.git
```

> 使用sparse checkout命令，下载特定的文件或文件夹

```bash
# 下载文件夹
git sparse-checkout add login-crud
```

> 如果你不需要这个文件夹了，还可以使用set命令切换到另一个文件夹

```bash
git sparse-checkout set antdv-theme-mgr
```



## 6.3 使用rebase合并commit

使用`rebase`命令可以修改和合并commit信息

1. 使用`git rebase -i commitId` 修改某个commit的信息，(注：打开的是vim编辑器，不了解可以先学习一下)，修改完成`:wq`保存即可

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/2c5ccf43e526cfa1e238eb406069dc1b.png)

2. 使用`git rebase -i HEAD~n`修改按照时间顺序由近到远显示最近提交的n条commit，比如`git rebase -i HEAD~3`

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/913d70545c7691f559b24b5daccdee80.png)

3. `git rebase -i --root`显示所有的commit信息

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/2939aba6ca5655b3659b8b7966072d61.png)



根据提示信息(下面的蓝字)，我们知道

- pick就是默认采用这个commit，不用管他
- edit就是对这条进行修改
- s就是合并
- f也是合并，但是只保留最前边的commit信息。如果加上-c那只保留最新的commit信息

合并commit可以使用`squash`或者`fixed`，区别是前者会保留commit信息



比如我们需要将3和4合并，并保留commit信息

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/503a58ae91c0a3ba8b5f790bd831d4cb.png)

可以使用`git rebase -i --root`

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/1c60820309da9f2df08ae5d2f280fb03.png)

这样修改即可

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/08555b6719dec7655705fa061bd0c3eb.png)

修改commit信息

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/d3a86d6789513f3efd98f6e924ae4564.png)

这个时候就是修改完的样子了

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/1d037392e5c764b763b76033211d2d85.png)

在github上的commit提交信息

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/55b1ad3f4eae799f9aadaa752af2e56c.png)

`squash 3 and 4`是这样

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/4df77539b54114d463c978fd012a4302.png)



