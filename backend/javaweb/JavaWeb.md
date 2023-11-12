# JavaWeb

JavaWeb

- 是用Java技术来解决相关web互联网领域的技术栈

## 1. JavaWeb技术栈

B/S架构(Browser/Server)

- 浏览器/服务器架构模式，它的特点是，客户端只需要浏览器，应用程序的逻辑和数据都存储在服务器端。浏览器只需要请求服务器，获取Web资源，服务器把Web资源发送给浏览器即可

静态资源

- HTML、CSS、JavaScript、图片等。负责页面展现

动态资源

- Servlet、JSP等。负责逻辑处理

数据库

- 负责存储数据

HTTP协议

- 定义通信规则

Web服务器

- 负责解析HTTP协议，解析请求数据，并发送响应数据

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/dd64cefd096a1ca19ada9f7042cd77dc.png)

## 2. HTTP

### 2.1 概念

HTTP

- 概念:HyperText Transfer Protocol，超文本传输协议，规定了浏览器和服务器之间数据传输的规贝

- HTTP协议特点:
  - 基于TCP协议:面向连接，安全
  - 基于请求-响应模型的:一次请求对应一次响应
  - HTTP协议是无状态的协议:对于事务处理没有记忆能力。每次请求-响应都是独立的。
    - 缺点:多次请求间不能共享数据。Java中使用会话技术(Cookie、Session)来解决这个问题
    - 优点:速度快



### 2.2 特点

HTTP协议有哪些特点：

* **基于TCP协议: **   面向连接，安全

  > TCP是一种面向连接的(建立连接之前是需要经过三次握手)、可靠的、基于字节流的传输层通信协议，在数据传输方面更安全

* **基于请求-响应模型:**   一次请求对应一次响应（先请求后响应）

  > 请求和响应是一一对应关系，没有请求，就没有响应

* **HTTP协议是无状态协议:**  对于数据没有记忆能力。每次请求-响应都是独立的

  > 无状态指的是客户端发送HTTP请求给服务端之后，服务端根据请求响应数据，响应完后，不会记录任何信息。
  >
  > - 缺点:  多次请求间不能共享数据
  > - 优点:  速度快
  >
  > 请求之间无法共享数据会引发的问题：
  >
  > - 如：京东购物。加入购物车和去购物车结算是两次请求
  > - 由于HTTP协议的无状态特性，加入购物车请求响应结束后，并未记录加入购物车是何商品
  > - 发起去购物车结算的请求后，因为无法获取哪些商品加入了购物车，会导致此次请求无法正确展示数据
  >
  > 具体使用的时候，我们发现京东是可以正常展示数据的，原因是Java早已考虑到这个问题，并提出了使用会话技术(Cookie、Session)来解决这个问题。具体如何来做，我们后面课程中会讲到。

  刚才提到HTTP协议是规定了请求和响应数据的格式，那具体的格式是什么呢?

### 2.3 请求数据格式

请求数据分为3部分:

1. 请求行:请求数据的第一行。其中GET表示请求方式，/
   表示请求资源路径，HTTP/1.1表示协议版本
2. 请求头:第二行开始，格式为key: value形式。
3. 请求体:POST请求的最后一部分，存放请求参数

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/3eabb13bbee1d3a0eab65babc751d5e0.png)

常见的HTTP请求头

- Host:表示请求的主机名
- User-Agent:浏览器版本，例如Chrome浏览器的标识类似Mozilla/5.0 ...Chrome/79，IE浏览器的标识类似Mozilla/5.o (Windows NT ...) like Gecko;
- Accept:表示浏览器能接收的资源类型，如`text/*`，`image/*`或者`*/*`表示所有;
- Accept-Language:表示浏览器偏好的语言，服务器可以据此返回不同语言的网页;
- Accept-Encoding:表示浏览器可以支持的压缩类型，例如gzip, deflate等。

GET请求和POST请求区别

- GET请求请求参数在请求行中，没有请求体。POST请求请求参数在请求体中
- GET请求请求参数大小有限制，POST没有



### 2.4 响应数据格式

响应数据分为3部分:

1. 响应行:响应数据的第一行。其中HTTP/1.1表示协议版
   本，200表示响应状态码，OK表示状态码描述
2. 响应头:第二行开始，格式为key: value形式
3. 响应体:最后一部分。存放响应数据

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/bd07e17ac413d695dc256099bc83a390.png)

常见的HTTP响应头

- Content-Type:表示该响应内容的类型，例如text/html,image/jpeg;
- Content-Length:表示该响应内容的长度（字节数);
- Content-Encoding:表示该响应压缩算法，例如gzip;
- Cache-Control:指示客户端应如何缓存，例如max-age=300表示可以最多缓存300秒

状态码分类

