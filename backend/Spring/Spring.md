# Spring

官网：https://spring.io/

## 1.Spring简介

Spring框架概述

- spring是一个开源的轻量级Java开发应用框架，可以简化企业级应用开发。Spring解决了开发者在JavaEE开发中遇到的许多常见的问题，提供了功能强大IOC、AOP及Web MVC等功能。是当前企业中Java开发几乎不能缺少的框架之一。Spring的生态及其完善，不管是Spring哪个领域的解决方案都是依附于在Spring Framework基础框架的。

Spring生态圈的主要组成

- Spring Framework
- Spring Boot
- Spring Cloud

### 1.2 Spring Framework

Spring Framework

- Spring Framework是Spring生态圈中最基础的项目，是其他项目的根基



Spring Framework系统框架

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/1e7c394368be6addec9c7c524579369a.png)



### 1.3 核心概念

代码书写现状
- 耦合度偏高

解决方案

- 使用对象时，在程序中不要主动使用`new`产生对象，转换为由外部提供对象

---

**IoC ( Inversion of Control )控制反转**

- 使用对象时，由主动`new`产生对象转换为由外部提供对象，此过程中对象创建控制权由程序转移到外部，此思想称为控制反转

`Spring`技术对`IoC`思想进行了实现

- `Spring`提供了一个容器，称为`IoC`容器，用来充当`IoC`思想中的外部)
- `IoC`容器负责对象的创建、初始化等一系列工作，被创建或被管理的对象在`IoC`容器中统称为`Bean`

**DI ( Dependency Injection )依赖注入**

- 在容器中建立`bean`与`bean`之间的依赖关系的整个过程，称为**依赖注入**

目标:**充分解耦**

- 使用`IoC`容器管理`bean (IoC)`

- 在`Ioc`容器内将有依赖关系的`bean`进行关系绑定`(DI)`

最终效果

- 使用对象时不仅可以直接从`IoC`容器中获取，并且获取到的`bean`已经绑定了所有的依赖关系



### 1.4 IoC入门案例

思路分析：

1. 管理什么？（Service与Dao）
2. 如何将被管理的对象告知IoC容器？（配置）
3. 被管理的对象交给IoC容器，如何获取到IoC容器？（接口）
4. IoC容器得到后，如何从容器中获取bean？（接口方法）
5. 使用Spring导入哪些坐标？（pom.xml）

步骤：

1. 创建Javaweb项目，创建BookDao，BookSerive接口及其实现类
2. 导入Spring-context

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/ed77a2c2e315e4740ce9cb4dc4913fe2.png)

3. 创建Spring配置文件，配置Bean

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/c503a3b1b4caae4cf1d6adfbe98d2e3f.png)

4. 在app中获取bean对象

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/bdc6beaa5a9abb05d23fd5b9366cfadd.png)



### 1.5 DI入门案例

思路分析：

1. 基于IoC管理bean

2. Service中使用new形式创建的Dao对象是否保留?(否)
3. Service中需要的Dao对象如何进入到service中?（提供方法)
4. Service与Dao间的关系如何描述?（配置)

步骤：

1. 删除使用new形式创建对象的代码，提供对应的`setter`方法

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/cd6532a3203510c77b03a5bc0e99c096.png)

2. 配置servicce与dao之间的关系

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/e492c33a045889f020b4495f68127f67.png)

## 2. XML配置

### 2.1 Bean的配置

#### 2.1.1 bean的基础配置

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/e8e91f37bf7b0dbe6d4cc670b9a6f46e.png)

#### 2.1.2 bean的作用范围配置

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/d9dd3ea36fef74f1c593eeb2564c0006.png)

bean默认为单例，需要手动设置"scope=prototype"来设置非单例bean

适合交给容器进行管理的bean

- 表现层对象
- 业务层对象
- 数据层对象
- 工具对象

不适合交给容器进行管理的bean

- 封装实体的域对象



#### 2.1.3 bean实例化

bean本质上就是对象，创建bean使用构造方法完成

---

**实例化bean的三种方式**

- 构造方法

   提供可访问的构造方法

```java
public class BookDaoImpl implements BookDao{
    public BookDaoImpl(){
        System.out.println("book constructor is running ...");
    }
    public void save(){
        System.out.println("book dao save ...");
    }
}
```

​		配置

```xml
<bean
	id="bookDao"
	class="com.itheima.dao.impl.BookDaoImpl"
/>	
```

​	无参构造方法如果不存在，将抛出异常`BeanCreationException`

---

- 静态工厂

```java
public class OrderDaoFactory {
	public static OrderDao getOrderDao(){
		return new OrderDaoImpl();
	}
}
```

​	配置

```xml
<bean
	id="orderDao"
	factory-method="getOrderDao"
	class="com.itheima.factory.OrderDaoFactory"
/>
```

---

-  实例工厂

```java
public class UserDaoFactory {
	public UserDao getUserDao(){
		return new UserDaoImpl();
	}
}
```

​	配置

```xml
<bean id="userDaoFactory"-class="com.itheima.factory.UserDaoFactory" />
<!-- 创建多余bean，不合理-->

<bean
	id="userDao"
	factory-method="getUserDao"
    factory-bean="userDaoFactory"
/>
```

---

- **FactoryBean实例化**

```java
public class UserDaoFactoryBean implements FactoryBean<UserDao>{
	public UserDao getObject() throws Exception {
		return new UserDaoImpl();
	}
	public class<?> getobjectType() {
		return UserDao.class;
	}
}

```

​		配置

```xml
<bean
	id="userDao"
	class="com.itheima.factory. UserDaoFactoryBean"
/>
```



#### 2.1.4 bean的生命周期

生命周期

- 从创建到消亡的完整过程

bean生命周期

- bean从创建到销毁的整体过程

bean生命周期控制

- 在bean创建后到销毁前做一些事情

---

提供生命周期控制方法

```java
public class BookDaoImpl implements BookDao {
	public void save() {
		System.out.println( "book dao save ... " );
	}
	public void init(){
		system.out.print1n( "book init ..." );
	}
	public void destory(){
		system.out.println( "book destory ..." );
	}
}
```

 

配置生命周期控制方法

- xml

```xml
<bean id="bookDao"class=" com.itheima.dao .impl.BookDaoImpl" init-method="init" destroy-method= "destory" />
```

- 实现InitializingBean,DisposableBean接口

```java
public class BookServiceImpl implements BookService,InitializingBean,DisposableBean {
	public void save() {
		system.out.println( "book service save ..." );
	}
	public void afterPropertiesSet() throws Exception{
		system.out.println( "afterPropertiesset" );
	}
	public void destroy() throws Exception {
		System.out.println( "destroy" );
	}
}
```

---

初始化容器

1. 创建对象（内存分配)
2. 执行构造方法
3. 执行属性注入( set操作）
4. 执行bean初始化方法

使用bean

1. 执行业务操作

关闭/销毁容器

1. 执行bean销毁方法

---

bean销毁时机

- 容器关闭前触发bean的销毁
- 关闭容器方式︰
  - 手工关闭容器
    `ConfigurableApplicationcontext`接口`close()`操作
  - 注册关闭钩子，在虚拟机退出前先关闭容器再退出虚拟机
    `ConfigurableApplicationContext`接口`registerShutdownHook()`操作

```java
public class AppForLifeCycle {
	public static void main( String[] args ) {
		classPathXmlApplicationContext ctx = new ClassPathXmlApplicationContext( "applicationContext.xml" );
    	ctx.close();
	}
}
```



### 2.3 依赖注入

思考︰向一个类中传递数据的方式有几种?

- 普通方法(set方法)
- 构造方法

思考︰依赖注入描述了在容器中建立bean与bean之间依赖关系的过程，如果bean运行需要的是数字或字符串呢?

- 引用类型
- 简单类型（基本数据类型与string )

依赖注入方式

- setter注入
  - 简单类型
  - 引用类型
- 构造器注入
  - 简单类型
  - 引用类型



#### 2.3.1 setter注入

引用类型

- 在bean中定义引用类型属性并提供可访问的set方法

```java
public class BookServiceImpl implements BookService{
	private BookDao bookDao;
	public void setBookDao(BookDao bookDao) {
		this.bookDao = bookDao;
	}
}
```

- 配置中使用`property`标签`ref`属性注入引用类型对象

```xml
<bean id="bookService" class=" com.itheima.service.impl.BookServiceImpl">
	<property name="bookDao" ref="bookDao" />
</bean>
<bean id="bookDao" class="com.itheima.dao.impl.BookDaoImpl" />
```



简单类型

- 在bean中定义引用类型属性并提供可访问的set方法

```java
public class BookDaoImpl implements BookDao {
	private int connectionNumber;
	public void setConnectionNumber(int connectionNumber) {
		this.connectionNumber = connectionNumber;
	}
}
```

- 配置中使用`property`标签 `value`属性注入简单类型数据

```xml
<bean id="bookDao" class="com.itheima.dao.impl.BookDaoImpl">
	<property name="connectionNumber" value="10" />
</bean>
```



#### 2.3.2 构造器注入

引用类型

-  在bean中定义引用类型属性并提供可访问的构造方法

```java
public class BookServiceImpl implements BookService{
	private BookDao bookDao;
	public BookServiceImp1( BookDao bookDao) {
		this.bookDao = bookDao;
	}
}
```

- 配置中使用`constructor-arg`标签 `ref`属性注入引用类型对象

```xml
<bean id="bookService" class="com.itheima. service.impl.BookServiceImpl">
	<constructor-arg name="bookDao" ref="bookDao" />
</bean>
<bean id="bookDao" class="com.itheima.dao.impl.BookDaoImpl" />
```



简单类型

-   在bean中定义引用类型属性并提供可访问的`set`方法

```java
public class BookDaoImpl implements BookDao {
	private int connectionNumber;
	public void setConnectionNumber( int connectionNumber) {
		this.connectionNumber = connectionNumber;
	}
}
```

- 配置中使用`constructor-arg`标签`value`属性注入简单类型数据

```xml
<bean id="bookDao" class="com.itheima.dao.impl.BookDaoImpl">
	<constructor-arg name="connectionNumber" value="10" />
</ bean>
```



参数适配

- 配置中使用`constructor-arg`标签`type`属性设置按形参类型注入

```xml
<bean id="bookDao" class="com.itheima.dao.impl.BookDaoImpl">
	<constructor-arg type="int" value="10" />
	<constructor-arg type="java.lang.String" value="mysql"/>
</ bean>
```

- 配置中使用`constructor-arg`标签`index`属性设置按形参位置注入

```xml
<bean id="bookDao" class="com.itheima.dao.impl.BookDaoImpl">
	<constructor-arg index="e" value="10" />
	<constructor-arg index="1" value="mysql" />
</bean>
```



#### 2.3.3 依赖注入方式选择

1. 强制依赖使用构造器进行，使用setter注入有概率不进行注入导致null对象出现
2. 可选依赖使用setter注入进行，灵活性强
3. Spring框架倡导使用构造器，第三方框架内部大多数采用构造器注入的形式进行数据初始化，相对严谨
4. 如果有必要可以两者同时使用，使用构造器注入完成强制依赖的注入，使用setter注入完成可选依赖的注入
5. 实际开发过程中还要根据实际情况分析，如果受控对象没有提供setter方法就必须使用构造器注入
6. **自己开发的模块推荐使用setter注入**



#### 2.3.4 依赖自动装配

依赖自动装配

- IoC容器根据bean所依赖的资源在容器中自动查找并注入到bean中的过程称为自动装配

自动装配方式

- 按类型（常用)
- 按名称
- 按构造方法
- 不启用自动装配



配置中使用`bean`标签 `autowire`属性设置自动装配的类型

 ```xml
 <bean id="bookDao" class="com.itheima.dao.impl.BookDaoImpl" />
 <bean id="bookService" class="com.itheima.service.impl.BookServiceImpl" autowire="byType" />
 ```



依赖自动装配特征

- 自动装配用于引用类型依赖注入，不能对简单类型进行操作
- 使用按类型装配时( byType )必须保障容器中相同类型的bean唯一，推荐使用
- 使用按名称装配时( byName )必须保障容器中具有指定名称的bean，因变量名与配置耦合，不推荐使用
- 自动装配优先级低于setter注入与构造器注入，同时出现时自动装配配置失效

#### 2.3.5 集合对象注入

注入**数组**对象

```xml
<property name="array">
	<array>
    	<value>100</value>
    	<value>200</value>
    	<value>300</value>
  	</array>
</property>
```

 注入**List**对象

```xml
<property name="list">
	<list>
		<value>itcast</value>
        <value>itheima</value>
        <value>boxuegu</value>
    </list>
</property>
```

注入**Set**对象

```xml
<property name="set">
	<set>
		<value>itcast</value>
        <value>itheima</value>
        <value>boxuegu</value>
    </set>
</property>
```

注入**Map**对象

```xml
<property name="map">
	<map>
		<entry key="country" value="china"/>
		<entry key="province" value="henan"/>
        <entry key="city" value="kaifeng"/>
    </map>
</property>
```

注入**Properties**对象

````xml
<property name="properties">
	<props>
		<prop key="country" >china</prop>
        <prop key="province ">henan</prop>
        <prop key="city">kaifeng</prop>
    </props>
</property>
````

### 2.4 容器

1. 创建容器

