## 1. 简介

**Spring Security**是Spring家族中的一个安全管理框架。相比与另外一个安全框架**Shiro**，它提供了更丰富的功能，社区资源也比shiro丰富。

一般来说中大型的项目都是使用SpringSecurity来做安全框架。小项目有Shiro的比较多，因为相比与SpringSecurity，Shiro的上手更加的简单。

### 1.1 核心功能

一般Web应用的需要进行**认证**和**授权**。

- 认证:验证当前访问系统的是不是本系统的用户，并且要确认具体是哪个用户
- 授权:经过认证后判断当前用户是否有权限进行某个操作

而认证和授权也是SpringSecurity作为安全框架的核心功能。

### 1.2 认证

**官方说法**

> 认证就是确认一个人或者一个实体的身份 是否真实的过程。在计算机领域中，认证通常用于确认一个用户是否是合法的用户。认证的过程通常包括用户提供凭证（例如用户名和密码〉以及系统对凭证的验证。

**通俗说法**

- 例如您去银行取钱，银行会要求您出示身份证等证件以确认您的身份，这就是一种身份认证。在计算机系统中，也会要求用户提供类似于身份证的凭证（例如用户名和密码)，以确认用户是否有权访问该系统中的资源。

**那么Spring Security都支持哪些认证呢?**

- 基于表单的认证
  - 用户在Web页面上输入用户名和密码，然后将其提交到服务器进行验证。这种方式是Web应用程序中最常见的认证方式。
- 基于HTTP基本认证
  - 用户在浏览器中输入URL时，浏览器会弹出对话框要求用户输入用户名和密码。这种方式适用于RESTful Web服务等无状态应用程序。
- 基于OAuth2认证
  - OAuth2是一个开放的标准协议，允许用户授权第三方应用程序访问他们的受保护资源。SpringSecurity支持OAuth2认证方式，可以方便地与第三方应用程序集成。
- 基于记住我认证
  - 记住我认证允许用户在关闭浏览器后保持登录状态。用户在首次登录后，系统会生成一个持久性Cookie，保存在用户的浏览器中。当用户再次访问该网站时，系统会使用Cookie中的信息自动认证用户。
- 基于LDAP认证
  - LDAP是轻量级目录访问协议，用于访问和维护分布式目录服务。Spring Security支持使用LDAP进行用户身份验证。

### 1.3 授权

**怎么理解授权呢?**

授权通常是指系统对用户进行访问控制的过程。也就是说，如果用户经过了认证，系统需要决定该用户能够访问哪些资源，以及以什么样的方式进行访问。例如，系统可以授权某个用户访问某个文件，但只能以只读模式进行访问。授权可以帮助系统保护用户的隐私和数据的安全，防止未经授权的用户访问系统中的敏感资源。



### 1.4 其他功能

**Session管理**

- Spring Security 可以跟踪用户的会话状态，并提供管理和控制用户会话的能力。通过对Session的管理，可以防止会话劫持和其他安全威胁。

**CSRF防护**

- Spring Security可以防止跨站请求伪造攻击(CSRF)，它会在表单中添加随机生成的Token，以确保每个请求都是合法的。

**密码加密和哈希**

- Spring Security提供了多种密码加密和哈希算法，包括BCrypt、PBKDF2和SHA-256等。这些算法可以帮助应用程序保护用户密码和敏感数据的安全。

**身份认证和授权缓存**

- Spring Security提供了身份认证和授权缓存，可以减少重复的数据库或LDAP访问，提高应用程序的性能。

**集成其他安全框架**

- Spring Security可以与其他安全框架（如Apache Shiro)集成，以提供更全面的安全解决方案。

## 2. 快速入门

### 2.1 准备工作

1. 创建一个Maven项目
2. 导入依赖

```xml
<parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>2.5.14</version>
</parent>

<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
    <dependency>
        <groupId>org.projectlombok</groupId>
        <artifactId>lombok</artifactId>
        <optional>true</optional>
    </dependency>
</dependencies>
```

3. 创建启动类

```java
@SpringBootApplication
public class app {
  public static void main(String[] args) {
    SpringApplication.run(app.class, args);
  }
}
```

4. 创建控制器

```java
@RestController
public class testController {
  @RequestMapping("/test")
  public String test() {
    return "test";
  }
}
```



### 2.2 引入SpringSecurity

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-security</artifactId>
</dependency>
```

引入依赖后我们在尝试去访问之前的接口就会自动跳转到一个SpringSecurity的默认登陆页面，默认用户名是user，密码在控制台上，必须登录才能对接口进行访问

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/42eee028ae9ae3498e6464d3e4c8d134.png)

访问资源时默认跳转到登录界面

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/43e9bc185897dfaf7eddbd9b32c5e66b.png)

## 3. 基础



Spring Security通过一些列的过滤器完成了用户身份认证及其授权工作，每个过滤器都有不同分工，当然这些过滤器并不是全部都一起工作，而是根据我们需要什么功能，才会选取对应的过滤器加入。当然这些过滤器并不是直接加入web的过滤器中，而是通过一个过滤器代理完成。web过滤器中只会加入一个或多个过滤器代理，然后由这些代理负责管理哪些Security Filter需要加入进来。

<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/088efe8f2a4f734168aa06504aa0a854.png" style="zoom:50%;" />

如果有多个过滤器链代理的话，那么就会变成这样:

<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/6a7dac169069540398256b35138053b5.png" style="zoom:50%;" />

### 3.1 组件介绍

**Authentication (Principal)**
封装用户身份信息，顶层接口，主要实现如下

- AbstractAuthenticationToken ()
  -  RememberMeAuthenticationToken rememberMe 登陆后封装的身份信息
  - UsernamePasswordAuthenticationToken 用户名密码登录后封装的身份信息

**AuthenticationManager**
身份认证器的代理，主要负责多个认证器的代理，管理多个AuthenticationProvider,主要实现如下

- ProviderManager (authenticate)



**AuthenticationProvider**
真正实现认证工作，多个provider受AuthenticationManager管理，主要实现如下

- AbstractUserDetailsAuthenticationProvider

  - DaoAuthenticationProvider

  - RememberMeAuthenticationProvider

**UserDetailsService**
负责定义用户信息的来源，从不同来源加载用户信息，唯一的方法: loadUserByUsername，主要实现类:

- UserDetailsManager
  - InMemoryUserDetailsManagero
  - JdbcUserDetailsManager
- 自定义

**UserDetails**
定义用户身份信息，比Authentication信息更详细，主要实现

- User
- 一般我们自定义

**FilterChainProxy**
Spring Securty Filter的入口，FilterChainProxy管理多个filter

**AbstractHttpConfigurer**
构建所有过滤器的核心组件，主要方法init()和configure(),主要实现类

- FormLoginConfigurer
- CorsConfigurer
- CsrfConfigurer
- HttpBasicConfigurer
- LogoutConfigurer
- ...

**一图理清基本组件关系**

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/ee4a68843f5117bd4d47756fe9028864.png)



### 3.2 登录表单配置

**用户信息**

1. 配置默认用户信息

```yml
spring:
  security:
    user:
      name: lglbc
      password: 123456
