## 1. 项目简介

项目实现了登录，管理成员，上传文件，修改密码信息等功能，类似低配版[若依管理系统](https://gitee.com/y_project/RuoYi-Vue)

项目使用到了`swagger`作为前端接口文档，访问`http:/localhost:8080/swagger-ui.html`

项目已上传至[github](https://github.com/pepedd864/smart_campus)

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/e1a68eacc0e11b3aa91b2b4c4984ecf8.png)

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/f6edc321385a9047bd7cee144a7968b0.png)

## 2. 结构

项目使用的是单模块+三层架构（持久层、服务层、表现层）设计，比较简单

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/9f3c4f10de434a0cf9c61805b971e70e.png)

spingboot 版本为`2.5.14`

项目依赖如下

```xml
<!-- 阿里数据库连接池 -->
<dependency>
    <groupId>com.alibaba</groupId>
    <artifactId>druid-spring-boot-starter</artifactId>
    <version>1.2.16</version>
</dependency>
<dependency>
    <groupId>com.baomidou</groupId>
    <artifactId>mybatis-plus-boot-starter</artifactId>
    <version>3.4.1</version>
</dependency>
<dependency>
    <groupId>com.mysql</groupId>
    <artifactId>mysql-connector-j</artifactId>
    <version>8.0.32</version>
    <scope>runtime</scope>
</dependency>

<dependency>
    <groupId>javax.xml.bind</groupId>
    <artifactId>jaxb-api</artifactId>
    <version>2.3.1</version>
</dependency>

<!--mybatis-plus的代码生成器 -->
<dependency>
    <groupId>com.baomidou</groupId>
    <artifactId>mybatis-plus-generator</artifactId>
    <version>3.5.2</version>
</dependency>
<dependency>
    <groupId>org.freemarker</groupId>
    <artifactId>freemarker</artifactId>
    <version>2.3.31</version>
</dependency>

<!--前后端接口框架:swagger-->
<dependency>
    <groupId>io.springfox</groupId>
    <artifactId>springfox-swagger2</artifactId>
    <version>2.7.0</version>
</dependency>
<!--swagger ui-->
<dependency>
    <groupId>io.springfox</groupId>
    <artifactId>springfox-swagger-ui</artifactId>
    <version>2.7.0</version>
</dependency>
<!--swagger2  增强版接口文档-->
<dependency>
    <groupId>com.github.xiaoymin</groupId>
    <artifactId>knife4j-spring-boot-starter</artifactId>
    <version>2.0.4</version>
</dependency>

<dependency>
    <groupId>com.alibaba</groupId>
    <artifactId>fastjson</artifactId>
    <version>1.2.29</version>
</dependency>

<!-- JWT生成Token-->
<dependency>
    <groupId>io.jsonwebtoken</groupId>
    <artifactId>jjwt</artifactId>
    <version>0.7.0</version>
</dependency>

<!-- 文件上传依赖 -->
<dependency>
    <groupId>commons-fileupload</groupId>
    <artifactId>commons-fileupload</artifactId>
    <version>1.4</version>
</dependency>

<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-configuration-processor</artifactId>
    <optional>true</optional>
</dependency>
<dependency>
    <groupId>org.projectlombok</groupId>
    <artifactId>lombok</artifactId>
    <optional>true</optional>
</dependency>
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-test</artifactId>
    <scope>test</scope>
</dependency>
```

## 3. 使用MyBatisPlus代码生成器

使用MyBatisPlus代码生成器，快速生成`domain`、`mapper`、`service`代码

### 3.1 依赖坐标

```xml
<!--mybatis-plus的代码生成器 -->
<dependency>
    <groupId>com.baomidou</groupId>
    <artifactId>mybatis-plus-generator</artifactId>
    <version>3.5.2</version>
</dependency>
<dependency>
    <groupId>org.freemarker</groupId>
    <artifactId>freemarker</artifactId>
    <version>2.3.31</version>
</dependency>
```

### 3.2 快速生成代码

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/eadb237b1784107f0fe3ad3d002b01b7.png)

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/f61ba684a7c36578c2c07800b900055a.png)

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/e79562671d3dfba03836eace33384d80.png)