```java
// 1. 加载类路径下的配置文件
ApplicationContext ctx = new ClassPathXmlApplicationContext("applicationContext.xml");
// 2. 从文件系统加载配置文件
ApplicationContext ctx = new ClassPathXmlApplicationContext("file:D:\\workspace\\spring_quickstart\\src\\main\\resources\\applicationContext.xml");
```

2. 获取Bean

```java
// 1. 使用bean名称获取
DataSource dataSource = (DataSource) ctx.getBean("dataSource");
// 2. 使用bean名称获取并指定类型
DataSource dataSource = ctx.getBean("dataSource", DataSource.class);
// 3. 使用bean类型获取
DataSource dataSource = ctx.getBean(DataSource.class);
```

### 2.5 案例：数据源对象管理

1. 引入alibaba druid

```xml
<dependency>
    <groupId>com.alibaba</groupId>
    <artifactId>druid</artifactId>
    <version>1.2.5</version>
</dependency>
```

2. 定义bean管理DruidDataSource对象

```xml
<!--applicationContext.xml-->
<bean id="dataSource" class="com.alibaba.druid.pool.DruidDataSource">
    <property name="driverClassName" value="com.mysql.jdbc.Driver"/>
    <property name="url" value="jdbc:mysql://localhost:3306/spring_db"/>
    <property name="username" value="root"/>
    <property name="password" value="123456"/>
</bean>
```

3. 引入c3p0

```xml
<dependency>
    <groupId>c3p0</groupId>
    <artifactId>c3p0</artifactId>
    <version>0.9.1.2</version>
</dependency>
```

4. 创建一个c3p0的连接池对象

```xml
<!--创建一个C3P0连接池对象，-->
<bean id="dataSource" class="com.mchange.v2.c3p0.ComboPooledDataSource">
    <property name="driverClass" value="com.mysql.jdbc.Driver"/>
    <property name="jdbcUrl" value="jdbc:mysql://localhost:3306/spring_db"/>
    <property name="user" value="root"/>
    <property name="password" value="123456"/>
    <property name="maxPoolSize" value="1000"/>
</bean>
```

5. 导入MySQL Connector

```xml
<dependency>
    <groupId>com.mysql</groupId>
    <artifactId>mysql-connector-j</artifactId>
</dependency>
```

---

> 使用properties文件

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- 1.引入context命名空间 -->
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"

       xmlns:context="http://www.springframework.org/schema/context"
       xsi:schemaLocation="
        http://www.springframework.org/schema/beans
        http://www.springframework.org/schema/beans/spring-beans.xsd

        http://www.springframework.org/schema/context
        http://www.springframework.org/schema/context/spring-context.xsd
     ">
    <!--2. 使用context命名空间加载properties文件-->
    <context:property-placeholder location="classpath:*.properties" system-properties-mode="NEVER"/>
    <!-- NEVER: 不从系统环境变量中获取值 -->
    <!--classpath:*.properties *通配符，使用当前目录所有properties文件-->
    <!--classpath*:*.properties *通配符，使用当前工程所有properties文件-->
    
    <!--3. 使用${}获取properties文件中的值-->
    <bean class="com.alibaba.druid.pool.DruidDataSource">
        <property name="driverClassName" value="${jdbc.driver}"/>
        <property name="url" value="${jdbc.url}"/>
        <property name="username" value="${jdbc.username}"/>
        <property name="password" value="${jdbc.password}"/>
    </bean>

</beans>
```

## 3. 注解开发

### 3.1 注解与配置文件

1. 使用`@Component`注解

```java
@Component("bookDao")
public class BookDaoImpl implements BookDao {
  public void save() {
    System.out.println("save book");
  }
}
```

2. 在applicationContext.xml中加入`context:component:scan`

```xml
<context:component-scan base-package="com.example.spring_quickstart.dao.impl" />
```

3. 最后可以直接使用

```java
 BookDao bookDao = (BookDao) ctx.getBean("bookDao");
```

注意

- Spring提供了多个注解名称用于分辨不同类的作用，但实际上都是一样的

```java
// 三种不同的注解方式
@Component("bookDao")
@Repository("bookDao")
@Service("bookService")
public class BookDaoImpl implements BookDao {
  public void save() {
    System.out.println("save book");
  }
}
```

### 3.2 纯注解开发

- Spring3.0升级了纯注解开发模式，使用Java类替代配置文件，开启了Spring快速开发赛道
- Java类替代了Spring核心配置文件

```java
@Configuration
@ComponentScan({"com.example.spring_quickstart.dao","com.example.spring_quickstart.Service"})
public class SpringConfig {
}
```

- `@Configuration`用于设定当前类为配置类
- `@ComponentScan()`用于设定扫描的软件包，此注解只能加一次，多个数据使用数组格式

```java
// 使用
public class app {
  public static void main(String[] args) {
    ApplicationContext ctx = new AnnotationConfigApplicationContext(SpringConfig.class);
    BookDao bookDao = ctx.getBean(BookDao.class);
    System.out.println(bookDao);
  }
}
```

### 3.3. bean管理

使用注解管理bean

#### 3.3.1 bean作用范围

使用`@Scope()`定义使用范围

```java
@Repository()
@Scope("singleton")
public class BookDaoImpl implements BookDao {
}
```

#### 3.3.2 bean生命周期

使用`@PostConstruct`和`@PreDestroy`定义bean生命周期

```java
@Repository()
@Scope("singleton")
public class BookDaoImpl implements BookDao {
  public void save() {
    System.out.println("save book");
  }

  @PostConstruct
  public void init() {
    System.out.println("init...");
  }

  @PreDestroy
  public void destroy() {
    System.out.println("destroy...");
  }
}
```

### 3.4 依赖注入

#### 3.4.1 自动注入

- 使用`@Autowired`注解开启自动装配模式(按类型)

```java
@Component("bookService")
public class BookServiceImpl implements BookService {
  @Autowired
  private BookDao bookDao;

  public void setBookDao(BookDao bookDao) {
    this.bookDao = bookDao;
  }

  public void save() {
    bookDao.save();
  }
}
```

注意

- 自动装配基于反射设计创建对象并**暴力反射对应属性为私有属性初始化数据**，因此无需提供`setter`方法
- 自动装配**建议使用无参构造方法创建对象**（默认），如果不提供对应构造方法，请**提供唯一的构造方法**

---

指定名称装配bean

```java
@Component("bookService")
public class BookServiceImpl implements BookService {
  @Autowired
  @Qualifier("bookDao")
  private BookDao bookDao;
  public void save() {
    bookDao.save();
  }
}
```

注意

- `@Qualifier`无法单独使用，需配合`@Autowired`使用

---

使用`@Value`可以进行简单类型的注入

```java
@Repository("bookDao")
@Scope("singleton")
public class BookDaoImpl implements BookDao {
  @Value("${name}")
  private String label;
  public void save() {
    System.out.println("save book--" + label);
  }

  @PostConstruct
  public void init() {
    System.out.println("init...");
  }

  @PreDestroy
  public void destroy() {
    System.out.println("destroy...");
  }
}
```

---

加载properties文件

- 使用`@PropertySource`加载单一properties文件

```java
@Configuration
@ComponentScan({"com.example.spring_quickstart.dao","com.example.spring_quickstart.Service"})
@PropertySource("classpath:jdbc.properties")
public class SpringConfig {
}
```

- 注意
  - 路径仅支持单一文件配置，多文件请使用数组格式配置，不允许使用通配符`*`

### 3.5 第三方bean管理

使用`@bean`管理第三方bean

```java
@Configuration
@ComponentScan({"com.example.spring_quickstart.dao","com.example.spring_quickstart.Service"})
@PropertySource("classpath:jdbc.properties")
public class SpringConfig {
  @Bean
  public DataSource dataSource()
  {
    DruidDataSource ds = new DruidDataSource();
    ds.setDriverClassName("com.mysql.jdbc.Driver");
    ds.setUrl("jdbc:mysql://localhost:3306/spring_db");
    ds.setUsername("root");
    ds.setPassword("123456");
    return ds;
  }
}
```

---

将独立配置类加入配置

- 方式一：导入式

```java
public class JdbcConfig {
  @Bean
  public DataSource dataSource()
  {
    DruidDataSource ds = new DruidDataSource();
    ds.setDriverClassName("com.mysql.jdbc.Driver");
    ds.setUrl("jdbc:mysql://localhost:3306/spring_db");
    ds.setUsername("root");
    ds.setPassword("123456");
    return ds;
  }
}
```

- 使用`@Import`注解手动加入配置类到核心配置，此注解只能添加一次，多个数据请用数组格式

```java
@Configuration
@Import(JdbcConfig.class)
public class SpringConfig {   
}
```



- 方式二：扫描式，使用`@ComponentScan`注解扫描配置类所在的包，加载对应的配置类信息

```java
@Configuration
@ComponentScan({"com.example.spring_quickstart.config","com.example.spring_quickstart.dao","com.example.spring_quickstart.Service"})
@PropertySource("classpath:jdbc.properties")
public class SpringConfig {
}
```

### 3.6 第三方bean依赖注入

- 简单类型注入

```java
public class JdbcConfig {
  @Value("com.mysql.jdbc.Driver")
  private String driver;
  @Value("jdbc:mysql://localhost:3306/spring_db")
  private String url;
  @Value("root")
  private String usrname;
  @Value("123456")
  private String password;

  @Bean
  public DataSource dataSource() {
    DruidDataSource ds = new DruidDataSource();
    ds.setDriverClassName(driver);
    ds.setUrl(url);
    ds.setUsername(usrname);
    ds.setPassword(password);
    return ds;
  }
}
```

- 引用类型依赖注入

```java
 @Bean
  public DataSource dataSource(BookDao bookDao) {
    System.out.println(bookDao);
    DruidDataSource ds = new DruidDataSource();
    // 属性设置
    return ds;
  }
```

注意

- 引用类型注入只需要为bean定义方法设置形参即可，容器会根据类型自动装配对象

### 3.7 XML配置对比注解配置

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/998d3bba80bad77c83ca289b8f52176f.png)

## 4. Spring整合MyBatis、JUnit

### 4.1  Spring整合MyBatis

1. 导入坐标

```xml
<dependency>
    <groupId>com.alibaba</groupId>
    <artifactId>druid</artifactId>
    <version>1.2.5</version>
</dependency>
<dependency>
    <groupId>org.mybatis</groupId>
    <artifactId>mybatis</artifactId>
    <version>3.5.11</version>
</dependency>
<dependency>
    <groupId>com.mysql</groupId>
    <artifactId>mysql-connector-j</artifactId>
</dependency>
<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-jdbc</artifactId>
    <version>6.0.3</version>
</dependency>
<dependency>
    <groupId>org.mybatis</groupId>
    <artifactId>mybatis-spring</artifactId>
    <version>3.0.1</version>
</dependency>
```

2. 使用Java类替代核心配置文件

```java
// SpringConfig

@Configuration
@ComponentScan({"com.example.spring_quickstart.dao", "com.example.spring_quickstart.Service"})
@PropertySource("classpath:jdbc.properties")
@Import({JdbcConfig.class, MyBatisConfig.class})
public class SpringConfig {
}
```

3. 创建jdbc配置类

```java
// jdbcConfig

public class JdbcConfig {

  @Value("${jdbc.driver}")
  private String diver;
  @Value("${jdbc.url}")
  private String url;
  @Value("${jdbc.username}")
  private String username;
  @Value("${jdbc.password}")
  private String password;

  @Bean
  public DataSource dataSource() {
    DruidDataSource ds = new DruidDataSource();
    ds.setDriverClassName(diver);
    ds.setUrl(url);
    ds.setUsername(username);
    ds.setPassword(password);
    return ds;
  }
}
```

4. 整合MyBatis

```java
// MyBatisConfig

@Bean
public SqlSessionFactoryBean sqlSessionFactory(DataSource dataSource) {
  SqlSessionFactoryBean ssfb = new SqlSessionFactoryBean();
  ssfb.setTypeAliasesPackage("com.example.spring_quickstart.entity");
  ssfb.setDataSource(dataSource);
  return ssfb;
}

@Bean
public MapperScannerConfigurer mapperScannerConfigurer() {
  MapperScannerConfigurer msc = new MapperScannerConfigurer();
  msc.setBasePackage("com.example.spring_quickstart.dao");
  return msc;
}
```

### 4.2 Spring 整合JUnit

使用Spring整合Junit专用的类加载器

```java
@Runwith(SpringJUnit4ClassRunne.class)
@ContextConfiguration(classes = SpringConfig.class)
public class BookServiceTest {
	@Autowired
	private BookService bookService;
    