```



**基本登录表单配置**

2. 添加SecurityConfig

```java
@Configuration
public class SecurityConfig {
    @Bean
    public SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        http.authorizeHttpRequests((auth) ->{
            try {
                auth.anyRequest().authenticated()
                        .and()
                        .formLogin()
//                        .loginPage("/login.html")
                        .loginProcessingUrl("/login")
//                        .defaultSuccessUrl("/")
//                        .failureForwardUrl("/loginFail")
                        .permitAll()
                        .and()
                        .csrf().disable();
            } catch (Exception e) {
                throw new RuntimeException(e);
            }

        });
        return http.build();
    }
}
```

- authorizeHttpRequests ():开启权限配置
- anyRequest().authenticated()所有请求都需要认证
- and()返回HttpSecurity，从头开始配置
- formLogin()开启表单登陆，引入表单登陆过滤器(默认也会引入)
- loginPage("/login.html")自定义登录页面
- loginProcessingUrl("/login")定义登录提交的接口地址
- defaultSuccessUrl设置登录成功后的跳转地址
- failureUrl设置登录失败后的跳转地址
- permitAll()允许这些地址不需要认证
- csrf().disable()security支持csrf 防护，默认是开启，为了测试方便，这里暂时禁用，后面章节会详细介绍



**创建登录界面**

在resources/static下面新建login.html，和上面配置的路径一致

```html
<!DOCTYPE html>
<html lang="en" xmlns:th="http://www.thymeleaf.org">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<div th:text="SPRING_SECURITY_LAST_EXCEPTION"></div>
<form action="/login" method="post">
    用户名:<input name="username" type="text"><br>
    密码:<input name="password" type="password"><br>
    <button type="submit">登陆</button>
</form>
</body>
</html>
```

- action: loginProcessingUrl("/login")使用此值
- name:默认username和password

我如何知道默认key是username和password呢?有两种方法可以确定∶

- 第一种:根据默认表单页面，查看网络请求，就能拿到
- 第二种:看源码



**验证登录**

- 验证成功

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/fb36da2a1971224f2f173fe7e0f13260.png)

- 验证失败

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/7a58cd26445835907bbc75ff4a886aa9.png)



**添加登录成功失败处理器**

- 登录成功json

```java
.successHandler(new AuthenticationSuccessHandler() {
    @Override
    public void onAuthenticationSuccess(HttpServletRequest request, HttpServletResponse response, Authentication authentication) throws IOException, ServletException {
        Map<String,Object> result = new HashMap<>();
        result.put("code",0);
        result.put("msg","登陆成功");
        result.put("data",authentication);
        writeResp(result,response);
    }
})
```

<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/6e771590a897ae795c3f460c4d0e6778.png" style="zoom:67%;" />

- 登录失败json

```java
.failureHandler(new AuthenticationFailureHandler() {
    @Override
    public void onAuthenticationFailure(HttpServletRequest request, HttpServletResponse response, AuthenticationException exception) throws IOException, ServletException {
        Map<String,Object> result = new HashMap<>();
        result.put("code",-1);
        result.put("msg","登陆失败");
        result.put("data",exception.getMessage());
        writeResp(result,response);
    }
})
```

<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/c964d919718411255d162a0a678a5d42.png" style="zoom:67%;" />



### 3.3 登录用户数据获取

**通过SecurityContextHolder获取**

```java
@RequestMapping("/")
@ResponseBody
public String index(){
    Authentication authentication = SecurityContextHolder.getContext().getAuthentication();
    return JSON.toJSONString(authentication);
}
```

 **注入Authentication**

```java
@RequestMapping("/authentication")
@ResponseBody
public String index(Authentication authentication){
    return JSON.toJSONString(authentication);
}
```

**如何在异步线程中当前登录信息**

很多同学在学习了通过SecurityContextHolder之后，就想尝试下，发现在正常使用中，是可以拿到用户信息的，但是在异步线程中就拿不到了，这个其实可以通过调整他的策略来实现在异步线程中获取用户信息。
SecurityContextHolder主要有三种策略:

- MODE_THREADLOCAL
  - 默认策略，使用THREADLOCAL实现，只在当前线程中保存用户信息
- MODE_INHERITABLETHREADLOCAL
  - 支持在多线程中传递用户信息，使用这种策略，当我们启动新线程时，security会将当前线程的用户信息拷贝一份到新线程中
- MODE_GLOBAL
  - security将数据保存在一个全局变量中，也能解决多线程问题，一般很少用
  - 如果使用默认策略，在异步线程中获取用户信息，返回为空:



```java
@RequestMapping("/async")
@ResponseBody
public String async(){
    new Thread(new Runnable() {
        @Override
        public void run() {
            Authentication authentication = SecurityContextHolder.getContext().getAuthentication();
            System.out.println(JSON.toJSON(authentication));
        }
    }).start();
    return JSON.toJSONString("success");
}
```

调整vm配置，添加`-Dspring.security.strategy=MODE_INHERITABLETHEREADLOCAL`

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/d0955cdc236cca9380dbba495896a757.png)



### 3.4 基于多种方式配置登录用户：menory、MyBatis

#### 3.4.1 基于内存方式

**基于内存方式**

其实我们在配置文件中写的用户信息，最终也是被读到内存中的

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/f2aa82704ca7eca5c9abeb760cbacf2c.png)

这一块就是基于内存方式构建了用户信息，定义了默认的用户信息来源。

**配置内存方式**

```java
@Bean
public InMemoryUserDetailsManager inMemoryUserDetailsManager(){
    UserDetails userDetails1 = User.withUsername("memory1").password("{noop}memory1").roles("memory1").build();
    UserDetails userDetails2 = User.withUsername("memory2").password("{noop}memory2").roles("memory1").build();
    return new InMemoryUserDetailsManager(userDetails1,userDetails2);
}
```

#### 3.4.2 基于MyBatis方式

**引入依赖**

```java
implementation 'org.mybatis.spring.boot:mybatis-spring-boot-starter:+'
```

**定义user**

```java
@Data
public class User implements UserDetails {
    private Integer id;
    private String username;
    private String password;
    private Boolean enabled;
    private Boolean accountNonExpired;
    private Boolean accountNonLocked;
    private Boolean credentialsNonExpired;
}
```

**定义UserDetailService**

```java
@Service
public class MyUserDetailService implements UserDetailsService {
    @Autowired
    private UserMapper userMapper;
    @Override
    public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {
        User user = userMapper.loadUserByUserName(username);
        if (Objects.isNull(user)) {
            throw new UsernameNotFoundException("user is null");
        }
        user.setRoles(userMapper.getRolesByUid(user.getId()));
        return user;
    }
}
```

**创建MyBatis mapper**

```java
@Mapper
public interface UserMapper {
    @Select("select r.* from user_role ur LEFT JOIN role r on ur.rid=r.id where ur.uid=#{id}")
    public List<User.Role> getRolesByUid(@Param("id") Integer id);