### 3.3 检查生成的代码

需要注意`pojo`的主键唯一，否则会报错

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/6c9e1a589ff800f5aed7e025d6513d67.png)



### 3.4 配置分页插件

```java
@Configuration
@MapperScan("com.demo.modules_campus.mapper")
public class MybatisPlusConfig {
  /***
   * 分页插件
   * @return
   */
  @Bean
  public MybatisPlusInterceptor mybatisPlusInterceptor() {
    MybatisPlusInterceptor mybatisPlusInterceptor = new MybatisPlusInterceptor();
    mybatisPlusInterceptor.addInnerInterceptor(new PaginationInnerInterceptor(DbType.MYSQL));
    return mybatisPlusInterceptor;
  }
}
```



## 4. 登录功能

登录接口创建在`SystemController`下，前后端使用`session`传递信息

依赖

```xml
<dependency>
    <groupId>javax.xml.bind</groupId>
    <artifactId>jaxb-api</artifactId>
    <version>2.3.1</version>
</dependency>
```

### 4.1 获取验证码

验证码接口为`http://localhost:8080/sms/system/getVerifiCodeImage`，方式为`GET`请求

```java
/***
 * 获取验证码图片,返回给浏览器
 * @param session session
 * @param response response
 * @throws IOException IOException
 */
@RequestMapping("/getVerifiCodeImage")
public void getVerifiCodeImage(HttpSession session, HttpServletResponse response) throws IOException {
  // 获取验证码图片
  BufferedImage verifiCodeImage = CreateVerifiCodeImage.getVerifiCodeImage();
  // 获取验证码图片中的值
  String verifiCode = new String(CreateVerifiCodeImage.getVerifiCode());
  // 将验证码中的值保存到session中 用于登录时校验
  session.setAttribute("code", verifiCode);
  // 将验证码图片响应给客户端
  ImageIO.write(verifiCodeImage, "jpg", response.getOutputStream());
}
```

1. 获取验证码图片，方法在`utils/CreateVerifiCodeImage.java`下
2. 用`session`保存验证码的值
3. 将验证码响应给客户端

### 4.2 对登录信息进行校验

登录接口为`http://localhost:8080/sms/system/login`，方式为`POST`请求

```java
/***
 * 登录 进行验证码的校验 以及用户名密码的校验
 * 登录成功时生成的token返回给客户端
 * @param loginForm 生成的登录表单
 * @param session session
 * @return return
 */
@PostMapping("/login")
public Result<Object> login(@RequestBody LoginForm loginForm, HttpSession session) {
  // 获取验证码
  String code = (String) session.getAttribute("code");
  // 判断是否失效
  if (code == null || "".equals(code)) {
    return Result.fail().message("验证码失效,请重新获取");
  }
  // 获取用户输入的验证码
  String userInputCode = loginForm.getVerifiCode();
  // 判断验证码是否正确
  if (!code.equalsIgnoreCase(userInputCode)) {
    // 销毁session中的验证码
    session.removeAttribute("code");
    return Result.fail().message("验证码错误");
  }
  // 销毁session中的验证码
  session.removeAttribute("code");
  // 判断用户类型
  Integer userType = loginForm.getUserType();
  // 获取用户输入的用户名和密码
  String username = loginForm.getUsername();
  String password = MD5.encrypt(loginForm.getPassword());
  Map<String, Object> map = new LinkedHashMap<>();

  if (userType == 1) {
    Admin admin = adminService.selectAdminByUsernameAndPassword(username, password);
    if (admin != null) {
      // 登录成功后需要根据用户id和用户类型生成Token
      String token = JwtHelper.createToken(admin.getId().longValue(), userType);
      map.put("token", token);
      return Result.ok(map);
    }
    return Result.fail().message("用户名或密码错误");
  } else if (userType == 2) {
    Student student = studentService.selectAdminByUsernameAndPassword(username, password);
    if (student != null) {
      String token = JwtHelper.createToken(student.getId().longValue(), userType);
      map.put("token", token);
      return Result.ok(map);
    }
    return Result.fail().message("用户名或密码错误");
  } else if (userType == 3) {
    Teacher teacher = teacherService.selectAdminByUsernameAndPassword(username, password);
    if (teacher != null) {
      String token = JwtHelper.createToken(teacher.getId().longValue(), userType);
      map.put("token", token);
      return Result.ok(map);
    }
    return Result.fail().message("用户名或密码错误");
  }
  return null;
}
```

