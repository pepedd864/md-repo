

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/ac35f27e3f9077d87a91a45ce28d6a48.png)

## 1. 初识Docker

### 1.1 Docker概念

Docker概念

- Docker是一个开源的应用容器引擎
- 诞生于2013年初，基于Go语言实现，dotCloud公司出品(后改名为Docker Inc)
- Docker可以让开发者打包他们的应用以及依赖包到一个轻量级、可移植的容器中，然后发布到任何流行的Linux机器上。
- 容器是完全使用沙箱机制，相互隔离
- 容器性能开销极低。

**和虚拟机相比**

| 特性   | 普通虚拟机                                                   | Docker                                               |
| ------ | ------------------------------------------------------------ | ---------------------------------------------------- |
| 跨平台 | 通常只能在桌面级系统运行，例如Windows/Mac，无法在不带图形界面的服务器上运行 | 支持的系统非常多，各类Winddows和Linux都支持          |
| 性能   | 性能损耗大，内存占用高，因为是把整个完整的系统都虚拟出来了   | 性能好，只虚拟软件所需运行环境，最大化减少没用的配置 |
| 自动化 | 需要手动安装所有东西                                         | 一个命令就可以自动部署好所需环境                     |
| 稳定性 | 稳定性不高，不同系统差异大                                   | 稳定性好，不同系统都一样的部署方式                   |

**打包、分发、部署**

打包

- 就是把你软件运行所需的依赖、第三方库、软件打包到一起，变成一个安装包

分发

- 你可以把你打包好的"安装包“上传到一个镜像仓库，其他人可以非常方便的获取和安装

部署

- 拿着"安装包"就可以一个命令运行起来你的应用，自动模拟出一摸一样的运行环境，不管是在Windows/Mac/Linux。

**Docker部署的优势**

常规应用开发部署方式:自己在Windows上开发、测试-->到Linux服务器配置运行环境部署。

**Docker通常用来做什么**

- 应用分发、部署，方便传播给他人安装。特别是开源软件和提供私有部署的应用

- 快速安装测试/学习软件，用完就丢（类似小程序)，不把时间浪费在安装软件上。例如Redis / MongoDB /ElasticSearch/ ELK

- 多个版本软件共存，不污染系统，例如Python2、Python3，Redis4.0，Redis5.0
- Windows上体验/学习各种Linux系统

**重要概念:镜像、容器**

镜像

- 可以理解为软件安装包，可以方便的进行传摇和安装。

容器

- 软件安装后的状态，每个软件运行环境部是独立的、隔离的，称之为容器。

**镜像加速源**

| 镜像加速器         | 镜像加速器地址                     |
| ------------------ | ---------------------------------- |
| Docker中国官方镜像 | https://registry.docker-cn.com     |
| DaoCloud镜像站     | http://f1361db2.m.daocloud.io      |
| Azure中国镜像      | https://dockerhub.azk8s.cn         |
| 科大镜像站         | https://docker.mirrors.ustc.edu.cn |

### 1.2 安装Docker

1. centos

```bash
#1、yum包更新到最新
yum update
#2、安装需要的软件包，yum-util提供yum-config-manager功能，另外两个是devicemapper驱动依赖的
yum install -y yum-utils device-mapper-persistent-data lvm2
#3、设置yum源
yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
#4、安装docker ,出现输入的界面都按y
yum install -y docker-ce
# 5、查看docker版本，验证是否验证成功
docker -v
```

2. ubuntu

```bash
# 首先，更新软件包索引，并且安装必要的依赖软件，来添加一个新的 HTTPS 软件源：
sudo apt update
sudo apt install apt-transport-https ca-certificates curl gnupg-agent software-properties-common
# 使用下面的 curl 导入源仓库的 GPG key：
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
# 将 Docker APT 软件源添加到你的系统：
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
# 1. 想要安装 Docker 最新版本，运行下面的命令
sudo apt install docker-ce docker-ce-cli containerd.io
# 2. 想要安装指定版本，首先列出 Docker 软件源中所有可用的版本
apt list -a docker-ce
# 通过在软件包名后面添加版本=<VERSION>来安装指定版本：
sudo apt install docker-ce=<VERSION> docker-ce-cli=<VERSION> containerd.io
# 验证服务启动状态
sudo systemctl status docker
# 阻止 Docker 自动更新
sudo apt-mark hold docker-ce
```

### 1.3 Docker架构

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/1642c8c5684a7012c433e3ee4fe61004.png)