	@Test
	public void testsave(){
		bookService.save();
	}
}
```

## 5. AOP

- AOP(Aspect Oriented Programming)面向切面编程，一种编程范式，指导开发者如何组织程序结构
  - OOP(object Oriented Programming)面向对象编程

- 作用︰在不惊动原始设计的基础上为其进行功能增强

- Spring理念: 无入侵式/无侵入式

### 5.1 AOP 核心概念

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/5c882dd0ef8ba409b965d515cc8b32d8.png)

- 连接点 ( JoinPoint )︰程序执行过程中的任意位置，粒度为执行方法、抛出异常、设置变量等
  - 在SpringAOP中，理解为方法的执行
- 切入点( Pointcut ) :匹配连接点的式子
  - 在SpringAOP中，一个切入点可以只描述一个具体方法，也可以
    匹配多个方法
    - 一个具体方法: com.itheima.dao包下的BookDao接口中的无形参无返回值的save方法
      匹配多个方法:所有的save方法，所有的get开头的方法，所有以Dao结尾的接口中的任意方法，所有带有一个参数的方法
- 通知( Advice ):在切入点处执行的操作，也就是共性功能
  - 在SpringAOP中，功能最终以方法的形式呈现
- 通知类∶定义通知的类
- 切面( Aspect )︰描述通知与切入点的对应关系

### 5.2 AOP 入门案例

- 案例设定︰测定接口执行效率
- 简化设定︰在接口执行前输出当前系统时间

- 开发模式:XML or **注解**

- 思路分析
  1. 导入坐标（pom.xml）
  2. 制作连接点方法（原始操作，dao接口与实现类）
  3. 制作共性功能（通知类与操作）
  4. 定义切入点
  5. 绑定切入点与通知关系（切面）

1. 导入坐标

```java
<dependency>
    <groupId>org.aspectj</groupId>
    <artifactId>aspectjweaver</artifactId>
    <version>1.9.4</version>
</dependency>
```

2. 定义dao接口与实现类

```java
public interface BookDao {
  public void save();
  public void update();
}
```

```java
public class BookDaoImpl implements BookDao {
  public void save() {
    System.out.println(System.currentTimeMillis());
    System.out.println("BookDao.save");
  }

  public void update() {
    System.out.println("BookDao.update");
  }
}
```

3. 定义通知类`aop.MyAdvice`类，制作通知

```java
public class MyAdvice {
  public void method() {
    System.out.println(System.currentTimeMillis());
  }
}
```

4. 定义切入点

```java
public class MyAdvice {
  @Pointcut("execution(void com.example.spring_quickstart.dao.BookDao.update())")
  private void pt(){}
}
```

- 切入点定义依托一个不切实际的方法进行，即无参数，无返回值，无逻辑定义

5. 绑定切入点与通知关系，并指定通知添加到原始连接顶的具体执行位置

```java
public class MyAdvice {
  @Pointcut("execution(void com.example.spring_quickstart.dao.BookDao.update())")
  private void pt(){}
  @Before("pt()")
  public void method() {
    System.out.println(System.currentTimeMillis());
  }
}
```

6. 定义通知类受Spring容器管理，并定义当前类为切面类

```java
@Component
@Aspect
public class MyAdvice {
  @Pointcut("execution(void com.example.spring_quickstart.dao.BookDao.update())")
  private void pt(){}
  @Before("pt()")
  public void method() {
    System.out.println(System.currentTimeMillis());
  }
}
```

7. 在Spring配置类中加入`@EnableAspectJAutoProxy`，开启Spring对AOP注解驱动的支持

```java
@Configuration
@ComponentScan({"com.example.spring_quickstart"})
@EnableAspectJAutoProxy
public class SpringConfig {
}
```

### 5.3 AOP工作流程

1. Spring容器启动
2. 读取所有切面配置中的切入点
3. 初始化bean，判定bean对应的类中的方法是否匹配到任意切入点
   - 匹配失败，创建对象
   - 匹配成功，创建原始对象（目标对象）的代理对象

4. 获取bean执行方法
   - 获取bean，调用方法并执行，完成操作
   - 获取的bean是代理对象时，根据代理对象的运行模式运行原始方法与增强的内容，完成操作

### 5.4 AOP核心概念

- 目标对象（Target ）︰原始功能去掉共性功能对应的类产生的对象，这种对象是无法直接完成最终工作的
- 代理（ Proxy ）︰目标对象无法直接完成工作，需要对其进行功能回填，通过原始对象的代理对象实现

- SpringAOP的本质：代理模式

### 5.5 AOP切入点表达式

- 切入点：要增强的方法
- 切入点表达式：要增强的方法的描述方式

- 描述方法
  - 方法一：`excution(void com.example.spring_quickstart.dao.impl.BookDao.Update())`
  - 方式二：`excution(void com.example.spring_quickstart.dao.impl.BookDaoImpl.Upadate())`

- 标准格式
  - `动作关键字 (访问修饰符 返回值 包名.类/接口名.方法名（参数）异常名)`

```java
execution (public User com.itheima.service.UserService.findById (int))
```

- 动作关键字︰描述切入点的行为动作，例如execution表示执行到指定切入点
- 访问修饰符: public , private等，可以省略
- 返回值
- 包名
- 类/接口名
- 方法名
- 参数
- 异常名︰方法定义中抛出指定异常，可以省略

---

>  使用通配符描述切入点

- `*`单个独立的任意符号，可以独立出现，也可以作为前缀或者后缀的匹配符出现

```java
execution (public * com.itheima.*.UserService.find*(*))
```

匹配`com.itheima`包下的任意包中的`UserService`类或接口中所有`find`开头的带有一个参数的方法

- `..`：多个连续的任意符号，可以独立出现，常用于简化包名与参数的书写

```java
execution (public User com..UserService.findById(..))
```

匹配`com`包下的任意包中的`UserService`类或接口中所有名称为`findByld`的方法

- `+`：专用于匹配子类类型

```java
execution(* *..*Service+.*(..))
```

---

> 书写技巧

- 所有代码按照标准规范开发，否则以下技巧全部失效
- 描述切入点**通常描述接口**，而不描述实现类
- 访问控制修饰符针对接口开发均采用public描述（**可省略访问控制修饰符描述**）
- 返回值类型对于增删改类使用精准类型加速匹配，对于查询类使用`*`通配快速描述
- **包名**书写**尽量不使用`..`匹配**，效率过低，常用`*`做单个包描述匹配，或精准匹配
- **接口名**/类名书写名称与模块相关的**采用`*`匹配**，例如`UserService`书写成`*Service`，绑定业务层接口名
- **方法名**书写以**动词**进行**精准匹配**，名词采用`*`匹配，例如`getByld`书写成`getBy*`,`selectAll`书写成`selectAll`
- 参数规则较为复杂，根据业务方法灵活调整
- 通常**不使用异常**作为**匹配**规则

### 5.6 AOP通知类型

- AOP通知描述了抽取的共性功能，根据共性功能抽取的位置不同，最终运行代码时要将其加入到合理的位置
- AOP通知共分为5种类型
  - 前置通知
  - 后置通知
  - 环绕通知（重点）
  - 返回后通知（了解）
  - 抛出异常后通知（了解）

1. 前置通知`@Before("pt()")`

```java
@Before("pt()")
public void before() {
  System.out.println("before");
}
```

2. 后置通知`@After("pt()")`

```java
@After("pt()")
public void after() {
  System.out.println("after");
}
```

3. 环绕通知 `@Around("pt()")`

```java
@Around("pt()")
public void around(ProceedingJoinPoint pjp) throws Throwable {
  System.out.println("before");
  // 对原始操作的调用 
  pjp.proceed();
  System.out.println("after");
}
```

4. 成功返回后通知`@AfterReturning("pt()")`

```java
@AfterReturning("pt()")
public void afterReturning() {
  System.out.println("afterReturning");
}
```

5. 抛出异常后通知`@AfterThrowing("pt()")`

```java
@AfterThrowing("pt()")
public void afterThrowing() {
  System.out.println("afterThrowing");
}
```



`@Around`注意事项

1. 环绕通知必须依赖形参ProceedingJoinPoint才能实现对原始方法的调用，进而实现原始方法调用前后同时添加通知
2. 通知中如果未使用ProceedingJoinPoint对原始方法进行调用将跳过原始方法的执行
3. 对原始方法的调用可以不接收返回值，通知方法设置成void即可，如果接收返回值，必须设定为Object类型
4. 原始方法的返回值如果是void类型，通知方法的返回值类型可以设置成void，也可以设置成Object
5. 由于无法预知原始方法运行后是否会抛出异常，因此环绕通知方法必须抛出Throwable对象

```java
@Around("pt()")
public Object around(ProceedingJoinPoint pjp) throws Throwable {
  System.out.println("before");
  Object ret =  pjp.proceed();
  System.out.println("after");
  return ret;
}
```

### 5.7 AOP通知获取数据

- 获取切入点方法的参数
  - JoinPoint :适用于前置、后置、返回后、抛出异常后通知
  - ProceedJointPoint :适用于环绕通知
- 获取切入点方法返回值
  - 返回后通知
  - 环绕通知
- 获取切入点方法运行异常信息
  - 抛出异常后通知
  - 环绕通知

---

获取参数

- JoinPoint对象描述了连接点方法的运行状态，可以获取到原始方法的调用参数

```java
@Before("pt()")
public void before(JoinPoint jp) {
	object[] args = jp.getArgs();
	System.out.println(Arrays.toString(args));
}
```

- ProceedJointPoint是JoinPoint的子类

```java
@Around("pt()")
public 0bject around(Proceeding]oinPoint pjp) throws Throwable {
	object[] args = pjp.getArgs();
	System.out.println(Arrays.tostring(args));
    object ret = pjp.proceed();
	return ret;
}
```

---

获取返回值

- 抛出异常后通知可以获取切入点方法中出现的异常信息，使用形参可以接收对应的异常对象

```java
@AfterReturning(value = "pt()",returning = "ret")
public void afterReturning(String ret) {
	System.out.println("afterReturning advice ..."+ret);
}
```

- 环绕通知中可以手工书写对原始方法的调用，得到的结果即为原始方法的返回值

```java
@Around("pt()")
public Object around(ProceedingJoinPoint pjp) throws Throwable {
	object ret = pjp.proceed();
	return ret;
}
```

### 5.8 案例:百度网盘密码数据兼容处理

需求:对百度网盘分享链接输入密码时尾部多输入的空格做兼容处理

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/62fb3439056ccc940133e87ea17f28fa.png)

分析:

1. 在业务方法执行之前对所有的输入参数进行格式处理——trim()
2. 使用处理后的参数调用原始方法——环绕通知中存在对原始方法的调用

```java
@Around( "DataAdvice.servicePt()")
public 0bject trimstring(ProceedingJoinPoint pjp) throws Throwable {
	object[] args = pjp.getArgs();
	//对原始参数的每一个参数进行操作
	for (int i = 0; i < args.length; i++) {
		//如果是字符串数据
		if(args[i].getclass().equals(String.class)){
			//取出数据，trim()操作后，更新数据
			args[i] = args[i].toString().trim();
		}
	}
	return pjp.proceed(args);
}
```

## 6. Spring事务

### 6.1 事务简介

- 事务作用︰在数据层保障一系列的数据库操作同成功同失败
- Spring事务作用︰在数据层或**业务层**保障一系列的数据库操作同成功同失败

```java
public interface PlatformTransactionManager{
	void commit(Transactionstatus status) throws TransactionException;
    void rollback(TransactionStatus status) throws TransactionException;
}
```

### 6.2 案例:银行账户转账

模拟银行账户间转账业务

- 需求:实现任意两个账户间转账操作
- 需求微缩︰A账户减钱，B账户加钱
- 分析∶
  1. 数据层提供基础操作，指定账户减钱(outMoney )，指定账户加钱（inMoney )
  2. 业务层提供转账操作 ( transfer )，调用减钱与加钱的操作
  3. 提供2个账号和操作金额执行转账操作
  4. 基于Spring整合MyBatis环境搭建上述操作

- 结果分析︰
  1. 程序正常执行时，账户金额A减B加，没有问题
  2. 程序出现异常后，转账失败，但是异常之前操作成功，异常之后操作失败，整体业务失败

- 解决方法
  1. 在业务层接口上添加Spring事务管理

```java
public interface AccountService {
	@Transactional
	public void transfer(String out,String in,Double money);
}
```

注意

- Spring注解式事务通常添加在业务层接口中而不会添加到业务层实现类中，降低耦合
- 注解式事务可以添加到业务方法上表示当前方法开启事务，也可以添加到接口上表示当前接口所有方法开启事务

2. 设置事务管理器

```java
// jdbcConfig