1. 获取存在`session`中的验证码和请求体中用户输入的验证码
2. 判断`session`是否过期（过期时`code`为空），然后校验验证码
3. 销毁`session`中的验证码
4. 验证用户名和密码（密码使用了`MD5`加密存储，方法在`utils/MD5.java`下）
5. 登录成功根据用户类型生成对应的`token`（`JwtToken`方法在`utils/JwtHelper.java`下）
6. 返回用户信息

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/6a4b8deb18006b390d2f9b61d2ed24aa.png)

### 4.3 获取用户信息

接口`http://localhost:8080/sms/system/getInfo`，方式`GET`

```java
/***
 * 根据token获取用户信息
 * @param token
 * @return
 */

@GetMapping("/getInfo")
public Result<Object> getInfo(@RequestHeader("token") String token) {
  // 先判断token是否有效
  if (JwtHelper.isExpiration(token)) {
    return Result.build(null, ResultCodeEnum.CODE_ERROR);
  }
  // 解析token 获取用户id和用户类型 返回给浏览器
  Long userId = JwtHelper.getUserId(token);
  Integer userType = JwtHelper.getUserType(token);
  Map<String, Object> map = new LinkedHashMap<>();
  map.put("userType", userType);
  if (userType == 1) {
    Admin admin = adminService.selectAdminById(userId);
    map.put("user", admin);
  } else if (userType == 2) {
    Student student = studentService.selectStudentById(userId);
    map.put("user", student);
  } else if (userType == 3) {
    Teacher teacher = teacherService.selectTeacherById(userId);
    map.put("user", teacher);
  }
  return Result.ok(map);
}
```

1. 从请求头中获取`token`，判断是否有效
2. 解析`token`，获取用户id和用户类型
3. 调用服务层方法，获取用户信息，返回浏览器

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/95fb598550012ef9d54f06bb29de0eb4.png)

## 5. 管理

### 5.1 年级管理

根据前端的接口完成接口实现即可

```java
@Api(tags = "年级管理")
@RestController
@RequestMapping("/sms/gradeController")
public class GradeController {

  @Resource
  private GradeService gradeService;

  /***
   * 获取年级列表
   * @param pn  当前页码
   * @param size  每页显示的条数
   * @param gradeName 年级名称
   * @return Page 对象
   */
  @ApiOperation(value = "获取年级列表", notes = "获取年级列表")
  @RequestMapping("/getGrades/{pn}/{size}")
  public Result<Object> getGrades(@ApiParam("当前页码") @PathVariable("pn") Integer pn,
                                  @ApiParam("页码大小") @PathVariable("size") Integer size,
                                  @ApiParam("模糊查询条件") String gradeName) {
    Page<Grade> page = gradeService.page(new Page<>(pn, size), new LambdaQueryWrapper<Grade>()
        .like(StrUtil.isNotBlank(gradeName), Grade::getName, gradeName).orderByAsc(Grade::getId));
    return Result.ok(page);
  }

  /***
   * 单条删除和批量删除
   * @param ids 请求体中待删除的年级集合
   * @return 返回结果
   */

  @DeleteMapping("/deleteGrade")
  public Result<Object> deleteGrade(@RequestBody List<Integer> ids) {
    // 长度为1时删除单条
    if (ids.size() == 1)
      gradeService.removeById(ids.get(0));
    else
      gradeService.removeByIds(ids);
    return Result.ok();
  }

  /***
   * 添加或修改年级
   * @param grade 请求体中的年级对象
   * @return 返回结果
   */

  @PostMapping("/saveOrUpdateGrade")
  public Result<Object> saveOrUpdateGrade(@RequestBody Grade grade) {
    // 判断请求体中是否有id
    if (grade.getId() == null)
      gradeService.save(grade);
    else
      gradeService.updateById(grade);

    return Result.ok();
  }

  /***
   * 获取所有年级名称
   * @return
   */

  @GetMapping("/getGrades")
  public Result<Object> getGrades() {
    List<Grade> grades = gradeService.list();
    return Result.ok(grades);
  }

}
```

