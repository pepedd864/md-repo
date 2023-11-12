## 1. 基础概念

### 1.1 什么是 Tailwind CSS

就是一个 CSS 框架，和你知道的 bootstrap，element ui，Antd，bulma。一样。将一些 css 样式封装好，用来加速我们开发的一个工具。

和其他的 CSS 框架有什么区别？
CSS 发展到现在，基本经历了三个阶段。

**第一个阶段，原生写法**
是类似于编程中面向过程的写法，需要什么样式，自己在 css 中写什么样式。对代码有洁癖的程序员会进行简单的 css 复用。但是也只是简单的复用，大多数时候还是需要什么写什么，想怎么写怎么写。

**第二个阶段，CSS 组件化。**
类似于编程中面向对象的写法，将相同视觉的 UI 封装成一个**组件**。比如一个按钮，整个项目中，这个按钮被多次使用，并且样式一致。那么就可以封装成一个按钮类。使用的时候直接使用这个类名称就 OK。

这也是 `bootstrap`，`element ui`，`Antd`，`bulma`的做法。

这种框架的优势在于，封装了大量常见的 UI。比如你需要一个表单，，需要一个导航，需要一个弹窗，Card 卡片。有现成的 class。直接拿过来用，就可以快速的完成效果。完全不需要动手写 css。

这也是目前比较流行的方法。这几年几乎很少有项目是自己一点一点手写样式的了，多多少少都会使用到一些 css 框架。

对于一些需要**快速交付**的项目，非常适合使用这种组件化 css 框架。

**第三个阶段，CSS 零件化。**
也叫做 **CSS 原子化**。和上面第一个阶段第二个阶段都有类似的地方。依旧是组件，只是每个组件都是一个单一功能的 css 属性。

上面第一个阶段的时候，我们讲了有些有对代码有追求的人，会开始复用 css。
比如页面中大量的用到`float:left`。那么就可以封装一个类，比如是这样

```css
.left {float:left}
```

然后需要使用 `float:left` 的时候，直接使用`.left` 就可以。

但是我们自己写 css 的时候，仅仅是封装一些常用的简单的类，绝大多数的 css，都需要动手去写 css。比如你要写个宽度 12 像素。你就得老老实实的去写 `width:12px`，逃避不了，不过估计也没人想过逃避。

**Tailwind CSS 就是第三个阶段的产物，它做了什么呢？**
它将所有的 css 属性全部封装成语义化的类，比如你想要一个 `float:left`，它已经帮你封装好了，你直接使用一个 `float-left` 就可以。

需要一个宽度为 12 像素，只需要写 `w-3` 就可以。

---

举一个完整的例子，你可能需要实现下面这样一个效果：

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/82dbf264f620701441db2133ae58e6ef.png)

```css
<div class="chat-notification">
  <div class="chat-notification-logo-wrapper">
    <img class="chat-notification-logo" src="/img/logo.svg" alt="ChitChat Logo">
  </div>
  <div class="chat-notification-content">
    <h4 class="chat-notification-title">ChitChat</h4>
    <p class="chat-notification-message">You have a new message!</p>
  </div>
</div>

<style>
  .chat-notification {
    display: flex;
    max-width: 24rem;
    margin: 0 auto;
    padding: 1.5rem;
    border-radius: 0.5rem;
    background-color: #fff;
    box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
  }
  .chat-notification-logo-wrapper {
    flex-shrink: 0;
  }
  .chat-notification-logo {
    height: 3rem;
    width: 3rem;
  }
  .chat-notification-content {
    margin-left: 1.5rem;
    padding-top: 0.25rem;
  }
  .chat-notification-title {
    color: #1a202c;
    font-size: 1.25rem;
    line-height: 1.25;
  }
  .chat-notification-message {
    color: #718096;
    font-size: 1rem;
    line-height: 1.5;
  }
</style>
```

但是使用 Tailwind CSS，你只需要这样写就可以

```css
<div class="p-6 max-w-sm mx-auto bg-white rounded-xl shadow-md flex items-center space-x-4">
  <div class="flex-shrink-0">
    <img class="h-12 w-12" src="/img/logo.svg" alt="ChitChat Logo">
  </div>
  <div>
    <div class="text-xl font-medium text-black">ChitChat</div>
    <p class="text-gray-500">You have a new message!</p>
  </div>
</div>
```



### 1.2 Tailwind CSS 有什么优点？

**可定制化程度极高。**
你可以随心所欲写出自己的样式。想怎么折腾怎么折腾。
如果使用 bootstrap，你如果想改变一个按钮的样式，就会比较困难。你得用覆盖式的写法，通过自己的样式覆盖掉 bootstrap 自带的样式。如果框架本身不支持修改，你通过自己的写法去修改框架本身的特性，这是一种很脏的写法。非常别扭。
但是这个问题在 Tailwind CSS 完全不存在。Tailwind CSS 没有自以为是的封装任何样式给你。

**不需要在写 css。**
使用 Tailwind CSS，基本可以不用再写 css。所有的效果都可以通过 class 名来完成。我用 Tailwind CSS 写了几个页面，到目前为止，还没有写过一行 css。

**不需要再为 class 取个什么名字而苦恼。**
对于经常手写 css 的程序员来说，最大的噩梦可能就是怎么给 class 取名了。尤其是在同一个区块里面，区块名称，子元素名称，等等，一个页面动辄几十个几百个类名。非常痛苦。而这其中，真正能复用的 class 可能就个别几个。

使用 Tailwind CSS 完全不用为取名字烦恼，因为所有的 css 属性都被框架语义化封装好了。只需要在 class 里面引用就好。