@Bean
public PlatformTransactionManager transactionManager(DataSource dataSource){
  DataSourceTransactionManager transactionManager = new DataSourceTransactionManager();
  transactionManager.setDataSource(dataSource);
  return transactionManager;
}
```

注意

- 事务管理器要根据实现技术进行选择
- MyBatis框架使用的是JDBC事务

3. 在SpringConfig配置类中添加`@EnableTransactionManagement`，开启注解式事务驱动

### 6.3 事务角色

事务角色

- 事务管理员︰发起事务方，在Spring中通常指代业务层开启事务的方法
- 事务协调员︰加入事务方，在Spring中通常指代数据层方法，也可以是业务层方法

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/11275c119d949de126b588b2e51aaef3.png)

### 6.4 事务相关配置

| 属性                   | 作用                        | 示例                                      |
| ---------------------- | --------------------------- | ----------------------------------------- |
| readonly               | 设置是否为只读事务          | readOnly=true只读事务                     |
| timeout                | 设置事务超时时间            | timeout  = -1(永不超时)                   |
| rollbackFor            | 设置事务回滚异常(class)     | rollbackFor ={ NullPointException.class}  |
| rollbackForClassName   | 设置事务回滚异常(string)    | 同上格式为字符串                          |
| noRollbackFor          | 设置事务不回滚异常(class)   | noRollbackFor ={NullPointException.class} |
| noRollbackForClassName | 设置事务不回滚异常( string) | 同上格式为字符串                          |
| propagation            | 设置事务传播行为            | .....                                     |

### 6.5 事务传播行为

事务传播行为

- 事务协调员对事务管理员所携带事务的处理态度

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/1c2df486a8edf0e9f8c289bb7dc3ddf7.png)



![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/1189a249e077cc1d210ec6250d6ed07b.png)



### 6.5 案例:转账业务追加日志

转账业务追加日志

- 需求∶实现任意两个账户间转账操作，并对每次转账操作在数据库进行留痕
- 需求微缩︰A账户减钱，B账户加钱，数据库记录日志
- 分析:
  1. 基于转账操作案例添加日志模块，实现数据库中记录日志
  2. 业务层转账操作( transfer )，调用减钱、加钱与记录日志功能
- 实现效果预期∶
  - 无论转账操作是否成功，均进行转账操作的日志留痕

- 存在的问题:
  - 日志的记录与转账操作隶属同一个事务，同成功同失败
- 实现效果预期改进:
  - 无论转账操作是否成功，**日志必须保留**

- 解决方法
  1. 在业务层接口上添加Spring事务，设置事务传播行为`REQUIRES_NEW`（需要新事务)

```java
public interface LogService {
  @Transactional(propagation = Propagation.REQUIRES_NEW)
  void log(String out, String in, Double money);
}
```



# SpringMVC

## 1.SpringMVC概述

- SpringMVC是一种基于Java实现MVC模型的轻量级web框架，与Servelet一样是表现层框架

### 1.1 SringMVC入门案例

1. 使用SpringMVC技术需要先导入SpringMVC坐标与Servlet坐标

```xml
<dependency>
    <groupId>javax.servlet</groupId>
    <artifactId>javax.servlet-api</artifactId>
    <version>3.1.0</version>
    <scope>provided</scope>
</dependency>
<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-webmvc</artifactId>
    <version>5.2.10.RELEASE</version>
</dependency>
```

2. 创建SpringMIVC控制器类(等同于Servlet功能）

```java
@Controller
public class UserController {
	@RequestMapping("/save")
    @ResponseBody
	public string save(){
		System.out.println("user save ..." );
    	return "{ 'info ' : 'springmvc ' }";
	}
}
```

3. 初始化SpringMVC环境(同Spring环境)，设定SpringMVC加载对应的bean

```java
@Configuration
@ComponentScan("com.itheima.controller")
public class SpringMvcConfig {
}
```

4. 初始化Servlet容器，加载SpringMVC环境，并设置SpringMVC技术处理的请求

```java
public class ServletContainersInitConfig extends AbstractDispatcherServletInitializer {
	protected webApplicationContext createServletApplicationcontext() {
		AnnotationConfigwebApplicationContext ctx = new AnnotationConfigwebApplicationContext();
    	ctx.register( SpringMvcConfig.class);
		return ctx;
	}
	protected String[] getServletMappings( ) {
		return new String[]{"/"};
	}
	protected webApplicationContext createRootApplicationContext() {
		return null;
	}ff
}
```

启动服务器初始化过程

1. 服务器启动，执行`ServletContainersInitConfig`类，初始化web容器
2. 执行`createServletApplicationContext`方法，创建了`WebApplicationContext`对象
3. 加载`SpringMvcConfig`
4. 执行`@ComponentScan`加载对应的`bean`
5. 加载`UserController`，每个`@RequestMapping`的名称对应一个具体的方法
6. 执行`getServletMappings`方法，定义所有的请求都通过`SpringMVC`

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/8a15245aee2749f500acb5da4fa685d9.png)

单次请求过程

1. 发送请求`localhost/save`

2. web容器发现所有请求都经过`SpringMVC`，将请求交给`SpringMVC`处理
3. 解析请求路径`/save`
4. 由`/save`匹配执行对应的方法`save()`
5. 执行`save()`
6. 检测到有`@ResponseBody`直接将`save()`方法的返回值作为响应求体返回给请求方

### 1.2 Controller加载控制与业务bean加载控制

- SpringMVC相关bean(表现层bean)
- Spring控制的bean
  - 业务bean (Service)
  - 功能bean (DataSource等)

- SpringMVC相关bean加载控制
  - SpringMVC加载的bean对应的包均在com.itheima.controller包内
- Spring相关bean加载控制
  - 方式一: Spring加载的bean设定扫描范围为com.itheima，排除掉controller包内的bean
  - 方式二:Spring加载的bean设定扫描范围为精准范围，例如service包、dao包等
  - 方式三:不区分Spring与SpringMVC的环境，加载到同一个环境中

`@ComponentScan`

- 类型：类注解
- 范例

```java
@Configuration
@ComponentScan(value = "com.itheima",
	excludeFilters = @ComponentScan.Filter(
		type = FilterType.ANNOTATION,
		classes = Controller.class
	)
)
public class SpringConfig {
}
```

属性

- excludeFilters:排除扫描路径中加载的bean，需要指定类别(type)与具体项(Ciasses)
- includeFilters:加载指定的bean，需要指定类别(type）与具体项(classes)

 

Servlet简化开发

```java
public class ServletConfig extends AbstractAnnotationConfigDispatcherServletInitializer {

  @Override
  protected Class<?>[] getRootConfigClasses() {
    return new Class[]{SpringConfig.class};
  }

  @Override
  protected Class<?>[] getServletConfigClasses() {
    return new Class[]{SpringMvcConfig.class};
  }

  @Override
  protected String[] getServletMappings() {
    return new String[]{"/"};
  }
}
```



## 2. 请求与响应

### 2.1 请求映射路径

`@RequestMapping`

- 类型：方法注解 类注解
- 位置：SpringMVC控制器方法定义上方
- 作用：设置当前控制器方法请求访问路径，如果设置在类上统一设置当前控制器方法请求访问路径前缀
- 属性
  - value（默认)︰请求访问路径，或访问路径前缀

```java
@Controller
@RequestMapping("/user")
public class UserController {

  @RequestMapping("/save")
  @ResponseBody
  public String save() {
    System.out.println("save");
    return "{'msg':'save'}";
  }
}
```

### 2.2 请求参数

- 普通参数
  - get请求使用url地址传参，地址参数名与形参变量名相同，post请求使用form表单，表单参数名与形参变量名相同，定义形参即可接收参数
  - 请求参数名与形参变量名不同，使用`@RequestParam`绑定参数关系

```java
@Controller
public class UserController {

  @RequestMapping("/save")
  @ResponseBody
  public String save(String name) {
    System.out.println(name);
    return "{'msg':'save'}";
  }
}
```

- POJO参数
  - 请求参数名与形参对象属性名相同，定义PO0类型形参即可接收参数

- 嵌套POJO参数
  - 请求参数名与形参对象属性名相同，按照对象层次结构关系即可接收嵌套POJO属性参数

- 乱码处理，在servlet配置文件中添加过滤器，可以解决POST传参乱码

```java
protected Filter[] getServletFilters() {
  CharacterEncodingFilter filter = new CharacterEncodingFilter();
  filter.setEncoding("UTF-8");
  return new Filter[]{filter};
}
```

- 在pom.xml中添加配置`<uriEncoding>UTF-8</uriEncoding>`，解决GET乱码问题

```xml
<plugins>
    <plugin>
        <groupId>org.apache.tomcat.maven</groupId>
        <artifactId>tomcat7-maven-plugin</artifactId>
        <version>2.2</version>
        <configuration>
            <port>8081</port>
            <path>/</path>
            <uriEncoding>UTF-8</uriEncoding>
        </configuration>
    </plugin>
</plugins>
```

---

日期类型参数传递

- 名称: @DateTimeFormat
- 类型:形参注解
- 位置: SpringMVC控制器方法形参前面
- 作用:设定日期时间型数据格式
- 属性:pattern:日期时间格式字符串

```java
@RequestMapping("/dataParam")
@ResponseBody
public String dataParam(@DateTimeFormat(pattern = "yyyy-MM-dd") Date date){
	System.out.println("参数传递date ==> "+date);
    return "{'module':'data param'}";
}
```



### 2.3 响应

- 响应页面

```java
@RequestMapping("/toPage")
public String toPage(){
	return "page.jsp";
}
```

- 响应数据
  - 名称:`@ResponseBody`
  - 类型:方法注解
  - 位置:SpringMVC控制器方法定义上方
  - 作用:设置当前控制器返回值作为响应体

```java
@RequestMapping("/toJsonPO30")
@ResponseBody
public User toJsonPOJO(){
	User user = new User();
    user.setName("赵云");
    user.setAge(41);
	return user;
}
```



## 3. REST风格

### 3.1 REST简介

- REST (Representational State Transfer)，表现形式状态转换
  - 传统风格资源描述形式
    - http://localhost/user/getById?id=1
    - http://localhost/user/saveUser
  - REST风格描述形式
    - http://localhost/user/1
    - http://localhost/user

- 优点:
  - 隐藏资源的访问行为，无法通过地址得知对资源是何种操作
  - 书写简化

- 按照REST风格访问资源时使用**行为动作**区分对资源进行了何种操作
  - http://localhost/users	查询全部用户信息`GET`（查询）
  - http://localhost/users/1 查询指定用户信息`GET`（查询）
  - http://localhost/users    添加用户信息`POST`（新增/保存）
  - http://localhost/users  修改用户信息`PUT`（修改/更新）
  - http://localhost/users/1  删除用户信息`DELETE`（删除）

- 根据REST风格对资源讲行访问称为**RESTful**
- 注意
  - 上述行为是约定方式，约定不是规范，可以打破，所以称REST风格，而不是REST规范
  - 描述模块的名称通常使用复数，也就是加s的格式描述，表示此类资源，而非单个资源，例如: users、books、account...



## 4. SSM整合

SSM整合流程

1. 创建工程
2. SSM整合
   - Spring
     - SpringConfig
   - MyBatis
     - MybatisConfig
     - JdbcConfig
     - jdbc.properties
   - SpringMVC
     - ServletConfig
     - SpringMvcConfig
3. 功能模块
   - 表与实体类
   - dao(接口+自动代理)
   - service（接口+实现类)
     - 业务层接口测试（整合JUnit )
   - controller
     -  表现层接口测试( PostMan )

### 4.1 整合流程

- 配置
  - SpringConfig
  - JDBCConfig、jdbc.propertiesMyBatisConfig
- 模型
  - Book
- 数据层标准开发
  - BookDao
- 业务层标准开发
  - BookService
  - BookServiceImpl
- 测试接口
  - BookServiceTest

### 4.2 表现层数据封装

- 设置统一数据返回结果类

```java
public class Result {
    private Object data;
    private Integer code;
    private String msg;
}
```

- 注意
  - Result类中的字段并不是固定的，可以根据需要自行增减提供若干个构造方法，方便操作

---

- 设置统一数据返回结果编码

```java
public class Code {
	public static final Integer SAVE_OK = 20011;
    public static final Integer DELETE_OK = 20021;
    public static final Integer UPDATE_OK = 20031;
    public static final Integer GET_OK = 20041;
	public static final Integer SAVE_ERR = 20010;
    public static final Integer DELETE_ERR = 20020;
    public static final Integer UPDATE_ERR = 20030;
    public static final Integer GET_ERR = 20040;
}
```

- 注意
  - Code类的常量设计也不是固定的，可以根据需要自行增减，例如将查询再进行细分为`GET_OK`，`GET_ALL_OK`，`GET_PAGE_OK`

---

- 根据情况设定合理的Result

```java
@RequestMapping("/books")
public class Bookcontroller {
	@Autowired
	private BookService bookService;
    