- 镜像(lmage) : Docker镜像(lmage) ，就相当于是一个root文件系统。比如官方镜像ubuntu:16.04就包含了完整的一套Ubuntu16.04最小系统的root文件系统。
- 容器(Container):镜像(lmage）和容器(Container)的关系，就像是面向对象程序设计中的类和对象一样，镜像是静态的定义，容器是镜像运行时的实体。容器可以被创建、启动、停止、删除、暂停等。
- 仓库(Repository) :仓库可看成一个代码控制中心,用来保存镜像。

### 1.4 Docker安装软件

**直接安装的缺点**

- 安装麻烦，可能有各种依赖，运行报错。例如: WordPress，ElasticSearch，Redis，ELK。
- 可能对Windows 并不友好，运行有各种兼容问题，软件只支持Linux 上跑
- 不方便安装多版本软件，不能共存。
- 电脑安装了—堆软件，拖慢电脑速度
- 不同系统和硬件，安装方式不一样

**Docker安装的优点**

- —个命令就可以安装好，快速方便
- 有大量的镜像，可直接使用
- 没有系统兼容问题，Linux专享软件也照样跑
- 支持软件多版本共存
- 用完就丢，不拖慢电脑速度
- 不同系统和硬件，只要安装好Docker其他都一样了，一个命令搞定所有

**Docker 镜像仓库**

- https://hub.docker.com/



## 2. Docker命令

### 2.1 Docker服务相关命令

- 启动Docker服务

```bash
systemctl start docker
```

- 停止

```bash
systemctl top docker
```

- 重启

```bash
systemctl restart docekr
```

- 查看状态

```bash
systemctl status docker
```

- 设置开机启动

```bash
systemctl enable docker
```

### 2.2 镜像相关命令

- 查看镜像

```bash
docker images
docker images -q # 查看所用镜像的id 
```

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/11fae3d5f622b488d19a5ff15fd99316.png)

- 搜索镜像

```bash
docker search redis
```

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/ab3ab8bd192be05d5ffc971ac617b157.png)

- 拉取镜像

```bash
docker pull redis:version
```

- 删除镜像

```bash
docker rmi 492d05aa2c3c  # id
docker rmi redis:latest  # name
```

- 删除所有镜像

```bash
docker rmi `docker images -q`
```



### 2.3 容器相关命令

- 查看容器

```bash
docker ps	 # 查看正在运行的容器
docker ps -a # 查看历史容器
```

- 创建并启动容器

```bash
docker run 参数
```

- 参数说明
  - `-i` : 保持容器运行。通常与 `-t` 同时使用。加入`it`这两个参数后，容器创建后自动进入容器中，退出容器后，容器自动关闭。
  - `-t`:为容器重新分配一个伪输入终端，通常与`-i`同时使用。
  - `-d`:以守护(后台)模式运行容器。创建一个容器在后台运行，需要使用`docker exec`进入容器。退出后，容器不会关闭。
  - `-it`:创建的容器一般称为交互式容器，`-id`创建的容器一般称为守护式容器
  - `--name`:为创建的容器命名。

- 进入容器

```bash
docker exec 参数 # 退出容器，容器不会关闭
```

- 停止容器

```bash
docekr stop 容器名称
```

- 启动容器

```bash 
docker start 容器名称
```

- 删除容器：如果容器是运行状态则删除失败，需要停止容器才能删除

```bash
docker rm 容器名称
docker rm `docker ps -ap` #删除所有容器
```

- 查看容器信息

```bash
docker inspect 容器名称
```



## 3. Docker容器的数据卷

### 3.1 数据卷概念

数据卷

- 数据卷是宿主机中的一个目录或文件
- 当容器目录和数据卷目录绑定后，对方的修改会立即同步

- 一个数据卷可以被多个容器同时挂载
- 一个容器也可以挂载多个数据卷

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/565117a28636b0138cf2e14189e98196.png)

数据卷的作用

- 容器数据持久化
- 外部机器和容器间接通信
- 容器之间数据交换



### 3.2 配置数据卷

- 创建容器时，使用`-v`参数设置数据卷

```bash
docker run ... -v 宿主机目录（文件）:容器内目录（文件）...
```

- 注意事项:
  1. 目录必须是绝对路径
  2. 如果目录不存在，会自动创建
  3. 可以挂载多个数据卷



### 3.3 数据卷容器

多容器进行数据交换