    @Select("select * from user where username=#{uname} limit 1")
    public User loadUserByUserName(String uname);
}
```

**创建需要的表**

```sql
CREATE TABLE `role` (
`id` int(11) NOT NULL AUTO_INCREMENT,
`name` varchar(32) DEFAULT NULL,
`nameZh` varchar(32) DEFAULT NULL,
PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
CREATE TABLE `user` (
`id` int(11) NOT NULL AUTO_INCREMENT,
`username` varchar(32) DEFAULT NULL,
`password` varchar(255) DEFAULT NULL,
`enabled` tinyint(1) DEFAULT NULL,
`accountNonExpired` tinyint(1) DEFAULT NULL,
`accountNonLocked` tinyint(1) DEFAULT NULL,
`credentialsNonExpired` tinyint(1) DEFAULT NULL,
PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
CREATE TABLE `user_role` (
`id` int(11) NOT NULL AUTO_INCREMENT,
`uid` int(11) DEFAULT NULL,
`rid` int(11) DEFAULT NULL,
PRIMARY KEY (`id`),
KEY `uid` (`uid`),
KEY `rid` (`rid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


INSERT INTO `role` (`id`, `name`, `nameZh`)
VALUES
(1,'ROLE_dba','数据库管理员'),
(2,'ROLE_admin','系统管理员'),
(3,'ROLE_user','用户');
INSERT INTO `user` (`id`, `username`, `password`, `enabled`,
`accountNonExpired`, `accountNonLocked`, `credentialsNonExpired`)
VALUES
(1,'root','{noop}123',1,1,1,1),
(2,'admin','{noop}123',1,1,1,1),
(3,'sang','{noop}123',1,1,1,1);
INSERT INTO `user_role` (`id`, `uid`, `rid`)
VALUES
(1,1,1),
(2,1,2),
(3,2,2),
(4,3,3);
```



### 3.5 配置多个数据源

**定义两组UserDetailService**

```java
@Bean
public UserDetailsService userDetailsService1(){
    UserDetails userDetails = User.withUsername("memory1").password("{noop}memory1").roles("memory1").build();
    return new InMemoryUserDetailsManager(userDetails);
}
@Bean
public UserDetailsService userDetailsService2(){
    UserDetails userDetails = User.withUsername("memory2").password("{noop}memory2").roles("memory2").build();
    return new InMemoryUserDetailsManager(userDetails);
}
```

**定义AuthenticationManager**

```java
@Bean
public AuthenticationManager authenticationManager(){
    DaoAuthenticationProvider provider = new DaoAuthenticationProvider();
    provider.setUserDetailsService(userDetailsService1());
    DaoAuthenticationProvider provider2 = new DaoAuthenticationProvider();
    provider2.setUserDetailsService(userDetailsService2());
    return new ProviderManager(provider2,provider);
}
```



### 3.6 实现验证码功能

SpringSecurity 默认是不支持验证码功能的，但是我们可以自己扩展，这也是我们使用SpringSecurity最大的好处，原生不支持，我们就自己扩展。

因为系统默认的有一个DaoAuthenticationProvider 认证处理器，但是他只支持用户名和密码方式登录，所以是不能使用现有的认证器，那我们是不是可以实现一个自己的认证器，来覆盖这个默认的认证器呢？答案当然是可以的，大概实现思路是这样的：

- 创建一个认证器 继承默认的密码认证器DaoAuthenticationProvider

- 定义验证码认证器的逻辑

- - 从session获取保存的验证码
  - 从请求参数中获取用户输入的验证码
  - 比对验证码
  - 如果匹配成功，则调用DaoAuthenticationProvider的authenticate方法，进行原先逻辑认证
  - 如果匹配失败，则抛出异常，不走后面的逻辑

- 将自定义的provider加到AuthenticationManager中

大致思路是这样，那么还有没有别的方式呢？当然有了，我们还可以通过过滤器实现，但是这个过滤器的优先级要先于认证过滤器之前，这个后面再和大家介绍，这节课我们先看下如何通过自定义认证器来实现验证码校验的功能。

**引入依赖**

```java
implementation 'com.github.penggle:kaptcha:2.3.2'
```

**配置验证码**

```java
@Bean
public Producer producer() {
    Properties properties = new Properties();
    properties.setProperty("kaptcha.image.width", "150");
    properties.setProperty("kaptcha.image.height", "50");
    properties.setProperty("kaptcha.textproducer.char.string", "012");
    properties.setProperty("kaptcha.textproducer.char.length", "4");
    Config config = new Config(properties);
    DefaultKaptcha defaultKaptcha = new DefaultKaptcha();
    defaultKaptcha.setConfig(config);
    return defaultKaptcha;
}
```

**创建验证码入口**

```java
@Autowired(required = false)
private Producer producer;
@RequestMapping("/kaptcha")
public void kaptcha(HttpServletResponse response, HttpSession session){
    response.setContentType("image/jpg");
    String text = producer.createText();
    session.setAttribute("KAPTCHA_CODE",text);
    BufferedImage image = producer.createImage(text);
    try(ServletOutputStream outputStream = response.getOutputStream()){
        ImageIO.write(image,"jpg",outputStream);
    } catch (IOException e) {
        throw new RuntimeException(e);
    }
}
```

**自定义验证码认证处理器**

```java
public class KaptchaAuthenticationProvider extends DaoAuthenticationProvider {
    @Override
    public Authentication authenticate(Authentication authentication) throws AuthenticationException {
        HttpServletRequest request = ((ServletRequestAttributes) Objects.requireNonNull(RequestContextHolder.getRequestAttributes())).getRequest();
        String kaptchaCode = (String) request.getSession().getAttribute("KAPTCHA_CODE");
        String inputKaptcha = request.getParameter("kaptcha");
        if (!StrUtil.equals(kaptchaCode, inputKaptcha)) {
            throw new InternalAuthenticationServiceException("验证码验证失败");
        }
        return super.authenticate(authentication);
    }
}
```

**自定义登录页面**

```html
<!DOCTYPE html>
<html lang="en" xmlns:th="http://www.thymeleaf.org">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<div th:text="${SPRING_SECURITY_LAST_EXCEPTION}"></div>
<form action="/login" method="post">
    用户名:<input name="username" type="text"><br>
    密码:<input name="password" type="password"><br>
    验证码:<input name="kaptcha" type="text"><br>
    <img src="/kaptcha">
    <button type="submit">登陆</button>
</form>
</body>
</html>
```

**配置SecurityFilterchain**

```java
@Bean
public SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
    http.authorizeHttpRequests((auth) ->{
        try {
            auth.antMatchers("/kaptcha").permitAll()
                    .anyRequest().authenticated()
                    .and().formLogin()
                    .loginPage("/login.html")
                    .loginProcessingUrl("/login")
                    .failureForwardUrl("/login.html")
                    .permitAll()
                    .and()
                    .csrf().disable();
        }
        catch (Exception e){
        }
    });
    return http.build();
}
```

**配置AuthenticationManager**

```java
@Bean
public UserDetailsService userDetailsService(){
    UserDetails userDetails = User.withUsername("memory1").password("{noop}memory1").roles("memory1").build();
    return new InMemoryUserDetailsManager(userDetails);
}

@Bean
public KaptchaAuthenticationProvider kaptchaAuthenticationProvider(){
    KaptchaAuthenticationProvider kaptchaAuthenticationProvider= new KaptchaAuthenticationProvider();
    kaptchaAuthenticationProvider.setUserDetailsService(userDetailsService());
    return kaptchaAuthenticationProvider;
}

@Bean
public AuthenticationManager authenticationManager(){
    return new ProviderManager(kaptchaAuthenticationProvider());
}
```

**验证登录**

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/37851a9dbd1fc6be3b941d4106e855cd.png)

### 3.7 使用JSON数据格式登录

在前面的章节中，我们使用表单方式完成登录提交，但是目前基本都是前后端分离项目，很少使用表单提交的方式，基本都是json方式，使用ajax提交，那么我们怎么将表单提交方式改成json格式登录呢？

**思路分析**

通过前面源码部分学习，我们已经知道在HttpSecurity配置中，每新增一种配置，都会加入一个过滤器，或者覆盖默认的过滤器，那么我们使用的表单登录也是同样使用过滤器，我们追踪源码看下他的过滤器：UsernamePasswordAuthenticationFilter

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/00e245373700f6de7a0baf5f72dc9cb4.png)

- 使用Obtain获取用户名和密码，其实就是通过request.getParameter获取
- 然后将用户名和密码封装在token
- 调用proverManager.authenticate()进行认证 所以基于这块我们可以参考上节课验证码的思路：

**实现思路**

- 写一个过滤器，继承UsernamePasswordAuthenticationFilter
- 从json格式参数中获取用户名和密码
- 然后进行封装成token
- 调用this.getAuthenticationManager().authenticate(authRequest) 完成认证
- 如果不是json格式请求则还是走原先的逻辑，调用父类attemptAuthentication(request, response);按照原先参数传递方式进行认证

**代码实现**

- 定义Json过滤器

```java
public class JsonLoginFilter extends UsernamePasswordAuthenticationFilter {
    @Override
    public Authentication attemptAuthentication(HttpServletRequest request, HttpServletResponse response) throws AuthenticationException {
        if (request.getContentType().equalsIgnoreCase(MediaType.APPLICATION_JSON_VALUE)){
            try {
                Map<String,String> map = new ObjectMapper().readValue(request.getInputStream(), new TypeReference<>() {
                });
                String userName = map.get(getUsernameParameter());
                String passwd = map.get(getPasswordParameter());
                UsernamePasswordAuthenticationToken authenticationToken = new UsernamePasswordAuthenticationToken(userName, passwd);
                return this.getAuthenticationManager().authenticate(authenticationToken);
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        }

        return super.attemptAuthentication(request, response);
    }
}
```

- 配置Json过滤器

```java
@Bean
public JsonLoginFilter jsonLoginFilter(){
    JsonLoginFilter jsonLoginFilter = new JsonLoginFilter();
    jsonLoginFilter.setAuthenticationManager(authenticationManager());
    jsonLoginFilter.setAuthenticationFailureHandler(new AuthenticationFailureHandler() {
        @Override
        public void onAuthenticationFailure(HttpServletRequest request, HttpServletResponse response, AuthenticationException exception) throws IOException, ServletException {
            Map<String,Object> result = new HashMap<>();
            result.put("code",-1);
            result.put("msg","登录失败");
            result.put("data",exception.getMessage());
            writeResp(result,response);
        }
    });
    jsonLoginFilter.setAuthenticationSuccessHandler(new AuthenticationSuccessHandler() {
                @Override
                public void onAuthenticationSuccess(HttpServletRequest request, HttpServletResponse response, Authentication authentication) throws IOException, ServletException {
                    Map<String,Object> result = new HashMap<>();
                    result.put("code",-1);
                    result.put("msg","登录成功");
                    result.put("data",authentication);
                    writeResp(result,response);
                }
            });
    return jsonLoginFilter;
}
```

- 配置SecurigyFilterChain

```java
@Bean
public SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
    http.authorizeHttpRequests().anyRequest().authenticated()
            .and()
            .addFilterAt(jsonLoginFilter(), UsernamePasswordAuthenticationFilter.class)
            .csrf().disable();
    return http.build();
}
```

### 3.8 使用过滤器方式实现验证码功能

**代码实现**

- 创建验证码过滤器

```java
public class KaptchaFilter extends UsernamePasswordAuthenticationFilter {
    @Override
    public Authentication attemptAuthentication(HttpServletRequest request, HttpServletResponse response) throws AuthenticationException {
        String kaptchaCode = (String) request.getSession().getAttribute("KAPTCHA_CODE");
        String inputKaptcha = request.getParameter("kaptcha");
        if (!StrUtil.equals(kaptchaCode, inputKaptcha)) {
            throw new InternalAuthenticationServiceException("验证码验证失败");
        }
        return super.attemptAuthentication(request, response);
    }
}
```

- 配置验证码过滤器

```java
@Bean
public KaptchaFilter kaptchaFilter(){
    KaptchaFilter kaptchaFilter = new KaptchaFilter();
    kaptchaFilter.setAuthenticationManager(authenticationManager());
    kaptchaFilter.setAuthenticationFailureHandler(new AuthenticationFailureHandler() {
        @Override
        public void onAuthenticationFailure(HttpServletRequest request, HttpServletResponse response, AuthenticationException exception) throws IOException, ServletException {
            Map<String,Object> result = new HashMap<>();
            result.put("code",-1);
            result.put("msg","登录失败");
            result.put("data",exception.getMessage());
            writeResp(result,response);
        }
    });
    kaptchaFilter.setAuthenticationSuccessHandler(new AuthenticationSuccessHandler() {
        @Override
        public void onAuthenticationSuccess(HttpServletRequest request, HttpServletResponse response, Authentication authentication) throws IOException, ServletException {
            Map<String,Object> result = new HashMap<>();
            result.put("code",-1);
            result.put("msg","登录成功");
            result.put("data",authentication);
            writeResp(result,response);
        }
    });
    return kaptchaFilter;
}
```

- 配置SecurityFilterChain

```java
@Bean
public SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
    http.authorizeHttpRequests((auth) ->{
        try {
            auth.antMatchers("/kaptcha").permitAll()
                    .anyRequest().authenticated()
                    .and().formLogin()
                    .loginPage("/login.html")
                    .loginProcessingUrl("/login")
                    .failureForwardUrl("/login.html")
                    .permitAll()
                    .and()
                    .addFilterAt(kaptchaFilter(), UsernamePasswordAuthenticationFilter.class)
                    .csrf().disable();
        }
        catch (Exception e){
        }
    });
    return http.build();
}
```



### 3.9 PasswordEncoder介绍

**主要方法**

- String encode(CharSequence rawPassword)：密码加密
- boolean matches(CharSequence rawPassword, String encodedPassword)：密码匹配
- boolean upgradeEncoding(String encodedPassword): 升级密码，使用新规则来更新旧密码规则

**主要实现**

- DelegatingPasswordEncoder 加密代理 默认的PassworderEncoder实例
- BCryptPasswordEncoder DelegatingPasswordEncoder 中默认的加密方式
- NoOpPasswordEncoder 不加密
- LazyPasswordEncoder 需要用的时候才初始化
- MessageDigestPasswordEncoder
- Md4PasswordEncoder

**默认PasswordEncoder**

```java
public static PasswordEncoder createDelegatingPasswordEncoder() {
  String encodingId = "bcrypt";
  Map<String, PasswordEncoder> encoders = new HashMap<>();
  encoders.put(encodingId, new BCryptPasswordEncoder());
  encoders.put("ldap", new org.springframework.security.crypto.password.LdapShaPasswordEncoder());
  encoders.put("MD4", new org.springframework.security.crypto.password.Md4PasswordEncoder());
  encoders.put("MD5", new org.springframework.security.crypto.password.MessageDigestPasswordEncoder("MD5"));
  encoders.put("noop", org.springframework.security.crypto.password.NoOpPasswordEncoder.getInstance());
  encoders.put("pbkdf2", new Pbkdf2PasswordEncoder());
  encoders.put("scrypt", new SCryptPasswordEncoder());
  encoders.put("SHA-1", new org.springframework.security.crypto.password.MessageDigestPasswordEncoder("SHA-1"));
  encoders.put("SHA-256",
    new org.springframework.security.crypto.password.MessageDigestPasswordEncoder("SHA-256"));
  encoders.put("sha256", new org.springframework.security.crypto.password.StandardPasswordEncoder());
  encoders.put("argon2", new Argon2PasswordEncoder());
  return new DelegatingPasswordEncoder(encodingId, encoders);
 }
```

**识别密码类型核心逻辑**

```java
public boolean matches(CharSequence rawPassword, String prefixEncodedPassword) {
  if (rawPassword == null && prefixEncodedPassword == null) {
   return true;
  }
  String id = extractId(prefixEncodedPassword);
  PasswordEncoder delegate = this.idToPasswordEncoder.get(id);
  if (delegate == null) {
   return this.defaultPasswordEncoderForMatches.matches(rawPassword, prefixEncodedPassword);
  }
  String encodedPassword = extractEncodedPassword(prefixEncodedPassword);
  return delegate.matches(rawPassword, encodedPassword);
 }
```

主要逻辑

- 如果密码为空，则返回true
- 解析密码ID->{xxxx}
- 根据ID从map中获取PassworderEncoder
- 如果获取不到PassworderEncoder: {xxxx}为空或者不是合法的值，则跑出异常
- 如果获取到，则使用对应的PasswordEncoder进行密码匹配



**验证默认的PassworderEncoder实例**

```java
public static void main(String[] args) {
    System.out.println("{pbkdf2}"+new Pbkdf2PasswordEncoder().encode("123456"));
    System.out.println("{bcrypt}"+new BCryptPasswordEncoder().encode("123456"));
}
```

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/08c81ca88e5988e9ccd7ba6b0a00a4d8.png)



**基于内存模式添加用户**

```java
@Bean
 public UserDetailsService userDetailsService(){
     UserDetails noop = User.withUsername("noop").password("{noop}123456").roles("admin").build();
     UserDetails bcypt = User.withUsername("bcrypt").password("{bcrypt}$2a$10$MI6ueeZD8uhAbCy1SH2FSuTxkARMc2x6Lzw.x4ax0ybpoXJLIrl8u").roles("admin").build();
     UserDetails pbkdf2 = User.withUsername("pbkdf2").password("{pbkdf2}ac487cc5d0df83aa3f4d130b1c94063feb6facfc597266175384b78eb432c382fe3aef332ffaff34").roles("admin").build();
     return new InMemoryUserDetailsManager(noop,bcypt,pbkdf2);
 }
```



**指定PasswordEncoder**

- 注入Bean

```java
@Bean
public PasswordEncoder passwordEncoder(){
    return new BCryptPasswordEncoder();
}
```

- 验证登录

还是基于上面的配置，使用：noop/123456 bcrypt/123456 pbkdf2/123456 发现全部登录失败，为什么呢

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/dd929731326ab43aba31a51ac3d95f05.png)