### 5.2 班级管理

```java
@Api(tags = "班级管理")
@RestController
@RequestMapping("/sms/clazzController")
public class ClazzsController {

  @Resource
  private ClazzService clazzService;
  @Resource
  private GradeService gradeService;

  /***
   * 获取班级列表
   * @param pn  当前页码
   * @param size  每页显示的条数
   * @param clazzName 班级名称
   * @return Page 对象
   */
  @ApiOperation(value = "获取班级列表", notes = "获取班级列表")
  @RequestMapping("/getClazzsByOpr/{pn}/{size}")
  public Result<Object> getGrades(@ApiParam("当前页码") @PathVariable("pn") Integer pn,
                                  @ApiParam("页码大小") @PathVariable("size") Integer size,
                                  @ApiParam("模糊查询条件") String clazzName) {
    Page<Clazz> page = clazzService.page(new Page<>(pn, size), new LambdaQueryWrapper<Clazz>()
        .like(StrUtil.isNotBlank(clazzName), Clazz::getName, clazzName).orderByAsc(Clazz::getId));
    return Result.ok(page);
  }

  /***
   * 单条删除和批量删除
   * @param ids 请求体中待删除的班级集合
   * @return 返回结果
   */

  @DeleteMapping("/deleteGrade")
  public Result<Object> deleteGrade(@RequestBody List<Integer> ids) {
    // 长度为1时删除单条
    if (ids.size() == 1)
      clazzService.removeById(ids.get(0));
    else
      clazzService.removeByIds(ids);
    return Result.ok();
  }

  /***
   * 添加或修改班级
   * @param clazz 请求体中的班级对象
   * @return 返回结果
   */

  @PostMapping("/saveOrUpdateGrade")
  public Result<Object> saveOrUpdateGrade(@RequestBody Clazz clazz) {
    // 判断请求体中是否有id
    if (clazz.getId() == null)
      clazzService.save(clazz);
    else
      clazzService.updateById(clazz);

    return Result.ok();
  }

  /***
   * 获取所有班级名称
   * @return
   */

  @GetMapping("/getClazzs")
  public Result<Object> getClazzs() {
    List<Clazz> clazzs = clazzService.list();
    return Result.ok(clazzs);
  }

}
```

### 5.3 教师管理

```java
@Api(tags = "教师管理")
@RestController
@RequestMapping("/sms/teacherController")
public class TeacherController {

  @Resource
  private TeacherService teacherService;
  @Resource
  private GradeService gradeService;

  /***
   * 获取班级列表
   * @param pn  当前页码
   * @param size  每页显示的条数
   * @param teacherName 班级名称
   * @return Page 对象
   */
  @ApiOperation(value = "获取班级列表", notes = "获取班级列表")
  @RequestMapping("/getTeachers/{pn}/{size}")
  public Result<Object> getGrades(@ApiParam("当前页码") @PathVariable("pn") Integer pn,
                                  @ApiParam("页码大小") @PathVariable("size") Integer size,
                                  @ApiParam("模糊查询条件") String teacherName) {
    Page<Teacher> page = teacherService.page(new Page<>(pn, size), new LambdaQueryWrapper<Teacher>()
        .like(StrUtil.isNotBlank(teacherName), Teacher::getName, teacherName).orderByAsc(Teacher::getId));
    return Result.ok(page);
  }

  /***
   * 单条删除和批量删除
   * @param ids 请求体中待删除的班级集合
   * @return 返回结果
   */

  @DeleteMapping("/deleteTeacher")
  public Result<Object> deleteGrade(@RequestBody List<Integer> ids) {
    // 长度为1时删除单条
    if (ids.size() == 1)
      teacherService.removeById(ids.get(0));
    else
      teacherService.removeByIds(ids);
    return Result.ok();
  }

  /***
   * 添加或修改班级
   * @param teacher 请求体中的班级对象
   * @return 返回结果
   */

  @PostMapping("/saveOrUpdateTeacher")
  public Result<Object> saveOrUpdateGrade(@RequestBody Teacher teacher) {
    // 判断请求体中是否有id
    if (teacher.getId() == null)
      teacherService.save(teacher);
    else
      teacherService.updateById(teacher);

    return Result.ok();
  }

  /***
   * 获取所有教师名称
   * @return
   */

  @GetMapping("/getTeachers")
  public Result<Object> getTeachers() {
    List<Teacher> teachers = teacherService.list();
    return Result.ok(teachers);
  }

}
```

