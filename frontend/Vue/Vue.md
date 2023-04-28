​	

[TOC]





第一部分 前端工程化  Webpack

学习时间:2022年10月26日-~2022年11月7日

# 1. Webpack基本使用

## 1.1 概念

**概念:**

-  `webpack` 是前端项目工程化的具体解决方案.

**主要功能:**

- 它提供了友好的前端**模块化开发**支持,以及**代码压缩混淆**、处理浏览器端`JavaScript` 的**兼容性**、**性能优化**等强大的功能.

**好处:**

- 让程序员把工作的重心放到具体功能的实现上,提高了前端**开发效率**和项目的**可维护性**.

**注意:**

- 目前`Vue，React`等前端项目,基本上都是基于`webpack`进行工程化开发的.

## 1.2 准备工作

1. 新建项目空白目录，并运行`npm init -y`命令，初始化包管理配置文件 `package.json`.

2. 新建`src`源代码目录.

3. 新建`src -> index.html`首页和`src -> index.js `脚本文件.
4. 初始化首页基本的结构.

5. 运行`npm install jquery -s`命令，安装`jQuery`.

6. 通过`ES6`模块化的方式导入`jQuery`.

## 1.3 在项目中安装webpack

在终端运行如下的命令，安装`webpack`相关的两个包:

- `npm install webpack@5.42.1 webpack-cli@4.7.2 -D`

**使用npm淘宝源:**

- `npm config set registry https://registry.npm.taobao.org`

**查看当前的下载源:**

- `npm config get registry`

## 1.4 在项目中配置webpack

1. 在项目根目录中，创建名为`webpack.config.js`的`webpack`配置文件，并初始化如下的基本配置:

```javascript
//使用Node.js 中的导出语法，向外导出一个 webpack的配置对象
module.exports = {
    //代表 webpack运行的模式，可选值有两个 development和production
    mode: 'development'
}
```

2. 在`package.json`的`scripts `节点下，新增`dev`脚本如下:

```javascript
 "scripts": {
    "dev":"webpack"	//添加脚本,可以通过npm run 执行dev
 },
```

3. 在终端中运行`npm run dev`命令，启动`webpack`进行项目的打包构建
3. 引入`dist`中的`main.js`

**注意：在Node.js-v16以上的版本,会出现打包失败的情况.**

**mode配置项:**

- `development`开发使用,节省打包时间
- `production`发布使用,节省体积

## 1.5 webpack中的默认约定

在`webpack 4.x和5.x`的版本中，有如下的默认约定:

1. 默认的打包入口文件为`src -> index.js`

2. 默认的输出文件路径为`dist -> main.js`

**注意:**可以在`webpack.config.js`中修改打包的默认约定

### 1.5.1 自定义打包的入口与出口

在`webipack.config.js`配置文件中，通过`entry`节点指定打包的入口.通过`output`节点指定打包的出口

**代码演示:**

```javascript
const path = require('path')//导入node.js中专门操作路径的模块

module.exports = {
    mode:'development',
	entry: path.join(__dirname,'./src/index.js'),//打包入口文件的路径
    output:{
		path:path.join(__dirname,'./dist'),//输出文件的存放路径
        filename:'bundle.js'//输出文件的名称
	}
}
```

## 1.6 webpack 的插件

通过安装和配置第三方的插件，可以拓展`webpack`的能力，从而让`webpack` 用起来更方便。最常用的`webpack`插件有如下两个:

1. `webpack-dev-server`
   - 类似于`node.js`阶段用到的`nodelmon`工具
   - 每当修改了源代码,`webpack` 会自动进行项目的打包和构建
2. `html-webpack-plugin`
   - `webpack `中的`HTML`插件(类似于一个模板引擎插件
   - 可以通过此插件自定制`index.html`页面的内容

### 1.6.1 安装webpack-dev-server

**安装:**

- `npm install webpack-dev-server@3.11.2 -D`

### 1.6.2 配置webpack-dev-server

修改`package.json -> scripts`中的`dev`命令如下:

```javascript
"scripts":{
	"dev":"webpack serve"//script节点下的脚本,可以通过npm run执行
}
```

2. 再次运行`npm run dev`命令，重新进行项目的打包

3. 在浏览器中访问http://localhost:8080地址，查看自动打包效果

   

**注意:此处使用最新的`webpack-cli`版本**

**注意:如果`localhost:8080`端口被占用,使用`netstat -ano`命令查看占用的进程的`PID`,使用`taskkill /F /PID xxx`命令结束进程**

**注意:此时生成的`bundle.js`文件位于[http://localhost:8080]:目录下,`index.html`需要以`../bundle.js`目录重新引入文件**

### 1.6.3 安装html-webpack-plugin

**安装:**

- `npm install html-webpack-plugin@5.3.2 -D`

### 1.6.4 配置html-webpack-plugin

```javascript
//1．导入HTML插件，得到一个构造函数
const HtmlPlugin = require('html-webpack-plugin')
                           
//2．创建HTML插件的实例对象
const htmlPlugin = new HtmlPlugin({
	template:'./src/index.html',//指定原文件的存放路径		filename:'./index.html'//指定生成的文件的存放路径
})
module.exports = {
    mode: 'development',
	plugins: [htmlPlugin]
    // 3，通过 plugins节点,使htmlPlugin 插件生效
}
```

### 1.6.5 devServer 节点

在`webpack.config.js` 配置文件中，可以通过`devServer`节点对`webpack-dev-server`插件进行更多的配置

**代码演示:**

```javascript
devServer:{
	open: true，//初次打包完成后，自动打开浏览器
	host: '127.0.0.1 ',//实时打包所使用的主机地址
    port: 80//实时打包所使用的端口号
}
```

**注意:**凡是修改了`webpack.config.js`配置文件，或修改了`package.json`配置文件，**必须重启实时打包的服务器**，否则最新的配置文件无法生效!

## 1.7 webpack中的loader

### 1.7.1 概念

在实际开发过程中，`webpack`默认只能打包处理以`.js`后缀名结尾的模块.其他非`.js`后缀名结尾的模块，`webpack` 默认处理不了，需要调用`loader`加载器才可以正常打包，否则会报错

loader 加载器的作用:**协助webpack打包处理特定的文件模块**.比如:

- **css-loader**可以打包处理`.css`相关的文件
- **less-loader**可以打包处理`.less`相关的文件
- **babel-loader**可以打包处理`webpack`无法处理的高级`JS`语法

### 1.7.2 打包处理css文件

**步骤:**

1. 运行`npm i style-loader@3.0.0 css-loader@5.2.6 -D`命令，安装处理`css`文件的`loader`

2. 在`webpack.config.js`的`module -> rules`数组中，添加 `loader`规则如下:

```javascript
module:{//所有第三方文件模块的匹配规则
	rules: [ //文件后缀名的匹配规则
	{test: /\.css$/,use:['style-loader','css-loader']}
  ]
}
```

其中，`test`表示匹配的**文件类型**，`use`表示对应要调用的`loader`

**注意:**

- `use`数组中指定的`loader`**顺序是固定的**

- 多个`loader`的调用顺序是**从后往前调用**

### 1.7.3 打包处理less文件

1. 运行`npm i less-loader@10.0.1 less@4.1.1 -D`命令
2. 在` webpack.config.js`的`module -> rules`数组中，添加`loader`规则如下:

```javascript
module:{//所有第三方文件模块的匹配规则
	rules:[//文件后缀名的匹配规则
		{test:/\.less$/,use:['style-loader','css-loader','less-loader']},
    ]
}
```



### 1.7.4 打包处理样式表中与url路径相关的文件

运行`npm i url-loader@4.1.1 file-loader@6.2.0 -D`命令
在`webpack.config.js`的`module -> rules`数组中，添加`loader`规则如下:

```javascript
module: {//所有第三方文件模块的匹配规则
	rules: [//文件后缀名的匹配规则
		{test:/\.jpg|png|gif$/,use:'ur1-loader?limit=22229'},
        ]
}
```


其中`?`之后的是` loader`的参数项:

- `limit`用来指定图片的大小，单位是字节`(byte)`
- 只有`≤limit`大小的图片，才会被转为`base64`格式的图片

### 1.7.5 打包处理js 文件中的高级语法

`webpack`只能打包处理一部分高级的`JavaScript`语法。对于那些`webpack`无法处理的高级`js `语法，需要借助于`babel-loader`进行打包处理.例如`webpack`无法处理下面的`JavaScript`代码:

```javascript
//1．定义了名为info的装饰器
function info( target){
//2．为目标添加静态属性info
    target.info = 'Person info'
}
//3.为 Person类应用info装饰器
@info
class Person{}
//4．打印 Person的静态属性info
console.log(Person.info)
```

#### 1.7.5.1 安装babel-loader

运行如下的命令安装对应的依赖包:

- `npm i babel-loader@8.2.2 @babel/core@7.14.6 @babel/plugin-proposal-decorators@7.14.5 -D`

在`webpack.config.js`的 `module -> rules`数组中，添加`loader`规则如下:

```javascript
//注意:必须使用exclude指定排除项;因为node_modules目录下的第三方包不需要被打包
{test:/\.js$/,use:'babel-loader', exclude:/node_modules/}
```

#### 1.7.5.2 配置babel-loader

在项目根目录下，创建名为`babel.config.js`的配置文件，定义`Babel`的配置项如下:

```javascript
module.exports = {
//声明babel可用的插件
	plugins:[['@babel/plugin-proposal-decorators',{legacy:true}]]
}
```

## 1.8 打包发布

### 1.8.1 配置webpack的打包发布

在`package.json`文件的`scripts`节点下，新增`build`命令如下:
```javascript
"scripts":{
	"dev:"webpack serve",//开发环境中，运行dev命令
	"buiid":"webpack --mode production"//项目发布时,运行build命令
}
```

`--model`是一个参数项，用来指定`webpack`的**运行模式**.`production`代表生产环境，会对打包生成的文件进行**代码压缩**和**性能优化**.

**注意:**

通过`--model`指定的参数项，**会覆盖`webpack.config.js `中的` model`选项**.

### 1.8.2 JavaScript文件统一生成到js目录中

在`webpack.config.js`配置文件的`output`节点中，进行如下的配置:

```javascript
output: {
	path:path.join(__dirname,'dist'),
	//明确告诉 webpack 把生成的 bundle.js文件存放到dist目录下的 js子目录中
	filename:'js/bundle.js'，
}
```

### 1.8.3 把图片文件统一生成到image目录中

修改`webpack.config.js `中的`url-loader`配置项，新增`outputPath`选项即可指定图片文件的输出路径:

```javascript
test:/\.jpg|png|gif$/,
use:{
	loader:'ur1-loader',
	options:{
		limit: 22228,
		//明确指定把打包生成的图片文件，存储到dist目录下的 image文件夹中
		outputPath: 'image',
		},
	}，
}
```

### 1.8.4 自动清理dist目录下的旧文件

为了在每次打包发布时自动清理掉`dist`目录中的旧文件，可以安装并配置`clean-webpack-plugin`插件:

#### 1.8.4.1 安装clean-webpack-plugin

- `npm install clean-webpack-plugin@3.0.0 -D`

```javascript
//1．按需导入插件、得到插件的构造函数之后，创建插件的实例对象
const {CleanwebpackPlugin} = require('clean-webpack-plugin')
const cleanPlugin = new CleanWebpackPlugin()
//2．把创建的 cleanPlugin 插件实例对象，挂载到plugins节点中
plugins:[htmlPlugin,cleanPlugin],//挂载插件
```

## 1.9 Source Map

### 1.9.1 概念

**`Source Map`就是一个信息文件，里面储存着位置信息**.也就是说，`Source Map`文件中存储着压缩混淆后的代码，所对应的**转换前的位置**.

有了它，出错的时候，除错工具将**直接显示原始代码，而不是转换后的代码**，能够极大的方便后期的调试.

## 1.10 webpack中@符号作用

略



## 1.11 安装vue_devtools

略



# 2. Vue

## 2.1 Vue简介

**官方概念:**Vue (读音/vju:/，类似于view)是一套用于**构建用户界面**的**前端框架**.

## 2.2 Vue的特性

vue框架的特性，主要体现在如下两方面:

1. 数据驱动视图
2. 双向数据绑定

### 2.2.1 数据驱动视图

在使用了`vue`的页面中，`vue `会**监听数据的变化**，从而**自动**重 新渲染页面的结构。

**好处:**当页面数据发生变化时，页面会自动重新渲染!

**注意:**数据驱动视图是**单向的数据绑定**.

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/8fc00411c84018604b2cddbbd5210878.png)

### 2.2.2 双向数据绑定

在**填写表单**时，双向数据绑定可以辅助开发者在**不操作DOM的前提下**，**自动**把用户填写的内容**同步到**数据源中。示意图如下:

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/0b1741068c2984567fc91914b0c3134b.png)