1. 多个容器挂载同一个数据卷
2. 数据卷容器

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/b76bafa5cb860d6a2618d811673f6e99.png)

---

配置数据卷容器

1. 创建启动c3数据卷容器，使用`-v`参数设置数据卷

```bash
docker run -it --name=c3 -v /volume centos:7 /bin/bash
```

2. 创建启动c1 c2 容器，使用`--volumes-from`参数设置数据卷

```bash
docker run -it --name=c1 --volumes-from c3 centos:7 /bin/bash
docker run -it --name=c2 --volumes-from c3 centos:7 /bin/bash
```



## 4. Docker应用部署

### 4.1 MySQL部署

- 容器内的网络服务和外部机器不能直接通信
- 外部机器和宿主机可以直接通信
- 宿主机和容器可以直接通信
- 当容器中的网络服务需要被外部机器访问时，可以将容器中提供服务的端口映射到宿主机的端口上。外部机器访问宿主机的该端口，从而间接访问容器的服务
- 这种操作称为：端口映射

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/84aebfd2297911f4cdf520aba6e203ce.png)



部署MySQL

1. 搜索MySQL镜像

```bash
docker search mysql
```

2. 拉取镜像

```bash
docker pull mysql:5.6
```

3. 创建容器，设置端口映射、目录映射

```bash
mkdir ~/mysql
cd ~/mysql
```

```bash
docker run -id \
-p 3307:3306 \
--name=c_mysql \
-v $PWD/conf:/etc/mysql/conf.d \
-v $PWD/logs:/logs \
-v $PWD/data:/var/lib/mysql \
-e MYSQL_ROOT_PASSWORD=123456 \
mysql
```

- 参数说明
  - `-p 3307:3306`： 将容器的3306端口映射到宿主机的3307端口。
  - `-v $PWD/conf:/etc/mysql/conf.d`: 将主机当前目录下的conf/my.cnf挂载到容器/etc/mysql/my.cnf。配置目录
  - `-v $PWD/logs:/logs`：将主机当前目录下的logs目录挂载到容器的/logs。日志目录
  - `-v $PWD/data:/var/lib/mysql`:将主机当前目录下的data目录挂载到容器的/var/lib/mysql。数据目录
  - `-e MYSQL_ROOT_PASSWORD=123456`:初始化root用户的密码。

4. 进入容器，操作mysql

```bash
docker exec -it c_mysql /bin/bash
```

5. 使用外机连接数据库

### 4.2 Tomcat部署

1. 搜索Tomcat镜像

```bash
docker search tomcat
```

2. 拉取镜像

```bash
docker pull tomcat
```

3. 创建容器，设置端口映射、目录映射

```bash 
mkdir ~/tomcat
cd ~/tomcat
```

```bash
docekr run -id --name=c_tomcat \
-p 8080:8080 \
-v $PWD:/usr/local/tomcat/webapps \
tomcat
```

- 参数说明
  - `-p 8080:8080`：将容器的8080端口映射到主机的8080端口
  - `-v $PWD:/usr/local/tomcat/webapps`: 将主机中当前目录挂载到容器的webapps

4. 使用外机访问tomcat



### 4.3 Nginx部署

1. 搜索nginx镜像

```bash
docker search nginx
```

2. 拉取镜像

```bash
docker pull nginx
```

3. 创建容器，设置端口映射、目录映射

```bash 
mkdir ~/nginx
cd ~/nginx	
mkdir conf
cd conf
# 在~/nginx/conf下创建nginx.conf文件，粘贴下面内容
vim nginx.conf
```

```
```

```bash
docker run -id --name=c_nginx \
-p 80:80 \
-v $PWD/conf/nginx.conf:/etc/nginx/nginx.conf \
-v $PWD/logs:/var/log/nginx \
-v $PWD/html:/usr/share/nginx/html \
nginx
```

- 参数说明
  - `-p 80:80`:将容器的80端口映射到宿主机的80端口。
  - `-v $PWD/conf/nginx.conf:/etc/nginx/nginx.conf`:将主机当前目录下的/conf/nginx.conf挂载到容器的:/etc/nginx/nginx.conf。配置目录
  - `-v $PWD/logs:/var/log/nginx`:将主机当前目录下的logs目录挂载到容器的/var/log/nginx。日志目录

4. 使用外机访问nignx

### 4.4 Redis部署

1. 搜索redis镜像

```bash
docker search redis
```

2. 拉取镜像

```bash
docker pull redis
```

3. 创建容器，设置端口映射、目录映射