| 状态码分类 | 说明                                                         |
| ---------- | ------------------------------------------------------------ |
| 1xx        | **响应中**---临时状态码，表示请求已经接受，告诉客户端应该继续请求或者如果它已经完成则忽略它 |
| 2xx        | **成功**---表示请求已经被成功接收，处理已完成                |
| 3xx        | **重定向**----重定向到其它地方:它让客户端再发起一个请求以完成整个处理。 |
| 4xx        | **客户端错误**----处理发生错误，责任在客户端，如:客户端的请求一个不存在的资源，客户端未被授权，禁止访问等 |
| 5xx        | **服务器错误**----处理发生错误，责任在服务端，如:服务端抛出异常，路由出错，HTTP版本不支持等 |



在HTTP1.1版本中，浏览器访问服务器的几种方式： 

| 请求方式 | 请求说明                                                     |
| :------: | :----------------------------------------------------------- |
| **GET**  | 获取资源。<br/>向特定的资源发出请求。例：http://www.baidu.com/s?wd=itheima |
| **POST** | 传输实体主体。<br/>向指定资源提交数据进行处理请求（例：上传文件），数据被包含在请求体中。 |
| OPTIONS  | 返回服务器针对特定资源所支持的HTTP请求方式。<br/>因为并不是所有的服务器都支持规定的方法，为了安全有些服务器可能会禁止掉一些方法，例如：DELETE、PUT等。那么OPTIONS就是用来询问服务器支持的方法。 |
|   HEAD   | 获得报文首部。<br/>HEAD方法类似GET方法，但是不同的是HEAD方法不要求返回数据。通常用于确认URI的有效性及资源更新时间等。 |
|   PUT    | 传输文件。<br/>PUT方法用来传输文件。类似FTP协议，文件内容包含在请求报文的实体中，然后请求保存到URL指定的服务器位置。 |
|  DELETE  | 删除文件。<br/>请求服务器删除Request-URI所标识的资源         |
|  TRACE   | 追踪路径。<br/>回显服务器收到的请求，主要用于测试或诊断      |
| CONNECT  | 要求用隧道协议连接代理。<br/>HTTP/1.1协议中预留给能够将连接改为管道方式的代理服务器 |



## 3. Tomcat

Web服务器

- 是一个应该程序（软件)，对HTTP协议的操作进行封装，使得程序员不必直接对协议进行操作，让web开发更加便捷。主要功能是“提供网上信息浏览服务”

### 3.1 基本使用

配置

1. 修改启动端口号：confg/server.xml

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/853abff957d89fa85614fa50608259a1.png)

注意：HTTP协议默认端口号为80，如果将Tomcat端口号改为80，则将来访问Tomcat时，将不用输入端口号



启动时可能出现的问题

1. 端口号冲突:找到对应程序，将其关闭掉
2. 启动窗口一闪而过:检查JAVA_HOME环境变量是否正确配置



Tomcat部署项目

- 将项目放置到webapps目录下，即部署完成
- 一般JavaWeb项目会被打成war包，然后将war包放到webapps目录下，Tomcat会自动解压缩war文件

### 3.2 在IDEA中使用Tomcat

**使用Tomcat Maven插件**

1. 在pom.xml添加Tomcat插件

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/a5651efcd2e39e9a3f409d6571023aef.png)

2. 在Maven-->插件中运行命令

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/b1f553aee561b8c181204a8c3bb83129.png)



**直接配置Tomcat调试**

1. 编辑配置

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/c4e6b906cb6a8cc2f70d2770bf140ed4.png)

2. 添加配置

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/b1e7811798fcb66b296cf1fc910fdb42.png)

3. 选择Tomcat本地服务器

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/83a98bcbdec6547439581c5eb6e704d8.png)

4. 相关配置

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/7cb091dd6bb13de0430b5670a700c2de.png)



## 4. Servlet

Servlet

- 是Java提供的一门动态web资源开发技术
- Servlet是JavaEE规范之一，其实就是一个接口，需要定义Servlet类实现Servlet接口，并由web服务器运行Servlet

### 4.1 创建项目

1. 打开IDEA新建Jakarta EE项目，选择web模板，选择Tomcat服务器，构建系统选择Maven

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/d6305aaeba3e23c9262c119bd208bced.png)

2. 选择Java EE8 JDK，规范选择servlet和server faces

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/4719e10fa302ecc7dd52f754dde6b9dd.png)

3. 得到如下项目结构

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/3e37faae579eaeecfede81286f53e8c5.png)

4. 编辑配置，选择Tomcat 8.5，新版本会有莫名其妙的BUG

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/effcd6ab03a90811a0374cfca086c0bc.png)

5. 找到Tomcat/conf下的logging.properties，打开文件

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/21f7dfca7dc50040f2a19b74cc476b66.png)

6. 找到`java.util.logging.ConsoleHandler.encoding = UTF-8`将其修改为`java.util.logging.ConsoleHandler.encoding = GBK`，解决控制台中文乱码问题

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/a5b26e000aaf327e236d51c901f9ceab.png)

7. Tomcat正常

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/17c6c1b3f1dba13cd272d8953935630b.png)

8. servlet正常

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/b7beed01ab068bb12da9f209f4d6d434.png)

### 4.2 快速入门

1. 创建web项目，导入Servlet依赖坐标

```xml
<dependency>
  <groupId>javax.servlet</groupId>
  <artifactId>javax.servlet-api</artifactId>
  <version>4.0.1</version>
  <scope>provided</scope>
</dependency>
```

