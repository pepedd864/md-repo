## SpringBoot 自定义注解校验验证码(使用注解、AOP、反射等技术)

在后端服务的开发中验证码的校验是不可或缺的部分

通常我们把验证码校验写成这样

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/f338a3079471b2c2b737614756e2543d.png)

从redis取出验证码的值，然后和前端传入的值进行比较，验证码校验无误后进行后续操作

我们发现，需要验证码的功能，**校验都是先于业务逻辑的**，因此我们可以定义注解+AOP在方法执行前完成验证码的校验。

### 1. Java中的注解

注解（`Annotation`）是Java SE 5.0 版本开始引入的概念，它是对 Java 源代码的说明，是一种元数据（描述数据的数据）。

- 注解的定义通过 `@interface` 表示，所有的注解会自动继承 `java.lang.Annotation` 接口，且不能再继承别的类或是接口。
- 注解的成员参数只能用 `public` 或默认 (`default`) 访问权修饰来进行修饰。
- 成员参数只能使用 8 种基本类型（byte、short、char、int、long、float、double、boolean）和 String、Enum、Class、annotations等数据类型，及其数组。
- 获取类方法和字段的注解信息，只能通过 Java 的反射技术来获取 Annotation 对象。
- 注解可以没有定义成员，只做标识。



### 2. 注解的分类

按照来源划分，注解可以分为 3 类

1. JDK的注解
2. 第三方的注解
3. 自定义注解



### 3. JDK注解

JAVA内置注解在 `java.lang` 中，4个元注解在 `java.lang.annotation` 中。

**JAVA内置注解**

- @Override （标记重写方法）
- @Deprecated （标记过时）
- @SuppressWarnings （忽略警告）

**元注解 (注解的注解)**

- @Target （注解的作用目标）
- @Retention （注解的生命周期）
- @Document （注解是否被包含在JavaDoc中）
- @Inherited （是否允许子类继承该注解）

**@Target**

`@Target` 注解表明该注解可以应用的JAVA元素类型。

| Target类型                  | 描述                                                         |
| --------------------------- | ------------------------------------------------------------ |
| ElementType.TYPE            | 应用于类、接口（包括注解类型）、枚举                         |
| ElementType.FIELD           | 应用于属性（包括枚举中的常量）                               |
| ElementType.METHOD          | 应用于方法                                                   |
| ElementType.PARAMETER       | 应用于方法的形参                                             |
| ElementType.CONSTRUCTOR     | 应用于构造函数                                               |
| ElementType.LOCAL_VARIABLE  | 应用于局部变量                                               |
| ElementType.ANNOTATION_TYPE | 应用于注解类型                                               |
| ElementType.PACKAGE         | 应用于包                                                     |
| ElementType.TYPE_PARAMETER  | 1.8版本新增，应用于类型变量                                  |
| ElementType.TYPE_USE        | 1.8版本新增，应用于任何使用类型的语句中（例如声明语句、泛型和强制转换语句中的类型） |

**@Retention**

`@Retention`  表明该注解的生命周期。

| 生命周期类型            | 描述                                                         |
| ----------------------- | ------------------------------------------------------------ |
| RetentionPolicy.SOURCE  | 编译时被丢弃，不包含在类文件中                               |
| RetentionPolicy.CLASS   | JVM加载时被丢弃，包含在类文件中，默认值                      |
| RetentionPolicy.RUNTIME | 始终不会丢弃，可以使用反射获得该注解的信息。由JVM 加载，包含在类文件中，在运行时可以被获取到。自定义的注解最常用的使用方式。 |

**@Document**

表明该注解标记的元素可以被Javadoc 或类似的工具文档化

**@Inherited**

表明使用了@Inherited注解的注解，所标记的类的子类也会拥有这个注解。



### 4. 注解的语法

```java
/**
 * 修饰符 @interface 注解名 {
 * 注解元素的声明1
 * 注解元素的声明2
 * }
 */
```

 - 修饰符：访问修饰符必须为public,不写默认为pubic；
 - 关键字：必须为@interface；
 - 注解名： 注解名称为自定义注解的名称，使用时还会用到；
 - 注解类型元素：注解类型元素是注解中内容，可以理解成自定义接口的实现部分；

```java
@Target({ElementType.TYPE})
@Retention(RetentionPolicy.RUNTIME)
@Documented
public @interface MyTestAnnotation {
    /**
     *    注解的元素声明的两种形式
     *    type elementName();
     *    type elementName() default value;  
     */
    String value() default "test";
}
```



### 5. 反射

什么是反射?

- 反射允许对封装类的字段，方法和构造函数的信息进行编程访问。

例如IDEA的代码提示功能，利用了反射获取类的信息

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/174efdd670e1b525cf83264f81448f41.png)

反射获取信息和使用

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/829722463ce9bda3ad9a1da8029dc2ed.png)



### 6. 使用反射获取成员变量

**Class类中用于获取成员变量的方法**

| 方法名                                | 说明                           |
| ------------------------------------- | ------------------------------ |
| `Field [] getFields()`                | 返回所有公共成员变量对象的数组 |
| `Field[] getDeclaredFields()`         | 返回所有成员变量对象的数组     |
| `Field getField(String name)`         | 返回单个公共成员变量对象       |
| `Field getDeclaredField(String name)` | 返回单个成员变量对象           |