    @GetMapping("/{id}")
	public Result getById(@PathVariable Integer id) {
		Book book = bookService.getById(id);
		Integer code = book != null ? code.GET_OK : Code.GET_ERR;
        String msg = book != null ? "":"数据查询失败,请重试!";
		return new Result(code,book,msg);
	}
}
```

### 4.3 异常处理器

出现异常现象的常见位置与常见诱因如下:

- 框架内部抛出的异常:因使用不合规导致
- 数据层抛出的异常:因外部服务器故障导致（例如:服务器访问超时)
- 业务层抛出的异常:因业务逻辑书写错误导致（例如:遍历业务书写操作，导致索引异常等)
- 表现层抛出的异常:因数据收集、校验等规则导致（例如:不匹配的数据类型间导致异常)
- 工具类抛出的异常:因工具类书写不严谨不够健壮导致（例如:必要释放的连接长期未释放等)

异常处理器

- 集中的、统一的处理项目中出现的异常

```java
@RestControllerAdvice
public class ProjectExceptionAdvice {
	@ExceptionHandler(Exception.class)
	public Result doException(Exception ex){
		return new Result(500,null);
	}
}
```



### 4.4 项目异常处理

项目异常分类

- 业务异常(BusinessException)
  - 规范的用户行为产生的异常
  - 不规范的用户行为操作产生的异常

- 系统异常(SystemException)
  - 项目运行过程中可预计且无法避免的异常

- 其他异常(Exception)
  - 编程人员未预期到的异常

---

项目异常处理方案

- 业务异常(BusinessException)
  - 发送对应消息传递给用户，提醒规范操作
- 系统异常(SystemException)
  - 发送固定消息传递给用户，安抚用户发
  - 送特定消息给运维人员，提醒维护
  - 记录日志
- 其他异常(Exception)
  - 发送固定消息传递给用户，安抚用户
  - 发送特定消息给编程人员，提醒维护(纳入预期范围内)
  - 记录日志

---

1. 自定义项目系统级异常

```java
public class SystemException extends RuntimeException
	private Integer code;
	public SystemException(Integer code, String message) {
		super(message);
		this.code = code;
	}
	public SystemException(Integer code,String message,Throwable cause) {
		super(message,cause);
		this.code = code;
	}
	public Integer getcode() {
		return code;
	}
	public void setCode(Integer code) {
		this.code = code;
	}
}
```

2. 自定义项目业务级异常

```java
public class BusinessException extends RuntimeException{
	private Integer code;
	public BusinessException(Integer code,String message) {
		super(message);
		this.code = code;
	}
	public BusinessException(Integer code,String message,Throwable cause) {
		super(message,cause);
		this.code = code;
	}
	public Integer getcode( ) {
		return code;
	}
	public void setCode(Integer code) {
		this.code = code;
	}
}
```

3. 自定义异常编码

```java
public class code {
	public static final Integer SYSTEM_UNKNOW_ERROR = 50001;
	public static final Integer SYSTEM_TIMEOUT_ERROR = 50002;
	public static final Integer PR0JECT_VALIDATE_ERROR = 60001;
    public static final Integer PROJECT_BUSINESS_ERROR = 60002;
}
```

4. 触发自定义异常

```java
@service
public class BookServiceImpl implements BookService {
	@Autowired
	private BookDao bookDao;
	public Book getById(Integer id) {
		if( id<0 ){
			throw new BusinessException(Code.PROJECT_BUSINESS_ERROR,"请勿进行非法操作!");
		}
		return bookDao.getById(id);
	}
}
```

5. 拦截并处理异常

```java
@RestControllerAdvice
public class ProjectExceptionAdvice {
	@ExceptionHandler(BusinessException.class)
	public Result doBusinessException(BusinessException ex){
		return new Result(ex.getCode(),null,ex.getMessage());
	}
	@ExceptionHandler(SystemException.class)
	public Result doSystemException(SystemException ex){
		//记录日志（错误堆栈)
		//发送邮件给开发人员
		//发送短信给运维人员
		return new Result(ex.getcode( ), null,ex.getMessage());
	}
	@ExceptionHandler(Exception.class)
	public Result doException(Exception ex){
		//记录日志（错误堆栈)
		//发送邮件给开发人员
        //发送短信给运维人员
		return new Result(Code.SYSTEM_UNKNOW_ERROR,null,"系统繁忙，请联系管理员!");
	}
}
```

6. 异常处理器效果对比

```java
{
	"data": {
		"id": 1,
		"type": "计算机理论"，
		"name": "Spring实战第5版"，
		"description": "Spring入门经典教程，深入理解Spring原理技术内幕"
	},
	"code" : 20041,
    "msg" : null
}
```

```java
{
	"data" : null,
	"code" : 60002,
	"msg":"请勿进行非法操作!"
}
```



## 5. 拦截器

### 5.1 拦截器简介

- 拦截器(Interceptor )是一种动态拦截方法调用的机制，在SpringWC中动态拦截控制器方法的执行

- 作用:
  - 在指定的方法调用前后执行预先设定的代码
  - 阻止原始方法的执行

执行流程

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/29c8e02ccfaccf0a0909ffaf033499e8.png)

### 5.2 拦截器与过滤器区别

- 归属不同:Filter属于Servlet技术，Interceptor属于SpringMVC技术
- 拦截内容不同:Filter对所有访问进行增强，Interceptor仅针对springMVc的访问进行增强

### 5.3 入门案例

1. 声明拦截器的bean，并实现HandlerInterceptor接口（注意:扫描加载bean)

```java
@Component
public class ProjectInterceptor implements HandlerInterceptor {
	public boolean preHandle(..) throws Exception {
		system.out.println("preHandle...");
		return true;
	}
	public void postHandle(..) throws Exception {
		system.out.println("postHandle...");
	}
	public void afterCompletion(..) throws Exception {
		system.out.println("afterCompletion...");
	}
}
```

2. 定义配置类，继承webMvcConfigurationSupport，实现addInterceptor方法（注意:扫描加载配置)

```java
@Configuration
public class SpringMvcSupport extends WebMvcConfigurationSupport {
	@Override
	public void addInterceptors(InterceptorRegistry registry) {
        ...
	}
}
```

3. 添加拦截器并设定拦截的访问路径，路径可以通过可变参数设置多个

```java
@Configuration
public class SpringMvcSupport extends WebMvcConfigurationSupport {
	@Autowired
	private ProjectInterceptor projectInterceptor;
    
	@Override
	public void addInterceptors( InterceptorRegistry registry) {
		registry.addInterceptor(projectInterceptor).addPathPatterns("/books");
	}
}
```

4. 使用标准接口WebMvcConfigurer简化开发（注意:侵入式较强)

```java
@Configuration
@ComponentScan("com.itheima.controller")
@EnablewebMvc
public class SpringMvcConfig implements webMvcConfigurer{
	@Autowired
	private ProjectInterceptor projectInterceptor;
    
	public void addInterceptors( InterceptorRegistry registry) {
		registry.addInterceptor(projectInterceptor).addPathPatterns("/books", "/books/*");
	}
}
```

### 5.4 拦截器参数

- 前置处理

```java
public boolean preHandle(HttpServletRequest request,
		HttpservletResponse response,
		object handler) throws Exception {
	System.out.println("preHandle...");
	return true;
}
```

- 参数
  - request:请求对象
  - response:响应对象
  - handler:被调用的处理器对象，本质上是一个方法对象，对反射技术中的Method对象进行了再包装
- 返回值
  - 返回值为false，被拦截的处理器将不执行

---

- 后置处理

```java
public void postHandle(HttpServletRequest request,
		HttpservletResponse response,object handler,
		ModelAndView modelAndView) throws Exception {
	System.out.println( "postHandle..." );
}
```

- 参数
  - modelAndView:如果处理器执行完成具有返回结果，可以读取到对应数据与页面信息，并进行调整

---

- 完成后处理

```java
public void afterCompletion(HttpServletRequest request,
		HttpServletResponse response,
		object handler,
		Exception ex) throws Exception {
	System.out.println("aftercompletion...");
}
```

- 参数
  - ex:如果处理器执行过程中出现异常对象，可以针对异常情况进行单独处理

### 5.5 拦截器链配置

- 当配置多个拦截器时，形成拦截器链
- 拦截器链的运行顺序参照拦截器添加顺序为准
- 当拦截器中出现对原始处理器的拦截，后面的拦截器均终止运行
- 当拦截器运行中断，仅运行配置在前面的拦截器的aftercompletion操作



拦截器链的运行顺序

- preHandle:与配置顺序相同，必定运行
- postHandle:与配置顺序相反，可能不运行
- afterCompletion:与配置顺序相反，可能不运行



# Maven

## 1. 分模块开发与设计

### 1.1 分模块开发意义

- 将原始模块按照功能拆分成若干个子模块，方便模块间的相互调用，接口共享

### 1.2 分模块设计

1. 编写模块代码
   - 注意
     - 分模块开发需要先针对模块功能进行设计，再进行编码。不会先将工程开发完毕，然后进行拆分
2. 通过maven指令安装模块到本地仓库( install指令)
   - 团队内部开发需要发布模块功能到团队内部可共享的仓库中（私服）

## 2. 依赖管理

依赖管理

- 依赖指当前项目运行所需的jar,一个项目可以设置多个依赖
- 格式

```xml
<!--设置当前项目所依赖的所有jar-->
<dependencies>
	<!--设置具体的依赖-->
    <dependency>
		<!--依赖所属群组id-->
		<groupId>org.springframework</groupId>
        <!--依赖所属项目id-->
		<artifactId>spring-webmvc</ artifactId>
        <!--依赖版本号-->
		<version>5.2.10.RELEASE</version>
    </dependency>
</ dependencies>
```

### 2.1 依赖传递

依赖具有传递性

- 直接依赖:在当前项目中通过依赖配置建立的依赖关系
- 间接依赖:被资源的资源如果依赖其他资源，当前项目间接依赖其他资源
- 特殊优先:当同级配置了相同资源的不同版本，后配置的覆盖先配置的

### 2.2 可选依赖与排除依赖

#### 2.2.1 可选依赖

- 可选依赖指对外隐藏当前所依赖的资源——不透明

```xml
<dependency>
	<groupId>com.itheima</ groupId>
	<artifactId>maven_03_pojo</ artifactId>
    <version>1.0-SNAPSHOT</version>
	<!--可选依赖是隐藏当前工程所依赖的资源，隐藏后对应资源将不具有依赖传递性-->
    <optional>false</optional>
</ dependency>
```

#### 2.2.2 排除依赖

- 排除依赖指主动断开依赖的资源，被排除的资源无需指定版—-不需要

```xml
<dependency>
<groupId>com.itheima</groupId>
<artifactId>maven_04_dao</ artifactId>
<version>1.0-SNAPSHOT</version>
  <!--排除依赖是隐藏当前资源对应的依赖关系-->
  <exclusions>
	<exclusion>
		<groupId>log4j</groupId>
		<artifactId>log4j</ artifactId>
    </exclusion>
	<exclusion>
			<groupId>org.mybatis</groupId>
    		<artifactId>mybatis</ artifactId>
    	</exclusion>
	</exclusions>
</dependency>
```

- 排除依赖资源仅指定`groupId` `artifactId`即可，无需指定`vesion`

## 3.继承与聚合

### 3.1 聚合

- 聚合:将多个模块组织成一个整体，同时进行项目构建的过程称为聚合
- 聚合工程:通常是一个不具有业务功能的“空”工程（有且仅有一个pom文件)
- 作用∶使用聚合工程可以将多个工程编组，通过对聚合工程进行构建，实现对所包含的模块进行同步构建
  - 当工程中某个模块发生更新(变更)时，必须保障工程中与已更新模块关联的模块同步更新，此时可以使用聚合工程来解决批量模块同步构建的问题

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/b6e89af56f25e72af757cab0aa41c949.png)

聚合工程开发

1. 创建Maven模块，设置打包类型为`pom`

```xml
<packaging>pom</packaging>
```

- 注意
  - 每个maven工程都有对应的打包方式，默认为jar, web工程打包方式为war

2. 设置当前聚合工程所包含的子模块名称

```xml
<modules>
	<module>../maven_ssm</module>
    <module>../maven_pojo</module>
    <module>../maven_dao</module>
</modules>
```

- 注意
  - 聚合工程中所包含的模块在进行构建时会根据模块间的依赖关系设置构建顺序，与聚合工程中模块的配置书写位置无关参与聚合的工程无法向上感知是否参与聚合，只能向下配置哪些模块参与本工程的聚合

### 3.2 继承

- 概念:继承描述的是两个工程间的关系，与java中的继承相似，子工程可以继承父工程中的配置信息，常见于依赖关系的继承
- 作用
  - 简化配置
  - 减少版本冲突

继承关系

1. 创建Maven模块，设置打包类型为pom

```xml
<packaging>pom</packaging>
```

- 注意
  - 建议父工程打包方式设置为pom

2. 在父工程的pom文件中配置依赖关系（子工程将沿用父工程中的依赖关系)

```xml
<dependencies>
    <dependency>
		<groupId>org.springframework</ groupId>
        <artifactId>spring-webmvc</artifactId>
        <version>5.2.10.RELEASE</version>
    </dependency>
    ...
</dependencies>
```

3. 配置子工程中可选的依赖关系

```xml
<dependencyManagement>
	<dependencies>
		<dependency>
			<groupId>com.alibaba</groupId>
            <artifactId>druid</ artifactId>
            <version>1.1.16</version>
		</dependency>
        ...
	</dependencies>
</dependencyManagement>
```

4. 在子工程中配置当前工程所继承的父工程

```xml
<!--定义该工程的父工程-->
<parent>
	<groupId>com.itheima</groupId>
	<artifactId>maven_parent</artifactId>
    <version>1.0-SNAPSHOT</version>
	<!--填写父工程的pom文件-->
	<relativePath>../maven_parent/pom.xml</relativePath>
</parent>
```

- 注意
  - 子工程中使用父工程中的可选依赖时，仅需要提供群组id和项目id，无需提供版本，版本由父工程统一提供，避免版本冲突
  - 子工程中还可以定义父工程中没有定义的依赖关系

### 3.3 聚合与继承的区别

- 作用
  - 聚合用于快速构建项目
  - 继承用于快速配置
- 相同点:
  - 聚合与继承的pom.xml文件打包方式均为pom，可以将两种关系制作到同一个pom文件中
  - 聚合与继承均属于设计型模块，并无实际的模块内容
- 不同点:
  - 聚合是在当前模块中配置关系，聚合可以感知到参与聚合的模块有哪些
  - 继承是在子模块中配置关系，父模块无法感知哪些子模块继承了自己

## 4. 属性

### 4.1 普通属性

1. 定义属性

```xml
<!--定义自定义属性-->
<properties>
	<spring.version>5.2.10.RELEASE</spring.version>
    <junit.version>4.12</junit.version>
</properties>
```

2. 引用属性

```xml
<dependency>
	<groupId>org.springframework</groupId>
    <artifactId>spring-context</ artifactId>
    <version>${spring.version}</version>