2. 创建：定义一个类，实现Servlet接口，并重写接口中所有方法，并在service方法中输入一句话

```java
public class ServletDemo implements Servlet{
    public void service(){}
}
```

3.  配置：在类上使用@WebServlet注解，配置盖Servlet的访问路径

```java
@WebServlet("/demo1")
public class ServletDemo implements Servlet{
    
}
```

4.  访问：启动Tomcat，浏览器输入URL访问该Servlet

**注意：**

- 如果出现WebServlet注解无效的情况，可以查看web.xml中web-app的版本是否大于3.0，并且metadata-compleete = false

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/87533d964e13cf089e106e11bafe945b.png)

### 4.3 Servlet执行流程

Servlet由谁创建? Servlet方法由谁调用?

- servlet由web服务器创建，Servlet方法由web服务器调用。

服务器怎么知道servlet中一定有service方法?

- 因为我们自定义的Servlet，必须实现Servlet接口并复写其方法，而Servlet接口中有service方法

Servlet生命周期

- 对象的生命周期指一个对象从被创建到被销毁的整个过程

Servlet运行在servlet容器(web服务器)中，其生命周期由容器来管理，分为4个阶段:

1. **加载和实例化**:默认情况下，当Servlet第一次被访问时，由容器创建servlet对象
2. **初始化**:在Servlet实例化之后，容器将调用servlet的`init()`方法初始化这个对象，完成一些如加载配置文件、创建连接等初始化的工作。**该方法只调用一次**
3. **请求处理**:每次请求servlet时，Servlet容器都会调用Servlet的`service()`方法对请求进行处理。
4. **服务终止**:当需要释放内存或者容器关闭时，容器就会调用servlet实例的`destroy()`方法完成资源的释放。在`destroy()`方法调用之后，容器会释放这个Servlet实例，该实例随后会被Java的垃圾收集器所回收



### 4.4 Servlet方法介绍

初始化方法，在Servlet被创建时执行，只执行一次

```java
void init(ServletConfig config)
```

提供服务方法，每次Servlet被访问，都会调用该方法

```java
void service(ServletRequest req, ServletResponse res)
```

销毁方法，当Servlet被销毁时，调用该方法。在内存释放或服务器关闭时销毁servlet

```java
void destroy()
```

获取ServletConfig对象

```java
ServletConfig getServletConfig()
```

获取Servlet信息

```java
String getServletlnfo()
```



### 4.5 Servlet体系结构

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/b2a459be84f4ff1ca4393cdd69ed24cc.png)

开发B/S架构的web项目，都是针对HTTP协议，所以自定义Servlet，会继承HttpServlet

#### 4.5.1 HttpServlet使用步骤

HttpServlet使用步骤

1. 继承HttpServlet
2. 重写doGet和doPost方法

#### 4.5.2 快速生成doGet和doPost方法模板

1. 右键文件夹，新建，选择servlet项目

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/fbaf6033b31fa020aecd5b4afee49b6f.png)

2. 默认的servlet模板

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/3b90109215cca65ce56362ea9a89cb4c.png)



#### 4.5.3 HttpServlet原理

HttpServlet原理

- 获取请求方式，并根据不同的请求方式，调用不同的doXxx方法



### 4.6 Servlet urlPattern配置

Servlet要想被访问，必须配置其访问路径(urlPattern)

1. 一个Servlet，可以配置多个urlPattern

```java
@WebServlet(urlPatterns = {"/demo1" , "/demo2"})
```

2. urlPattern配置规则
   ① 精确匹配
   ② 目录匹配
   ③ 扩展名匹配
   ④ 任意匹配



**① 精确匹配**

- 配置路径

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/9569967d76627efef8c15e029b1ec43a.png)

- 访问路径

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/259ce1e686bf6753f49e51ad5a47c053.png)

**② 目录匹配**

- 配置路径

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/d44cbb09e5a41e210cc5b79f821b59f5.png)

- 访问路径

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/8647ca09d2aea27ac04b4ef22a2f6f2b.png)

**③ 扩展名匹配**

- 配置路径

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/165190c79c17c07edd91a724c3690ce9.png)

- 访问路径

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/ed6e4204cf1be4cf5f87524bad7a1c1d.png)

**④ 任意匹配**

- 配置路径

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/ce6190fb1fb930fa10942ddb1972b22c.png)

- 访问路径

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/606bd7a2c2b88725efc5f6970487b881.png)

- `/`和`/*`区别:
  - 当我们的项目中的Servlet配置了“`/`”，会覆盖掉tomcat中的DefaultServlet，当其他的url-pattern都匹配不上时都会走这个Servlet
  - 当我们的项目中配置了“`/*`”，意味着匹配任意访问路径

**优先级**

- 精确路径>目录路径>扩展名路径>`/*`>`/`



### 4.7 XML配置方式编写Servlet

Servlet 从3.0版本后开始支持使用注解配置，3.0版本前只支持XML配置文件的配置方式



步骤