因为我们现在指定了PasswordEncoder=BcryptPasswordEncoder,替代了默认的DelegatingPasswordEncoder，所以我们只需要将密码前缀{xxx}去掉就行，但是使用其他加密方式:pbkdf2/123456 和 noop/123456 还是登录不上，因为你使用的是BcryptPasswordEncoder进行密码匹配，所以需要更新密码。

```java
@Bean
public UserDetailsService userDetailsService(){
    UserDetails noop = User.withUsername("noop").password("{noop}123456").roles("admin").build();
    UserDetails bcypt = User.withUsername("bcrypt").password("$2a$10$MI6ueeZD8uhAbCy1SH2FSuTxkARMc2x6Lzw.x4ax0ybpoXJLIrl8u").roles("admin").build();
    UserDetails pbkdf2 = User.withUsername("pbkdf2").password("{pbkdf2}ac487cc5d0df83aa3f4d130b1c94063feb6facfc597266175384b78eb432c382fe3aef332ffaff34").roles("admin").build();
    return new InMemoryUserDetailsManager(noop,bcypt,pbkdf2);
}
```



### 3.10 记住我功能

其实想要开启rememberMe功能，其实很简单，只需要简单的修改下配置即可：

```java
@Bean
public SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
    http.authorizeHttpRequests().anyRequest().authenticated()
            .and()
            .formLogin()
            .permitAll()
            .and()
            .rememberMe() // 开启rememberMe
            .and()
            .csrf().disable();
    return http.build();
}
```