</dependency>
```

### 4.2 资源文件引用属性

1. 定义属性

```xml
<!--定义自定义属性-->
<properties>
	<spring.version>5.2.10.RELEASE</ spring.version>
    <junit.version>4.12</junit.version>
	<jdbc.ur1>jdbc:mysql://127.0.0.1:3306/ssm_db</jdbc.url>
</ properties>
```

2. 配置文件中引用属性

```xml
jdbc.driver=com.mysql.jdbc.Driver
jdbc.url=${jdbc.ur1}
jdbc.username=root
jdbc.password=root
```

3. 开启资源文件目录加载属性的过滤器

```xml
<build>
	<resources>
		<resource>
			<directory>${project.basedir}/src/main/resources</directory>
            <filtering>true</filtering>
		</resource>
	</resources>
</ build>
```

4. 配置maven打war包 ，忽略web.xmll检查

```xml
<plugin>
	<groupId>org.apache.maven.plugins</ groupId>
    <artifactId>maven-war-plugin</ artifactId>
    <version>3.2.3</version>
	<configuration>
		<failonMissingwebxml>false</failOnMissingwebXml>
    </configuration>
</plugin>
```

### 4.3 其他属性

| 属性分类     | 引用格式                   | 示例                          |
| ------------ | -------------------------- | ----------------------------- |
| 自定义属性   | ${自定义属性名}            | `${spring.version}`           |
| 内置属性     | ${内置属性名}              | `${basedir}`  `${version}`    |
| Setting属性  | $ {setting.属性名}         | `${settings.localRepository}` |
| Java系统属性 | ${系统属性分类.系统属性名} | `${user.home}`                |
| 环境变量属性 | $ {env .环境变量属性名}    | `${env.JAVA_HOME}`            |

### 4.4 版本管理

工程版本:

- SNAPSHOT（快照版本)
  - 项目开发过程中临时输出的版本，称为快照版本
  - 快照版本会随着开发的进展不断更新
- RELEASE(发布版本)
  - 项目开发到进入阶段里程碑后，向团队外部发布较为稳定的版本，这种版本所对应的构件文件是稳定的，即便进行功能的后续开发，也不会改变当前发布版本内容，这种版本称为发布版本

发布版本

- alpha版
- beta版
- 纯数字版

## 5. 多环境配置与应用

多环境开发

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/d1c7d17ff597cb22417c92190bc69eca.png)

- maven提供配置多种环境的设定，帮助开发者使用过程中快速切换环境

### 5.1 配置

1. 定义多环境

```xml
<!--定义多环境-->
<profiles>
	<!--定义具体的环境:生产环境-->
    <profile>
	<!--定义环境对应的唯一名称-->
    <id>env_dep</id>
	<!--定义环境中专用的属性值-->
    <properties>
		<jdbc.url>jdbc :mysql://127.0.0.1:3306/ssm_db</jdbc.url>
     </properties>
	<!--设置默认启动-->
     <activation>
		<activeByDefault>true</activeByDefault>
      </activation>
	</ profile>
	<!--定义具体的环境:开发环境-->
   	<profile>
		<id>env_pro</id>
      …
	</profile>
</profiles>
```

2. 使用多环境

```bash
mvn 指令 -P 环境定义id
# 示例
mvn install -P pro_env
```

### 5.2 跳过测试

- 跳过测试

```bash
mvn 指令 —D skipTests
# 示例
mvn install -D skipTests
```

- 注意
  - 执行的项目构建指令必须包含测试生命周期，否则无效果。例如执行compile生命周期，不经过test生命周期

## 6. 私服

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/1d13dbce6d660b981d10bf8bb84475c8.png)

### 6.1 私服简介

- 私服是一台独立的服务器，用于解决团队内部的资源共享与资源同步问题
- Nexus
  - Sonatype公司的一款maven私服产品
  - 下载地址: https://help.sonatype.com/repomanager3/download

### 6.2 私服仓库分类

### 6.3 本地仓库访问私服配置

### 6.4 私服资源上传下载



# SpringBoot

## 1. SpringBoot简介

- SpringBoot是由Pivotal团队提供的全新框架，其设计目的是用来简化Spring应用的初始搭建以及开发过程

- Spring程序缺点
  - 配置繁琐
  - 依赖设置繁琐
- SpringBoot程序优点
  - 自动配置
  - 起步依赖（简化依赖配置）
  - 辅助功能（内置服务器，.......）

### 1.1 快速入门

1. 创建工程

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/4f0f5e15ff39abf6d6644df0d174ac0a.png)

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/793d7956aceb206f4f48ef098258f4b5.png)

2. 删除不必要文件

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/0920002c61df552b7bfc64d1d8fd2207.png)

3. 修改java版本

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/efcf23453e9c5c39c021f20c0bdb4c08.png)

4. 创建BookController，编写代码

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/1c70b3401c4ac18fe1abb5d05864b885.png)

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/eeb12aed22f17e7c80e987dfe9cae451.png)

5. 运行项目

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/b282c685bfcbe815f329fa6b2f4e13bd.png)

---

Spring程序与SpringBoot程序对比

| 类/配置文件            | Spring   | SpringBoot |
| ---------------------- | -------- | ---------- |
| pom文件中的坐标        | 手工添加 | 勾选添加   |
| web3.0配置类           | 手工制作 | 无         |
| Spring/SpringMVC配置类 | 手工制作 | 无         |
| 控制器                 | 手工制作 | 手工制作   |

注意

- 基于idea开发SpringBoot程序需要确保联网且能够加载到程序框架结构

### 1.2 SpringBoot程序快速启动

1. 对SpringBoot项目打包（执行Maven构建指令package）
2. 执行启动指令

```bash
java -jar springboot.jar
```

- 注意
  - jar支持命令行启动需要依赖maven插件支持，请确认打包时是否具有SpringBoot对应的maven插件

```xml
<build>
	<plugins>
		<plugin>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-maven-plugin</artifactId>
    	</plugin>
	</plugins>
</build>
```



### 1.3 起步依赖

- 起步依赖

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/d0e10510e5c1cb1bcc06f81137167f51.png)

- starter
  - SpringBoot中常见项目名称，定义了当前项目使用的所有项目坐标,
    以达到减少依赖配置的目的
- parent
  - 所有SpringBoot项目要继承的项目，定义了若干个坐标版本号（依赖管理，而非依赖），以达到减少依赖冲突的目的
  - spring-boot-starter-parent (2.5.0)与spring-boot-starter-parent (2.4.6）共计57处坐标版本不同
- 实际开发
  - 使用任意坐标时，仅书写GAV中的G和A，V由SpringBoot提供
  - 如发生坐标错误，再指定version（要小心版本冲突)



### 1.4 变更依赖

- 使用maven依赖管理变更起步依赖项

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/369ca41349648777a5555b45e20ef136.png)

- Jetty比Tomcat更轻量级，可扩展性更强（相较于Tomcat )，谷歌应用引擎（GAE)已经全面切换为Jetty

### 1.5 注意事项

springboot最新版本(已知>2.5.14)存在某些问题，比如使用`Autowired`自动填充在运行时会报错，使用低版本即可

![image-20230315190435298](https://gitee.com/pepedd864/cdn-repos/raw/master/img/1ee9b83f299d890891e05783759ba3cb.png)

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/c3c595e48bc781c40b57009a8b4c7b10.png)

## 2. 基础配置

### 2.1 配置格式

SpringBoot提供了多种属性配置格式

- application.properties

```properties
server.port=80
```

- application.yml

```yml
server:
	port: 81
```

- application.yaml

```yaml
server:
	port: 82
```

SpringBoot配置文件加载顺序

- application.properties  > application.yml  > application.yaml

注意

- SpringBoot核心配置文件名为application
- SpringBoot内置属性过多，且所有属性集中在一起修改，在使用时通过提示键+关键字修改属性

### 2.2 yaml

YAML (YAML Ain't Markup Language) ,一种数据序列化格式

优点:

- 容易阅读
- 容易与脚本语言交互
- **以数据为核心，重数据轻格式**

YAML文件扩展名

- **.yml（主流）**
- .yaml

---

语法规则

- 大小写敏感
- 属性层级关系使用多行描述，每行结尾使用冒号结束
- 使用缩进表示层级关系，同层级左侧对齐，只允许使用空格（不允许使用Tab键）
- 属性值前面添加空格（属性名与属性值之间使用冒号+空格作为分隔)
- `#`表示注释

核心规则:**数据前面要加空格与冒号隔开**

数组

- 数据在数据书写位置的下方使用减号作为数据开始符号，每行书写一个数据，减号与数据间空格分隔

 ```yaml
 likes:
   - music
   - movies
   - books
 ```

---

数据读取

- 使用`@Value`读取单个数据，属性名引用方式:`${一级属性名.二级属性名....}`

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/84cf1def01bb5bf82ca860699d3f7247.png)

- 封装全部数据到Environment对象

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/deb00da1fd6f3e2ea0454c269f427ac4.png)

- 自定义类封装指定数据

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/2ad4dc4e918550c15293620714671689.png)

### 2.3 多环境开发

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/6976b2c0b1f7cbd526d679576d67a9ab.png)

多环境启动

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/97472bb369d9be3f48be6560d9260ed7.png)

多环境启动命令格式

- 带参数启动SpringBoot

```bash
java -jar springboot.jar --spring.profiles.active=test
```

```bash
java -jar springboot.jar --server.port=88
```

```bash
java -jar springboot.jar --server.port=88 --spring.profiles.active=test
```

- 参数加载优先级
  - 参考https://docs.spring.io/spring-boot/docs/current/reference/html/spring-boot-features.htm2#boot-features-external-config

### 2.4 配置文件分类

- SpringBoot中4级配置文件
  - 1级: file : config/application. yml【最高】
  - 2级: file : application. yml
  - 3级: classpath: config/ application. yml
  - 4级: classpath: application.yml   【最低】

- 作用:
  - 1级与2级留做系统打包后设置通用属性
  - 3级与4级用于系统开发阶段设置通用属性

## 3. 整合第三方技术

### 3.1 整合JUnit

- SpringBoot整合JUnit

```java
@SpringBootTest
class Springboot07JunitApplicationTests {
	@Autowired
    private BookService bookService;
    
    @Test
	public void testSave(){
		bookService.save();
	}
}
```

### 3.2 整合MyBatis

1. 创建模块
2. 使用当前模块需要的技术集（MyBatis、MySQL）
3. 设置数据源参数

```yaml
spring:
  datasource:
    driver-class-name: com.mysql.cj.jdbc.Driver
    url: jdbc:mysql://localhost:3306/ssm_db
    username: root
    password: 123456
    type: com.alibaba.druid.pool.DruidDataSource
```

- 注意
  - SpringBoot版本低于2.4.3(不含)，Mysql驱动版本大于8.0时，需要在url连接串中配置时区，或在MySQL数据库端配置时区解决此问题

```
jdbc:mysql://localhost:3306/ssm_db?serverTimezone=UTC
```

4. 定义数据层接口与映射配置

```java
@Mapper
public interface UserDao {
    @Select("select * from user")
    public List<user> getAll();
}
```

### 3.3 整合Druid

1. 导入坐标

```xml
<!-- 阿里数据库连接池 -->
<dependency>
    <groupId>com.alibaba</groupId>
    <artifactId>druid-spring-boot-starter</artifactId>
    <version>1.2.16</version>
</dependency>
```

2. 指定数据源

```yaml
spring:
  datasource:
    type: com.alibaba.druid.pool.DruidDataSource
    driver-class-name: com.mysql.cj.jdbc.Driver
    url: jdbc:mysql://localhost:3306/db1
    username: root
    password: 123456
```

## 4.基于SpringBoot的SSMP整合案例

案例实现方案分析

- 实体类开发——使用Lombok快速制作实体类
- Dao开发——整合MyBatisPlus，制作数据层测试类
- Service开发——基于MyBatisPlus进行增量开发，制作业务层测试类
- Controller开发——基于Restful开发，使用PostMan测试接口功能
- Controller开发——前后端开发协议制作
- 页面开发——基于VUE+ElementUI制作，前后端联调，页面数据处理，页面消息处理
  - 列表、新增、修改、删除、分页、查询
- 项目异常处理
- 按条件查询——页面功能调整、Controller修正功能、Service修正功能

### 4.1 springboot创建工程

1. 导入坐标

```xml
<!--mybatisplus-->
 <dependency>
    <groupId>com.baomidou</groupId>
    <artifactId>mybatis-plus-boot-starter</artifactId>
    <version>3.4.3</version>
</dependency>
<!--druid-->
<dependency>
    <groupId>com.alibaba</groupId>
    <artifactId>druid-spring-boot-starter</artifactId>
    <version>1.2.6</version>
</dependency>
<!--lombok-->
<dependency>
    <groupId>org.projectlombok</groupId>
    <artifactId>lombok</artifactId>
    <optional>true</optional>
</dependency>
```

修改mysql-connector

```xml
<dependency>
    <groupId>com.mysql</groupId>
    <artifactId>mysql-connector-j</artifactId>
    <version>8.0.32</version>
    <scope>runtime</scope>
</dependency>
```

2. 修改启动类的名称(可选)

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/340fb490a72834bfb8e4ce77907f93c3.png)

3. 修改配置文件名称(可选)

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/872c44a265976709b95484bef49fa8dc.png)

4. 编写配置

