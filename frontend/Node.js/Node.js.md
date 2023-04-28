[TOC]

学习时间:2022年10月26日--~

# 1. Node.js介绍

## 1.1 概念

`Node.js is a JavaScript runtime built on Chrome's V8 JavaScript engine.`

- `Node.js `是一个基于`Chrome V8`引擎的`JavaScript`运行环境。

Node.js官网:[https://nodejs.org/zh-cn/]:

**注意:**

- Node.js 中无法调用DOM和BOM等浏览器内置API.

## 1.2 作用

`Node,js`作为一个`JavaScript`的运行环境，仅仅提供了基础的功能和`API`。然而，基于`Node.js` 提供的这些基础能，很多强大的工具和框架如雨后春笋，层出不穷，所以学会了`Node.js`，可以让前端程序员胜任更多的工作和岗位:

1. 基于`Express`框架(http://www.expressjs.com.cn/)，可以**快速构建Web应用**
2. 基于`Electron`框架(https://electronjs.org/)，可以**构建跨平台的桌面应用**

3. 基于`restify`框架(http://restify.com/)，可以快速**构建API接口项目**

4. **读写和操作数据库、创建实用的命令行工具**辅助前端开发

## 1.3 在Node.js环境中执行javascript代码

- 在文件目录下输入`cmd`快速进入命令提示符窗口,使用`node test.js`命令执行`js`脚本.

# 2. fs文件系统模块

## 2.1 概念

`fs`模块是`Node.js`官方提供的、用来操作文件的模块.

- `fs.readFile()`方法，用来读取指定文件中的内容.

- `fs.writeFile()`方法，用来向指定的文件中写入内容.

**导入`fs`模块:**

- `const fs = require('fs')`

## 2.2 读取指定文件中的内容

### 2.2.1 fs.readFile

使用`fs.readFile()`方法,可以读取指定文件中的内容.

**语法:**

- `fs.readFile(path,[options],callback)`

**参数:**

- **path:**字符串,表示**文件的路径**.
- **options:**表示以**什么编码格式来读取**文件.
- **callback:**文件读取完成后,通过**回调函数**拿到读取失败和成功的结果 `err`,`dataStr` 

**代码演示:**

```javascript
const fs = require('fs');
fs.readFile('./21.txt',function(err,dataStr){
    if(err){
        return console.log('文件读取失败:'+err.message);
    }
    console.log('文件内容:'+dataStr);
})
```

```
输出结果:
文件内容:313213
文件读取失败:ENOENT: no such file or directory, open 'C:\Users\admin\Desktop\project\Node.js\21.txt'
```

**返回值:**

- **成功:** `err`为`null`
- **失败:**` err`为错误对象,`dataStr`为`undefined`

## 2.3 向指定文件中写入内容

### 2.3.1 fs.writeFile

使用`fs.writeFile()`方法，可以向指定的文件中写入内容

**语法:**

- `fs.writeFiile(path,data,[options],callback)`

**参数:**

- **path:**需要指定一个文件路径的字符串，表示文件的存放路径

- **data:**需要写入的内容
- **options:**编码格式
- **callback:**回调函数

**代码演示:**

```javascript
const fs = require('fs');
fs.writeFile('f:/2.txt','213312',function(err){
    if(err){
       return console.log('文件写入失败:'+err.message);
    }
    else console.log('写入成功!');
})
```

```
输出结果:
写入成功!
文件写入失败:ENOENT: no such file or directory, open 'f:\2.txt'
```

**返回值:**

- **失败:**` err`为错误对象,`dataStr`为`undefined`

## 2.4 读取写入文件案例(整理成绩表)

**代码演示:**

```javascript
const fs = require('fs');
fs.readFile('1.txt','utf-8',function(err,dataStr){  //此处注意读入字符串的编码格式,使用utf-8格式可以防止dataStr无法使用split函数
    if(err)return console.log('读取文件失败:'+err.message);
    const dataOld = dataStr.split(' ');
    const dataNew = [];
    dataOld.forEach(item=>{
        dataNew.push(item.replace('=',':'))
    })
    const str = dataNew.join('\r\n');
    fs.writeFile('1.txt',str,function(err){
        if(err)return console.log('写入文件失败'+err.message);
        else console.log('文件写入成功');
    })
})
```

## 2.5 路径问题

动态拼接

- 在使用fs 模块操作文件时，如果提供的操作路径是以`./`或`../`开头的相对路径时，很容易出现路径动态拼接错误的问题。
- 原因
  - 代码在运行的时候，会以执行node命令时所处的目录，动态拼接出被操作文件的完整路径。
- 解决方法
  - 使用绝对路径
  - 使用`__dirname`进行拼接

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/62f6404e182c67f11a790a8b5166113c.png)



# 3. path路径模块

## 3.1 介绍

path模块是Node.js官方提供的、用来处理路径的模块。它提供了一系列的方法和属性，用来满足用户对路径的处理需求。

例如

- `path.join()`方法，用来将多个路径片段拼接成一个完整的路径字符串
- `path.basename()`方法，用来从路径字符串中，将文件名解析出来

## 3.2  路径拼接

### 3.2.1 path.join()

使用`path.join()`方法，可以把多个路径片段拼接为完整的路径字符串

语法

```js
path.join([...paths])
```

- `...paths`路径片段
- 返回值`string`

```js
const pathStr = path.join('/a','/b/c','../','./d','e')
console.log(pathStr)	// \a\b\d\e
//抵消\c
```

### 3.2.2 path.basename()

使用`path.basename()`方法，可以获取路径中的最后一部分，经常通过这个方法获取路径中的文件名

```js
path.basename(path[,ext])
```

- `path`必选参数，表示一个路径的字符串
- `ext`可选参数，表示文件拓展名
- 返回值：表示路径中最后一部分

### 3.2.3 path.extname()

使用`path.extname()`方法，可以获取路径中的扩展名部分

```js
path.extname(path)
```

## 3.3 综合案例--分离HTML文件中的css和js

```js
// node
const fs = require('fs');
const path = require('path');

const regStyle = /<style>([\s\S]*?)<\/style>/g;
const regScript = /<script>([\s\S]*?)<\/script>/g;

function resolveCSS(str) {
  let res = regStyle.exec(str);
  res = res[0].replace(/<style>/g, '').replace(/<\/style>/g, '');
  fs.writeFile(path.join(__dirname, 'static/style.css'), res, (err) => {
    if (err)
      return console.log(err);
    console.log('The css file was saved!');
  });
}

function resolveJS(str) {
  let res = regScript.exec(str);
  res = res[0].replace(/<script>/g, '').replace(/<\/script>/g, '');
  fs.writeFile(path.join(__dirname, 'static/script.js'), res, (err) => {
    if (err)
      return console.log(err);
    console.log('The js file was saved!');
  });
}

function resolveHTML(str) {
  let htmlstr = str.toString();
  htmlstr = htmlstr.replace(regStyle, '<link rel="stylesheet" href="style.css">').replace(regScript, '<script src="script.js"></script>');
  fs.writeFile(path.join(__dirname, 'static/index.html'), htmlstr, (err) => {
    if (err)
      return console.log(err);
    console.log('The html file was saved!');
  });
}

fs.readFile(path.join(__dirname, 'index.html'), (err, data) => {
  if (err)
    return console.log(err);
  resolveCSS(data);
  resolveJS(data);
  resolveHTML(data);
})
```

```html
<!--html-->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    body {
      background-color: #000;
      color: #fff;
    }
  </style>
</head>
<body>
  <script>
    console.log('Hello World');
  </script>
</body>
</html>
```



# 4. http模块

## 4.1 介绍

`http`模块是Nodejs 官方提供的、用来创建 web服务器的模块。通过 http模块提供的`http.createServer()`方法，就能方便的把一台普通的电脑，变成一台Web服务器，从而对外提供 Web资源服务。

```js
const http = require('http')
```

在Node.js 中，我们不需要使用IIS、Apache等这些第三方web服务器软件。因为我们可以基于Node.js 提供的http模块，通过几行简单的代码，就能轻松的手写一个服务器软件，
从而对外提供web 服务。

## 4.2 创建基本web服务器

### 4.2.1 步骤

1. 导入http模块

```js
const http = require('http')
```

2. 创建web服务器实例

```js
const server = http.createServer()
```

3. 为服务器实例绑定request事件

```js
server.on(request,(req,res) => {
    console.log('服务被访问')
})
```

4. 启动服务器

```js
server.listen(80,() => {
    console.log('服务运行在localhost:80')
})
```

### 4.2.2 req请求对象

只要服务器接收到了客户端的请求，就会调用通过`server.on()`为服务器绑定的`request`事件处理函数。
如果想在事件处理函数中，访问与客户端相关的数据或属性，可以使用如下的方式:

```js
server.on('request', (req) => {
    const str = `Your request url is ${req.url}, and request method is ${req.method}`
    consolo.log(str)
})
```

### 4.2.3 res响应对象

在服务器的`request`事件处理函数中，如果想访问与服务器相关的数据或属性，可以使用`res.end(str)`:

```js
server.on('request', (req) => {
    const str = `Your request url is ${req.url}, and request method is ${req.method}`
   	res.end(str)
})
```

### 4.2.4 解决中文乱码

当调用`res.end()`方法，向客户端发送中文内容的时候，会出现乱码问题，此时，需要手动设置内容的编码格式:

```js
res.setHeader('Content-Type', 'text/html; charset=utf-8')
res.end(str)
```



## 4.3 根据不同的url响应不同的内容

### 4.3.1 步骤

1. 获取请求url地址
2. 设置默认的响应内容为`404 Not Found`
3. 判断用户请求的是否为`/`或`index.html`首页
4. 判断用户请求的是否为`/about.html`关于页面
5. 设置`Content-Type`响应头，防止中文乱码
6. 使用`res.end()`把内容响应给客户端

```js
const http = require('http')
const server = http.createServer()

server.on('request', (req, res) => {
  const url = req.url
  let content = '<h1>404 Not Found</h1>'
  if (url == '/' || url == '/index.html' || url == '/index') {
    content = '<h1>首页</h1>'
  }
  else if (url == '/about.html' || url == '/about') {
    content = '<h1>关于</h1>'
  }
  res.setHeader('Content-Type', 'text/html; charset=utf-8')
  res.end(content)
})

server.listen(80, () => {
  console.log('server is running at http://localhost')
})
```

## 4.4 案例--创建一个web服务器

### 4.4.1 实现步骤

1. 导入需要的模块

```js
const http = require('http')
const fs = require('fs')
const path = require('path')
```

2. 创建基本的web服务器

```js
const server = http.createServer()
server.on('request', (req,res) => {})
server.listen(80,() => {})
```

3. 将资源的请求url地址映射为文件的存放路径

```js
const url = req.url
const fpath = path.join(__dirname, url)
```

4. 读取文件内容并响应给客户端

```js
fs.readFile(fpath,'utf-8',(err,dataStr) => {
    if(err) return res.end('404 Not Found')
    res.end(dataStr)
})
```

### 4.4.2 优化请求路径

```js
const url = req.url
let fpath = ''
if(url == '/') {
    fpath = path.join(__dirname, './static/index.html')
} else if(url == '/index.html') {
    fpath = path.join(__dirname, './static', url)
} 
```



# 5. 模块化

## 5.1 介绍

编程领域中的模块化，就是遵守固定的规则，把一个大文件拆成独立并互相依赖的多个小模块。
把代码进行模块化拆分的好处:

1. 提高了代码的复用性
2. 提高了代码的可维护性
3. 可以实现按需加载

## 5.2 模块的分类

Node.js 中根据模块来源的不同，将模块分为了3大类，分别是:

- 内置模块  (内置模块是由Node.js官方提供的，例如fs、path、http 等)
- 自定义模块（用户创建的每个.js 文件，都是自定义模块)
- 第三方模块（由第三方开发出来的模块，并非官方提供的内置模块，也不是用户创建的自定义模块，使用前需要先下载)

## 5.3 加载模块

使用`require()`方法，可以加载需要的内置模块、用户自定义模块、第三方模块进行使用。

```js
const fs = require('fs')
const custom = require('./custom.js')
const moment = require('moment')
```

注意

- 使用`require()`方法加载其它模块时，**会执行被加载模块中的代码**。

## 5.4 模块作用域

和**函数作用域**类似，在自定义模块中定义的变量、方法等成员，**只能在当前模块内被访问**，这种**模块级别的访问限制**，叫做**模块作用域**。

好处

- 防止全局变量污染

## 5.5 向外共享模块作用域中的成员

### 5.5.1 module对象

在每个`.js`自定义模块中都有一个`module`对象，它里面**存储了和当前模块有关的信息**

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/04a0cdd3fb87e1d448f6b4d0951d1b6e.png)