实现思路

- 当用户登录网站后，并且勾选rememberMe
- 服务端认证通过，则把用户信息进行算法加密，加密完成后，通过cookie，让浏览器把cookie保存在本地
- 当浏览器关闭后重新打开网站，浏览器会把cookie带给服务端
- 服务端校验cookie确定用户身份，进而自动登录



## 4. 进阶

### 4.1 并发会话控制

```java
@Configuration
public class SecurityConfig {
    @Bean
    public SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        http.authorizeHttpRequests()
                .anyRequest().authenticated()
                .and()
                .formLogin()
                .permitAll()
                .and()
                .sessionManagement()
                .maximumSessions(1); // 控制最大会话数为1
        return http.build();
    }
}
```

在两个浏览器登录的效果

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/bbe31a9c55364d523d1c238854fdcc38.png)



限制登录

```java
@Configuration
public class SecurityConfig {
    @Bean
    public SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        http.authorizeHttpRequests()
                .anyRequest().authenticated()
                .and()
                .formLogin()
                .permitAll()
                .and()
                .sessionManagement()
                .maximumSessions(1)
                .maxSessionsPreventsLogin(true); // 超出登录登录数量将不被允许
        return http.build();
    }
}
```



![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/7b586f45f9a2a6a577a45ef816170aa1.png)