```yaml
server:
  port: 8080

spring:
  datasource:
    type: com.alibaba.druid.pool.DruidDataSource
    driver-class-name: com.mysql.cj.jdbc.Driver
    url: jdbc:mysql://localhost:3306/db1
    username: root
    password: 123456
```

5. 编写实体类

```java
package com.demo.vuespringboot_ssmp.pojo;

import lombok.Data;

@Data
public class Book {
  public Integer id;
  private String name;
  private String type;
  private String description;
}
```

### 4.2 数据层开发

#### 4.2.1 依赖

- mybatisplus

- druid

```xml
<dependency>
    <groupId>com.baomidou</groupId>
    <artifactId>mybatis-plus-boot-starter</artifactId>
    <version>3.4.3</version>
</dependency>
<dependency>
    <groupId>com.alibaba</groupId>
    <artifactId>druid-spring-boot-starter</artifactId>
    <version>1.2.6</version>
</dependency>
```

#### 4.2.2 创建实体类以及对应的mapper

```java
@Data					// 使用lombok自动添加getter和setter
@TableName("tb_book")	// 使实体类对应数据库的表名
public class Book {
  public Integer id;
  private String name;
  private String type;
  private String description;
}
```

```java
@Mapper
public interface BookMapper extends BaseMapper<Book> {
// 继承mybatisplus的基础父类，提供一系列内置方法(前提是实体类名与数据库表名相同或者添加了表名注解)，也可以自己写方法调用数据库
  @Select("select * from tb_book where id = #{id}")
  public Book getBookById(Integer id);

}
```

#### 4.2.3 编写测试类

```java
@SpringBootTest
public class BookMapperTestCase {
  @Autowired
  private BookMapper bookMapper;

  @Test
  void testGetBookById() {
    System.out.println(bookMapper.selectById(1));// 使用的是mabatisplus内置的方法
  }
}
```

注意事项

- 使用mybatisplus内置的插入方法会出现报错，原因是mybatisplus默认使用了雪花算法生成id报错

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/81ad657fbd37a0a5100369c102dfa03b.png)

- 解决方法，添加id配置为auto

```yaml
mybatis-plus:
  global-config:
    db-config:
      id-type: auto
```

#### 4.2.4 显示mybatisplus的详细日志

```yaml
mybatis-plus:
  global-config:
    db-config:
      id-type: auto
  configuration:
    log-impl: org.apache.ibatis.logging.stdout.StdOutImpl
```

#### 4.2.5 分页

1. 创建分页拦截器

```java
@Configuration
public class MybatisplusConfig {
  @Bean
  public MybatisPlusInterceptor mybatisPlusInterceptor() {
    MybatisPlusInterceptor interceptor = new MybatisPlusInterceptor();
    interceptor.addInnerInterceptor(new PaginationInnerInterceptor());
    return interceptor;
  }
}
```

2. 编写测试类

```java
@Test
void testGetBookByPage() {
  IPage page = new Page(2, 5);
  bookMapper.selectPage(page, null);
}
```

### 4.3 业务层开发


Service层接口定义与数据层接口定义具有较大区别，不要混用

- `selectByUserNameAndPassword(String username,String password);`
- `login(String username,String password);`

创建service接口与实现类

```java
@Service
public class BookServiceImpl implements BookService {
  @Autowired
  private BookMapper bookMapper;

  @Override
  public Boolean save(Book book) {
    return bookMapper.insert(book) == 1;
  }

  @Override
  public Boolean update(Book book) {
    return bookMapper.updateById(book) == 1;
  }

  @Override
  public Boolean delete(Integer id) {
    return bookMapper.deleteById(id) == 1;
  }

  @Override
  public Book getById(Integer id) {
    return bookMapper.selectById(id);
  }

  @Override
  public List<Book> getAll() {
    return bookMapper.selectList(null);
  }

  @Override
  public IPage<Book> getPage(Integer page, Integer size) {
    IPage<Book> ipage = new Page(page, size);
    return bookMapper.selectPage(ipage, null);
  }
}
```

创建测试类

```java
@SpringBootTest
public class BookServiceTestCase {
  @Autowired
  private BookService bookService;

  @Test
  void testSave() {
    Book book = new Book();
    book.setName("SpringBoot");
    book.setType("Java");
    book.setDescription("SpringBoot是一个java框架");
    bookService.save(book);
  }

  @Test
  void testUpdate() {
    Book book = new Book();
    book.setId(18);
    book.setName("Django");
    book.setType("Python");
    book.setDescription("Django是一个python框架");
    bookService.update(book);
  }

  @Test
  void testDelete() {
    bookService.delete(16);
  }

  @Test
  void testGetAll() {
    bookService.getById(null);
  }

  @Test
  void testGetBookByPage() {
    IPage page = bookService.getPage(2, 5);
    System.out.println(page.getRecords());
    System.out.println(page.getTotal());
  }
}
```

### 4.4 业务层快速开发

- 使用MyBatisPlus提供有业务层通用接口（`ISerivce<T>`)与业务层通用实现类(`ServiceImpl<M,T>`)
- 在通用类基础上做功能重载或功能追加
- 注意重载时不要覆盖原始操作，避免原始提供的功能丢失

<img src="https://gitee.com/pepedd864/cdn-repos/raw/master/img/0057bd6b9cb653174bbc4633d2405068.png" style="zoom:67%;" />

```java
// 接口
public interface IBookService extends IService<Book> {

}

// 实现类
@Service
public class IBookServiceImpl extends ServiceImpl<BookMapper, Book> implements IBookService {
}

```

### 4.5 表现层

1. 创建controller

```java
@RestController
@RequestMapping("/books")
public class BookController {
  @Autowired
  private IBookService bookService;

  /***
   * 根据id查询图书
   * @param id
   * @return Book
   */
  @GetMapping("/{id}")
  public Book getById(@PathVariable Integer id) {
    return bookService.getById(id);
  }

  /***
   * 查询所有图书
   * @return List<Book>
   */
  @GetMapping
  public List<Book> getAll() {
    return bookService.list();
  }

  /***
   * 上传图书
   * @param book
   * @return Boolean
   */
  @PostMapping
  public Boolean save(@RequestBody Book book) {
    return bookService.save(book);
  }

  /***
   * 更新图书
   * @param book
   * @return Boolean
   */
  @PutMapping
  public Boolean update(@RequestBody Book book) {
    return bookService.updateById(book);
  }

  /***
   * 删除图书
   * @param id
   * @return Boolean
   */

  @DeleteMapping("/{id}")
  public Boolean delete(@PathVariable Integer id) {
    return bookService.removeById(id);
  }
}
```

2. 在BookService中编写分页方法

```java
public IPage<Book> getPage(Integer page, Integer size) {
  IPage ipage = new Page(page, size);
  bookMapper.selectPage(ipage, null);
  return ipage;
}
```

3. 在controller 中添加分页功能

```java
/***
 * 分页查询图书
 * @param page
 * @param size
 * @return IPage<Book>
 */
@GetMapping("/page/{page}/{size}")
public IPage<Book> getBookByPage(@PathVariable Integer page, @PathVariable Integer size) {
  IPage ipage = new Page(page, size);
  bookService.page(ipage, null);
  return ipage;
}
```

### 4.6 封装返回数据

1. 创建封装类Result

```java
public class Result {
  private int code;
  private String msg;
  private Object data;

  public Result(int code, String msg) {
    this.code = code;
    this.msg = msg;
  }

  public Result(int code, String msg, Object data) {
    this.code = code;
    this.msg = msg;
    this.data = data;
  }

  @Override
  public String toString() {
    return "Result{" +
        "code=" + code +
        ", msg='" + msg + '\'' +
        ", data=" + data +
        '}';
  }

  public int getCode() {
    return code;
  }

  public void setCode(int code) {
    this.code = code;
  }

  public String getMsg() {
    return msg;
  }

  public void setMsg(String msg) {
    this.msg = msg;
  }

  public Object getData() {
    return data;
  }

  public void setData(Object data) {
    this.data = data;
  }
}
```

2. 创建返回Code类

```java
public class Code {
  // 成功
  public static final int SAVE_OK = 20011;
  public static final int DELETE_OK = 20021;
  public static final int UPDATE_OK = 20031;
  public static final int GET_OK = 20041;
  public static final int LIST_OK = 20051;
  public static final int PAGE_OK = 20061;

  // 失败
  public static final int SAVE_ERR= 20010;
  public static final int DELETE_ERR = 20020;
  public static final int UPDATE_ERR = 20030;
  public static final int GET_ERR = 20040;
  public static final int LIST_ERR = 20050;
  public static final int PAGE_ERR = 20060;
}
```

### 4.7 前端开发

略

### 4.8 异常消息处理

#### 4.8.1 开发中请求接口的异常消息

- 正常业务消息

```json
{
    "code": 20041,
    "msg": "查询成功",
    "data": [
        {
            "id": 46,
            "name": "",
            "type": "eqweqwe3123",
            "description": "eqweq312412"
        },
        {
            "id": 47,
            "name": "qweqw342",
            "type": "eqweqwe",
            "description": "eqweq"
        }
    ]
}
```

- 后端业务异常

```json
{
    "timestamp": "2023-03-18T11:32:03.856+00:00",
    "status": 400,
    "error": "Bad Request",
    "path": "/books"
}
```

#### 4.8.2 使用AOP处理异常消息

- 创建advice类，添加`@RestControllerAdvice`注解，在处理异常方法上加上`@ExceptionHandler`注解

```java
@RestControllerAdvice
public class ProjectExceptionAdvice {
  @ExceptionHandler
  public Result handleException(Exception e) {
     // 记录日志
     // ...
      
    // 打印异常信息
    e.printStackTrace();
    return new Result(Code.ERROR, e.getMessage());
  }
}
```

- 在表现层中处理异常信息，并抛出异常

```java
@GetMapping("/{id}")
public Result getById(@PathVariable Integer id) throws IOException {
  Book book = bookService.getById(id);
  if (book == null)
    throw new IOException("查询失败");
  return new Result(Code.GET_OK, "查询成功", book);
}
```

### 4.9 添加条件查询

1. 在mapper中添加条件查询

```java
/***
 * 条件查询
 * @param book book
 *             name 图书名
 *             type 图书类型
 *             description 图书描述
 * @return List<Book>
 */
@Select("select * from tb_book where name like '%${name}%' and type like '%${type}%' and description like '%${description}%'")
public List<Book> getBook(Book book);
```

2. 业务层

```java
public List<Book> getBook(Book book) throws IOException {
  List<Book> books;
  try {
    books = bookMapper.getBook(book);
  } catch (Exception e) {
    throw new IOException("查询失败");
  }
  return books;
}
```

3. 表现层

```java
/***
 * 条件查询
 * @param book book
 *             name 图书名
 *             type 图书类型
 *             description 图书描述
 * @return Result
 */
@GetMapping("/")
public Result getBook(Book book) throws IOException {
  List<Book> books = bookService.getBook(book);
  if (!checkBooks(books))
    throw new IOException("查询失败");
  return new Result(Code.GET_OK, "查询成功", books);
}
```

### 4.10 打包项目

1. 运行package命令

```bash
mvn package
```

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/9c3df3829484c676f19e0c89b0e9075f.png)

2. 运行项目

```bash
java -jar 项目名称.jar
```

注意

- jar支持命令行启动需要依赖maven插件支持，请确认打包时是否具有SpringBoot对应的maven插件

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-maven-plugin</artifactId>
        </plugin>
    </plugins>
</build>
```

### 4.11 端口占用的解决方法

windows

```bash
# 查询端口
netstat -ano
# 查询指定端口
netstat -ano | findstr 端口号
# 根据进程PID查询进程名称
tasklist | findstr 进程PID
# 根据PID关闭进程
taskkill -f -pid 进程PID号 # 需要管理员权限
# 根据进程名称关闭进程
taskkill -f -t -im 进程名称
```

### 4.12 临时属性

在项目运行命令中加入临时属性

```bash
java -jar 项目名称 --临时属性 
```

- 多个属性之间使用空格间隔

可以在启动sprng boot 程序时断开读取外部临时配置对应的入口

```java
@SpringBootApplication
public class SsmpApplication {

  public static void main(String[] args) {

    // 去掉启动时的临时配置入口
    SpringApplication.run(SsmpApplication.class);
  }

}
```

## 5. 日志

### 5.1 日志概念

日志（( log）作用

- 编程期调试代码
- 运营期记录信息
  - 记录日常运营重要信息（峰值流量、平均响应时长……)
  - 记录应用报错信息（错误堆栈)
  - 记录运维过程数据（扩容、宕机、报警……)

### 5.2 基本用法

```java
// 创建日志对象
private static final Logger log = (Logger) LoggerFactory.getLogger(BookController.class);
```

```java
log.debug("信息");
log.info("信息");
log.warn("信息");
log.error("信息");
```

```yaml
# 显示日志等级
# application.yml
logging:
	# 设置分组
	group:
		ebank: com.demo.springboot.controller, com.demo.springboot.service
		iservice: com.alibaba
	level:
		root: debug
		# 设置某个包的日志级别
		com.demo.springboot: debug
		# 设置分组日志级别
		ebank: info
```

### 5.3 快速创建日志对象

1. 导入lombok

```xml
<dependency>
    <groupId>org.projectlombok</groupId>
    <artifactId>lombok</artifactId>
    <optional>true</optional>