1. 编写Servlet类
2. 在web.xml中配置该Servlet

```xml
<!--  全类名-->
<servlet>
  <servlet-name>demo</servlet-name>
  <servlet-class>com.test.SeervletDemo</servlet-class>
</servlet>
<!--  访问路径-->
<servlet-mapping>
  <servlet-name>demo</servlet-name>
  <url-pattern>/demo</url-pattern>
</servlet-mapping>
```



### 4.8 Requst 和 Response

Request

- 获取请求数据

Response

- 设置响应数据



### 4.9 Requst

Request

- 使用request对象来获取请求数据

#### 4.9.1 Request 继承体系

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/43eb4d47897b8853167489fc722223cd.png)

1. Tomcat需要解析请求数据，封装为request对象,并且创建request对象传递到service方法中
2. 使用request对象，查阅JavaEE API文档的HttpServletRequest接口

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/33bc0e25cd112ba3614a92a04d35d663.png)

#### 4.9.2 Request获取请求数据

请求数据分为3部分




- 请求行

```
GET /request-demo/req1?username=zhangsan HTTP/1.1
```

- 
  - `String getMethod()`:获取请求方式:GET
  - `String getContextPath()`:获取虚拟目录(项目访问路径): /request-demo
  - `StringBuffer getRequestURL()`:获取URL(统一资源定位符): http:/localhost:8080/request-demo/req1
  - `String getRequestURI()`:获取URI(统一资源标识符): /request-demo/req1
  - `String getQueryString():`获取请求参数（GET方式) : username=zhangsan&password=123


- 请求头

```
User-Agent: Mozilla/5.0 Chrome/91.0.4472.106
```

- 
  - `String getHeader(String name)`:根据请求头名称，获取值

- 请求体

```
username=superbaby&password=123
```

- 
  - `ServletlnputStream getInputStream()`:获取字节输入流
  - `BufferedReader getReader()`:获取字符输入流




请求参数获取方式

- GET方式

```java
String getQueryString()
```

- POST方式

```java
BufferedReader getReader()
```



#### 4.9.3 通用方式获取请求参数

`Map<String, String[] >getParameterMap()`

- 获取所有参数Map集合String[ ] 

`getParameterValues(String name)`

- 根据名称获取参数值（数组)String 

`getParameter(String name)`

- 根据名称获取参数值（单个值)



`Map<String, String[] >getParameterMap()`演示

 ```java
 @Override
 protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
   Map<String, String[]> map = req.getParameterMap();
   for(String key : map.keySet()){
     System.out.print(key+":");
     for(String value : map.get(key)){
       System.out.print(value);
     }
     System.out.println();
   }
 }
 ```



#### 4.9.4 Request请求参数中文乱码处理

请求参数如果存在中文数据，则会乱码



解决方案

- POST:设置输入流的编码

```java
req.setCharacterEncoding("UTF-8");
```

- GET:将读入的字符串转换为UTF-8编码，(Tomccat 8之后默认编码为UTF-8，已不存在中文乱码问题)

```java
username = new String(username.getBytes(StandardCharsets.IS0_8859_1),StandardCharsets.UTF_8);
```



URL编码

1. 将字符串按照编码方式转为二进制
2. 每个字节转为2个16进制数并在前边加上%

URL编解码方法

1. 编码

```java
URLEncoder.encode(str, "utf-8");
```

2. 解码

```java
URLDecoder.decode(str, "ISO-8859-1");
```



#### 4.9.5 Request请求转发

请求转发(forward)

- 一种在服务器内部的资源跳转方式

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/f93edb09178b74d834a247dea6cb383e.png)

实现方法

```java
req.getRequestDispatcher("资源B路径").forward(req,resp);
```

请求转发资源间共享数据: 使用Request对象

- `void setAttribute(String name, Object o)`:存储数据到request域中
- `Object getAttribute(String name)`:根据key，获取值
- `void removeAttribute(String name)`:根据key，删除该键值对

请求转发特点:

- 浏览器地址栏路径不发生变化
- 只能转发到当前服务器的内部资源
- —次请求，可以在转发的资源间使用request共享数据



### 4.10 Response

Response

- 使用response对象来设置响应数据

#### 4.10.1 Response设置响应数据

响应数据分为3部分

- 响应行

```
HTTP/1.1 200 OK
```


- 

  - `void setStatus(int sc)`:设置响应状态码




- 响应头

```
Content-Type: text/html
```


- 

  - `void setHeader(String name, String value)`∶设置响应头键值对




- 响应体

```
<html><head>head><body></body></html>
```

- 
  - `PrintWriter getWriter()`:获取字符输出流
  - `ServletOutputStream getOutputStream()`:获取字节输出流

#### 4.10.2 Response完成重定向

重定向(Redirect)

- 一种资源跳转方式

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/b30cec252f21793947f0780a78c28e91.png)

实现方法

```java
resp.setStatus(302);
resp.setHeader("location","资源B的路径");
```

或者

```java
resp.sendRedirect("资源B的路径");
```

资源路径为`虚拟路径 + WebServlet注解路径`



重定向特点:

- 浏览器地址栏路径发生变化
- 可以重定向到任意位置的资源(服务器内部、外部均可)
- 两次请求，不能在多个资源使用request共享数据

#### 4.10.3 路径问题

明确路径谁使用?

- 浏览器使用:需要加虚拟目录(项目访问路径)
- 服务端使用:不需要加虚拟目录



示例

- `<a href='路径'>`加虚拟目录
- `<form action='路径' >`加虚拟目录
- `req.getRequestDispatcher(“路径")`不加虚拟目录
- `resp.sendRedirect(“路径”)`加虚拟目录



动态获取虚拟路径

```java
String contextPath = request.getContextPath();
response.sendRedirect(contextPath+"/资源路径");
```



#### 4.10.4 Response响应字符数据

使用

1. 通过Response对象获取字符输出流

```java
PrintWriter writer = resp.getWriter();
```

2. 写数据

```java
writer.write("aaa");
```

3. 设置写文本类型和编码(识别HTML标签，防止中文乱码)

```java
response.setContentType("text/html; charset=utf-8");
```

4. 字符输出流不需要关闭



读入图片

```java
// 1. 读取文件
FileInputStream fis = new FileInputStream("/WEB-INF/classes/1.png");
// 2. 获取response输出字节流
ServletOutputStream os = response.getOutputStream();
// 3. 完成流的copy
IOUtils.copy(fis, os);
```

使用IOUtils工具类进行copy

1. 导入坐标

```xml
<dependency>
    <groupId>commons-io</groupId>
    <artifactId>commons-io</artifactId>
    <version>2.11.0</version>
</dependency>
```

2. 使用

```xml
IOUtils.copy(输入流, 输出流);
```

## 5. 案例-用户登录

### 5.1 准备工作

1. 登录界面代码，放入webapp文件夹中

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/64cbbd2f5d7823b8a7e8fd998b30e42e.png)

2. 创建数据库

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/f70ee64b6c59a5132974600e46731f27.png)

3. 创建User类

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/604ee87f258a02d55011b7e04c8c1a79.png)

4. 导入MyBatis，Mysql坐标

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/de66b241a9537b848de07a72cb66c6c6.png)

5. 创建mybatis-config.xml核心配置文件

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/f5a6eb6a2256d4badc410f5fb78646a9.png)

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE configuration
        PUBLIC "-//mybatis.org//DTD Config 3.0//EN"
        "https://mybatis.org/dtd/mybatis-3-config.dtd">
<configuration>
    <environments default="development">
        <environment id="development">
            <transactionManager type="JDBC"/>
            <dataSource type="POOLED">
                <property name="driver" value="com.mysql.jdbc.Driver"/>
                <property name="url" value="jdbc:mysql:///db1?useSSL=false&amp;useServerPrepStmts=true"/>
                <property name="username" value="root"/>
                <property name="password" value="123456"/>
            </dataSource>
        </environment>
    </environments>
    <mappers>
        <package name="com.test.mapper"/> <!-- 注意package和mapper-->
    </mappers>
</configuration>
```

6. 创建UserMapper接口

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/712dcd6333f1541e986cd4d5dcc0d3a2.png)

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/3b75b79d4490edfda30feb56707c64e4.png)

7. 创建UserMapper.xml映射文件

在resources下创建目录

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/9afc0f32c2406e3ce9c2be2582ad29ef.png)

创建UserMapper.xml

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/ea300eb399c5dd9e79e7b8abbca056cd.png)

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE mapper
        PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
        "https://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="com.test.mapper.UserMapper">
    <select id="selectBlog" resultType="com.test.pojo.User">
    </select>
</mapper>
```



### 5.2 登录流程

流程说明

1. 用户填写用户名密码，提交到LoginServlet
2. 在LoginServlet中使用MyBatis查询数据库，验证用户名密码是否正确
3. 如果正确，响应“登录成功”，如果错误，响应“登录失败”

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/21099e14cad958ed391f6516cf2c6c6f.png)

**代码实现**

1. 在UserMapper类中添加select方法

```java
@Select("select * from tb_user where username=#{username} and password=#{password}")
User select(@Param("username") String username, @Param("password") String password);
```

2. 创建com.test.web.response.LoginServlet  servlet类

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/390f487952b7bbb32121ec20125c7636.png)

编写代码

```java
// 1. 获取用户名密码
String username = request.getParameter("username");
String password = request.getParameter("password");

// 2. 调用MyBatis完成查询
// 2.1 获取sqlSessionFactory对象
String resource = "mybatis-config.xml";
InputStream inputStream = Resources.getResourceAsStream(resource);
SqlSessionFactory sqlSessionFactory = new SqlSessionFactoryBuilder().build(inputStream);
// 2.2 获取sqlSession对象
SqlSession sqlSession = sqlSessionFactory.openSession();
// 2.3 获取mapper接口的代理对象
UserMapper mapper = sqlSession.getMapper(UserMapper.class);
// 2.4 执行查询方法
User user = mapper.select(username, password);
// 2.5 释放资源
sqlSession.close();

// 获取对应的字符输出流，设置响应内容类型
response.setContentType("text/html;charset=utf-8");
PrintWriter writer = response.getWriter();
// 3. 判断user是否为空
if(user != null){
  // 登录成功
  writer.write("登录成功，欢迎您，" + user.getUsername());
}else{
  // 登录失败
  writer.write("登录失败，用户名或密码错误");
}
```