**好处:**开发者不再需要手动操作`DOM`元素，来获取表单元素最新的值!

## 2.3 MVVM

`MWVM`是`vue`实现数据驱动视图和双向数据绑定的核心原理。`MVVM`指的是 `Model、View和ViewModel`,它把每个`HTML`页面都拆分成了这三个部分，如图所示:

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/1ee97402e7110aaa46a4188a8cf9a6b2.png)

**在MVVM概念中:**

- `Model`表示当前页面渲染时所依赖的数据源.

- `View`表示当前页面所渲染的`DOM`结构.

- `ViewModel`表示`vue`的实例，它是`MVVM`的核心.

### 2.3.1 MVVM的工作原理

**`ViewModel`作为`MVVM`的核心**，是它把当前页面的**数据源**(`Model`)和**页面的结构**(`View`)连接在了一起.

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/0920e916c17c4e60e64e86c731ef3d54.png)

- 当**数据源发生变化**时，会被`ViewModel`监听到，`VM`会根据最新的数据源**自动更新**页面的结构
- 当**表单元素的值发生变化**时，也会被`VM`监听到，`VM`会把变化过后最新的值**自动同步**到`Model`数据源中

## 2.4 Vue的版本 

当前，`vue`共有3个大版本，其中:

- 2.x版本的`vue`是目前企业级项目开发中的主流版本

- 3.x版本的`vue`于2020-09-19发布，生态还不完善，尚未在企业级项目开发中普及和推广

- 1.x版本`vue`几乎被淘汰，不再建议学习与使用

**总结:**

3.x版本的`vue`是未来企业级项目开发的趋势;

2.x版本的`vue`在未来（1～2年内）会被逐渐淘汰;

# 3. Vue2的基本使用

**基本步骤:**

1. 导入`vue.js`的`script`脚本文件
2. 在页面中声明一个将要被`vue`所控制的`DOM`区域
3. 创建`vm`实例对象(`vue`实例对象)

```html
<body>
    <!-- 2．在页面中声明一个将要被vue所控制的DOM区域-->
    <div id="app">{{username]}</div>
    <!-- 1.导入vue.js 的script脚本文件-->
    <script src="./lib/vue-2.6.12.js"></ script>		<script>
        //3．创建vm实例对象(vue实例对象)
        const vm = new Vue({
            //3.1指定当前vm实例要控制页面的哪个区域
            el:'#app',
            //3.2指定Model数据源
            data: {
                username: 'zs'
            }
        })
    </script>
</body>
```

## 3.1 基本代码和MVVM的对应关系

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/ef974afcdbcc7fbff34b1b8c1555d866.png)

## 3.2 Vue的指令与过滤器

### 3.2.1 概念

**指令(Directives)**

- 是 vue为开发者提供的**模板语法**，用于**辅助开发者渲染页面的基本结构**

**vue中的指令按照不同的用途可以分为如下6大类:**

1. 内容渲染指令

2. 属性绑定指令

3. 事件绑定指令

4. 双向绑定指令

5. 条件渲染指令

6. 列表渲染指令

### 3.2.2 插值表达式

**语法:**` <p>{{}}</p>`

#### 3.2.2.1 使用 Javascript 表达式

- 在`vue`提供的模板渲染语法中，除了支持绑定简单的数据值之外，还支持`Javascript`表达式的运算.

**例如:**

- `{{number+1}}`
- `{{ok?''YES':'NO'}}`

### 3.2.3 内容渲染指令

**内容渲染指令**用来辅助开发者**渲染DOM元素的文本内容**。

常用的内容渲染指令有如下3个:

- `v-text`
- `{{ }}`
- `v-html`

**v-text**

**语法:**

```xml
<div v-text="username"></div>
```

**注意:`v-text`语法会覆盖元素内的默认值**

**{{ }}**

**语法:**` <p>{{}}</p>`

- `vue`提供的`{{}}`语法，专门用来解决`v-text` 会覆盖默认文本内容的问题.这种`{{}}`语法的专业名称是**插值表达式**(英文名为:Mustache).

**v-html**

**语法:**

```xml
<div v-html="username"></div>
```

- `v-text `指令和插值表达式只能渲染纯文本内容。如果要把包含`HTML`标签的字符串渲染为页面的`HTML`元素，则需要用到`v-html`这个指令:

**注意:插值表达式只能用在元素的内容节点中，不能用在元素的属性节点中.**

### 3.2.4 属性绑定指令

如果需要为元素的属性动态绑定属性值，则需要用到`v-bind`属性绑定指令

**语法:**`<div v-bind:bgcolor="">`

**简写:**`:`

在使用`v-bind`属性绑定期间，如果绑定内容需要进行动态拼接，则字符串的外面应该包裹单引号.

### 3.2.5 事件绑定指令

`vue`提供了`v-on`事件绑定指令，用来辅助程序员为`DOM`元素绑定事件监听.

**简写:**`@`

**语法：**

```xml
<button @click="add"></button>
methods:{
	add(){
	//在此访问data中的数据
	this.count++;
	}
}
```

#### 3.2.5.1 事件对象$event

`$event`为默认的事件对象,如果被覆盖,可以手动传递应该`$event`参数.

```xml
<button @click="add(n,$event)"></button>
methods:{
	add(n,e){
	}
}
```

#### 3.2.5.2 事件修饰符

vue提供了**事件修饰符**的概念，来辅助程序员更方便的**对事件的触发进行控制**。常用的5个事件修饰符如下:

| 事件修饰符 | 说明                                                    |
| ---------- | ------------------------------------------------------- |
| .prevent   | 阻止默认行为（例如:阻止`a`连接的跳转、阻止表单的提交等) |
| .stop      | 阻止事件冒泡                                            |
| .capture   | 以捕获模式触发当前的事件处理函数                        |
| .once      | 绑定的事件只触发1次                                     |
| .self      | 只有在`event.target`是当前元素自身时触发事件处理函数    |

**语法:**

```xml
<button @click.prevent="add"></button>
```

#### 3.2.5.3 按钮修饰符

在监听键盘事件时，我们**经常需要判断详细的按键**.此时，可以为键盘相关的事件添加**按键修饰符**

**语法:**

```xml
<button @keyup.enter="submit"></button>
<button @keyup.esc="back"></button>
```

### 3.2.6 双向绑定指令

`vue`提供了`v-model`**双向数据绑定指令**，用来辅助开发者在不操作`DOM`的前提下，**快速获取表单的数据**.

  ```xml
  <input type="text" v-model="username"></input>
  ```

```xml
<select v-model="city">
    <option value="">请选择</option>
    <option value="1">北京</option>
    <option value="2">上海</option>
    <option value="3">广州</option>
</select>
<input type="text" v-model="city">
```

#### 3.2.6.1 v-model指令修饰符

| 修饰符  | 作用                           | 示例                            |
| ------- | ------------------------------ | ------------------------------- |
| .number | 自动将用户的输入值转为数值类型 | `<input v-model.number="age"/>` |
| .trim   | 自动过滤用户输入的首尾空白字符 | `<input v-model.trim="msg"/>`   |
| .lazy   | 在“change”时而非“input”时更新  | `<input v-model.lazy="msg"/>`   |

### 3.2.7 条件渲染指令

**条件渲染指令**用来辅助开发者**按需控制DOM的显示与隐藏**.条件渲染指令有如下两个，分别是:

- `v-if`
- `v-show`

**语法:**

```html
<p v-if="flag">这是v-if控制的元素</p>
<p v-show="flag">这是v-show控制的元素</p>
```

**注意:**

- `v-show`的原理是:动态为元素添加或移除`display: none`样式，来实现元素的显示和隐藏

- `v-if`的原理是:每次动态创建或移除元素，实现元素的显示和隐藏

- **如果要频繁的切换元素的显示状态，用`v-show`性能会更好**
- **如果初始状态为false,而且后期也很可能不需要展示出来的,使用`v-if`**
- **在绝大多数情况下,不用考虑性能,直接使用`v-if`就行**

**v-else和v-else-if**

`v-else`指令

- 即充当`v-if`的`else`块

`v-else-if `指令

- 顾名思义，充当`v-if `的“`else-if`块”，可以连续使用.

**注意:**

- `v-else-if`和`v-else`指令必须配合`v-if` 指令一起使用，否则它将不会被识别!

**代码演示:**

```xml
<input type="text" v-model="score"/>
<div v-if="score>=90">优秀</div>
<div v-else-if="score>=80&&score<90">良好</div>
<div v-else-if="score>=60&&score<80">及格</div>
<div v-else-if="score>=0&&score<60">不及格</div>
```