</dependency>

<build>
    <plugins>
        <plugin>
            <configuration>
                <excludes>
                    <exclude>
                        <groupId>org.projectlombok</groupId>
                        <artifactId>lombok</artifactId>
                    </exclude>
                </excludes>
            </configuration>
        </plugin>
    </plugins>
</build>
```

2. 添加日志注解`@Slf4j`

```java
@Slf4j
@RestController
@RequestMapping("/books")
public class BookController {
  @Autowired
  private IBookService bookService;
```

3. 使用日志对象

```java
log.debug("信息");
```

### 5.4 日志输出格式

```yaml
# 设置日志模板格式
pattern:
	console: "%d - %m %n" # 1
	console: "%d %clr(%5p) %m %n" # 2
```

### 5.5 文件记录日志

```yaml
# 基本的文件日志配置
pattern:
	name: server.log
```

```yaml
# 滚动日志
logging:
  file:
    name: "server.log"
  logback:
    rollingpolicy:
      max-file-size: 4KB
      file-name-pattern: n%d{yyyy-MM-dd}.%i.server.log
```

## 6. 热部署

### 6.1 快速入门

热部署

- 在不重启服务器的情况下更新代码

添加依赖

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-devtools</artifactId>
</dependency>
```

修改代码

重新构建项目(`Ctrl + F9`)

关于热部署

- 重启（Restart)∶自定义开发代码，包含类、页面、配置文件等，加载位置restart类加载器
- 重载（ReLoad) : jar包，加载位置base类加载器

### 6.2 自动热部署

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/3e5b76b68695149e60a51e5a0a34d837.png)

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/07c5ff794f4437edf5f606936824e93a.png)

注意

- 修改代码后IDEA窗口失去焦点后5秒自动构建

### 6.3 热部署范围

默认不触发重启的目录列表

- /META-INF /maven
- /META-INF /resources
- /resources
- /static
- /public
- /templates

```yaml
# 自定义排除项
spring:
  devtools:
    restart:
      exclude: static/**,public/**,config/**
```

### 6.4 使用JRebel进行热部署

1. 在idea上下载JRebel插件

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/aaa0d9f65a3106332930bb77a537df8c.png)

2. 激活插件

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/6d377ce0e3d23fad613c754e0221f093.png)

3. 下载本地激活服务器[下载](https://github.com/ilanyu/ReverseProxy/releases/tag/v1.4)

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/02c557a26b6ccf4ae50c04e60e06de6e.png)

4. 运行服务器

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/5c03b058404c4c811c1b6e6d236808bb.png)

5. [生成GUID](https://www.guidgen.com/)

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/9c63b1f85f611a184180ae3615996f6f.png)

6. 激活

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/9d5dbbec21710a97e7a6b5d9c31383b6.png)

7. 设置为离线

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/34ddc1dc9cc073715977d5187afc58b7.png)

8. 以JRebel运行

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/c70b952540e2952c67f687b36ee987fd.png)

9. 修改代码，按`Ctrl+F9`重新构建，JRebel会自动部署



## 7. JWT

### 7.1 简介

1. 什么是JWT
   - JSON Web Token，通过数字签名的方式，以JSON对象为载体，在不同的服务终端之间安全的传输信息。
2. 有什么用
   - JWT最常见的场景就是授权认证，一旦用户登录，后续每个请求都将包含JWT，系统在每次处理用户请求的之前，都要先进行JWT安全校验，通过之后再进行处理。
3. 组成
   - JWT由3部分组成，用`.`拼接
     - header
     - Payload
     - Signature

### 7.2 使用

```java
private long time = 1000 * 60 * 60 * 24;  // 一天
  private String signature = "admin";

  // 加密生成token
  @Test
  public void JwtTest() {
    JwtBuilder jwtBuilder = Jwts.builder();
    String jwtToken = jwtBuilder  // 创建jwtToken
        // header
        .setHeaderParam("typ", "JWT")
        .setHeaderParam("alg", "HS256")
        // payload
        .claim("userId", 1)
        .claim("userName", "admin")
        .claim("userType", 1)
        .setSubject("admin-test")
        .setExpiration(new Date(System.currentTimeMillis() + time)) // 设置有效时间
        .setId(UUID.randomUUID().toString())
        // signature
        .signWith(SignatureAlgorithm.HS256, signature) //签名
        .compact();
    System.out.println(jwtToken);
  }

  // 解密
  @Test
  public void parse() {
    String token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOjEsInVzZXJOYW1lIjoiYWRtaW4iLCJ1c2VyVHlwZSI6MSwic3ViIjoiYWRtaW4tdGVzdCIsImV4cCI6MTY3OTU2ODY5MiwianRpIjoiMDExMzRjOGUtZjBlMi00YTA0LWFkZjctMTU0NDAxOWM4MTZmIn0.wXSCIH7uPWrP5PTDLCapWx2NrFW2jdslJe2UtWxrHC0";
    JwtParser jwtParser = Jwts.parser();
    Jws<Claims> claimsJws = jwtParser.setSigningKey(signature).parseClaimsJws(token);
    Claims body = claimsJws.getBody();
    System.out.println(body.get("userId"));
    System.out.println(body.get("userName"));
    System.out.println(body.getId());
    System.out.println(body.getSubject());
    System.out.println(body.getExpiration());
  }
```



# MyBatisPlus

- MyBatisPlus (简称MP）是基于MyBatis框架基础上开发的增强型工具，旨在简化开发、提高效率

## 1. 简介

### 1.1 入门案例

1. 创建模块，选择依赖（MySQL Driver）
2. 手动添加MyBatisPlus依赖

```xml
<dependency>
	<groupId>com.baomidou</groupId>
    <artifactId>mybatis-plus-boot-starter</artifactId>
    <version>3.4.1</version>
</dependency>
```

3. 使用druid

```xml
<dependency>
    <groupId>com.alibaba</groupId>
    <artifactId>druid-spring-boot-starter</artifactId>
    <version>1.2.16</version>
</dependency>
```

4. 设置Jdbc参数（application.yml）

```yml
server:
  port: 80

spring:
  datasource:
    type: com.alibaba.druid.pool.DruidDataSource
    driver-class-name: com.mysql.cj.jdbc.Driver
    url: jdbc:mysql://localhost:3306/ssm_db
    username: root
    password: 123456
```

5. 制作实体类与标结构（类名与表名对应，属性名与字段名对应）

6. 定义数据接口，继承`BaseMapper<实体类>`

```java
@Mapper
public interface BookDao extends BaseMapper<Book> {
}
```

7. 测试类中注入dao接口，测试功能

```java
@SpringBootTest
class SpringbootMybatisplusApplicationTests {

  @Autowired
  private BookDao bookDao;

  @Test
  void contextLoads() {
    List<Book> books = bookDao.selectList(null);
    System.out.println(books);
  }
}
```

### 1.2 MyBatisPlus概述

- MyBatisPlus是基于MyBatis框架基础上开发的增强型工具，旨在简化开发、提高效率
- 官网: https://mybatis.plus/ https://mp.baomidou.com/

- 注意最新的springboot版本使用mybatisplus会出现无法创建bean的情况

### 1.3 MyBatisPlus特征

- 无侵入:只做增强不做改变，不会对现有工程产生影响
- 强大的CRUD操作:内置通用Mapper，少量配置即可实现单表CRUD操作
- 支持Lambda:编写查询条件无需担心字段写错
- 支持主键自动生成
- 内置分页插件
- ...

## 2. 标准数据层开发

### 2.1 标准数据层CRUD功能

| 功能       | 自定义接口                              | MyBatisPlus接口                                |
| ---------- | --------------------------------------- | ---------------------------------------------- |
| 新增       | `boolean save(T t)`                     | `int insert(T t)`                              |
| 删除       | `boolean delete(int id)`                | `int deleteById(Serialzable id)`               |
| 修改       | `boolean update(T t)`                   | `int updateById(T t)`                          |
| 根据id查询 | `T getById(int id)`                     | `T selectById(T t)`                            |
| 查询全部   | `List<T> getAll()`                      | `List<T> selectList()`                         |
| 分页查询   | `PageInfo<T> getAll(int page,int size)` | `IPage<T> selectPage(IPage<T> page)`           |
| 按条件查询 | `List<T> getAll(Condition condition)`   | `IPage<T> selectPage(Wrapper<T> queryWrapper)` |

---

### 2.2 lombok

- Lombok，一个Java类库，提供了一组注解，简化PO]0实体类开发

```xml
<dependency>
	<groupId>org.projectlombok</groupId>
    <artifactId>lombok</artifactId>
	<version>1.18.12</version>
	<scope>provided</scope>
</dependency>
```

- 常用注解：`@Data`
  - 为当前实体类在编译期设置对应的`get/set`方法，无参/无参构造方法，`toString`方法，`hashCode`方法，`equals`方法等

```java
@Data 
public class User {
	private Long id;
    private String name;
    private String password;
    private Integer age;
    private String tel;
}
```

### 2.3 分页功能

1. 设置分页拦截器作为Spring管理的bean（config.MybatisPlusConfig.java）

```java
@Configuration
public class MybatisPlusConfig {

  @Bean
  public MybatisPlusInterceptor mpInterceptor(){
    // 1. 定义拦截器
    MybatisPlusInterceptor mpInterceptor = new MybatisPlusInterceptor();
    // 2. 添加具体拦截器
    mpInterceptor.addInnerInterceptor(new PaginationInnerInterceptor());
    return mpInterceptor;
  }
}
```

2. 执行分页查询

```java
IPage page = new Page(2,3);	 // 当前页 每页多少条
userDao.selectPage(page,null);
System.out.println("当前页码："+page.getCurrent()); 
System.out.println("每页数据总量:"+page.getsize());
System.out.println("总页数:"+page .getPages());
System.out.println("数据总量:"+page.getTotal());
System.out.println("当前页数据:"+page.getRecords());
```

3. （可选）开启日志

```yaml
# 开启mybatis-plus的日志
mybatis-plus:
  configuration:
    log-impl: org.apache.ibatis.logging.stdout.StdOutImpl
```



### 2.4 DQL编程控制

#### 2.4.1 条件查询

- 格式一：常规格式

```java
QueryWrapper<User> qw = new QueryWrapper<User>(); 
//查询年龄大于等于18岁，小于65岁的用户
qw.lt( "age",65);
qw.ge( "age",18);
List<User> userList = userDao.selectList(qw);
System.out.println(userList);
```

- 格式二：链式编程格式

```java
QueryWrapper<User> qw = new QueryWrapper<User>();
//查询年龄大于等于18岁，小于65岁的用户
qw.lt("age",65).ge("age",18);
List<User> userList = userDao.selectList(qw);
System.out.println(userList);
```

- 格式三：lambda格式

```java
QueryWrapper<User> qw = new QueryWrapper<User>();
//查询年龄大于等于18岁，小于65岁的用户
qw.lambda().lt(User::getAge,65).ge(User::getAge,18);
List<User> userList = userDao.selectList(qw);
System.out.println(userList);
```

- 格式四：lambda格式

```java
LambdaQueryWrapper<User> lqw = new LambdaQueryWrapper<User>();
//查询年龄大于等于18岁，小于65岁的用户
lqw.lt(User::getAge,65).ge(User::getAge,18);
List<User> userList = userDao.selectList(lqw);
System.out.println(userList);
```



---

组合查询条件

- and

```java
qw.lambda().lt(User::getAge,65).ge(User::getAge,18);
```

- or

```java
qw.lambda().lt(User::getAge,65).or().ge(User::getAge,18);
```



#### 2.4.2 null值的处理

- if语句控制条件追加

```java
LambdaQueryWrapper<User> lqw = new LambdaQueryWrapper<User>();
if(null != userQuery.getAge()){
	lqw.ge(User::getAge,userQuery.getAge());
}
if(null != userQuery.getAge2()){
	lqw.lt(User::getAge,userQuery.getAge2());
}
List<User> userList = userDao.selectList(lqw);
System.out.println(userList);
```

- 条件参数控制

```java
LambdaQueryWrapper<User> lqw = new LambdaQuerywrapper<User>();
lqw.ge(null != userQuery.getAge(),User::getAge,userQuery.getAge());
lqw.lt(null != userQuery.getAge2(),User::getAge,userQuery.getAge2());
List<User> userList = userDao.selectList(lqw);
System.out.println(userList);
```

- 条件参数控制（链式编程）

```java
LambdaQueryWrapper<User> lqw = new LambdaQueryWrapper<User>();
lqw.ge(null != userQuery.getAge(),User::getAge,userQuery.getAge())
	.lt(null != userQuery.getAge2(),User::getAge,userQuery.getAge2());
List<User> userList = userDao.selectList(lqw);
System.out.println(userList);
```

#### 2.4.3 查询投影

- 查询结果包含模型类中部分属性

```java
LambdaQueryWrapper<User> lqw = new LambdaQueryWrapper<User>();
lqw.select(User::getId,User::getName,User::getAge);
List<User> userList = userDao.selectList(lqw);
System.out.println(userList);
```

- 查询结果包含模型类中未定义的属性

```java
QueryWrapper<User> qm = new QueryWrapper<User>();
qm.select("count(*) as nums ,gender");
qm.groupBy("gender");
List<Map<String,object>> maps = userDao.selectMaps(qm);
System.out.println(maps);
```

#### 2.4.4 查询条件设置