### 4.2 session共享解决方案

前面所有的会话都是基于单机，如果服务部署在集群中，就会出现session失效的问题，为什么在集群环境下会出现session失效呢？

**集群环境下session失效的原因**

当用户第一次访问项目时，是机器1处理了登录请求，然后将session信息保存在机器1的内存中，登陆之后，用户再次访问，由于负载均衡，用户被路由到了机器2，但是机器2没有保存用户登陆的session信息，所以会引导用户到登陆页面，进行登陆操作，这就是session失效。

**搭建两个服务**

创建一个项目，开启security，配置一个controller

```
@RestController
public class IndexController {
    @Value("${server.port}")
    public Integer port;
    @RequestMapping("/")
    public String index(Authentication authentication){
        return "hello"+authentication.getName()+",i`m port:"+port;
    }
}
```

分别打成两个jar包，启动端口分别为8080和8081

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/d8c4bbd4959ad4f02846483754b9a1fa.png)

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/67b944fa0b617b0bff3d252637e05ed2.png)

**安装nginx**

我这边安装的有可视化界面的nginx WebUi，docker安装

```
docker run -itd --restart=always --name=nginxWebUI -v /home/nginxWebUI:/home/nginxWebUI -e BOOT_OPTIONS="--server.port=8083" --privileged=true --net=host  cym1102/nginxwebui:latest /bin/bash
```

**访问nginx 页面**

浏览器输入 http://192.168.64.2:8083

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/b08fc2d5316d703ccdea8694166afd5d.png)

**配置负载均衡**

使用IP Hash策略，权重分别为10和1

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/1dc3ccdf6585acc8201bdff9a866ee27.png)

**配置反向代理**

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/36de679ce24080330cd2fcba9104b505.png)

**启用配置**

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/18fa27c963cfbbedfd64364d8117a5e7.png)

**访问服务地址**

http://192.168.64.2 输入用户名和密码：user/123456

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/ca181a73c5cc802905781ae3a14c41b9.png)

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/c2c0369511b7330ed994b8f478cbe681.png)

登陆成功，当前是8080机器响应，成功登陆到8080机器 我们刚才配置的权重是8080=10，8081=1，我们可以验证我们刷新页面10次，是否会跳转到8081机器

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/ff31e784cba6e6dc733b07767988a322.png)

刷到第11次之后，我们跳转到了登录页面，因为8081机器没有保存登录用户的session信息，所以需要登录，这也就是session在集群下，为什么会失效的原因，那么我们看下有哪些解决方案？

**session 失效解决方案**

主要三种

- session复制

- - 多个服务之间相互复制session信息，用户登录任何一机器，生成的session信息都会在其他服务之间保存一份
  - 其实tomcat通过IP组播的方式支持了这种，但是不建议使用，因为随着机器越多，复制的就越多，效率和并发都会相应的降低

- Session 粘滞

- - 即会话保持，始终保证用户在一台机器上，也就不会出现session丢失的问题
  - 但是无法解决并发问题，因为每台机器都维护自己的session，无法进行统一管理

- session 共享

- - 将所有机器产生的session会话放在统一存储空间中，任何机器都能访问
  - 一般可以借助redis或memcached 都可以实现，这节内容主要使用redis完成session共享

**利用spring-session+redis 实现session 共享**

引入spring-session相关依赖

```
    implementation 'org.springframework.boot:spring-boot-starter-data-redis'
    implementation 'org.springframework.session:spring-session-data-redis'
```

配置securityConfig

```
    @Autowired
    private FindByIndexNameSessionRepository sessionRepository;
    @Bean
    public SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        http.authorizeHttpRequests()
                .anyRequest().authenticated()
                .and()
                .formLogin()
                .permitAll().and()
                        .sessionManagement()
                                .maximumSessions(-1)
                                        .sessionRegistry(sessionRegistry());
        http.csrf().disable();
        return http.build();
    }
    @Bean
    public SpringSessionBackedSessionRegistry sessionRegistry(){
        return new SpringSessionBackedSessionRegistry(sessionRepository);
    }
```

配置redis 连接信息

```
server.port=8081
spring.security.user.password=123456
spring.redis.port=6379
spring.redis.host=192.168.64.2
```

重新打两个包：8080，8081

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/1d5eb272302c3a12a72e9d9596698128.png)

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/4ca358dbd406dab2e1c484f62b39edc9.png)

将负载均衡的权重给移除

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/28837e563d31e7573d6b4ab826166acb.png)

访问验证

http://192.168.64.2

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/4e6e8dea6da797b48e2ff01954d3bba7.png)

点击登录，跳转到8081

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/ba4ec569106fcdbd0c05e96b5bf2e655.png)

刷新页面，跳转到8080

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/cc430abf281604deb7e71eb1f4ec3527.png)

再刷新，跳转到8081

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/35be088c5b2913d66a285dac280af1a8.png)

session 共享已经实现，我们再看下redis中存储的数据

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/66809d0cd3cccdc08a0d810fbe01bf9d.png)



### 4.3 spring + spring security跨域问题

#### 4.3.1 跨域问题

**什么是跨域**

> 浏览器不能执行其他网站的脚本，从一个域名的网页去请求另一个域名的资源时，域名、端口、协议任一不同，都是跨域。跨域是由浏览器的同源策略造成的，是浏览器施加的安全限制。a页面想获取b页面资源，如果a、b页面的协议、域名、端口、子域名不同，所进行的访问行动都是跨域的。浏览器不能执行其他网站的脚本，从一个域名的网页去请求另一个域名的资源时，域名、端口、协议任一不同，都是跨域。跨域是由浏览器的同源策略造成的，是浏览器施加的安全限制。a页面想获取b页面资源，如果a、b页面的协议、域名、端口、子域名不同，所进行的访问行动都是跨域的。

**演示**

- 后端接口

```java
@RequestMapping
@RestController
public class IndexController {
    @PostMapping("/cors")
    public String hello() {
        return "hello";
    }
}
```

- 前端页面

```html
<!DOCTYPE html>
<html>
 <head>
  <meta charset="utf-8" />
  <title></title>
  <!-- <script src="https://unpkg.com/vue@next"></script> -->
  <script src="js/v3.2.8/vue.global.prod.js" type="text/javascript" charset="utf-8"></script>
  <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
 </head>
 <body>
  <div id="app">
   <button @click="sendCorsRequest">发起跨域请求</button>
  </div>
  <script>
   const App = {
    data() {
     return {
     }
    },
    methods: {
     sendCorsRequest() {
      axios.post('http://localhost:8080/cors', {
       firstName: 'Fred',
       lastName: 'Flintstone'
      })
      .then(function (response) {
       console.log(response)
      })
      .catch(function (error) {
       console.log(error);
      });
     }
    },
    
   };
   Vue.createApp(App).mount('#app');
  </script>
 </body>