### 3.2.8 列表渲染指令

`vue`提供了`v-for`列表渲染指令，用来辅助开发者基于一个数组来循环渲染一个列表结构。`v-for`指令需要使用`item in items`形式的特殊语法，其中:

- `items`是待循环的数组
- `item`是被循环的每一项 

**代码演示:**

```xml
<table class="table table-border table-hover table-striped"><!-- 使用bootstrap样式表 -->
    <thead>
        <th>索引</th>
        <th>ID</th>
        <th>姓名</th>
    </thead>
    <tbody>
        <tr v-for="(item,index) in list" :key="item.id" :title="'项'+(index+1)">
            <td>{{index+1}}</td>
            <td>{{item.id}}</td>
            <td>{{item.name}}</td>
        </tr>
    </tbody>
    <tfoot></tfoot>
</table>
```

**注意:**

- 使用`v-for`指令,那么就要绑定一个 `:key`属性
- `:key`属性只能是 字符串或者数字类型.
- `key`值不可重复,否则终端会报错
- `key`值不能使用`index`(因为`index`的值不具备唯一性)

### 3.2.9 过滤器

过滤器(Filters）是`vue`为开发者提供的功能，常用于文本的格式化。过滤器可以用在两个地方︰插值表达式和`v-bind`属性绑定.

**在最新`Vue3`中 过滤器 已被废除**

## 3.3 侦听器

### 3.3.1 简介

**watch 侦听器**允许开发者监视数据的变化，从而**针对数据的变化做特定的操作**.

**代码演示:**

```javascript
const vm = new Vue({
    el: '#app',
    data:{
        username:''
    },
    watch:{
        //监听username值的变化
        //newVal 是“变化后的新值”，oldVal是“变化之前的旧值”
        username(newVal,oldVal){
            console.log(newVal,oldVal)
        }
    }
})
```

### 3.3.2 方法格式侦听器和对象格式侦听器

**方法格式侦听器:**

```javascript
username(newVal,oldVal){
    console.log(newVal,oldVal)
}
```

- **缺点1:** 无法在刚进入页面时自动触发
- **缺点2:**如果侦听的是一个对象,对象的属性发生变化,不会触发侦听器

**对象格式侦听器:**

```javascript
username{
    hander(newVal,oldVal){
        console.log(newVal,oldVal);
    },
        //immediate 选项默认值是 false 
        //immediate 的作用是 控制侦听器是否自动触发一次
        immediate:true,
}
```

- **优点1:**可以通过`immediate` 选项自动触发
- **优点2:**可以通过`deep`选项侦听对象中每一个属性的变化

**注意:**

- 如果要侦听的是对象的子属性的变化,必须包裹一层单引号

- `'info.username'(newVal){}`

## 3.4 计算属性

计算属性指的是**通过一系列运算**之后，最终得到一个**属性值**。
**这个动态计算出来的属性值**可以被模板结构或`methods`方法使用.

**代码演示:**

```html
<div class="bg" :style="{background:rgb}">{{rgb}}</div>
<script>
    const vm = new Vue({
        el: '.app',
        data: {
            r:0,
            g:0,
            b:0,
        },
        computed:{
            rgb(){
                return `rgb(${this.r},${this.g},${this.b})`
            }
        }
    });
</script> 
```

**注意:**

- 使用`{}`插入想要的数据
- 使用`${}`传递数据(ES6语法)
- 使用``包裹想要的传递数据的语句(ES6语法)

**特点:**

- 定义的时候，要被定义为“方法”
- 在使用计算属性的时候，当普通的属性使用即可

## 3.5 axios

- `axios`是一个专注于网络请求的库

**中文官网:**

https://axios-http.com/zh/docs/intro

**语法:**

```javascript
axios({
    method:'请求的类型",
    url: '请求的 URL地址',
    //url中的查询参数
    params:{
    	id:1
	}
}).then((result) => {
    //.then用来指定请求成功之后的回调函数
    //形参中的 result是请求成功之后的结果
})
```

**返回值:**

- `Promise`实例

**注意:**

- 使用`url`时应注意`url`的协议

- `result`并不是服务器返回的真实数据,`result.data`中的才是
- `axios`在请求到数据之后,在真正的数据之外,还套用了一层壳

### 3.5.1 结合async和await调用axios

**代码演示:**

```html
```

### 3.5.2 使用解析赋值

### 3.5.3 基于axios.get和axios.post发起请求

## 3.6 vue-cli

### 3.6.1 简介

`vue-cli`是`Vue.js`开发的标准工具。它简化了程序员基于`webpack`创建工程化的`Vue`项目的过程

**中文官网:** [https://cli.vuejs.org/zh/]:

### 3.6.2 安装和使用

`vue-cli`是`npm`上的一个全局包，使用`npm install`命令，即可方便的把它安装到自己的电脑上

- `npm install -g @vue/cli`

**使用步骤:**

1. 在终端运行以下命令`vue create 项目的名称`

**注意:**如果出现脚本无法运行的情况,请在管理员权限下的`powershell`中运行以下命令`set-ExecutionPolicy RemoteSigned`选择Y,即可执行脚本

2. 在出现的选择界面选择指定配置项`Manually select features`

3. 配置界面中选择以下项目:`babel` ,`CSS Pre-processors`
4. 在选择`Vue`版本界面选择 `Vue 2.x`版本
5. 在样式表选择界面选择`Less`
6. 配置项安放位置选择默认 `In dedicated config files`独立文件中

7. 设置 配置项 是否设为预设
8. 设置 预设 名称
9. vue-cli 自动创建项目

### 3.6.3 首次运行项目

1. `cd .\项目名目录\`
2. `npm run serve`

3. 使用浏览器访问`http://localhost:8080/`(默认为该地址)

### 3.6.4 项目的src目录构成

- **assets 文件夹:**存放项目中用到的静态资源文件，例如: css样式表、图片资源
- **components 文件夹:**程序员封装的、可复用的组件，都要放到`components`目录下
- **main.js** 是项目的入口文件。整个项目的运行，要先执行`main.js`
- **App.vue** 是项目的根组件

## 3.7 组件的基本使用

### 3.7.1 vue中的组件化开发

`vue`是一个**支持组件化开发**的前端框架.

`vue`中规定:**组件的后缀名**是`.vue`.

### 3.7.2 导入vue根组件

```javascript
import 组件 from './组件名.vue'
new Vue({
    el:'#app',	//index.html中指定的div元素
    render:h=>h(组件名),
}).$mount('#app')	//与el属性完全相同
```

### 3.7.3 vue组件的三个组成部分

每个`.vue`组件都由3部分构成，分别是:

- `template`->组件的模板结构
- `script` ->组件的`JavaScript`行为
- `style` ->组件的样式

**代码演示:**

```html
<template>
  <!-- template 标签下只能有一个根节点 -->
  <div class="test-box">
    <h3>这是用户自定义的Vue组件---{{username}}</h3>
  </div>
</template>
<script>
  //默认导出
  export default{
    data() {
      return {
        username:'admin',
      }
    },
  }
</script>
<style lang="less">
   /* 使用less语法 */
  div{
    background-color: pink;
  }
</style>
```

**注意:**

- 组件中的`data`不能指向对象
- 组件中的`data`必须是一个函数
- `template`标签下只能有一个根节点

### 3.7.4 使用组件的三个步骤

1. 使用`import`语法导入需要的组件

2. 使用`components`节点注册组件
3. 以标签形式使用刚才注册的组件

**代码演示:**

```html
<template>
 <div class="app-container">
  <h1>Vue根节点</h1>
  <hr/>
  <!-- 使用组件标签 -->
  <Left></Left>
 </div>
</template>
<script>
//导入vue组件
import left from '@/components/left.vue'
//默认导出
export default {
  //注册组件
  //在components节点下注册的组件为私有组件
 components:{
  'Left':left,
 }
};
</script>
<style lang="less"> 
.app-container{
  background-color: rgb(230,230,230);
}
</style>
```

### 3.7.5 使用Vue.component注册全局组件

在`vue`项目的`main.js`入口文件中，通过`Vue.component()`方法，可以注册全局组件.

**代码演示:**

```javascript
import left from '@/components/left.vue'
Vue.component('Left',left)
```

### 3.7.6 组件里的props

`props`是组件的**自定义属性**，在**封装通用组件**的时候，合理地使用`props`可以极大的**提高组件的复用性**

`props`中的数据,可以直接在模板结构中使用

**代码演示:**

```html
<component init="6"></component>
props:['init']	//'init为自定义属性名'
```

**注意:**

- `props`属性需要在**组件标签内定义**
- `<p init="6"></p>`属性中的值为字符串型
- 使用`v-bind`绑定属性后,属性值为数字型
- `props`是只读的,如果后期需要修改,应该将`props`中的值转存到 `data`中

### 3.7.7 props 的 default 默认值

在声明自定义属性时，可以通过`default`来定义属性的默认值。

**代码演示:**

```javascript
props:{
    init:{
        default:0,
    }
}
```

### 3.7.8 props 的 type 值类型

在声明自定义属性时，可以通过`type`来**定义属性的值类型**。

**代码演示:**

```javascript
props:{
    init:{
        default:0,
        type:Number,
    }
}
```

### 3.7.9 props 的 required 必填项

**代码演示:**

```javascript
props:{
    init:{
        default:1,
        type:Number,
        required:true,
    }
}
```

### 3.7.10 组件之间的样式冲突问题

默认情况下，**写在.vue组件中的样式会全局生效**，因此很容易造成**多个组件之间的样式冲突问题**

导致组件之间样式冲突的根本原因是︰

- 单页面应用程序中，所有组件的DOM结构，都是基于**唯一的index.html页面**进行呈现的
- 每个组件中的样式，都会**影响整个index.html页面**中的DOM元素

**解决方法:**

- 使用`scoped`属性

**语法:**

- `<style scoped></style>`

**原理:**

- 编译器在`style`包含的元素标签内自动添加一个`data-v-xxx`属性
- 对应的`style`样式中多了一个`data-v-xxx`的属性选择器

### 3.7.11 使用deep修改子组件的样式

**语法:**

- `/deep/ element{样式表}`

**作用:** 在父组件中修改子组件样式,当使用第三方UI库时,如果有修改组件默认样式的需求,需要使用`/deep/`

### 3.7.12 组件的实例对象

**组件的实例化过程:**

- **`Vue`组件需要在使用标签引用后才会真正实例化,不使用标签则不实例化**

## 3.8 组件的生命周期

### 3.8.1 生命周期和生命周期函数

**生命周期**(Life Cycle)

- 是指一个组件从**创建**->**运行**-→**销毁**的整个阶段，**强调的是一个时间段**.

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/6f2c97f045ba988851b02056c01c8d62.png)

**Init Event & Lifecycle**

- 初始化事件和生命周期函数

**beforeCreate**

- 组件中的` props data methods  `尚未被创建,都处于不可用状态

**Init injections & reactivity**

- 初始化 `props data methdos`

**created** 

- 组件的` props data methods `已创建好,都处于可用的状态,但是组件的模板结构尚未生成

**beforeMount**

- 将要把内存中编译好的HTML结构渲染到浏览器中。此时浏览器中还没有当前组件的DOM结构.

**Create vm.$el and replace "el" with it** 

- 用内存中编译生成的`HTML`结构,替换掉`el` 属性指定的`DOM`元素.

**mounted**

- 已经把内存中的`HTML`结构，成功的渲染到了浏览器之中。此时浏览器中已然包含了当前组件的`DOM`结构.

**beforeUpdate**

- 将要根据变化过后,最新的数据,重新渲染组件的模板结构

**Virtual DOM re-render and patch** 

- 根据最新的数据,重新渲染组件的`DOM`结构

**Updated**

- 已经根据最新的数据，完成了组件`DOM`结构的重新渲染.

**beforeDestroy**

- 将要销毁此组件,此时尚未销毁

**Teardown watchers ,child components and event listeners**

- 销毁当前组件的数据侦听器,子组件,事件监听

**destroyed**

- 组件已经被销毁,此组件在浏览器中对应的`DOM`结构已被完全移除



**生命周期函数:**

- 是由`vue`框架提供的内置函数，会伴随着组件的生命周期，自动按次序执行。

| 函数              | 描述                                                         |
| ----------------- | ------------------------------------------------------------ |
| `beforeCreate()`  | 组件中的` props data methods  `尚未被创建,都处于不可用状态   |
| `created()`       | 组件的` props data methods `已创建好,都处于可用的状态,但是组件的模板结构尚未生成 |
| `beforeMount()`   | 将要把内存中编译好的HTML结构渲染到浏览器中。此时浏览器中还没有当前组件的DOM结构. |
| `mounted()`       | 已经把内存中的`HTML`结构，成功的渲染到了浏览器之中。此时浏览器中已然包含了当前组件的`DOM`结构. |
| `beforeUpdate()`  | 将要根据变化过后,最新的数据,重新渲染组件的模板结构           |
| `Updated()`       | 已经根据最新的数据，完成了组件`DOM`结构的重新渲染.           |
| `beforeDestroy()` | 将要销毁此组件,此时尚未销毁                                  |
| `destroyed()`     | 组件已经被销毁,此组件在浏览器中对应的`DOM`结构已被完全移除   |

**代码演示:**

```javascript
<script>
//默认导出
export default {
  beforeCreate:{

  },
  created:{

  },
};
</script>
```

## 3.9 组件之间的数据共享

### 3.9.1 组件之间的关系

**组件之间常见的关系:**

- 父子关系
- 兄弟关系

### 3.9.2 父组件向子组件共享数据

父组件向子组件共享数据需要使用**自定义属性**

**代码演示:**

```html
//父组件
<father :msg="message" :user="userinfo"></father>
data(){
	return{
		message:'Vue father',
		userinfo:{name:'zs',age:18}
	}
}
```

```html
//子组件
<template>
    <div>
        <h5>Son组件</h5>
        <p>父组件传递的 msg  值{{msg}}</p>
        <p>父组件传递的 user 值{{user}}</p>
    </div>
</template>
props:['msg','user']
```

**注意:**

- 不要在子组件中修改父组件传递的值,因为值已经存储在了`props`中

### 3.9.3 子组件向父组件共享数据

子组件向父组件共享数据需要使用**自定义属性**

**代码演示:**

```java
//子组件
export default {
    data(){
		return { count: 0}
},
methods:{
    add(){
	this.count += 1
    //修改数据时，通过 $emit(）触发自定义事件
    this.$emit('numnchamge',this.count)
    }
  }
}                                    
```

```javascript
//父组件
<Son@numchange="getNewCount"></Son>
export default {
	data(){
		return { countFromSon: 0 }
}，
methods:{
	getNewCount(val){
		this.countFromSon = val
		}
	}
}
```

### 3.9.4 兄弟组件之间的数据共享

在`vue2.x`中，兄弟组件之间数据共享的方案是`EventBus`.

**EventBus的使用步骤**

1. 创建`eventBus.js`模块，并向外共享一个`Vue`的实例对象
2. 在**数据发送方**，调用`bus.$emit`('事件名称'，要发送的数据)方法**触发自定义事件**
3. 在**数据接收方**，调用`bus.$on`('事件名称'，事件处理函数)方法**注册一个自定义事件**

**代码演示:**

```javascript
import bus from './eventBus.js'
//兄弟组件A(数据发送方)
export default {
 data(){
	return{
	msg:'hello vue.js'
    }
   },
    methods:{
        sendMsg(){
            bus.$emit('share',this.msg)
        }
	}
}
```

```javascript
import Vue from 'vue'
//eventBus.js
//向外共享Vue的实例对象
export default new Vue()
```

```javascript
import bus from './eventBus.js'
//兄弟组件B（数据接收方)
export defaul{
    data(){
	return{
		msgFromLeft:'',
		}
	},
    created(){
        bus.$on('share',val=>{
            this.msgFromLeft = val
        })
    }
}
```

## 3.10 ref 引用

### 3.10.1 简介

`ref`用来辅助开发者在**不依赖于jQuery**的情况下，获取`DOM`元素或组件的引用。
每个`vue`的组件实例上，都包含一个`$refs`对象，里面存储着对应的`DOM`元素或组件的引用。默认情况下，组件的`$refs`指向一个空对象.

### 3.10.2 引用DOM

**代码演示**:

```html
<h3 ref="x1">count组件</h3>
<script>
    this.$refs.x1.style.color='red'
</script>
```

### 3.10.3 引用组件

**代码演示**:

```html
<component ref="x1">count组件</component>
<script>
    this.$refs.x1.count = 0;
</script>
```

### 3.10.4 $nextTick(callback)方法

组件的`$nextTick(callback)`方法，会把`callback`回调推迟到下一个`DOM`更新周期之后执行.

**作用:**使回调函数可以操作到最新的`DOM`元素

**代码演示:**

```javascript
this.$nextTick(()=>{
    this.$refs.com.func()
})
```

**注意:**不能使用`update()`函数,因为组件数据更新时会触发`update()`,而不是组件`DOM`更新时触发.

## 3.11 数组中的方法

### 3.11.1 some方法

**特点:**在找到元素后跳出循环

**代码演示:**

```javascript
const arr=['23','31','23','234'];
arr.some((item,index)=>{
  if(item=='31')
  {
    console.log(item);
    return true;
  }
})
```

### 3.11.2 every方法

**特点:**全部为某个值是结果才为某个值

**代码演示:**

```javascript
const result = arr.every(item =>item.state===true)
```

### 3.11.3 reduce方法

**特点:**循环累加

**代码演示:**

```javascript
const result = arr.filter(item =>item.state).reduce((累加的结果，当前循环项)=>{
    return amt += item.price * item.count

}，初始值)
```

```javascript
//reduce简写
const result = arr.filter(item =>item.state).reduce((累加的结果，当前循环项)=>amt += item.price * item.count，初始值)
```

##  3.12 动态组件

### 3.12.1 概念

**动态组件：**

- 动态切换组件的显示和隐藏

### 3.12.2 component 标签

`vue`提供了一个内置的`<component>`组件，专门用来实现动态组件的渲染.

**语法:**

- `<component is="test"></component>`静态绑定
- `<component :is="test"></component>`动态绑定

### 3.12.3 keep-alive 标签

默认情况下，切换动态组件时无法保持组件的状态.此时可以使用`vue` 内置的`<keep-alive>`组件保持动态组件的状态.

**语法:**

- `<keep-alive><component :is="test"></component></keep-alive>`

#### 3.12.3.1 keep-alive 对应的生命周期函数

| 函数        | 描述                                                         |
| ----------- | ------------------------------------------------------------ |
| deactivated | 当组件**被缓存**时，会自动触发组件的`deactivated`生命周期函数. |
| activated   | 当组件**被激活**时，会自动触发组件的`activated`生命周期函数. |

#### 3.12.3.2 keep-alive 的 include 和 exclude 属性

- `include`属性用来指定:只有**名称匹配的组件**会被缓存.

- `exclude`属性用来指定:**那些组件不会被缓存**.

- 多个组件名之间使用**英文的逗号**分隔

```html
<keep-alive include="MyLeft,MyRight">
    <component :is="comName"></component>
</keep-alive>
```

#### 3.12.3.3 组件注册名称和组件声明名称name

 **组件注册名称:**

```xml
<header></header>
<body></body>
<footer></footer>
components: {
    header,
    body,
    footer,
}
```

**组件声明名称name:**

```xml
<keep-alive include="MyLeft,MyRight"></keep-alive>
//Left.vue 
export default {
	name:'MyLeft',
}
```

**主要作用:**

- 结合`<keep-alive>`标签实现组件缓存的功能,以及在调试工具中查看组件的 `name` 名称

**注意:**

- `name`内名称首字母应该大写

## 3.13 插槽

### 3.13.1 概念

**插槽(Slot)**是`vue`为**组件的封装者**提供的能力。允许开发者在封装组件时，把**不确定的、希望由用户指定的部分**定义为插槽.

### 3.13.2 基本用法

**代码演示:**

```xml
<!-- component.vue -->
<slot name="default"></slot><!-- 接收App.vue传递的组件和标签 -->
<!-- App.vue -->
<component>
    <template v-slot:default>
        <div>向组件传递的一个div标签</div>
    </template>
</component>
```

### 3.13.3 v-slot 的简写

**语法:**

- `v-slot `->`#`

### 3.13.4 后备内容

封装组件时，可以为预留的`<slot>`插槽提供后备内容（默认内容）。如果组件的使用者没有为插槽提供任何内容，则后备内容会生效.

**代码演示:**

```xml
<slot><h1>这是slot标签的后背内容</h1></slot>
```

###  3.13.5 作用域插槽的基本用法

**代码演示:**

```xml
<template #content="obj">
    <h1>{{obj}}</h1>
</template>
<!-- component.vue -->
<slot name="content" msg="hello world"></slot>
```

## 3.14 自定义指令

**vue中的自定义指令:**

- 私有自定义指令

- 全局自定义指令

### 3.14.1 私有自定义指令

在每个`vue`组件中,可以在`directives`节点下声明私有自定义指令

```javascript
directives:{
    color:{
        //为绑定到的 HTML 元素设置颜色
        bind(el,binding){
            //形参中的el是绑定了此指令的,原生的DOM对象
            el.style.color = binding.value;
        }
    }
}
```

### 3.14.2 update函数

`bind`函数只调用一次:当指令第一次绑定到元素时调用,当DOM更新时`bind`函数不会被触发.`update`函数会在每次DOM更新时被调用.

```javascript
directives:{
    color:{
        //每次 DOM 更新时被调用
        update(el,binding){
            el.style.color = binding.value;
        }
    }
}
```

### 3.14.3 函数简写

```javascript
directives:{
    color(el,binding):{
        el.style.color = binding.value;
    }
}
```

### 3.14.4 全局自定义指令

全局共享的自定义指令需要通过`Vue.directive()`进行在`main.js`文件中声明

```javascript
Vue.directive('color',function(el,binding){
    el.style.color = binding.value;
})
```

## 3.15 过渡和动画

Vue 在插入、更新或者移除 DOM 时，提供多种不同方式的应用过渡效果。包括以下工具：

- 在 CSS 过渡和动画中自动应用 class
- 可以配合使用第三方 CSS 动画库，如 Animate.css
- 在过渡钩子函数中使用 JavaScript 直接操作 DOM
- 可以配合使用第三方 JavaScript 动画库，如 Velocity.js

### 3.15.1 单元素/组件过渡

Vue 提供了 `transition` 的封装组件，在下列情形中，可以给任何元素和组件添加进入/离开过渡

- 条件渲染 (使用 `v-if`)
- 条件展示 (使用 `v-show`)
- 动态组件
- 组件根节点

```html
<!-- html -->
<div id="demo">
  <button v-on:click="show = !show">
    Toggle
  </button>
  <transition name="fade">
    <p v-if="show">hello</p>
  </transition>
</div>
```

```javascript
//Javascript
new Vue({
  el: '#demo',
  data: {
    show: true
  }
})
```

```css
/*CSS*/
.fade-enter-active, .fade-leave-active {
  transition: opacity .5s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}
```

**注意**:

- CSS样式表中的类选择器对应HTML中的`transition`的`name`属性

### 3.15.2 过渡的类名

| 类名             | 描述                                                         |
| ---------------- | ------------------------------------------------------------ |
| `v-enter`        | 定义进入**过渡的开始**状态。在元素被插入之前生效，在元素被插入之后的下一帧移除。 |
| `v-enter-active` | 定义**进入过渡生效时的状态**。在整个进入过渡的阶段中应用，在元素被插入之前生效，在过渡/动画完成之后移除。这个类可以被用来定义进入过渡的过程时间，延迟和曲线函数。 |
| `v-enter-to`     | **2.1.8 版及以上**定义进入**过渡的结束状态**。在元素被插入之后下一帧生效 (与此同时 `v-enter` 被移除)，在过渡/动画完成之后移除。 |
| `v-leave`        | 定义**离开过渡的开始状态**。在离开过渡被触发时立刻生效，下一帧被移除。 |
| `v-leave-active` | 定义**离开过渡生效时的状态**。在整个离开过渡的阶段中应用，在离开过渡被触发时立刻生效，在过渡/动画完成之后移除。这个类可以被用来定义离开过渡的过程时间，延迟和曲线函数。 |
| `v-leave-to`     | **2.1.8 版及以上**定义**离开过渡的结束状态**。在离开过渡被触发之后下一帧生效 (与此同时 `v-leave` 被删除)，在过渡/动画完成之后移除。 |



# 4. 路由

## 4.1 概念

路由(router)是对应关系

即Hash 地址与组件之间的对应关系

## 4.2 工作方式

1. 用户点击页面的路由链接
2. URL地址栏中Hash值发生变化
3. 前端路由监听到Hash地址的变化
4. 前端路由把当前Hash地址对应的组件渲染到浏览器中

## 4.3 vue-router

`vue-router`是`vue.js `官方给出的路由解决方案。它只能结合`vue`项目进行使用，能够轻松的管理SPA项目中组件的切换.

`vue-router`的官方文档地址: [https://router.vuejs.org/zh/]:

### 4.3.1 安装配置

1. 安装`vue-router`包
2. 创建路由模块
3. 导入并挂载路由模块
4. 声明路由链接和占位符

**安装vue-router包**

- ` npm i vue-router@3.5.2 -S`

**在`src`源代码目录下，新建`router/index.js`路由模块，并初始化如下的代码**

```javascript
//1．导入 Vue和 VueRouter 的包
import Vue from 'vue '
import VueRouter from 'vue-router'
//2．调用Vue.use()函数，把 VueRouter安装为Vue的插件
    Vue.use(VueRouter)
//3．创建路由的实例对象
const router = new VueRouter({
    routes:[]
})
//4．向外共享路由的实例对象
export default router
```

**在`main.js`中导入并挂载路由模块**

```javascript
import router from '@/router/index.js'
new Vue({
    router:router
}) 
```

**声明路由链接和占位符**

```javascript
//	@/router/index.js

//导入的组件
import home from '@/component/home.vue'
import movie from '@/component/movie.vue'
import about from '@/component/about.vue'

const router = new VueRouter({
    routes:[
        {path: '/home',component: home},
        {path: '/movie',component: movie},
        {path: '/about',component: about},
    ]
})
```

```xml
//占位符
<router-view></router-view>
```

### 4.3.2 使用router-link替代a标签

**语法:**

```xml
<router-link to="/home">首页</router-link>
<router-link to="/movie">电影</router-link>
<router-link to="/about">关于</router-link>
```

## 4.4 vue-router的常见用法

### 4.4.1 路由重定向

**路由重定向**:

- 用户在访问**地址A**的时候，**强制用户跳转**到地址C，从而展示特定的组件页面。通过路由规则的`redirect`属性，指定一个新的路由地址，可以很方便地设置路由的重定向

```javascript
const router =new VueRouter({
    routes: [
        {path:'/',redirect: '/home'},
        {path: '/home',component: home},
        {path: '/movie',component: movie},
        {path: '/about',component: about},
    ]
})
```

### 4.4.2 嵌套路由

通过路由实现**组件的嵌套展示**，叫做嵌套路由.

#### 4.4.2.1 声明子级链接和占位符

```xml
<!-- about.vue 下 -->
<router-link to="/about/tap1">tap1 </router-link>
<router-link to="/about/tap2">tap2</router-link>
<router-view></router-view>
```

#### 4.4.2.2 声明嵌套路由规则

使用 `children`属性声明子路由规则

```javascript
//在/router/index.js下
const router = new VueRouter({
    routes: [
        { path: '/', redirect: '/home' },
        { path: '/home', component: home },
        { path: '/movie', component: movie },
        {
            path: '/about',
            component: about,
            children: [
                {path:'/',redirect:'tap1'},
                { path: 'tap1', component: tap1 },
                { path: 'tap2', component: tap2 },
            ]
        },
    ]
})
```

#### 4.4.2.3 默认子路由

**默认子路由:**

- 如果`children`组中，某个路由规则的`path`值为空字
  符串，则这条路由规则，叫做**“默认子路由”**

```javascript
children: [
    { path: '', component: tap1 }, //默认子路由
    { path: 'tap2', component: tap2 },
]
```

## 4.5 动态路由

### 4.5.1 概念

**动态路由**:把 `Hash`地址中**可变的部分**定义为**参数项**，从而**提高路由规则的复用性**.

### 4.5.2 基本用法

在`vue-router`中使用英文的冒号(`:`）来定义路由的参数项

- `{path: '/movie/:id', component: movie}`

在子组件中获得路由的参数项:

- `this.$route.params.id`

### 4.5.3 为路由规则开启 props 传参

**路由规则**

```javascript
{path: ':id',component: movie, props: true}
```

**接收props**

```javascript
props:['id']
```

### 4.5.4 查询参数 query

在路由“参数对象”中，需要使用`this.$route.query`来访问查询参数

### 4.5.5  完整路径 fullpath

在`this.$route`中,`path`只是路径部分;`fullPath`是完整的地址

## 4.6 导航

### 4.6.1 声明式导航和编程式导航

在浏览器中，**点击链接实现导航**的方式，叫做**声明式导航**.

- 普通网页中点击`<a>`链接、`vue`项目中点击`<router-link>`都属于声明式导航

在浏览器中，**调用API方法**实现导航的方式，叫做**编程式导航**.

- 普通网页中调用`location.href`跳转到新页面的方式，属于编程式导航

### 4.6.2 vue-router中的编程式导航

vue-router提供了许多编程式导航的API，其中最常用的导航API分别是:

| 函数                               | 描述                                         |
| ---------------------------------- | -------------------------------------------- |
| `this.$router.push('hash地址')`    | 跳转到指定`hash`地址，并增加一条历史记录     |
| `this.$router.replace('hash地址')` | 跳转到指定`hash`地址，并替换掉当前的历史记录 |
| `this.$router.go(数值 n)`          | 前进或者后退 n 个历史记录                    |
| `this.$router.forward()`           | 前进一个历史记录                             |
| `this.$router.back()`              | 后退一个历史记录                             |

### 4.6.3 导航守卫

**导航守卫**可以控制**路由的访问权限**.

#### 4.6.3.1 全局前置守卫

每次发生路由的**导航跳转**时，都会触发**全局前置守卫**。因此，在全局前置守卫中，程序员可以对每个路由进行**访问权限**的控制:

```javascript
router.beforeEach((to,from,next) =>{
    //to是将要访问的路由的信息对象
	//from是将要离开的路由的信息对象
	//next是一个函数，调用next()表示放行，允许这次路由导航
})
```

只要发生了路由的跳转，必然会触发`beforeEach`指定的`function`回调函数

#### 4.6.3.2 next函数的3种调用方式

| 方式             | 描述                                                 |
| ---------------- | ---------------------------------------------------- |
| `next()`         | 当前用户拥有后台主页的访问权限，直接放行             |
| `next('/login')` | 当前用户没有后台主页的访问权限，强制其跳转到登录页面 |
| `next(false)`    | 当前用户没有后台主页的访问权限，不允许跳转到后台主页 |

#### 4.6.3.3 控制访问权限

1. 要拿到用户将要访问的`hash`地址

2. 判断`hash`地址是否等于`/main`.

2. 1. 如果等于`/main`，证明需要登录之后，才能访问成功

2. 2. 如果不等于`/main`，则不需要登录，直接放行`next()`

3. 如果访问的地址是`/main`.则需要读取`localStorage`中的`token`值

3. 1. 如果有`token`，则放行

3. 2. 如果没有`token`，则强制跳转到`/login`登录页

```javascript
router.beforeEach((to,from，next) =>{
    if(to.path === '/main'){
		const token = localStorage.getItem('token')
        if (token){
			next() //访问的是后台主页，且有token的值
        }else {
			next('/login')//访问的是后台主页,但是没有 token的值
        }
	}else{
	next()//访问的不是后台主页，直接放行
	}
})
```

# 5. Vue3简介

## 5.1 Vue3.x和Vue2.x的对比

`vue2.x`中绝大多数的`API`与特性，在`vue3.x`中同样支持。同时，`vue3.x`中还新增了3.x所特有的功能、并废弃了某些2.x中的旧功能:

**新增的功能例如:**

- 组合式`API`

- 多根节点组件
- 更好的`TypeScript`支持等

**废弃的旧功能如下:**
过滤器、不再支持`$on`,`$off `和`$once`实例方法等

**详细的变更信息，请参考官方文档给出的迁移指南:**
https://v3.vuejs.org/guide/migration/introduction.html

## 5.2 选项式API和组合式API

在`Vue2.x`的学习笔记中使用的均为**选项式API风格**

**选项式 API**

使用**选项式 API**，我们可以用包含多个选项的对象来描述组件的逻辑，例如 `data`、`methods` 和 `mounted`。选项所定义的属性都会暴露在函数内部的 `this` 上，它会指向当前的组件实例.

```html
<script>
export default {
  data() {
    return {
      count: 0
    }
  },
  methods: {
    increment() {
      this.count++
    }
  },
  mounted() {
    console.log(`The initial count is ${this.count}.`)
  }
}
</script>
```

**组合式API**

通过组合式 API，我们可以使用导入的 API 函数来描述组件逻辑。在单文件组件中，组合式 API 通常会与`<script setup>`搭配使用。这个 `setup` attribute 是一个标识，告诉 Vue 需要在编译时进行一些处理，让我们可以更简洁地使用组合式 API。比如，`<script setup>` 中的导入和顶层变量/函数都能够在模板中直接使用.

```html
<script setup>
import {ref, onMounted } from 'vue'
const count = ref(0)
function increment() {
  count.value++
}
onMounted(() => {
  console.log(`The initial count is ${count.value}.`)
})
</script>
```

**区别:**

- 它们只是同一个底层系统所提供的两套不同的接口
- 选项式 API 是在组合式 API 的基础上实现的
- 选项式 API 以“组件实例”的概念为中心 (即上述例子中的 `this`)
- 组合式 API 的核心思想是直接在函数作用域内定义响应式状态变量，并将从多个函数中得到的状态组合起来处理复杂问题

**在项目中:**

- 当你不需要使用构建工具，或者打算主要在低复杂度的场景中使用 Vue，例如渐进增强的应用场景，推荐采用选项式 API。
- 当你打算用 Vue 构建完整的单页应用，推荐采用组合式 API + 单文件组件。

# 6. 单页面应用程序(SPA)

## 6.1 概念

单页面应用程序（英文名: Single Page Application）简称`SPA`，顾名思义，指的是**一个` Web` 网站中只有唯一的一个`HTML`页面**，所有的功能与交互都在这唯一的一个页面内完成.

**特点:**

单页面应用程序将所有的功能局限于一个`web`页面中，**仅在该`web`页面初始化时加载相应的资源**(`HTML`、`JavaScript`和`CSS`).

一旦页面加载完成了，`SPA`**不会因为用户的操作而进行页面的重新加载或跳转**。而是利用`JavaScript`动态地变换`HTML`的内容，从而实现页面与用户的交互.

## 6.2 优缺点

### 6.2.1 优点

- **良好的交互体验**
- **良好的前后端工作分离模式**
- **减轻服务器的压力**

**良好的交互体验**

- 单页应用的内容的改变不需要重新加载整个页面

- 获取数据也是通过Ajax异步获取

- 没有页面之间的跳转，不会出现“白屏现象”

**良好的前后端工作分离模式**

- 后端专注于提供API接口，更易实现API接口的复用
- 前端专注于页面的渲染，更利于前端工程化的发展

**减轻服务器的压力**

- 服务器只提供数据，不负责页面的合成与逻辑的处理，吞吐能力会提高几倍

### 6.2.2 缺点

- **首屏加载慢**
- **不利于SEO**

**解决方案1**:

- 路由懒加载
- 代码压缩
- CDN加速
- 网络传输压缩

**解决方案2**:

- SSR服务器端渲染

## 6.3 创建vue的SPA项目

vue官方提供了两种快速创建工程化的SPA项目的方式:

- 基于`vite `创建SPA项目
- 基于`vue-cli `创建SPA项目

|                            | vite              | vue-cli                |
| -------------------------- | ----------------- | ---------------------- |
| 支持的`vue`版本            | 仅支持`vue3.x`    | 支持`3.x`和`2.x`       |
| 是否基于`webpack`          | 否                | 是                     |
| 运行速度                   | 快                | 较慢                   |
| 功能完整度                 | 小而巧（逐渐完善) | 大而全                 |
| 是否建议在企业级开发中使用 | 目前不建议        | 建议在企业级开发中使用 |

# 7. vite 的基本使用

## 7.1 创建项目

```javascript
npm init vite-app 项目名称
cd 项目名称
npm install 
npm run dev
```

# 8. 组件库

## 8.1 概念

在实际开发中，前端开发者可以把**自己封装的`.vue`组件**整理、打包、并**发布为`npm `的包**，从而供其他人下载和使用。这种可以直接下载并在项目中使用的现成组件，就叫做 **`vue` 组件库**.

## 8.2 vue组件库和bootstrap的区别

**二者之间存在本质的区别:**

- `bootstrap`只提供了纯粹的原材料（css样式、HTML结构以及JS特效)，**需要由开发者做进一步的组装和改造**

- `vue `组件库是**遵循`vue`语法、高度定制的现成组件，开箱即用**

## 8.3 常用的 vue 组件库

**PC端**

- Element Ul ( https://element.eleme.cn/#/zh-CN)

- View Ul ( http://v1.iviewui.com/)

**移动端**

- Mint UI ( http://mint-ui.github.io/#!/zh-cn)
- Vant ( https://vant-contrib.gitee.io/vant/#/zh-CN/ )
  

## 8.4 Element UI

`Element UI`是饿了么前端团队开源的一套PC端vue组件库。支持在`vue2`和`vue3`的项目中使用:

- `vue2`的项目使用旧版的Element UI( https://element.eleme.cn/#/zh-CN )

- `vue3`的项目使用新版的Element Plus (https://element-plus.gitee.io/#/zh-CN)

### 8.4.1 安装和引入 element UI

**安装**

```
npm i element-ui -S
```

**引入 element ui**

开发者可以一次性完整引入所有的`element-ui`组件，或是根据需求，只按需引入用到的`element-ui`组件:

**完整引入**

```javascript
//1. 引入组件
import ElementUI from 'element-ui'
//2. 引入样式
import 'element-ui/lib/theme-chalk/index.css'
//3. 把ElementUI 注册为 vue 的插件
//注册后即可在每个组件中直接使用element ui 的组件
Vue.use(ElementUI)
```

**按需引入**
借助 `babel-plugin-component`，我们可以只引入需要的组件，以达到减小项目体积的目的。

1. 安装`babel-plugin-component`

```
npm install babel-plugin-component -D
```

2. 修改根目录下的`babel.config.js`配置文件，新增`plugins`节点如下:

```javascript
module.exports = {
    presets: [ '@vue/cli-plugin-babel/preset' ],
	plugins: [
    	[
			'component',
            {
				libraryName: 'element-ui',
				styleLibraryName: 'theme-chalk'，
			}，
		],
    ]
}
```

3. 如果你**只希望引入部分组件**，比如`Button`，那么需要在`main.js`中写入以下内容:

```javascript
import {Button} from 'element-ui'
Vue.component(Button.name,Button)
//或 Vue.use(Button)
```

### 8.4.2 把组件的导入和注册封装为独立的模块

**步骤**

1. 在`src`目录下新建`element-ui/index.js`模块，并声明如下的代码:

```javascript
//→模块路径	/src/element-ui/index.js
import Vue from 'vue'
//按需导入 element ui 的组件
import { Button，Input } from 'element-ui'
/注册需要的组件
vue.use(Button)
Vue.use(Input)
//在main.js中导入
import './element-ui'
```

## 8.5 Vant-UI

Vant 是一个**轻量、可定制的移动端组件库**，于 2017 年开源。

### 8.5.1 安装和引入Vant-UI

**安装：**

```
npm i vant@next -S
```

**全部引入**

```javascript
// 1. 引入你需要的组件
import Vant from 'vant';
// 2. 引入组件样式
import 'vant/lib/index.css';
const Vue = createApp();
// 3. 注册你需要的组件
Vue.use(Vant);
```



# 9. axios 拦截器

## 9.1 在 vue2 项目中全局配置 axios

安装`axios`

```javascript
npm install axios@0.21.1 -S
```

需要在`main.js`入口文件中，通过`Vue`构造函数的`prototype`原型对象全局配置 `axios`:

```javascript
//1. 导入 axios
import axios from 'axios'
//2. 配置请求根路径
axios.defaults.baseURL = 'https://www.escook.cn'
//3. 通过 Vue 构造函数的原型对象,全局配置 axios
Vue.prototype.$http = axios
```

```javascript
//在App.vue组件中发起axios请求
methods:{
    async getInfo(){
        const {data: res} = await this.$http.get('/api/get',{params:{name: 'zs',age:20}})
        console.log(res)
    }
}
```

## 9.2 拦截器概念

**拦截器**（英文: Interceptors）会在**每次发起ajax请求和得到响应**的时候自动被触发。

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/f8ce14173b79a510f80888f597713ad3.png)

## 9.3 配置请求拦截器

通过`axios.interceptors.request.use(成功的回调,失败的回调)`可以配置请求拦截器.

```javascript
axios.interceptors.request.use( function (config){
	//Do something before request is sent
	return config;
}, function (error){
	//Do something with request error
	return Promise.reject(error);
})
```

**注意:失败的回调函数可以被省略**

### 9.3.1 请求拦截器 - Token认证

```javascript
import axios from 'axios"
axios.defaults.baseURL = "https://www.escook.cn'
//配置请求的拦截器
axios.interceptors.request.use(config =>{
    //为当前请求配置Token认证字段
	config.headers.Authorization = 'Bearer xxx'
    return config
})
Vue.prototype.$http = axios
```

### 9.3.2 请求拦截器–展示Loading效果

借助于`element ui`提供的`Loading`效果组件(https://element.eleme.cn/#lzh-CN/component/loading)可以方便的实现`Loading`效果的展示:

```javascript
//1．按需导入 loading效果组件
import { Loading } from 'element-ui'
//2．声明支量，用来存储Loading组件的实例对象
let loadingInstance = null
//配置请求的拦截器
axios.interceptors.request.use(config =>{
	//3．调用loading组件的 service()方法，创建loading组件的实例，并全屏展示 loading效果
    loadingInstance = Loading.service({ fullscreen: true })
	return config
})
```

### 9.3.3 配置响应拦截器

通过`axios.interceptors.response.use(成功的回调，失败的回调)`可以配置响应拦截器。

```javascript
//配置响应拦截器
axios.interceptors.response.use(function (response) {
	//关闭 loading 效果
	return response;
},function (error) {
	return Promise.reject(error);
});
```

**注意:失败的回调函数可以被省略**

# 10. proxy 跨域代理

## 10.1 跨域代理问题

- vue项目运行的地址: http://localhost:8080/
- API接口运行的地址: https://www.escook.cn/api/users

由于当前的API接口**没有开启CORS**跨域资源共享，因此默认情况下，上面的接口**无法请求成功**!

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/a75956df43c63e6e24d0d23af52cc696.png)

## 10.2 通过代理解决

通过`vue-cli`创建的项目在遇到接口跨域问题时，可以通过**代理**的方式来解决:

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/003c04bd35be607832602d497abd985b.png)

1. 把axios 的**请求根路径**设置为**vue项目的运行地址**（接口请求不再跨域)

2. vue项目发现请求的接口不存在，把请求**转交给proxy 代理**

3. 代理把请求根路径**替换为**`devServer.proxy`属性的值，**发起真正的数据请求**

4. 代理把请求到的数据，**转发给axios**

## 10.3 在项目中配置 proxy 代理

1. 在 `main.js` 入口文件中，把**` axios` 的请求根路径**改造为**当前`web`项目的根路径**:
2. 在**项目根目录**下创建`vue.config.js`的配置文件，并声明如下的配置;

```javascript
module.exports = {
    devServer:{
	//当前项目在开发调试阶段，
	//会将任何未知请求(没有匹配到静态文件的请求)代理到https://ww.escook.cn
         proxy:'https://www.escook.cn',
	},
}
```

**注意:**

- `devServer.proxy`提供的代理功能，仅在**开发调试阶段生效**
- 项目上线发布时，依旧需要API接口服务器**开启CORS**跨域资源共享

# 11. vuex

## 11.1 简介

Vuex是实现组件全局状态（数据)管理的一种机制，可以方便的实现组件之间数据的共享。

![9](https://gitee.com/pepedd864/cdn-repos/raw/master/img/c25e7b066b4a55331b91dfd5199b33d3.png)

使用vuex统一管理状态的好处

- 能够在vuex中集中管理共享的数据，易于开发和后期维护
- 能够高效地实现组件之间的数据共享，提高开发效率
- 存储在vuex中的数据都是响应式的，能够实时保持数据与页面的同步

一般情况下，只有组件之间共享的数据，才有必要存储到vuex中;对于组件中的私有数据，依旧存储在组件自身的data中即可。

## 11.2 基本使用

1. 安装

```bash
npm install vuex --save
```

2. 导入vuex包

```js
import Vuex from 'vuex'
Vue.use(Vuex)
```

3. 创建store对象

```js
const store = new Vuex.store({
    // state 中存放的就是全局共享的数据
    state: {count: 0}
})
```

4. 将store对象挂载到vue实例中 

```js
new vue({
    el: '#app',
    render: h => h(app),
    router,
    store
})
```



## 11.3 vuex核心概念

### 11.3.1 state

State提供唯一的公共数据源，所有共享的数据都要统一放到Store的State中进行存储。

```js
const store = new Vuex.Store({
    state: {count: 0}
})
```

组件访问State中数据

```js
// 第一种方式
this.$store.state.全局数据名称
// 第二种方式
// 1. 从vuex中按需导入mapState函数
import { mapState } from 'vuex'
// 2. 将全局数据，映射为当前组件的计算computed属性
computed: {
    ...mapState (['count'])
}
```

### 11.3.2 Mutation

Mutation用于变更Store中的数据。

1. 只能通过mutation变更Store数据，不可以直接操作Store 中的数据。
2. 通过这种方式虽然操作起来稍微繁琐一些，但是可以集中监控所有数据的变化。

```js
const store = new Vuex.Store({
    state: {
        count: 0
    },
    mutation: {
        add(state,step) {
            // 变更状态
            state.count += step
        }
    }
})
```

```js
// 触发mutation
methods: {
    handle1 () {
        // 触发mutations 的第一种方式
        this.$store.commit('add',step)
    }
}
```

```js
// 触发mutation的第二种方式
import { mapMutations } from 'vuex'
methods: {
    ...mapMutation(['add','sub']),
    handler(){
        this.sub()
    }
}
```

### 11.3.3 Action

Action用于处理异步任务。

如果通过异步操作变更数据，必须通过Action，而不能使用Mutation，但是在Action中还是要通过触发Mutation 的方式间接变更数据。

```js
const store = new Vuex.Store({
    // ...
    mutations: {
        add(state) {
            state.count++
        }
    },
    actions: {
        addAsync(context) {
            setTimeout(() => {
                // Action中不能直接修改state的数据
                context.commit('add')
            },1000)
        }
    }
})
```

```js
// 触发Action
methods: {
    handle() {
        // 第一种方式，dispatch用于触发Action
        this.$store.dispatch('addAsync')
    }
}
```

触发actions异步任务时携带参数

```js
const store = new Vuex.Store({
    // ...
    mutations: {
        addN(state,step) {
            state.count += step
        }
    },
    actions: {
        addNAsync(context,step) {
           setTimeout(() => {
                context.commit('addN',step)
           },1000)
        }
    }
})
```

触发actions的第二种方式

```js
// 1. 导入mapActions函数
import { mapActions } from 'vuex'
// 2. 将指定的actions函数，映射为当前组件的methods函数
methods: {
    ...mapActions(['addAsync','addNAsync']),
        handler() {
        this.addAsync()
    }
}
```



### 11.3.4 Getter

Getter用于对 Store中的数据进行加工处理形成新的数据。

1. Getter可以对Store 中已有的数据加工处理之后形成新的数据，类似Vue的计算属性。
2. Store中数据发生变化，Getter的数据也会跟着变化。

```js
const store = new Vuex.Store({
    state: {
        count: 0
    },
    getters: {
        showNum: state => {
            return '当前最新的数量是['+ state.count +']'
        }
    }
})
```

访问getter的第一种方式

```js
this.$store.getters.名称
```

访问getters的第二种方式

```js
import { mapGetters } from 'vuex'

computed: {
    ...mapGetters(['showNum'])
}
```



## 11.4 案例--Todos

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/d72fda73d39d2a186c3e2ca8187cc1e7.png)

### 11.4.1 初始化项目

1. 创建项目

```bash
vue create vuex-todos
```

2. 安装依赖

```bash
npm i vuex axios ant-design-vue@1.7.8
npm i eslint less -D
```

3. 配置项目

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/7fa82e70053d862296fa67b53ecacd58.png)

```js
// prettierrc.js
module.exports = {
  printWidth: 200, // 200个字符每行
  tabWidth: 2,
  semi: false,    // 不使用分号
  singleQuote: true,  // 使用单引号
  trailingComma: 'none',  // 不使用尾逗号，eslint会报错
  bracketSpacing: true,   // 在对象字面量声明所使用的的花括号后（{）和前（}）输出空格
  insertSpaceBeforeFunctionParenthesis: true, // 在函数的左括号之前输出一个空格
}
```

```js
// .eslintrc.js
module.exports = {
  env: {
    browser: true,
    es2021: true
  },
  extends: [
    'plugin:vue/vue3-essential',
    'standard',
    'eslint:recommended'
  ],
  overrides: [
  ],
  parserOptions: {
    ecmaVersion: 'latest',
    sourceType: 'module'
  },
  plugins: [
    'vue'
  ],
  rules: {
  }
}
```



### 11.4.2 vuex如何起作用的

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/e02e34167ca0e6d38c54f1fdcc03fb1f.png)

组件或者视图通过store访问数据，可以实现异步访问(Actions)和数据加工(Getter)的操作

### 11.4.3 实现代码

```js
// main.js

// 导入Vue
import Vue from 'vue'
import App from './App.vue'
// 导入store
import store from '@/store'
// 导入ant-design-vue
import Antd from 'ant-design-vue'
import 'ant-design-vue/dist/antd.css'

Vue.config.productionTip = false
// 使用ant-design-vue
Vue.use(Antd)
// 创建一个Vue实例，挂载到#app上
new Vue({
  store,
  render: (h) => h(App)
}).$mount('#app')

```

```vue
<template>
  <div id="app">
    <h1>{{ title }}</h1>
    <div class="row">
      <a-input class="input" placeholder="请输入任务" :value="$store.state.inputValue" @change="ValueChangeHandler" />
      <a-button type="primary" class="button" @click="addItemToList">添加</a-button>
    </div>

    <a-list class="list" bordered>
      <a-list-item v-for="list in this.$store.getters.viewList" :key="list.index">
        <a-checkbox :checked="list.status" @click="cbStatusChange(list.index)"></a-checkbox>
        <a-list-item-meta :title="list.info" />
        <a @click="removeItemById(list.index)">删除</a>
      </a-list-item>
      <div class="footer">
        <span>{{ this.$store.getters.unDoneLength }}条未完成任务</span>
        <a-button-group>
          <a-button :type="this.$store.state.viewKey === 'all' ? 'primary' : 'default'" @click="changeList('all')">全部</a-button>
          <a-button :type="this.$store.state.viewKey === 'undone' ? 'primary' : 'default'" @click="changeList('undone')">未完成</a-button>
          <a-button :type="this.$store.state.viewKey === 'done' ? 'primary' : 'default'" @click="changeList('done')">已完成</a-button>
        </a-button-group>
        <a @click="cleanDone">清除已完成</a>
      </div>
    </a-list>
  </div>
</template>

<script>
export default {
  name: 'App',
  data () {
    return {
      title: '待办事项'
    }
  },
  created () {
    // 使用异步获取数据
    this.$store.dispatch('getList')
  },
  methods: {
    // 改变输入框的值
    ValueChangeHandler (e) {
      this.$store.commit('setInputValue', e.target.value)
    },
    // 添加任务
    addItemToList () {
      if (this.$store.state.inputValue.length <= 0) {
        // 如果输入框为空，提示用户
        this.$message.error('请输入任务')
      } else {
        this.$store.commit('addItemToList', this.$store.state.inputValue.trim())
      }
    },
    // 删除任务
    removeItemById (index) {
      this.$store.commit('removeItemById', index)
    },
    // 改变任务状态
    cbStatusChange (index) {
      this.$store.commit('itemStatusChangeById', index)
    },
    // 清除已完成
    cleanDone () {
      this.$store.commit('cleanDone')
    },
    // 改变列表
    changeList (key) {
      this.$store.commit('changeViewList', key)
    }
  }
}
</script>

<style lang="less" scoped>
#app {
  margin: 0 auto;
  width: 500px;
  height: 650px;
  .row {
    display: flex;
    align-items: center;
  }
  .footer {
    display: flex;
    justify-content: space-around;
    align-items: center;
  }
}
</style>

```

```js
// store.js

import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)
// 导出一个store对象
export default new Vuex.Store({
  state: {
    lists: [], // 列表数据
    inputValue: 'input', // input的值
    nextId: 0, // 下一个id
    viewKey: 'all' // 显示列表的状态
  },
  mutations: {
    // 初始化列表数据
    initList (state, list) {
      state.lists = list
      state.nextId = state.lists.length // 初始化nextId为lists的长度
    },
    // 改变input的值
    setInputValue (state, value) {
      state.inputValue = value
    },
    // 添加任务
    addItemToList (state, value) {
      const obj = {
        index: state.nextId++,
        info: value,
        status: false
      }
      state.lists.push(obj)
    },
    // 通过id删除任务
    removeItemById (state, id) {
      const i = state.lists.findIndex((x) => x.index === id)
      if (i !== -1) {
        state.lists.splice(i, 1)
      }
    },
    // 通过id改变任务的状态
    itemStatusChangeById (state, id) {
      const i = state.lists.findIndex((x) => x.index === id)
      if (i !== -1) {
        state.lists[i].status = !state.lists[i].status
      }
    },
    // 清除已完成的任务
    cleanDone (state) {
      // 直接赋值会导致视图不更新，所以需要使用splice方法
      for (let i = 0; i < state.lists.length; i++) {
        if (state.lists[i].status) {
          state.lists.splice(i, 1)
          i--
        }
      }
    },
    // 改变显示列表的状态
    changeViewList (state, key) {
      state.viewKey = key
    }
  },
  actions: {
    // 获取列表数据
    getList (context) {
      // 发起axios请求,这里省略
      context.commit('initList', [
        { index: 0, info: '任务1', status: false },
        { index: 1, info: '任务2', status: true },
        { index: 2, info: '任务3', status: true },
        { index: 3, info: '任务4', status: false }
      ])
    }
  },
  getters: {
    // 未完成的任务数量
    unDoneLength (state) {
      return state.lists.filter((x) => x.status === false).length
    },
    // 显示列表
    viewList (state) {
      if (state.viewKey === 'all') return state.lists
      if (state.viewKey === 'undone') return state.lists.filter((x) => x.status === false)
      if (state.viewKey === 'done') return state.lists.filter((x) => x.status === true)
    }
  }
})

```



# 12. vue-roter

## 12.1 简介

目前前端流行的三大框架，都有自己的路由实现：

- Angular的ngRouter
- React的ReactRouter
- Vue的vue-router

vue-router是Vue.js官方的路由插件，它和vue.js是深度集成的，适合用于构建单页面应用。
我们可以访问其官方网站对其进行学习：https://router.vuejs.org/zh/

vue-router是基于路由和组件的

- 路由用户设定访问路径的，将路径和组件映射起来。
- 在vue-router的单页面应用中，页面的路径的改变就是组件的切换

## 12.2 基本使用

1. 安装vue-router

```bash
npm install vue-router --save
```

2. 在模块化工程中使用它（因为是一个插件，所以可以通过Vue.use()来安装路由功能）

   - 导入路由对象，并且调用Vue.use(VueRouter)

   - 创建路由实例，并且传入路由映射配置

   - 在Vue实例中挂载创建的路由实例

3. 使用vue-router的步骤：

   - 第一步：创建路由组件

   - 第二步：配置路由映射：组件和路径映射关系

   - 第三步：使用路由：通过`<router-link>`和`<router-view>`



# 13. JSX

JSX是React中的用法，可以理解为将DOM元素当作变量使用

```jsx
const element = <h1>Hello, world!</h1>;
```

## 13.1 基本使用

1. 新建JSX文件
2. 安装js语法编写代码

```js
export default {
  name: 'CustomJSX',
  data () {
    return {}
  }
}
```

3. 添加`render`函数，通过`return`返回组件

```jsx
export default {
  name: 'CustomJSX',
  data () {
    return {}
  },
  render (h) {
    return (
      <div>
        <div>Custom JSX</div>
        <div>Custom JSX</div>
      </div>
    )
  }
}
```

4. 在vue文件中引入，然后注册组件，像使用vue组件一样使用

```vue
<div class="footer"><Customjsx /></div>
import Customjsx from './components/infocard.jsx'
components: {
  Customjsx
},
```

## 13.2 样式绑定

### 13.2.1 行内样式

行内样式，使用`-`连接的属性改为大写，属性与属性之间使用`,`分割

```jsx
render (h) {
  return (
    <div>
      <div style={{ color: '#1890ff', marginTop: '10px' }}>Custom JSX</div>
      <div>Custom JSX</div>
    </div>
  )
}
```

### 13.2.2 文件引入

文件引入样式

```jsx
import './style.less'  //文件引入
export default {
  name: 'CustomJSX',
  data () {
    return {}
  },
  render (h) {
    return (
      <div>
        <div style={{ color: '#1890ff', marginTop: '10px' }}>Custom JSX</div>
        <div class={'title-c'}>Custom JSX</div>
      </div>
    )
  }
}

```

## 13.3 动态传参

### 13.3.1 父向子传参

1. 在子组件中

```jsx
import './style.less'
export default {
  name: 'CustomJSX',
  data () {
    return {}
  },
  props: { // 接收父组件传递的参数
    msg: {
      type: String,
      default: ''
    }
  },
  render (h) {
    const { msg } = this // 获取父组件传递的参数
    return (
      <div>
        <div>{ msg }</div>
      </div>
    )
  }
}
```

2. 父组件中

```vue
<Customjsx :msg="`title`"/>
```

### 13.3.2 子组件向父组件传参

1. 子组件

```jsx
import './style.less'
export default {
  name: 'CustomJSX',
  data () {
    return {}
  },
  methods: { // 事件处理函数
    handleClick (event, info) {
      this.$emit('on-click', { info }) // 传递参数info
    }
  },
  render (h) {
    const { handleClick } = this
    return (
      <div>
        <div onClick={ ($event) => handleClick($event, '子组件参数') }>title</div>
      </div>
    )
  }
}
```

2. 父组件中接收

```vue
<Customjsx @on-click="onClick"/>
methods: {
  onClick (val) {
    console.log('click', val)
  }
},
```



## 13.4 事件绑定

1. 子组件点击事件

```jsx
import './style.less'
export default {
  name: 'CustomJSX',
  data () {
    return {}
  },
  methods: { // 事件处理函数
    handleClick (event) {
      console.log(event, 'click')
    }
  },
  render (h) {
    const { handleClick } = this
    return (
      <div>
        <div onClick={ ($event) => handleClick($event) }>title</div> // 获取原生事件
      </div>
    )
  }
}
```

## 13.5 生命周期函数

使用生命周期函数，可以使组件发起网络请求

```jsx
import './style.less'
export default {
  name: 'CustomJSX',
  data () {
    return {}
  },
  methods: { // 事件处理函数
    handleClick (event, info) {
      this.$emit('on-click', { info }) // 传递参数info
    }
  },
  created () { // 生命周期函数
    console.log('created子组件创建')
  },
  mounted () {
    console.log('mounted子组件挂载')
  },
  render (h) {
    const { handleClick } = this
    return (
      <div>
        <div onClick={ ($event) => handleClick($event, '子组件参数') }>title</div>
      </div>
    )
  }
}
```



## 13.6 循环渲染

子组件

```jsx
// 人员列表组件
const ListItem = {
  name: 'ListItem',
  props: {
    personList: Array
  },
  render (h) {
    const { personList } = this
    return (
      <ul class="list-view">
        {
          /* 循环渲染 */
          personList.map((mp, index) => {
            return (
              <li>
                <p class={'tag-short-view'}>{ index + 1}</p>
                <p>姓名：{mp.name}</p>
                <p>年龄：{mp.age}</p>
              </li>
            )
          })
        }
      </ul>
    )
  }
}

export default {
  name: 'Customjsx',
  data () {
    return {}
  },
  props: {
    dataList: {
      type: Array,
      default: () => []
    }
  },
  methods: {},
  created () {},
  mounted () {},
  render (h) {
    return (
      <div>
        {/* 人员列表组件 */}
        <ListItem personList={this.dataList} />
      </div>
    )
  }
}
```

 父组件

```vue
<Customjsx :dataList="dataList"/>
data () {
    return {
      dataList: [
        {
          name: 'Alice',
          age: 25
        },
        {
          name: 'Bob',
          age: 30
        },
        {
          name: 'Charlie',
          age: 20
        },
        {
          name: 'David',
          age: 28
        },
        {
          name: 'Eve',
          age: 22
        }
      ]
    }
  },
```



## 13.7 具名插槽

在vue中不能使用

### 13.7.1 定义插槽 

在jsx中定义插槽

```jsx
// 人员列表组件
const ListItem = {
  name: 'ListItem',
  props: {
    personList: Array
  },
  render (h) {
    const { personList } = this
    return (
      <div>
        <ul class="list-view">
          {
            /* 循环渲染 */
            personList.map((mp, index) => {
              return (
                <li>
                  <p class={'tag-short-view'}>{ index + 1}</p>
                  <p>姓名：{mp.name}</p>
                  <p>年龄：{mp.age}</p>
                </li>
              )
            })
          }
        </ul>
        {
          /* 插槽位置 */
          this.$scopedSlots.header()
        }
      </div>
    )
  }
}

// 插槽内容
const SlotContent = {
  render (h) {
    return (
      <div>插槽内容</div>
    )
  }
}

export default {
  name: '',
  data () {
    return {}
  },
  props: {
    dataList: {
      type: Array,
      default: () => []
    }
  },
  methods: {},
  created () {},
  mounted () {},
  render (h) {
    // 具名插槽
    const scopedSlots = {
      header: (props) => <SlotContent></SlotContent>
    }
    return (
      <div>
        {/* 人员列表组件 */}
        <ListItem personList={this.dataList} scopedSlots={scopedSlots}/> {/* 向子组件传递插槽 */}
      </div>
    )
  }
}
```

### 13.7.2 插槽区域向插槽传递参数

插槽区域

```jsx
data () {
  return {
    userInfo: {
      name: '张三',
      age: 18
    }
  }
},
render (h) {
    const { userInfo } = this
    return (
      {
        /* 插槽位置 */
        this.$scopedSlots.header({ userInfo }) /* 向插槽传递参数 */
      }
    )
}
```

父组件

```jsx
const scopedSlots = {
  header: (props) => <strong>{ props.userInfo.name } { props.userInfo.age }</strong>
}
```