### 5.5.2 module.exports对象

在自定义模块中，可以使用`module.exports`对象，将模块内的成员共享出去，供外界使用。

外界用`require()`方法导入自定义模块时，得到的就是`module.exports`所指向的对象。

```js
const age = 20
// 向module.exports 对象上挂载username属性
module.exports.username = 'zhangsan'
// 向module.exports 对象上挂载func方法
module.exports.func = function () {
    console.log('node.js')
}
module.exports.age = age
```

注意

- 使用`require()`方法导入模块时，导入的结果，永远以`module.exports`指向的对象为准。

```js
module.exports = {
    name: 'zhangsan',
    func() {
        console.log('Node.js')
    }
}
```

### 5.5.3 exports对象

由于`module.exports`单词写起来比较复杂，为了简化向外共享成员的代码，Node 提供了exports 对象。

默认情况下,`exports`和`module.exports`指向同一个对象。最终共享的结果还是以`module.exports`指向的对象为准。

### 5.5.4 exports和module.exports的使用误区

`require()`模块时，得到的永远是`module.exports`指向的对象

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/9d8b31e79fa5a3ecf591662d29bef94d.png)

注意

- 为了防止混乱，建议不要在同一个模块中同时使用`exports`和`module.exports`

### 5.5.5 模块化规范