### 5.4 学生管理

### 5.5 管理员管理

## 6. 上传图片

### 6.1 依赖坐标

```xml
<!-- 文件上传依赖 -->
<dependency>
    <groupId>commons-fileupload</groupId>
    <artifactId>commons-fileupload</artifactId>
    <version>1.4</version>
</dependency>
```

### 6.2 实现接口

```java
/***
 * 上传图片
 * @param multipartFile 图片
 * @return 图片的相对路径
 * @throws IOException  IOException
 */
@PostMapping("/headerImgUpload")
public Result<Object> headerImgUpload(@RequestPart("multipartFile") MultipartFile multipartFile) throws IOException {
  // 获取文件名
  String originalFilename = multipartFile.getOriginalFilename();
  // 断言文件名不为空
  assert originalFilename != null;
  // 获得文件格式
  String suffix = originalFilename.substring(originalFilename.lastIndexOf("."));
  // 为了避免文件名重复,使用uuid作为文件名
  String fileName = UUID.randomUUID() + suffix;
  // 保存路径
  String filePath = "C:/Users/admin/Desktop/workspace/IDEA-Workplace/campus/modules_campus/src/main/resources/static/static/upload/" + fileName;
  // 保存文件
  multipartFile.transferTo(new File(filePath));
  return Result.ok("/upload/".concat(fileName));
}
```

1. 文件上传在`RequestPart`下的`MultipartFile`实现，使用`POST`加上对应参数即可
2. 获取文件后缀，并用`uuid`替代文件名
3. 设置保存路径，这里设置的是本地`static/upload`下
4. 使用`MultipartFile`的导出文件方法加上`java`的新建文件对象，写入文件
5. 返回图片地址

### 6.3 需要重启访问图片的问题

上传图片后，由于图片保存在项目目录下，而前端访问的是后端编译后的资源，故需要重定向到项目目录下才能访问

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/c423516a63e119af0bf64e06845adb3e.png)

---

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/a1fa148b0635fc9329d76859d0b2c18f.png)

### 6.4 解决方法

1. 在`application.yml`中定义资源路径

```yaml
upload:
  file:
    location: C:/Users/admin/Desktop/workspace/IDEA-Workplace/campus/modules_campus/src/main/resources/static/static/upload/
```

2. 创建配置类

```java
@Configuration
public class SpringMvcConfig implements WebMvcConfigurer {
  @Value("${upload.file.location}")
  private String uploadPath;

  /***
   * 配置静态资源映射，解决上传文件后需要重新编译才能访问的问题
   * @param registry
   */

  @Override
  public void addResourceHandlers(ResourceHandlerRegistry registry) {
    if (!registry.hasMappingForPattern("/upload/**")) {
      registry.addResourceHandler("/upload/**").addResourceLocations("file:" + uploadPath);
    }
  }
}
```



## 7. 工具类

`utils`目录下存放了项目主要的工具类

### 7.1 绘制验证码

不依赖其他接口，由后端直接生成，可移植