</html>
```

- 发送跨域请求

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/60aa247a60c8563dace489e57d67043f.png)



#### 4.3.2 Spring解决跨域

**Cors注解**

- 标注在方法上

```java
@RequestMapping
@RestController
public class IndexController {
    @RequestMapping("/cors")
    @CrossOrigin("http://127.0.0.1:8848")
    public String hello() {
        return "hello";
    }
}
```

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/bec98563026cd3d90c45f6028b2e7159.png)

- 标注在类上

```java
@RequestMapping
@RestController
@CrossOrigin("http://127.0.0.1:8848")
public class IndexController {
    @RequestMapping("/cors")
    public String hello() {
        return "hello";
    }
}
```

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/82bf6d120645be06defb54b4533b1d23.png)

**配置 CorsRegistry**

```java
@Configuration
public class WebMVCConfig implements WebMvcConfigurer {
    @Override
    public void addCorsMappings(CorsRegistry registry) {
        registry.addMapping("/cors")
                .allowCredentials(false)
                .allowedHeaders("*")
                .allowedMethods("POST")
                .allowedOrigins("*");
    }
}
```

**Cors 过滤器**

```java
@Configuration
public class WebMvcFilterConfig {
    @Bean
    FilterRegistrationBean<CorsFilter> cors(){
        FilterRegistrationBean<CorsFilter> registrationBean = new FilterRegistrationBean<>();
        CorsConfiguration configuration = new CorsConfiguration();
        configuration.addAllowedHeader("*");
        configuration.addAllowedMethod("*");
        configuration.addAllowedOrigin("*");
        configuration.addExposedHeader("*");
        UrlBasedCorsConfigurationSource source = new UrlBasedCorsConfigurationSource();
        source.registerCorsConfiguration("/**",configuration);
        registrationBean.setFilter(new CorsFilter(source));
        return registrationBean;
    }
}
```



### 4.4 自定义异常处理器

在Spring Security中异常分为两种：

- AuthenticationException 认证异常
- AccessDeniedException 权限异常 

**自定义异常处理器**

- 配置SecurityConfig

```java
@Bean
public SecurityFilterChain config(HttpSecurity http) throws Exception {
    http.authorizeHttpRequests()
            .anyRequest().authenticated()
            .and()
            .formLogin()
            .loginPage("/login.html")
            .loginProcessingUrl("/login")
            .permitAll()
            .and()
            .cors()
            .configurationSource(corsConfigurationSource())
            .and()
            .exceptionHandling()
            .authenticationEntryPoint(new AuthenticationEntryPoint() {
                @Override
                public void commence(HttpServletRequest request, HttpServletResponse response, AuthenticationException authException) throws IOException, ServletException {
                    Map<String, Object> result = new HashMap<>();
                    result.put("code", -1);
                    result.put("msg", "authenticationEntryPoint");
                    result.put("data", authException.getMessage());
                    System.out.println("调用次数");
                    writeResp(result, response);
                }
            }).accessDeniedHandler(new AccessDeniedHandler() {
                @Override
                public void handle(HttpServletRequest request, HttpServletResponse response, AccessDeniedException accessDeniedException) throws IOException, ServletException {
                    Map<String, Object> result = new HashMap<>();
                    result.put("code", -1);
                    result.put("msg", "accessDeniedHandler");
                    result.put("data", accessDeniedException.getMessage());
                    writeResp(result, response);
                }
            })
            .and()
            .csrf().disable();
    http.headers().cacheControl();
    return http.build();
}
```



### 4.5 方法权限注解,权限表达式

**注解介绍**

- @PostAuthorize:在目标方法执行之后进行权限校验
- @PostFilter：在目标方法执行之后对方法的返回结果进行过滤
- @PreAuthorize：在目标方法执行之前进行权限校验。
- @PreFilter：在目标方法执行之前对方法参数进行过滤。
- @Secured：访问目标方法必须具备相应的角色
- @DenyAll：拒绝所有访问
- @PermitAll: 允许所有访问
- @RolesAlowed:访问目标方法必须具有的角色

**权限表达式**

- hasRole(role):当前用户是否具备指定角色
- hasAnyRole(role ...):当前用户是否具备指定角色中的任意一个
- hasAuthority(authority):当前用户是否具备指定的权限
- hasAnyAuthority(authority ...):当前用户是否具备指定的权限任意一个
- principal:当前登录主体
- authentication:context中authentication对象
- permitAll():允许所有请求
- denyAll():拒绝所有请求
- isAnonymous():当前用户是否是一个匿名用户

**权限注解用法**

```java
@Service
public class UserService {
    @PreAuthorize("hasRole('ADMIN')")
    public String hello() {
        return "hello";
    }
    @PreAuthorize("hasRole('ADMIN') and authentication.name=='lglbc'")
    public String hello2() {
        return "hello";
    }
    @PreAuthorize("hasRole('ADMIN') and authentication.name==#name")
    public String hello3(String name) {
        return "hello";
    }

    @PreFilter(value = "filterObject.id%2!=0",filterTarget = "users")
    public void addUsers(List<User> users, Integer other) {
        System.out.println("users = " + JSON.toJSONString(users));
    }
    @PostFilter("filterObject.id%2==0")
    public List<User> getAll() {
        List<User> users = new ArrayList<>();
        for (int i = 0; i < 10; i++) {
            users.add(new User(i, "lglbc_:" + i));
        }
        return users;
    }

    @Secured({"ROLE_ADMIN","ROLE_USER"})
    public User getUserByUsername(String username) {
        return new User(99, username);
    }

    @DenyAll
    public String denyAll() {
        return "DenyAll";
    }

    @PermitAll
    public String permitAll() {
        return "PermitAll";
    }
    @RolesAllowed({"ADMIN","USER"})
    public String rolesAllowed() {
        return "RolesAllowed";
    }

}

@SpringBootTest
class Day15ApplicationTests {
    @Autowired
    private UserService userService;

    @Test
    @WithMockUser(roles = "ADMIN")
    void preauthorizeTest01() {
        String result = userService.hello();
        assertNotNull(result);
    }

    @Test
    @WithMockUser(roles = "ADMIN", username = "lglbc")
    void preauthorizeTest02() {
        String result = userService.hello2();
        assertNotNull(result);
    }

    @Test
    @WithMockUser(roles = "ADMIN", username = "lglbc")
    void preauthorizeTest03() {
        String result = userService.hello3("lglbc");
        assertNotNull(result);
    }

    @Test
    @WithMockUser(username = "lglbc")
    void preFilterTest01() {
        List<User> users = new ArrayList<>();
        for (int i = 0; i < 10; i++) {
            users.add(new User(i, "lglbc_:" + i));
        }
        userService.addUsers(users, 99);
    }