```bash 
mkdir ~/redis
cd ~/redis
```

```bash
docekr run -id --name=c_redis \
-p 6379:6379 \
redis:5.0
```

4. 使用外机连接redis

```bash
redis-cli.exe -h ip -p 6369
```



## 5.Dockerfile

###  5.1 docker镜像原理

Linux文件系统

- Linux文件系统由bootfs和rptfs两部分组成
- bootfs:包含bootloader (引导加载程序）和kernel(内核)
- rootfs: root文件系统，包含的就是典型Linux系统中的/dev,/proc，/bin，/etc等标准目录和文件
- 不同的linux发行版，bootfs基本一样，而rootfs不同，如ubuntu, centos等

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/cd8d848e4515d34348bc494547b24db4.png)

docker镜像原理

- Docker镜像是由特殊的文件系统叠加而成
- 最底端是bootfs，并使用宿主机的bootfs
- 第二层是root文件系统rootfs,称为base image
- 然后再往上可以叠加其他的镜像文件
- 统一文件系统(Union File System)技术能够将不同的层整合成一个文件系统，为这些层提供了一个统一的视角，这样就隐藏了多层的存在，在用户的角度看来，只存在一个文件系统。
- 一个镜像可以放在另一个镜像的上面。位于下面的镜像称为父镜像，最底部的镜像成为基础镜像。
- 当从一个镜像启动容器时，Docker会在最顶层加载一个读写文件系统作为容器

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/2b6a98592320150d014f85a7f66ac34e.png)



### 5.2 制作镜像

1. 容器转为镜像

```bash
docker commit 容器id 镜像名称:版本号
```

```bash
docker save -o 压缩文件名称 镜像名称:版本号
```

```bash
docker load -i 压缩文件名称
```

### 5.3 dockerfile

dockerfile概念

- Dockerfile是一个文本文件
- 包含了一条条的指令
- 每一条指令构建一层，基于基础镜像，最终构建出一个新的镜像
- 对于开发人员:可以为开发团队提供一个完全一致的开发环境
- 对于测试人员:可以直接拿开发时所构建的镜像或者通过Dockerfile文件构建一个新的镜像开始工作了
- 对于运维人员:在部署时，可以实现应用的无缝移植

常用关键字

| 关键字      | 作用                     | 备注                                                         |
| ----------- | ------------------------ | ------------------------------------------------------------ |
| FROM        | 指定父镜像               | 指定dockerfile基于哪个image构建                              |
| MAINTAINER  | 作者信息                 | 用来标明这个dockerfile谁写的                                 |
| LABEL       | 标签                     | 用来标明dockerfile的标签可以使用Label代替Maintainer最终都是在docker image基本信息中可以查看 |
| RUN         | 容器启动命令             | 提供启动容器时候的默认命令和ENTRYPOINT配合使用.格式CMD command param1 param2或者CMD ["command","param1","param2"] |
| ENTRYPOINT  | 入口                     | 一般在制作一些执行就关闭的容器中会使用                       |
| COPY        | 复制文件                 | build的时候复制文件到image中                                 |
| ADD         | 添加文件                 | build的时候添加文件到image中不仅仅局限于当前build上下文可以来源于远程服务 |
| ENV         | 环境变量                 | 指定build时候的环境变量可以在启动的容器的时候通过-e覆盖格式ENV name=value |
| ARG         | 构建参数                 | 构建参数只在构建的时候使用的参数如果有ENV那么ENV的相同名字的值始终覆盖arg的参数 |
| VOLUME      | 定义外部可以挂载的数据卷 | 指定build的image那些目录可以启动的时候挂载到文件系统中启动容器的时候使用-v绑定格式VOLUME["目录"] |
| EXPOSE      | 暴露端口                 | 定义容器运行的时候监听的端口启动容器的使用-p来绑定暴露端口格式:EXPOSE 8080或者EXPOSE 8080/udp |
| WORKDIR     | 工作目录                 | 指定容器内部的工作目录如果没有创建则自动创建如果指定/使用的是绝对地址如果不是/开头那么是在上一条workdir的路径的相对路径 |
| USER        | 指定执行用户             | 指定build或者启动的时候用户在RUN CMD ENTRYPONT执行的时候的用户 |
| HEALTHCHECK | 健康检查                 | 指定监测当前容器的健康监测的命令基本上没用因为很多时候应用本身有健康监测机制 |
| ONBUILD     | 触发器                   | 当存在ONBUILD关键字的镜像作为基础镜像的时候当执行FROM完成之后会执行ONBUILD的命令但是不影响当前镜像用处也不怎么大 |
| STOPSIGNAL  | 发送信号量到宿主机       | 该STOPSIGNAL指令设置将发送到容器的系统调用信号以退出。       |
| SHELL       | 指定执行脚本的shell      | 指定RUN CMD ENTRYPOINT执行命令的时候使用的shell              |



