## 1. 基础

## 2. 案例

### 2.1 登录

#### 2.1.1 基于Session实现登录

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/22b7c5b5520e60eb1f83b56b3c35adbe.png)

实现：略

#### 2.1.2 集群的session共享问题-redis替代session

session共享问题:多台Tomcat并不共享session存储空间，当请求切换到不同tomcat服务时导致数据丢失的问题。

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/7fbba76c414d761241c2cde554ad954c.png)

#### 2.1.3 基于Redis实现共享session登录

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/5ed1d420c1d827b2599e5d718a90b83b.png)

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/1efb444b7c911c24302b7224bc74a878.png)

实现：略



### 2.2 缓存

#### 2.2.1 概念

**缓存**就是数据交换的缓冲区（称作Cache)，是存贮数据的临时地方，一般读写性能较高。