**响应式设计**
Tailwind CSS 遵循移动优先的设计模式。断点系统很灵活。也是目前所有 css 框架里做的最好的。比如你要实现一个媒体查询，根据不同的屏幕宽度实现不同的图片宽度。
按照之前的写法，你可能得这么干

```css
@media only screen and (max-width:1280px) { 
    .img {     
    width:196px; 
    } 
}
@media only screen and (max-width: 760px) { 
    .img {     
    width:128px; 
    } 
}
```

但是在 Tailwind CSS，一句话就能搞定：

```css
<img class="w-16 md:w-32 lg:w-48" src="...">
```



**一套专业的 UI 属性值**

Tailwind CSS 虽然没有封装任何 UI，但是他默认提供的一些属性值都是很专业的。比如颜色

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/9fcb34586bd9609f148a9c8b75906c98.png)

还有各种内边距外边距，宽高，文字大小行高颜色等等。即使你不懂设计，按照他内置的属性做出来的东西，也不会太差。

### 1.3 Tailwind CSS 有什么缺点？

**类名很长**
正如 Tailwind CSS 官网首页的口号一样，从此让你写样式不再离开 html 页面。Tailwind CSS 将 HTML 与 CSS 高度解耦，把本来 CSS 的一些工作转嫁给了 HTML。好处是使用 Tailwind CSS 你可以从此不再写 css。但坏处是你的 html 标签的类名会很长很长。比如

```css
<a href="#" class="text-sm font-medium bg-purple-600 rounded-full py-4 px-11 text-white inline-block border border-solid shadow hover:text-purple-600 hover:bg-white hover:border-purple-600 transition duration-300" role="button">Start Ticketing</a>
```

虽然 Tailwind CSS 也支持把很多属性提取成一个组件，但是对于不会再次复用的 class。提取组件也没什么必要。

**熟悉使用有成本**

这一点逃避不了，所有的新技术，所有的 css 框架都有熟悉成本。Tailwind CSS 也一样。比如你想做一个圆角，那你得知道 Tailwind CSS 里面的圆角属性怎么写，边框怎么写，边框样式怎么写等等。你需要不断的去看文档。



## 2. 快速入门

### 2.1 安装（在vue中使用Tailwind）

1. 创建工程

```bash
vue create tailwind-vue
```

2. 安装tailwindcss及其依赖

```bash
npm install -D tailwindcss@latest postcss@latest autoprefixer@latest
```

3. 创建配置文件`tailwind.config.js` `postcss.config.js`

```bash
npx tailwindcss init -p
```

4. 创建好的配置文件应该是这样的

```js
// tailwind.config.js
module.exports = {
  content: [],
  theme: {
    extend: {},
  },
  variants: {
    extend: {},
  },
  plugins: [],
}

```

```js
// postcss.config.js
module.exports = {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}
```



### 2.2 在项目中引入Tailwind

创建 `./src/index.css` 文件 并使用 `@tailwind` 指令来包含 Tailwind的 `base`、 `components` 和 `utilities` 样式，来替换掉原来的文件内容。

```css
/* ./src/index.css */
@tailwind base;
@tailwind components;
@tailwind utilities;
```

Tailwind 会在构建时将这些指令转换成所有基于您配置的设计系统生成的样式文件。

最后，确保您的 CSS 文件被导入到您的 `./src/main.js` 文件中。

```js
// src/main.js
import { createApp } from 'vue'
import App from './App.vue'
import './index.css'

createApp(App).mount('#app')
```



## 3. 使用

### 3.1 基础用法

Tailwind CSS提供了一整套预定义的 CSS 类名，可以用于快速构建网页界面。

1. 功能前缀：表示该类名所表示的功能，比如用于设置颜色的类名前缀为 `text-`，用于设置背景颜色的类名前缀为 `bg-`，用于设置边框颜色的类名前缀为 `border-` 等等。
2. 功能值：表示该类名所要设置的具体属性值，比如 `text-red-500` 表示将文本颜色设置为红色，`bg-gray-200` 表示将背景颜色设置为灰色，`border-solid border-2 border-blue-500` 表示将边框设置为蓝色实线边框，边框宽度为 2 像素。
3. 可选状态：表示该类名所要设置的状态，比如 `hover:text-red-500` 表示鼠标悬浮在元素上时将文本颜色设置为红色，`active:bg-gray-200` 表示元素被点击时将背景颜色设置为灰色，`disabled:opacity-50` 表示元素被禁用时将不透明度设置为 50%。
4. 定位和布局：用于设置元素的定位和布局属性，常用的类名包括 `relative`（相对定位）、`absolute`（绝对定位）、`inset-*`（设置元素边界偏移量）、`flex`（弹性布局）等等。
5. 背景和边框：用于设置元素的背景和边框属性，常用的类名包括 `bg-*`（设置背景颜色）、`border-*`（设置边框样式和颜色）、`rounded-*`（设置元素圆角）、`shadow-*`（设置元素阴影）等等。
6. 文本和字体：用于设置文本和字体属性，常用的类名包括 `text-*`（设置文本颜色和大小）、`font-*`（设置字体系列和大小）、`uppercase`（将文本转换为大写）、`italic`（设置文本为斜体）等等。
7. 动画和过渡：用于设置元素的动画和过渡效果，常用的类名包括 `animate-*`（设置动画效果）、`transition-*`（设置过渡效果）、`duration-*`（设置动画或过渡的持续时间）等等。
8. 响应式前缀：Tailwind CSS 的类名前缀可以加上响应式前缀来设置不同的屏幕尺寸下的样式。常用的响应式前缀包括 `sm:`（小屏幕）、`md:`（中等屏幕）、`lg:`（大屏幕）和 `xl:`（超大屏幕）。