3. 运行项目，servlet正常



### 5.3 用户注册

流程说明:

1. 用户填写用户名、密码等信息，点击注册按钮，提交到RegisterServlet

2. 在RegisterServlet中使用MyBatis 保存数据
3. 保存前，需要判断用户名是否已经存在:根据用户名查询数据库

 ![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/1816e7a630274434aa55363abed44657.png)

**代码实现**

1. 在UserMapper类中添加selectByUsername和add方法

```java
@Select("select * from tb_user where username=#{username}")
User selectByUsername(@Param("username")  String username);

@Insert("insert into tb_user values(null, #{username}, #{password})")
void add(User user);
```

2. 创建com.test.web.response.RegisterServlet  servlet类

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/5a26df37870204e3fe43751af4fc0009.png)

编写代码

```java
// 1. 接受用户数据
String username = request.getParameter("username");
String password = request.getParameter("password");
// 封装用户对象
User user = new User(null, username, password);

// 2. 调用mapper 根据用户名查询用户
String resource = "mybatis-config.xml";
InputStream inputStream = Resources.getResourceAsStream(resource);
SqlSessionFactory sqlSessionFactory = new SqlSessionFactoryBuilder().build(inputStream);
SqlSession sqlSession = sqlSessionFactory.openSession();
UserMapper mapper = sqlSession.getMapper(UserMapper.class);
User u = mapper.selectByUsername(username);

// 3. 判断用户是否存在
if (u == null) {
  // 用户不存在，可以添加用户
  mapper.add(user);
  // 提交事务
  sqlSession.commit();
  // 释放资源
  sqlSession.close();
} else {
  // 用户已存在，不可以添加用户
  response.setContentType("text/html;charset=utf-8");
  response.getWriter().write("用户名已存在");
}
```



### 5.4 代码优化

创建SqlSessionFactory代码优化

```java
String resource = "mybatis-config.xml";
InputStream inputStream = Resources.getResourceAsStream(resource);
SqlSessionFactory sqlSessionFactory = new SqlSessionFactoryBuilder().build(inputStream);
```

问题:

1. 代码重复，应使用工具类

2. SqlSessionFactory 重复创建，浪费资源

解决方案

- 创建SqlSessionFactory工具类

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/491dce89625268330bdeb5725d780f1d.png)

编写代码

```java
public static SqlSessionFactory sqlSessionFactory;
static {
  // 静态代码块会随着类的加载而执行，只会执行一次
  try {
    String resource = "mybatis-config.xml";
    InputStream inputStream = Resources.getResourceAsStream(resource);
    sqlSessionFactory = new SqlSessionFactoryBuilder().build(inputStream);
  } catch (IOException e) {
    throw new RuntimeException(e);
  }
}

public static SqlSessionFactory getSqlSessionFactory() {
  return sqlSessionFactory;
}
```

替换之前的代码

```java
SqlSessionFactory sqlSessionFactory = sqlSessionFactoryUtil.getSqlSessionFactory();
```

## 6. JSP

概念:

- Java Server Pages，Java服务端页面
- 一种动态的网页技术，其中既可以定义HTML、JS、CSS等静态内容，还可以定义Java代码的动态内容
- JSP = HTML + Java
- JSP的作用:简化开发，避免了在Servlet中直接输出HTML标签

### 6.1 快速入门

1. 导入坐标

```xml
<dependency>
    <groupId>javax.servlet.jsp</groupId>
    <artifactId>jsp-api</artifactId>
    <version>2.2</version>
</dependency>
```

2. 创建jsp文件，编写代码

### 6.2 JSP原理

JSP原理

- JSP本质上是一个servlet
- JSP在被访问时，由JSP容器(Tomcat)将其转换为Java文件(Servlet)，在由JSP容器(Tomcat)将其编译，最终对外提供服务的其实就是这个字节码文件

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/ec23a7c53f3b4705fe73817afa30cc03.png)

### 6.3 JSP脚本

JSP脚本

- JSP脚本用于在JSP页面内定义Java代码