```java
public class CreateVerifiCodeImage {

  private static int WIDTH = 90;
  private static int HEIGHT = 35;
  //字符大小
  private static int FONT_SIZE = 20;
  //验证码
  private static char[] verifiCode;
  //验证码图片
  private static BufferedImage verifiCodeImage;

  /**
   * @description: 获取验证码图片
   * @param: no
   * @return: java.awt.image.BufferedImage
   */
  public static BufferedImage getVerifiCodeImage() {
    // create a image
    verifiCodeImage = new BufferedImage(WIDTH, HEIGHT, BufferedImage.TYPE_INT_BGR);
    Graphics graphics = verifiCodeImage.getGraphics();

    verifiCode = generateCheckCode();
    drawBackground(graphics);
    drawRands(graphics, verifiCode);

    graphics.dispose();

    return verifiCodeImage;
  }

  /**
   * @description: 获取验证码
   * @param: no
   * @return: char[]
   */
  public static char[] getVerifiCode() {
    return verifiCode;
  }

  /**
   * @description: 随机生成验证码
   * @param: no
   * @return: char[]
   */
  private static char[] generateCheckCode() {
    String chars = "0123456789abcdefghijklmnopqrstuvwxyz" + "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    char[] rands = new char[4];
    for (int i = 0; i < 4; i++) {
      int rand = (int) (Math.random() * (10 + 26 * 2));
      rands[i] = chars.charAt(rand);
    }
    return rands;
  }

  /**
   * @description: 绘制验证码
   * @param: g
   * @param: rands
   * @return: void
   */
  private static void drawRands(Graphics g, char[] rands) {
    g.setFont(new Font("Console", Font.BOLD, FONT_SIZE));

    for (int i = 0; i < rands.length; i++) {

      g.setColor(getRandomColor());
      g.drawString("" + rands[i], i * FONT_SIZE + 10, 25);
    }
  }

  /**
   * @description: 绘制验证码图片背景
   * @param: g
   * @return: void
   */
  private static void drawBackground(Graphics g) {

    g.setColor(Color.white);
    g.fillRect(0, 0, WIDTH, HEIGHT);

    // 绘制验证码干扰点
    for (int i = 0; i < 200; i++) {
      int x = (int) (Math.random() * WIDTH);
      int y = (int) (Math.random() * HEIGHT);
      g.setColor(getRandomColor());
      g.drawOval(x, y, 1, 1);

    }
  }


  /**
   * @description: 获取随机颜色
   * @param: no
   * @return: java.awt.Color
   */
  private static Color getRandomColor() {
    Random ran = new Random();
    return new Color(ran.nextInt(220), ran.nextInt(220), ran.nextInt(220));
  }
}
```

### 7.2 MD5

也是不依赖其他，可移植

```java
public final class MD5 {

  /***
   * MD5加密
   * @param strSrc  要加密的字符串
   * @return  加密后的字符串
   */
  public static String encrypt(String strSrc) {
    try {
      char[] hexChars= { '0', '1', '2', '3', '4', '5', '6', '7', '8',
          '9', 'a', 'b', 'c', 'd', 'e', 'f' };
      byte[] bytes = strSrc.getBytes();
      MessageDigest md = MessageDigest.getInstance("MD5");
      md.update(bytes);
      bytes = md.digest();
      int j = bytes.length;
      char[] chars = new char[j * 2];
      int k = 0;
      for (int i = 0; i < bytes.length; i++) {
        byte b = bytes[i];
        chars[k++] = hexChars[b >>> 4 & 0xf];
        chars[k++] = hexChars[b & 0xf];
      }
      return new String(chars);
    } catch (NoSuchAlgorithmException e) {
      e.printStackTrace();
      throw new RuntimeException("MD5加密出错！！+" + e);
    }
  }
}
```

### 7.3 生成token

依赖

```xml
<!-- JWT生成Token-->
<dependency>
    <groupId>io.jsonwebtoken</groupId>
    <artifactId>jjwt</artifactId>
    <version>0.7.0</version>
</dependency>
```



根据项目的需要编写的对应方法，移植时需要修改部分方法