Node.,js 遵循了CommonJS模块化规范，CommonJS规定了**模块的特性**和**各模块之间如何相互依赖**。
CommonJS规定:

1. 每个模块内部,`module`变量代表当前模块。
2. `module`变量是一个对象，它的`exports`属性(即`module.exports`）是对外的接口。
3. 加载某个模块，其实是加载该模块的`module.exports`属性。`require()`方法用于加载模块。

## 5.6 npm与包

### 5.6.1 包

- Node.js 中的第三方模块又叫做包。

- 不同于Node.js 中的内置模块与自定义模块，包是由第三方个人或团队开发出来的，免费供所有人使用。
- 由于Node.js的内置模块仅提供了一些底层的API，导致在基于内置模块进行项目开发的时，效率很低。包是基于内置模块封装出来的，提供了更高级、更方便的API，极大的**提高了开发效率**。

### 5.6.2 npm

- npm, Inc.公司提供了一个包管理工具，我们可以使用这个包管理工具，从https://registry.npmjs.org/服务器把需要的包下载到本地使用。
- 这个包管理工具的名字叫做Node Package Manager (简称npm包管理工具)，这个包管理工具随着Node.js的安装包一起被安装到了用户的电脑上。

### 5.6.3 案例--使用moment格式化时间

1. 安装

```bash
npm install moment # 或者 npm i moment 
```

2. 编写代码

```js
// 导入包
const moment = require('moment')
// 格式化时间
const date = moment().format('YYYY-MM-DD HH:mm:ss');
// 输出
console.log(date);
```

### 5.6.4 切换npm的下包镜像源

```bash
# 查看当前的下包镜像源
npm config get registry
# 将下包的镜像源切换为淘宝镜像源
npm config set registry=https://registry.npm.tabao.org/
```

### 5.6.5 npm的基本使用

安装

```bash
npm install 包@指定版本  # 或者 npm i 包@指定版本
```

初次装包完成后，在项目文件夹下多一个叫做`node_modules`的文件夹和`package-lock.json`的配置文件。
其中:

- `node_modules`文件夹用来存放所有已安装到项目中的包。`require()`导入第三方包时，就是从这个目录中查找并加载包。`package-lock.json`配置文件用来记录`node_modules`目录下的每一个包的下载信息，例如包的名字、版本号、下载地址等。

### 5.6.6 包的语义化版本规范

包的版本号是以“点分十进制”形式进行定义的，总共有三位数字，例如2.24.0

其中每一位数字所代表的的含义如下:

- 第1位数字:大版本
- 第2位数字:功能版本
- 第3位数字:Bug修复版本

版本号提升的规则

- 只要前面的版本号增长了，则后面的版本号归零

### 5.6.7 包管理配置文件

npm规定，在项目根目录中，必须提供一个叫做`package.json`的包管理配置文件。用来记录与项目有关的一些配置信息。例如:

- 项目的名称、版本号、描述等
- 项目中都用到了哪些包
- 哪些包只在开发期间会用到
- 哪些包在开发和部署时都需要用到

### 5.6.8 快速创建package.json

npm包管理工具提供了一个快捷命令，可以在执行命令时所处的目录中，快速创建`package.json`这个包管理配置文件:

```bash
npm init -y
```

注意

1. 上述命令**只能在英文的目录下成功运行**，所以，项目文件夹的名称一定要使用英文命名，不要使用中文，不能出现空格。
2. 运行`npm install `命令安装包的时候，npm包管理工具会自动把包的名称和版本号，记录到`package.json`中。

### 5.6.9 dependencies节点

`package.json`文件中，有一个`dependencies`节点，专门用来记录使用`npm install`命令安装了哪些包。

下载一个剔除了`node_modules`文件夹的项目，可以使用`npm install`或者`npm i`安装所有依赖

### 5.6.10 devDependencies节点

如果某些包只在项目开发阶段会用到，在项目上线之后不会用到，则建议把这些包记录到`devDependencies`节点中。

与之对应的，如果某些包在开发和项目上线之后都需要用到，则建议把这些包记录到`dependencies`节点中。

```bash
npm i 包名 -D
npm install 包名 --save-dev
```

### 5.6.11 包的分类

#### 5.6.11.1 项目包

那些被安装到项目的`node_modules`目录中的包，都是项目包。

项目包又分为两类，分别是:

- 开发依赖包(被记录到devDependencies节点中的包，只在开发期间会用到)
- 核心依赖包(被记录到dependencies节点中的包，在开发期间和项目上线之后都会用到)

```bash
npm i 包名 -D # 开发依赖包
npm i 包名    # 核心依赖包
```

#### 5.6.11.2 全局包

在执行`npm install`命令时，如果提供了`-g`参数，则会把包安装为全局包。
全局包会被安装到`C:\Users\用户目录\AppData\Roaming\npm(node_modules`目录下。

```bash
npm i 包名 -g
npm uninstall 包名 -g
```

注意

1. 只有**工具性质**的包，才有全局安装的必要性。因为它们提供了好用的终端命令

2. 判断某个包是否需要全局安装后才能使用，可以参考官方提供的使用说明即可。

### 5.6.12 规范的包结构

一个规范的包，它的组成结构，必须符合以下3点要求:

1. 包必须以单独的目录而存在
2. 包的顶级目录下要必须包含`package.json`这个包管理配置文件
3. `package.json`中必须包含`name`，`version`，`main`这三个属性，分别代表包的名字、版本号、包的入口。

注意:以上3点要求是一个规范的包结构必须遵守的格式，关于更多的约束，可以参考如下网址:

https://yarnpkg.com/zh-Hans/docs/package-json

### 5.6.13 开发自己的包

1. 新建包文件夹，作为包的根目录
2. 在包目录下新建三个文件
   - `package.json`（包管理配置文件）
   - `index.js` （包的入口文件）
   - `README.md`（包的说明文档）

#### 5.6.13.1 初始化package.json

```json
{
    "name": " 包名",
    "version": "1.0.0",
    "main": "index.js",
    "description": "包的介绍",
    "keywords": ["word1","word2","word3"],
    "license": "ISC"
}
```

#### 5.6.13.2 在index.js中定义

```js
/*
代码...
*/
module.exports = {
    // 导出的对象或者方法
}
```

入口文件中需要导出多个对象时可以展开(`...`展开运算符)之后再导出

```js
const date = require('./src/dateFormat')
const escape = require('./src/htmlEscape')

module.exports = {
    ...date,
    ...escape
}
```



## 5.7 模块的加载机制

### 5.7.1 优先从缓存中加载

模块在第一次加载后会被缓存。这也意味着多次调用`require()`不会导致模块的代码被执行多次。

注意

- 不论是内置模块、用户自定义模块、还是第三方模块，它们都会优先从缓存中加载，从而提高模块的加载效率。

### 5.7.2 内置模块的加载机制

内置模块是由Nodejs官方提供的模块，**内置模块的加载优先级最高**
例如，`require("fs')`始终返回内置的fs模块，即使在`node_modules`目录下有名字相同的包也叫做fs。

### 5.7.3 自定义模块的加载机制

使用`require()`加载自定义模块时，必须指定以`./`或`../`开头的路径标识符。在加载自定义模块时，如果没有指定`./`或`../`这样的路径标识符，则node 会把它当作内置模块或第三方模块进行加载。

同时，在使用`require()`导入自定义模块时，如果省略了文件的扩展名，则Node.js 会按顺序分别尝试加载以下的文件

1. 按照确切的文件名进行加载
2. 补全`.js`扩展名进行加载
3. 补全`.json`扩展名进行加载
4. 补全`.node`扩展名进行加载
5. 加载失败，终端报错

### 5.7.4 第三方模块的加载机制

如果传递给 `require()`的模块标识符不是一个内置模块，也没有以`./`或`../`开头，则Node.js 会从当前模块的父目录开始，尝试从`/node_modules`文件夹中加载第三方模块。
如果没有找到对应的第三方模块，则移动到再上一层父目录中，进行加载，直到文件系统的根目录。

### 5.7.5 目录作为模块

当把目录作为模块标识符，传递给`require()`进行加载的时候，有三种加载方式:

1. 在被加载的目录下查找一个叫做`package.json`的文件，并寻找`main`属性，作为`require()`加载的入口
2. 如果目录里没有`package.json`文件，或者`main`入口不存在或无法解析，则Node.js将会试图加载目录下的`index.js`文件。
3. 如果以上两步都失败了，则Node.js 会在终端打印错误消息，报告模块的缺失:`Error: Cannot find module 'xxx'`



# 6. Express

## 6.1 简介

官方给出的概念

- Express是基于Node.js 平台，快速、开放、极简的Web开发框架。

Express的本质

- 就是一个npm 上的第三方包，提供了快速创建Web服务器的便捷方法。

对于前端程序员来说，最常见的两种服务器，分别是:

- Web网站服务器:专门对外提供 Web 网页资源的服务器。
- API接口服务器:专门对外提供API接口的服务器。

使用Express，我们可以方便、快速的创建Web 网站的服务器或API接口的服务器。

## 6.2 基本使用

1. 安装

```bash
npm i express@4.17.1
```

2. 创建基本的Web服务器

```bash
const express = require('express')
const app = express()
app.listen(80,() => {
	console.log('express server running at http://localhost')
})
```