- JSP脚本分类     
  - <%...%>∶内容会直接放到jspService(方法之中
  - <%=...%>∶内容会放到out.print()中，作为out.print()的参数
  - <%!...%>:内容会放到jspService()方法之外，被类直接包含

### 6.4 EL表达式

EL表达式

- Expression Language表达式语言，用于简化JSP页面内的Java代码
- 主要功能:获取数据
- 语法:` ${expression}`

JavaWeb中的四大域对象

1. page:当前页面有效
2. request:当前请求有效
3. session:当前会话有效
4. application:当前应用有效

**el表达式获取数据，会依次从这4个域中寻找，直到找到为止**

### 6.5 JSTL标签

JSP标准标签库(Jsp Standarded Tag Library)，使用标签取代JSP页面上的Java代码



###  6.6 JSP的缺点

由于JSP页面内，既可以定义HTML标签，又可以定义Java代码，造成了以下问题:

1. 书写麻烦:特别是复杂的页面
2. 阅读麻烦
3. 复杂度高:运行需要依赖于各种环境，JRE，JSP容器，JavaEE...
4. 占内存和磁盘:JSP会自动生成.java和.class文件占磁盘，运行的是.class文件占内存
5. 调试困难:出错后，需要找到自动生成的.java文件进行调试
6. 不利于团队协作:前端人员不会Java，后端人员不精HTML
7. 维护性差
8. ...

**现在主流是使用HTML+JS框架+AJAX实现前后端分离**

## 7. MVC模式

MVC是一种分层开发的模式，其中

- M: Model，业务模型，处理业务
- V: View，视图，界面展示
- C: Controller，控制器，处理请求，调用模型和视图

MVC好处

- 职责单一，互不影响
- 有利于分工协作
- 有利于组件重用

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/92bda45beff729ba935b354e99331834.png)

### 7.1 三层架构(SSM)

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/60c3f894d404c8698a14a1ad2bb8b319.png)

数据访问层

- 对数据库的CRUD基本操作

业务逻辑层

- 对业务逻辑进行封装，组合数据访问层层中基本功能，形成复杂的业务逻辑功能

表现层

- 接收请求，封装数据，调用业务逻辑层，响应数据

## 8. 会话跟踪技术

会话

- 用户打开浏览器，访问web服务器的资源，会话建立，直到有一方断开连接，会话结束。在一次会话中可以包含**多次请求和响应**

会话跟踪

- 一种维护浏览器状态的方法，服务器需要识别多次请求是否来自于同一浏览器，以便在同一次会话的多次请求间**共享数据**

- HTTP协议是**无状态**的，每次浏览器向服务器请求时，**服务器都会将该请求视为新的请求**，因此我们需要会话跟踪技术来实现会话内数据共享请求

实现方式

- 客户端会话跟踪技术:**Cookie**
- 服务端会话跟踪技术:**Session**

Cookie和Session都是来完成一次会话内多次请求间数据共享的

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/34c5c602dda6a1ecdcc031dc20150c35.png)

### 8.1 Cookie的基本使用

Cookie

- 客户端会话技术，将数据保存到客户端，以后每次请求都携带Cookie数据进行访问

Cookie的基本使用

- 发送Cookie
  1. 创建Cookie对象，设置数据

```java
Cookie cookie = new Cookie("key","value");
```

- 
  2. 发送Cookie到客户端:使用response对象

```java
response.addCookie(cookie);
```

- 获取Cookie
  1. 获取客户端携带的所有Cookie，使用request对象

```java
Cookie[]cookies = request.getCookies();
```

- 
  2.  遍历数组，获取每一个Cookie对象
  3. 使用Cookie对象方法获取数据

```java
cookie.getName();
cookie.getValue();
```



### 8.2 Cookie原理

Cookie的实现是基于HTTP协议的

- 响应头: set-cookie
- 请求头: cookie

### 8.3 Cookie存活时间

Cookie存活时间

- **默认情况下**，Cookie存储在浏览器内存中，**当浏览器关闭，内存释放，则Cookie被销毁**

- `setMaxAge(int seconds)`:设置Cookie存活时间
  1. 正数:将Cookie写入浏览器所在电脑的硬盘，持久化存储。到时间自动删除
  2. 负数:默认值，Cookie在当前浏览器内存中，当浏览器关闭，则Cookie被销毁
  3. 零:删除对应Cookie

### 8.4 Cookie存储中文

Cookie存储中文

- Cookie不能直接存储中文

解决方法

- 使用URL编码

### 8.5 Session的基本使用

Session

- 服务端会话跟踪技术:将数据保存到服务端

- JavaEE提供 HttpSession接口，来实现一次会话的多次请求间数据共享功能

- 使用

  1. 获取Session对象`HttpSession session = request.getSession();`

  2. Session对象功能:
     - `void setAttribute(String name, Object o)`:存储数据到session域中
     - `Object getAttribute(String name)`:根据key，获取值
     - `void removeAttribute(String name)`:根据key，删除该键值对

### 8.6 Session原理

Session原理

- Session是基于Cookie实现的

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/82d612e51fcd50539ad35c343077030c.png)

### 8.7 Session的钝化、活化

Session的钝化、活化

- **钝化**:在服务器正常关闭后，Tomcat会自动将Session数据写入硬盘的文件中
- **活化**:再次启动服务器后，从文件中加载数据到Session中

### 8.8 Session销毁

Session销毁

- 默认情况下，无操作，30分钟自动销毁

```xml
<!-- Web.xml中的配置-->
<session-config>
	<session-timeout>30</ session-timeout>
</session-config>
```

- 调用Session对象的`invalidate()`方法

## 9. Filter

Filter