### 5.4 案例：使用dockerfile发布spring boot项目

1. 打包springboot项目jar包，发送到Linux服务器上
2. 安装所需镜像（这里只需要Java17即可，即openjdk:17）
3. 创建dockerfile文件编写下面配置

```dockerfile
FROM openjdk:17
MAINTAINER pepedd <pepedd@qq.com>
ADD springboot_quickstart-0.0.1-SNAPSHOT.jar app.jar
CMD java -jar app.jar
```

4. 打包镜像

```bash 
docker build -f ./springboot_dockerfile -t app .
```

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/b93a701933c467f5d39cc558709c8b0f.png)

5. 查看镜像

```bash
docker images
```

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/3c1d24c41788101f064508c412e988fb.png)

6. 设置端口映射，运行镜像

```bash 
docker run -it -p 9000:80 app
```

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/6eb6eb8b0740a61ea287826a31567f8e.png)

7. 访问项目

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/43406cd3c4b003e7a57e079b6b6d5690.png)

## 6. Docker服务编排

### 6.1 服务编排

- 微服务架构的应用系统中一般包含若干个微服务，每个微服务一般都会部署多个实例，如果每个微服务都要手动启停，维护的工作量会很大。
  - 要从Dockerfile build image或者去dockerhub拉取image
  - 要创建多个container入
  - 要管理这些container (启动停止删除)

### 6.2 Docker Compose 

- Docker Compose是一个编排多容器分布式部署的工具，提供命令集管理容器化应用的完整开发周期，包括服务构建，启动和停止。使用步骤:
  1. 利用Dockerfile定义运行环境镜像
  2. 使用docker-compose.yml定义组成应用的各服务
  3. 运行docker-compose up启动应用

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/6eb28c71548de1f4f4d85d8dde97e095.png)

### 6.3 Docker Compose 安装与卸载

安装

```bash
#下载docker-compose文件
curl -L https://github.com/docker/compose/releases/download/2.16.0/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
#给文件可执行权限
chmod +x /usr/local/bin/docker-compose
# 查看版本信息
docker-compose -version
```

卸载

```bash
rm /usr/local/bin/docker-compose
```

###  6.4 使用docker compose

1. 创建docker-compose 目录

```bash
mkdir ~/docker-compose
cd ~/docker-compose
```

2. 编写docker-compose.yml文件

```yml
version: '3'
services: 
    nginx:
        image: nginx
        ports: 
        - 80: 80
        links:
        - app
        volumes:
        - ./nginx/conf.d:/etc/nginx/conf.d
     app:
        image: app
        expose:
        - "80"
```

3. 创建./nginx/conf.d目录

```bash
mkdir -p ./nginx.conf.d
```

4. 在./nginx/conf.d目录下编写app.conf

```conf
server {
	listen 80;
	access_log off;

	location / {
		proxy_pass http://app:80;
	}
}
```



## 7. Docker私有仓库

### 7.1 搭建仓库

```bash
# 1. 拉取私有仓库镜像
docker pull registry
# 2. 启动私有仓库容器
docker run -id --name=registry -p 5000:5000 registry
# 3. 打开浏览器 输入地址http://私有仓库ip:5000/v2/_catalog，看到{“repositories”:[]}表示私有仓库创建成功
# 4. 修改daemon.json
vim /etc/docker/daemon.json
# 在上述文件中添加一个key，保存退出。此步用于让docker信任私有仓库地址﹔注意将私有仓库服务器ip修改为自己私有仓库服务器真实ip
{ "insecure-registries ":[""私有仓库服务器ip: 5000""]}
# 5. 重启docker 服务
systemctl restart docker
docker start registry
```

### 7.2 上传镜像

```bash
# 1. 标记镜像为私有仓库镜像
docker tag centos:7 私有仓库服务器IP:5000/centos:7
# 2. 上传标记镜像
docker push 私有仓库服务器IP:5000/centos:7
```

### 7.3 拉取镜像

```bash
docker pull 私有仓库服务器IP:5000/centos:7
```