### 7. Spring AOP

#### 7.1 什么是AOP

AOP是Aspect Oriented Programming的缩写，意思是：面向切面编程，它是通过预编译方式和运行期动态代理实现程序功能的统一维护的一种技术。



#### 7.2 AOP中的概念

##### 7.2.1 通知(Advice)

在AOP术语中，切面要完成的工作被称为通知，通知定义了切面是什么以及何时使用。

Spring切面有5种类型的通知，分别是：

- 前置通知(Before)：在目标方法被调用之前调用通知功能
- 后置通知(After)：在目标方法完成之后调用通知，此时不关心方法的输出结果是什么
- 返回通知(After-returning)：在目标方法成功执行之后调用通知
- 异常通知(After-throwing)：在目标方法抛出异常后调用通知
- 环绕通知(Around)：通知包裹了被通知的方法，在被通知的方法调用之前和调用之后执行自定义的行为



##### 7.2.2 连接点(Join point)

连接点是在应用执行过程中能够插入切面的一个点，这个点可以是调用方法时、抛出异常时、修改某个字段时。



##### 7.2.3 切点(Pointcut)

切点是为了缩小切面所通知的连接点的范围，即切面在何处执行。我们通常使用明确的类和方法名称，或者利用正则表达式定义所匹配的类和方法名称来指定切点。



##### 7.2.4 切面(Aspect)

切面是通知和切点的结合。通知和切点共同定义了切面的全部内容：它是什么，在何时和何处完成其功能。



##### 7.2.5 引入(Introduction)

引入允许我们在不修改现有类的基础上，向现有类添加新方法或属性。



##### 7.2.6 织入(Weaving)

织入是把切面应用到目标对象并创建新的代理对象的过程。

切面在指定的连接点被织入到目标对象中，在目标对象的生命周期里，有以下几个点可以进行织入：

- 编译期：切面在目标类编译时被织入。这种方式需要特殊的编译器。AspectJ的织入编译器就是以这种方式织入切面的。
- 类加载期：切面在目标类加载到JVM时被织入。这种方式需要特殊的类加载器(ClassLoader)，它可以在目标类被引入应用之前增强该目标类的字节码。
- 运行期：切面在应用运行的某个时刻被织入。一般情况下，在织入切面时，AOP容器会为目标对象动态地创建一个代理对象。Spring AOP就是以这种方式织入切面的。



### 8. 开始动工

前面介绍了Java中的注解、AOP和反射，我们通过这三个个东西获取方法的参数并在方法之前执行验证码验证的操作

首先我们需要引入spring-aop

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-aop</artifactId>
    <version>${spring-boot.version}</version>
</dependency>
```

创建`VerifyCCaptha`注解

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/acda0c15043f62c377ebf0eadda56fb2.png)

```java
/**
 * 验证码校验注解
 *
 * @author pepedd864
 * @since 2023/12/5
 */
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.METHOD)
public @interface VerifyCaptcha {
  String code() default "0"; // 验证码 默认为第一个参数

  String uuid() default "1"; // 验证码uuid 默认为第二个参数
}
```



创建切面

```java
/**
 * 验证码验证切面
 *
 * @author pepedd864
 * @since 2023/12/5
 */
@Aspect
@Component
@Slf4j
public class VerifyCaptchaAop {
  @Autowired
  private RedisCache redisCache;


  /**
   * 校验验证码
   *
   * @param joinPoint     切点
   * @param verifyCaptcha 注解
   */
  @Before("@annotation(verifyCaptcha)")
  public void verifyCaptcha(JoinPoint joinPoint, VerifyCaptcha verifyCaptcha) {
    log.info("校验验证码...");
     // TODO 校验流程
  }
}
```

我们希望在方法上使用可以自动获取参数并校验验证码，就像这样

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/d58435ec3a33facd85293da3480d32cd.png)

而Java程序在运行时无法获取方法参数名，注解中也无法获取方法的参数。因此，我想到**使用数字获取方法中的第n个参数，并使用反射获取参数的值(其实可以使用JSON序列化反序列获取参数)**

于是code和uuid就变成了这样`0$code`、`0$uuid`

在aop中先分割注解中的参数，并转为数字

```java
// 分割参数 0$code.n1.n2  0$uuid.n1.n2 为 0 code.n1.n2; 0 uuid.n1.n2 两个部分
String[] split1 = verifyCaptcha.code().split("\\$");
String[] split2 = verifyCaptcha.uuid().split("\\$");

int n1 = Integer.parseInt(split1[0]);
int n2 = Integer.parseInt(split2[0]);
```

在方法中，我们可能只传入数字`0`、`1`等，于是我们也需要做出判断

```java
// 一级参数时
if (split1.length == 1) {
  // ...
}
if (split2.length == 1) {
  // ...
}
// 二级参数时
if (split1.length != 1 && split2.length != 1) {
    // ...
}
```

为了进行后续操作，我们先定义获取对象属性值的方法，它需要传入一个对象`obj`和属性的路径`n1.n2.n3`

```java
/**
 * 通过反射获取对象属性值
 *
 * @param obj             对象
 * @param propertyNameStr 属性名，支持多级，如：user.name
 * @return 属性值
 * @throws Exception 异常
 */
