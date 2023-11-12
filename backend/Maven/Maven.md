

Maven是专门用于管理和构建Java项目的工具，它的主要功能有:

- 提供了一套标准化的项目结构
- 提供了一套标准化的构建流程（编译，测试，打包，发布.…..)
- 提供了一套依赖管理机制
  - 依赖管理其实就是管理你项目所依赖的第三方资源(jar包、插件...)



![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/376ddac0de9942af3b483a4bf115b21d.png)



![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/83f30a20830592c2dc8b7f5fed2c4c1b.png)

## 1. 简介

Apache Maven

- Apache Maven是一个项目管理和构建工具，它基于项目对象模型(POM)的概念，通过一小段描述信息来管理项目的构建、报告和文档
- 官网: http://maven.apache.org/



Maven模型

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/e6dfc96d88cb2e7b2269b5ed2ce5c224.png)



仓库分类:

- 本地仓库:自己计算机上的一个目录
- 中央仓库:由Maven团队维护的全球唯一的仓库
  - 地址: https://repo1.maven.org/maven2/
- 远程仓库(私服):一般由公司团队搭建的私有仓库

当项目中使用坐标引入对应依赖jar包后，首先会查找本地仓库中是否有对应的jar包

- 如果有，则征项目直接引用;
- 如果没有，则去中央仓库中下载对应的jar包到本地仓库。

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/56f15f245d562ee811d7b748e298d595.png)

## 2. 安装配置

下载

1. 前往https://maven.apache.org/download.cgi下载 `Binary zip archive`

2. 选择安装位置解压

3. 配置环境变量

   1. 添加系统变量 `MAVEN_HOME` 为MAVEN安装路径
   2. 添加`path` 下`%MAVEN_HOME%\bin`
4. 配置本地仓库： 修改`conf/settings.xml`中的`<localRepository>`为一个指定目录
5. 配置阿里云私服:修改`conf/settings.xml`中的`<mirrors>`标签，为其添加如下子标签:

    ```xml
    <!--  配置阿里云  -->
    <mirror>
      <id>aliyunmaven</id>
      <mirrorOf>*</mirrorOf>
      <name>阿里云公共仓库</name>
      <url>https://maven.aliyun.com/repository/public</url>
    </mirror>
    ```

## 3. 基本使用

### 3.1 常用命令

Maven常用命令

- compile :编译
- clean:清理
- test:测试
- package:打包
- install:安装

### 3.2 Maven生命周期

Maven构建项目生命周期描述的是一次构建过程经历经历了多少个事件

Maven对项目构建的生命周期划分为3套

- clean:清理工作
- default:核心工作，例如编译，测试，打包，安装等
- site: 产生报告，发布站点等

### 3.3 依赖范围

依赖范围

- 通过设置坐标的依赖范围(scope)，可以设置对应jar包的作用范围:编译环境、测试环境、运行环境

```xml
<dependency>
  <groupId>junit</groupId>
  <artifactId>junit</artifactId>
  <version>4.13.2</version>
  <scope>test</scope>
</dependency>
```

| 依赖范围 | 编译classpath            | 测试classpath | 运行classpath | 例子              |
| -------- | ------------------------ | ------------- | ------------- | ----------------- |
| compile  | Y                        | Y             | Y             | logback           |
| test     | -                        | Y             | -             | Junit             |
| provided | Y                        | Y             | -             | servlet-api       |
| runtime  | -                        | Y             | Y             | jdbc驱动          |
| system   | Y                        | Y             | -             | 存储在本地的jar包 |
| import   | 引入DependencyManagement |               |               |                   |

## 4. MavenWeb项目

### 4.1 项目结构

从MavenWeb开发中的项目到部署的JavaWeb项目结构

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/16bf470cd207d1481a1a8804ec98146b.png)

编译后的Java字节码文件和resources的资源文件，放到WEB-INF下的classes目录下

pom.xml中依赖坐标对应的jar包，放入WEB-INF下的lib目录下



### 4.2 在IDEA中创建Maven项目

**使用骨架创建**

1. 填写项目名
2. 选择JDK
3. 选择Archetype --- webapp
4. 填写组ID，和版本
5. 创建

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/5c4c2484bf699e71999c352800b3d293.png)

6. 删除pom.xml中多余的坐标

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/803debfa56b0e20ea8d6b9577ef0ccf1.png)

7. 补全目录

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/ddb5afc11a71ad56e4e76cef6223ad92.png)



**创建空白项目**

1. 选择新建项目
2. 构建系统选择Maven
3. 选择JDK
4. 不要添加示例代码
5. 填写组ID

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/ee69a109f08b49fd94f317c2d8aba668.png)

6. 在项目结构-->Facet-->Web资源目录下点击目录-->创建Web资源目录

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/321a8b0089f628961f10411f3b570987.png)

7. 继续点击部署描述符下的添加-->添加web.xml

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/171b48185addf0e7f81776d3a1367cbc.png)

8. 补齐目录