```java
public class JwtHelper {
  private static long tokenExpiration = 24*60*60*1000;  // token过期时间
  private static String tokenSignKey = "123456";  // token签名密钥

  /***
   * 生成token
   * @param userId  用户id
   * @param userType  用户类型
   * @return  返回token
   */
  public static String createToken(Long userId, Integer userType) {
    String token = Jwts.builder()
        // 设置头信息
        .setSubject("YYGH-USER")
        // 设置过期时间
        .setExpiration(new Date(System.currentTimeMillis() + tokenExpiration))
        // 设置token主体部分，存储用户信息
        .claim("userId", userId)
//                .claim("userName", userName)
        .claim("userType", userType)
        // 设置签名密钥
        .signWith(SignatureAlgorithm.HS512, tokenSignKey)
        .compressWith(CompressionCodecs.GZIP)
        .compact();
    return token;
  }

  /***
   * 从token中获取用户id
   * @param token token字符串
   * @return  返回用户id
   */

  public static Long getUserId(String token) {
    if(StringUtils.isEmpty(token)) return null;
    Jws<Claims> claimsJws = Jwts.parser().setSigningKey(tokenSignKey).parseClaimsJws(token);
    Claims claims = claimsJws.getBody();
    Integer userId = (Integer)claims.get("userId");
    return userId.longValue();
  }

  /***
   * 从token字符串获取userType
   * @param token token字符串
   * @return  返回userType
   */

  public static Integer getUserType(String token) {
    if(StringUtils.isEmpty(token)) return null;
    Jws<Claims> claimsJws
        = Jwts.parser().setSigningKey(tokenSignKey).parseClaimsJws(token);
    Claims claims = claimsJws.getBody();
    return (Integer)(claims.get("userType"));
  }

  //从token字符串获取userName
  public static String getUserName(String token) {
    if(StringUtils.isEmpty(token)) return "";
    Jws<Claims> claimsJws
        = Jwts.parser().setSigningKey(tokenSignKey).parseClaimsJws(token);
    Claims claims = claimsJws.getBody();
    return (String)claims.get("userName");
  }

  /***
   * 判断token是否有效
   * @param token token字符串
   * @return  返回是否有效
   */

  public static boolean isExpiration(String token){
    try {
      boolean isExpire = Jwts.parser()
          .setSigningKey(tokenSignKey)
          .parseClaimsJws(token)
          .getBody()
          .getExpiration().before(new Date());
      //没有过期，有效，返回false
      return isExpire;
    }catch(Exception e) {
      //过期出现异常，返回true
      return true;
    }
  }


  /**
   * 刷新Token
   * @param token 旧token
   * @return  返回新token
   */
  public String refreshToken(String token) {
    String refreshedToken;
    try {
      final Claims claims = Jwts.parser()
          .setSigningKey(tokenSignKey)
          .parseClaimsJws(token)
          .getBody();
      refreshedToken = JwtHelper.createToken(getUserId(token), getUserType(token));
    } catch (Exception e) {
      refreshedToken = null;
    }
    return refreshedToken;
  }

  // 测试
  public static void main(String[] args) {
//        String token = JwtHelper.createToken(1L, "lucy");
//        System.out.println(token);
//        System.out.println(JwtHelper.getUserId(token));
//        System.out.println(JwtHelper.getUserName(token));
  }
}
```

### 7.4 获取token

```java
/***
 * 获取请求头中的token的信息
 */
public class AuthContextHolder {

  //从请求头token获取userid
  public static Long getUserIdToken(HttpServletRequest request) {
    //从请求头token
    String token = request.getHeader("token");
    //调用工具类
    Long userId = JwtHelper.getUserId(token);
    return userId;
  }

  //从请求头token获取name
  public static String getUserName(HttpServletRequest request) {
    //从header获取token
    String token = request.getHeader("token");
    //jwt从token获取username
    String userName = JwtHelper.getUserName(token);
    return userName;
  }
}
```



## 8. swagger

### 8.1 依赖坐标

```xml
<!--前后端接口框架:swagger-->
<dependency>
    <groupId>io.springfox</groupId>
    <artifactId>springfox-swagger2</artifactId>
    <version>2.7.0</version>
</dependency>
<!--swagger ui-->
<dependency>
    <groupId>io.springfox</groupId>
    <artifactId>springfox-swagger-ui</artifactId>
    <version>2.7.0</version>
</dependency>
<!--swagger2  增强版接口文档-->
<dependency>
    <groupId>com.github.xiaoymin</groupId>
    <artifactId>knife4j-spring-boot-starter</artifactId>
    <version>2.0.4</version>
</dependency>
```