public Object getProperty(Object obj, String propertyNameStr) throws Exception {
  String[] propertyNames = propertyNameStr.split("\\.");

  Object propertyValue = obj;

  for (String propertyName : propertyNames) {
    Field field = propertyValue.getClass().getDeclaredField(propertyName);
    field.setAccessible(true);
    propertyValue = field.get(propertyValue);
  }

  return propertyValue;
}
```



所以获取参数的操作就变成了这样

```java
// 通过 args1[0] 中的数字n 获取第n个参数
Object[] args = joinPoint.getArgs();
String code = "";
String uuid = "";

try {
  // 一级参数时
  if (split1.length == 1) {
    code = args[n1].toString();
  }
  if (split2.length == 1) {
    uuid = args[n2].toString();
  }
  // 二级参数时
  if (split1.length != 1 && split2.length != 1) {
    if (args.length > n1) {
      code = getProperty(args[n1], split1[1]).toString();
    }
    if (args.length > n2) {
      uuid = getProperty(args[n2], split2[1]).toString();
    }
  }
} catch (Exception e) {
  throw new RuntimeException("验证码参数错误");
}

log.info("code: {}", code);
log.info("uuid: {}", uuid);
```



校验验证码使用之前的逻辑即可

```java
// 校验验证码
String captchaCode = redisCache.getCacheObject(CacheConstants.CAPTCHA_CODE_KEY + uuid);
if (captchaCode == null) {
  throw new RuntimeException("验证码已过期");
}
if (!code.equalsIgnoreCase(captchaCode)) {
  throw new RuntimeException("验证码错误");
}
redisCache.deleteObject(CacheConstants.CAPTCHA_CODE_KEY + uuid);
```



完整代码如下

```java
package cn.pepedd.aop;

import cn.pepedd.annotation.VerifyCaptcha;
import cn.pepedd.constants.CacheConstants;
import cn.pepedd.redis.RedisCache;
import lombok.extern.slf4j.Slf4j;
import org.aspectj.lang.JoinPoint;
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Before;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import java.lang.reflect.Field;

/**
 * 验证码验证切面
 *
 * @author pepedd864
 * @since 2023/12/5
 */
@Aspect
@Component
@Slf4j
public class VerifyCaptchaAop {
  @Autowired
  private RedisCache redisCache;


  /**
   * 校验验证码
   *
   * @param joinPoint     切点
   * @param verifyCaptcha 注解
   */
  @Before("@annotation(verifyCaptcha)")
  public void verifyCaptcha(JoinPoint joinPoint, VerifyCaptcha verifyCaptcha) {
    log.info("校验验证码...");

    // 分割参数 0$code.n1.n2  0$uuid.n1.n2 为 0 code.n1.n2; 0 uuid.n1.n2 两个部分
    String[] split1 = verifyCaptcha.code().split("\\$");
    String[] split2 = verifyCaptcha.uuid().split("\\$");

    int n1 = Integer.parseInt(split1[0]);
    int n2 = Integer.parseInt(split2[0]);

    // 通过 args1[0] 中的数字n 获取第n个参数
    Object[] args = joinPoint.getArgs();
    String code = "";
    String uuid = "";

    try {
      // 一级参数时
      if (split1.length == 1) {
        code = args[n1].toString();
      }
      if (split2.length == 1) {
        uuid = args[n2].toString();
      }
      // 二级参数时
      if (split1.length != 1 && split2.length != 1) {
        if (args.length > n1) {
          code = getProperty(args[n1], split1[1]).toString();
        }
        if (args.length > n2) {
          uuid = getProperty(args[n2], split2[1]).toString();
        }
      }
    } catch (Exception e) {
      throw new RuntimeException("验证码参数错误");
    }

    log.info("code: {}", code);
    log.info("uuid: {}", uuid);

    // 校验验证码
    String captchaCode = redisCache.getCacheObject(CacheConstants.CAPTCHA_CODE_KEY + uuid);
    if (captchaCode == null) {
      throw new RuntimeException("验证码已过期");
    }
    if (!code.equalsIgnoreCase(captchaCode)) {
      throw new RuntimeException("验证码错误");
    }
    redisCache.deleteObject(CacheConstants.CAPTCHA_CODE_KEY + uuid);
  }

  /**
   * 通过反射获取对象属性值
   *
   * @param obj             对象
   * @param propertyNameStr 属性名，支持多级，如：user.name
   * @return 属性值
   * @throws Exception 异常
   */
  public Object getProperty(Object obj, String propertyNameStr) throws Exception {
    String[] propertyNames = propertyNameStr.split("\\.");

    Object propertyValue = obj;

    for (String propertyName : propertyNames) {
      Field field = propertyValue.getClass().getDeclaredField(propertyName);
      field.setAccessible(true);
      propertyValue = field.get(propertyValue);
    }

    return propertyValue;
  }
}
```



 