    @Test
    @WithMockUser(roles = "ADMIN")
    void postFilterTest01() {
        List<User> all = userService.getAll();
        assertNotNull(all);
        assertEquals(5, all.size());
        assertEquals(2, all.get(1).getId());
    }

    @Test
    @WithMockUser(roles = "ADMIN")
    void securedTest01() {
        User user = userService.getUserByUsername("lglbc");
        assertNotNull(user);
        assertEquals(99, user.getId());
        assertEquals("lglbc", user.getUserName());
    }

    @Test
    @WithMockUser(username = "lglbc")
    void denyAllTest01() {
//        userService.denyAll();
    }

    @Test
    @WithMockUser(username = "lglbc")
    void permitAllTest01() {
        String s = userService.permitAll();
        assertNotNull(s);
        assertEquals("PermitAll", s);
    }

    @Test
    @WithMockUser(roles = "ADMIN")
    void rolesAllowedTest01() {
        String s = userService.rolesAllowed();
        assertNotNull(s);
        assertEquals("RolesAllowed", s);
    }
}
```

**权限表达式用法**

```java
@Service
public class SecurityExpressService {
    @PreAuthorize("@permission.check(#value)")
    public String customPermission(String value){
        return value;
    }
    @PreAuthorize("hasAuthority('ROLE_admin')")
    public String hasAuthority(String value){
        return value;
    }
    @PreAuthorize("hasAnyAuthority('ROLE_admin','ROLE_user')")
    public String hasAnyAuthority(String value){
        return value;
    }
    @PreAuthorize("hasRole('admin')")
    public String hasRole(String value){
        return value;
    }
    @PreAuthorize("hasAnyRole('admin','user')")
    public String hasAnyRole(String value){
        return value;
    }
    @PreAuthorize("principal.username=='lglbc'")
    public String principal(String value){
        return value;
    }
    @PreAuthorize("permitAll()")
    public String permitAll(String value){
        return value;
    }
    @PreAuthorize("denyAll()")
    public String denyAll(String value){
        return value;
    }
}

@SpringBootTest
public class SecurityExpressTest {
    @Autowired
    private SecurityExpressService securityExpressService;
    @Test
    @WithMockUser(roles = "admin")
    public void hasAuthority(){
        securityExpressService.hasAuthority("hello");
    }
    @Test
    @WithMockUser(roles = "admin")
    public void hasAnyAuthority(){
        securityExpressService.hasAnyAuthority("hello");
    }
    @Test
    @WithMockUser(roles = "admin")
    public void hasRole(){
        securityExpressService.hasRole("hello");
    }
    @Test
    @WithMockUser(roles = "user")
    public void hasAnyRole(){
        securityExpressService.hasAnyRole("hello");
    }
    @Test
    @WithMockUser(roles = "admin",username = "lglbc")
    public void principal(){
        securityExpressService.principal("hello");
    }
    @Test
    @WithMockUser()
    public void permitAll(){
        securityExpressService.permitAll("hello");
    }
    @Test
    @WithMockUser(roles = "admin")
    public void denyAll(){
        securityExpressService.denyAll("hello");
    }
    @Test
    @WithMockUser(roles = "admin")
    public void customPermission(){
        securityExpressService.customPermission("lglbc");
    }
}
```



### 4.6 OAuth2

#### 4.6.1 OAuth2介绍

OAuth 2.0 是一种用于授权的开放标准，允许用户授权第三方应用程序访问他们的资源，例如照片、视频或其他个人信息。OAuth 2.0 提供了一些不同的授权模式，包括授权码模式、简化模式、密码模式和客户端模式等。这些授权模式允许客户端应用程序在不要求用户提供其密码或其他敏感信息的情况下，安全地访问受保护资源。

OAuth 2.0 的核心思想是将认证和授权分离开来，允许用户授权一个应用程序代表他们执行某些操作。OAuth 2.0 框架中的主要角色包括：

用户：资源的所有者，可以授权应用程序访问他们的资源。客户端：请求访问资源的应用程序。授权服务器：处理 OAuth 2.0 协议，负责验证用户身份并生成访问令牌。资源服务器：存储受保护的资源，并根据授权服务器颁发的访问令牌控制对这些资源的访问。OAuth 2.0 在互联网应用程序开发中被广泛使用，大多数社交网络和 API 都支持该协议。它允许开发人员构建安全的应用程序，用户可以控制对其资源的访问权限。



#### 4.6.2 OAuth2的四种模式

##### 4.6.2.1 授权码模式（Authorization Code Grant）

**什么是授权码模式**

授权码模式是 OAuth 2.0 的标准授权方式，常用于服务端应用程序，也适用于移动应用程序。该模式通过授权服务器为客户端生成一个授权码，在授权码的基础上请求访问令牌。

**授权流程**

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/d8a94161ba69d59215c6f32abfd7c503.png)

- 客户端向用户展示认证页面。
- 用户输入用户名和密码，向授权服务器发送请求。
- 授权服务器验证用户信息，如果验证成功，生成授权码。
- 授权服务器返回授权码给客户端。
- 客户端使用授权码向授权服务器请求令牌。
- 授权服务器验证授权码的有效性，如果有效则返回令牌。



##### 4.6.2.2 简化模式（Implicit Grant）

**什么是简化模式**

简化模式主要用于移动应用程序和 Web 前端应用程序等场景下。该模式省略了授权码这一步骤，直接通过浏览器在客户端和授权服务器之间进行交互。

**授权流程**

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/185753749abe16b172bf4003ef1dc61f.png)

- 客户端向授权服务器发送认证请求。
- 授权服务器验证用户身份，如果验证成功则向浏览器返回令牌。
- 浏览器将令牌传递给客户端。



##### 4.6.2.3 密码模式（Resource Owner Password Credentials Grant）

**什么是密码模式**

密码模式是一种简单的授权方式，主要用于受信任的客户端应用程序。该模式要求用户将自己的用户名和密码直接提供给客户端应用程序，客户端应用程序使用这些凭证向授权服务器请求访问令牌。

**授权流程**

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/693d2902f37b76109cca4a6f1e82ba67.png)

- 用户向客户端提供用户名和密码。
- 客户端向授权服务器发送包含用户凭证的请求。
- 授权服务器验证用户凭证，如果验证成功则返回令牌。

##### 4.6.2.4 客户端模式（Client Credentials Grant）

**什么是客户端模式**

客户端模式适用于后台服务与其他服务进行通信的场景。该模式下，客户端应用程序通过自身的身份向授权服务器请求访问令牌，并使用该令牌访问资源服务器。

**授权流程**

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/2528d2a3222eb71734a4e2f0eb220f42.png)

- 客户端向授权服务器发送包含自身身份信息的请求，包括客户端 ID 和密钥。
- 授权服务器验证客户端身份，如果验证成功则返回令牌。
- 客户端使用令牌向资源服务器请求访问资源。