- 概念: Filter表示过滤器，是JavaWeb三大组件(Servlet、Filter、Listener)之一。
- 过滤器可以把对资源的请求拦截下来，从而实现一些特殊的功能。
- 过滤器一般完成一些通用的操作，比如:权限控制、统一编码处理、敏感字符处理等等..

### 9.1 快速入门

1. 定义类，实现Filter接口，并重写其所有方法

```java
public class FilterDemo implements Filter{
	public void init(FilterConfig filterConfig);
    public void doFilter(servletRequest request
    public void destroy();
}
```

2. 配置Filter拦截资源的路径:在类上定义@WebFilter注解

```java
@WebFilter("/*")
public class FilterDemo implements Filter {
```

3. 在doFilter方法中输出一句话，并放行

```java
public void doFilter(ServletRequest request, ser
    // 注意使用javax.servlet-api的版本要3.1
	system.out.println("filter被执行了...");
    //放行
	filterCh ain .doFilter(request , response);
}
```

### 9.2 Filter执行流程

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/42d946bf4318f0983d98b8b98e819703.png)

### 9.3 Filter 拦截路径配置

Filter可以根据需求，配置不同的拦截资源路径

- 拦截具体的资源:/index.jsp:只有访问index.jsp时才会被拦截。
- 目录拦截:/user*:访问/user下的所有资源，都会被拦截
- 后缀名拦截: *.jsp:访问后缀名为jsp的资源，都会被拦截
- 拦截所有:/*:访问所有资源，都会被拦截

### 9.4 过滤器链

过滤器链

- 一个Web应用，可以配置多个过滤器，这多个过滤器称为过滤器链

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/ea812f034d20ead88dcf471c74ca8424.png)

- 注解配置的Filter，优先级按照过滤器类名(字符串)的自然排序

## 10. Listener

Listener

- 概念:Listener表示监听器，是JavaWeb 三大组件(Servlet、Filter、Listener)之一。
- 监听器可以监听就是在application,session,request三个对象创建、销毁或者往其中添加修改删除属性时自动执行代码的功能组件
- Listener分类: JavaWeb中提供了8个监听器

| 监听器分类         | 监听器名称                      | 作用                                         |
| ------------------ | ------------------------------- | -------------------------------------------- |
| ServletContext监听 | servletContextListener          | 用于对ServletContext对象进行监听(创建、销毁) |
|                    | servletContextAttributeListener | 对ServletContext对象中属性的监听(增删改属性) |
| Session监听        | HttpSessionListener             | 对Session对象的整体状态的监听(创建、销毁)    |
|                    | HttpSessionAttributeListener    | 对Session对象中的属性监听(增删改属性)        |
|                    | HttpSessionBindingListener      | 监听对象于Session的绑定和解除                |
|                    | HttpsessionActivationListener   | 对Session数据的钝化和活化的监听              |
| Request监听        | servletRequestListener          | 对Request对象进行监听(创建、销毁)            |
|                    | servletRequestAttributeListener | 对Request对象中属性的监听(增删改属性)        |

## 11. AJAX

AJAX

- 概念:AJAX(Asynchronous JavaScript And XML):异步的JavaScript和XML

- AJAX作用:
  1. 与服务器进行数据交换:通过AJAX可以给服务器发送请求，并获取服务器响应的数据
     - 使用了AJAX和服务器进行通信，就可以使用HTML+AJAX来替换JSP页面了
  2. 异步交互:可以在**不重新加载整个页面**的情况下，与服务器交换数据并**更新部分网页**的技术，如:搜索联想、用户名是否可用校验，等等.

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/e7dd2371c068e2331adb79a1e321e166.png)

同步和异步

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/d82819f71f277571967e123a08b62bb9.png)

### 11.1 快速入门

1. 编写AjaxServlet，并使用response输出字符串
2. 创建XMLHttpRequest对象:用于和服务器交换数据

```js
var xmlhttp;
if (window.XMLHttpRequest){
	// code for IE7+, Firefox, Chrome, Opera,Safari
    xmlhttp = new XMLHttpRequest();
}else {
	// code for IE6,IE5
	xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
}
```

3. 向服务器发送请求

```js
xmlhttp.open("GET","url");
xmlhttp.send();//发送请求
```

4. 获取服务器响应数据

```js
xmlhttp.onreadystatechange = function (){
	if (xmlhttp.readyState == 4 && xmlhttp.status == 200){
        alert(xmlhttp.responseText);
	}
}
```

### 11.2 Axios异步框架

Axios异步框架

- Axios 对原生的AJAX进行封装，简化书写
- 官网: https://www.axios-http.cn

#### 11.2.1 快速入门

1. 引入axios的js文件

```html
<script src="js/axios-0.18.0.js"></script>
```

2. 使用axios 发送请求，并获取响应结果

```js
axios({
	method:"get",
	url:"http:ilocalhost:8080/ajax-demo1/aJAXDemo1?username=zhangsan"
}).then(function (resp){
	alert(resp.data);
});
```

```js
axios({
	method:"post",
	url:"http:ilocalhost:8080/ajax-demo1/aJAXDemo1",
    data:"username=zhangsan”
}).then(function (resp){
	alert(resp.data);
});
```

