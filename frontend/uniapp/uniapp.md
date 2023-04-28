## 1. uniapp介绍

`uni-app` 是一个使用 [Vue.js (opens new window)](https://link.juejin.cn/?target=https%3A%2F%2Fvuejs.org%2F)开发所有前端应用的框架，开发者编写一套代码，可发布到iOS、Android、Web（响应式）、以及各

种小程序（微信/支付宝/百度/头条/飞书/QQ/快手/钉钉/淘宝）、快应用等多个平台。

是目前**全端开发框架的佼佼者**

## 2. uniapp 生态介绍

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/7befea4fadd2806e7e266115864ad124.webp)

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/cbb17ffb2e7de0c0fb90193a91dbb879.webp)

## 3. uniapp项目创建

​	uniapp 项目开发方式分为两种

1. vue-cli （只开 h5端 或者 只开发 微信小程序端）
2. HBuilderX 可视化 （**多端开发首选** **只开发 手机APP**）

### 3.1 HBuilderX

如果你要使用uiapp开发多端，那么就必须要选择和它配套的编辑工具了 `HBuilderX` 。考虑到后期要使用更多的 uniapp的功能，建议提前注册一个uniapp的开发账号。 [注册](https://link.juejin.cn/?target=https%3A%2F%2Faccount.dcloud.net.cn%2Foauth2%3Freg%3D2%26redirect_uri%3Dhttp%3A%2F%2Fext.dcloud.net.cn%2Fauth%2Fdcloud%2Fcallback%26client_id%3DDCLOUD_DEV%26response_type%3Dcode)

### 3.2 创建项目

![image-20220814184653455](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c6a541b4cb5c45daae95d74ba9b97b38~tplv-k3u1fbpfcp-zoom-in-crop-mark:1512:0:0:0.awebp)

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/7be70da763fdd7a0c6e2b190590357fa.webp)

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/4548ab48df911a70732ba23790c7fbd5.webp)

## 4. uniapp 开发环境搭建

uniapp 是全端开发框架，假如我们想要开发全端，那么首先需要搭建好各个端对应的环境。以下拿比较典型的 微信小程序、H5 和 安卓App来演示。

### 4.1 微信小程序

想要开发一款微信小程序，必须要注册[微信开发者账号](https://link.juejin.cn/?target=https%3A%2F%2Fmp.weixin.qq.com%2Fcgi-bin%2Fregistermidpage%3Faction%3Dindex%26lang%3Dzh_CN%26token%3D)，同时获取对应的appid。

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/b9067a3e4f32369da3ad25cdfd3f0b13.webp)

获取appid

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/51a0722804ccad6ac56f3873aedb2d47.webp)

打开服务端口

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/fa538f3a84f77521e7e05a50d6461dc0.webp)

在 HBuilderX 中运行项目

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/134426e3e7e6b00f9e3e1cdb9bba24b6.webp)



### 4.2 APP

1. 打开Android Studio

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/755490f7214c17e68d8a68542c57fde2.webp)

2. 选择要安装的手机型号

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/4f3723f9e505ccdd0c0791b61f504e9a.webp)

3. 选择安装对应的安卓系统版本 下载过程比较慢，因为系统镜像比较大

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/41afe72c30c5132ba3b7bc476ed9804f.webp)

4. 运行

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/22c7f2b82b260ba0ecbd4f73f0000107.webp)

5. 回到HBuilderX中运行

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/b770413af152e2194a45ec6ad57e55a1.webp)

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/05ceb590082d60c715e1149bb7bceb6f.webp)

## 5. uniapp项目结构介绍

介绍https://uniapp.dcloud.net.cn/tutorial/project.html

```
┌─uniCloud              云空间目录，阿里云为uniCloud-aliyun,腾讯云为uniCloud-tcb 
│─components            符合vue组件规范的uni-app组件目录
│  └─comp-a.vue         可复用的a组件
├─hybrid                App端存放本地html文件的目录
├─platforms             存放各平台专用页面的目录
├─pages                 业务页面文件存放的目录
│  ├─index
│  │  └─index.vue       index页面
│  └─list
│     └─list.vue        list页面
├─static                存放应用引用的本地静态资源（如图片、视频等）的目录，注意：静态资源只能存放于此
├─uni_modules           存放[uni_module](/uni_modules)。
├─wxcomponents          存放小程序组件的目录
├─nativeplugins         App原生插件 详见
├─unpackage             非工程代码，一般存放运行或发行的编译结果
├─main.js               Vue初始化入口文件
├─App.vue               应用配置，用来配置App全局样式以及监听 应用生命周期
├─manifest.json         配置应用名称、appid、logo、版本等打包信息
├─pages.json            配置页面路由、导航条、选项卡等页面类信息
└─uni.scss              这里是uni-app内置的常用样式变量
```

## 6. uniapp开发规范

为了实现多端兼容，综合考虑编译速度、运行性能等因素，`uni-app` 约定了如下开发规范

### 6.1 页面和组件文件遵循vue的规范

1. 比如 新建页面 `goods.vue`
2. 比如 新建组件 `it-item.vue`

### 6.2 内置标签使用小程序的规范

```vue
<view>小程序中的块级标签</view>
```

### 6.3 数据绑定和事件处理使用vue的规范

```vue
<template>
	<view>
		<view class="item" v-for="item in list" :key="item" @click="handleClick(item)">{{item}}</view>
	</view>
</template>
<script>
	export default {
		data(){
			return {
				list:['a','b','c']
			}
		},
		methods:{
			handleClick(letter){
				console.log(letter)
			}
		}
	}
</script>
```

### 6.4 能力接口API 使用 微信小程序的规范

比如弹出显示框，发送网络请求等

```js
wx.showToast({
  title: '成功',
  icon: 'success',
  duration: 2000
})

wx.request({
  url: 'example.php', //仅为示例，并非真实的接口地址
  data: {
    x: '',
    y: ''
  },
  header: {
    'content-type': 'application/json' // 默认值
  },
  success (res) {
    console.log(res.data)
  }
})
```

考虑到跨端，我们将会使用 `uniapp` 统一封装的API。简称 `uni api`

## 7. uniapp 生命周期

uniapp中，生命周期分类三大类

1. 应用生命周期 **小程序规范**
2. 页面生命周期 **小程序规范**
3. 组件生命周期 **vue规范**

### 7.1 应用生命周期

| 函数名               | 说明                                                         |
| -------------------- | ------------------------------------------------------------ |
| onLaunch             | 当`uni-app` 初始化完成时触发（全局只触发一次）               |
| onShow               | 当 `uni-app` 启动，或从后台进入前台显示                      |
| onHide               | 当 `uni-app` 从前台进入后台                                  |
| onError              | 当 `uni-app` 报错时触发                                      |
| onUniNViewMessage    | 对 `nvue` 页面发送的数据进行监听，可参考 [nvue 向 vue 通讯(opens new window)](https://link.juejin.cn/?target=https%3A%2F%2Funiapp.dcloud.io%2Ftutorial%2Fnvue-api%3Fid%3Dcommunication) |
| onUnhandledRejection | 对未处理的 Promise 拒绝事件监听函数（2.8.1+）                |
| onPageNotFound       | 页面不存在监听函数                                           |
| onThemeChange        | 监听系统主题变化                                             |

### 7.2 页面生命周期

| 函数名                              | 说明                                                         | 平台差异说明                                                 | 最低版本 |
| ----------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | -------- |
| onInit                              | 监听页面初始化，其参数同 onLoad 参数，为上个页面传递的数据，参数类型为 Object（用于页面传参），触发时机早于 onLoad | 百度小程序                                                   | 3.1.0+   |
| onLoad                              | 监听页面加载，其参数为上个页面传递的数据，参数类型为 Object（用于页面传参），参考[示例](https://link.juejin.cn/?target=https%3A%2F%2Funiapp.dcloud.net.cn%2Fapi%2Frouter%23navigateto) |                                                              |          |
| onShow                              | 监听页面显示。页面每次出现在屏幕上都触发，包括从下级页面点返回露出当前页面 |                                                              |          |
| onReady                             | 监听页面初次渲染完成。注意如果渲染速度快，会在页面进入动画完成前触发 |                                                              |          |
| onHide                              | 监听页面隐藏                                                 |                                                              |          |
| onUnload                            | 监听页面卸载                                                 |                                                              |          |
| onResize                            | 监听窗口尺寸变化                                             | App、微信小程序、快手小程序                                  |          |
| onPullDownRefresh                   | 监听用户下拉动作，一般用于下拉刷新，参考[示例](https://link.juejin.cn/?target=https%3A%2F%2Funiapp.dcloud.net.cn%2Fapi%2Fui%2Fpulldown) |                                                              |          |
| onReachBottom                       | 页面滚动到底部的事件（不是scroll-view滚到底），常用于下拉下一页数据。具体见下方注意事项 |                                                              |          |
| onTabItemTap                        | 点击 tab 时触发，参数为Object，具体见下方注意事项            | 微信小程序、QQ小程序、支付宝小程序、百度小程序、H5、App、快手小程序、京东小程序 |          |
| onShareAppMessage                   | 用户点击右上角分享                                           | 微信小程序、QQ小程序、支付宝小程序、字节小程序、飞书小程序、快手小程序、京东小程序 |          |
| onPageScroll                        | 监听页面滚动，参数为Object                                   | nvue暂不支持                                                 |          |
| onNavigationBarButtonTap            | 监听原生标题栏按钮点击事件，参数为Object                     | App、H5                                                      |          |
| onBackPress                         | 监听页面返回，返回 event = {from:backbutton、 navigateBack} ，backbutton 表示来源是左上角返回按钮或 android 返回键；navigateBack表示来源是 uni.navigateBack ；详细说明及使用：[onBackPress 详解 (opens new window)](https://link.juejin.cn/?target=http%3A%2F%2Fask.dcloud.net.cn%2Farticle%2F35120)。支付宝小程序只有真机能触发，只能监听非navigateBack引起的返回，不可阻止默认行为。 | app、H5、支付宝小程序                                        |          |
| onNavigationBarSearchInputChanged   | 监听原生标题栏搜索输入框输入内容变化事件                     | App、H5                                                      | 1.6.0    |
| onNavigationBarSearchInputConfirmed | 监听原生标题栏搜索输入框搜索事件，用户点击软键盘上的“搜索”按钮时触发。 | App、H5                                                      | 1.6.0    |
| onNavigationBarSearchInputClicked   | 监听原生标题栏搜索输入框点击事件（pages.json 中的 searchInput 配置 disabled 为 true 时才会触发） | App、H5                                                      | 1.6.0    |
| onShareTimeline                     | 监听用户点击右上角转发到朋友圈                               | 微信小程序                                                   | 2.8.1+   |
| onAddToFavorites                    | 监听用户点击右上角收藏                                       | 微信小程序                                                   | 2.8.1+   |

### 7.3 组件生命周期

|               |                                                              |              |          |
| ------------- | ------------------------------------------------------------ | ------------ | -------- |
| 函数名        | 说明                                                         | 平台差异说明 | 最低版本 |
| beforeCreate  | 在实例初始化之前被调用。[详见(opens new window)](https://link.juejin.cn/?target=https%3A%2F%2Fcn.vuejs.org%2Fv2%2Fapi%2F%23beforeCreate) |              |          |
| created       | 在实例创建完成后被立即调用。[详见(opens new window)](https://link.juejin.cn/?target=https%3A%2F%2Fcn.vuejs.org%2Fv2%2Fapi%2F%23created) |              |          |
| beforeMount   | 在挂载开始之前被调用。[详见(opens new window)](https://link.juejin.cn/?target=https%3A%2F%2Fcn.vuejs.org%2Fv2%2Fapi%2F%23beforeMount) |              |          |
| mounted       | 挂载到实例上去之后调用。[详见 (opens new window)](https://link.juejin.cn/?target=https%3A%2F%2Fcn.vuejs.org%2Fv2%2Fapi%2F%23mounted)注意：此处并不能确定子组件被全部挂载，如果需要子组件完全挂载之后在执行操作可以使用`$nextTick`[Vue官方文档(opens new window)](https://link.juejin.cn/?target=https%3A%2F%2Fcn.vuejs.org%2Fv2%2Fapi%2F%23Vue-nextTick) |              |          |
| beforeUpdate  | 数据更新时调用，发生在虚拟 DOM 打补丁之前。[详见(opens new window)](https://link.juejin.cn/?target=https%3A%2F%2Fcn.vuejs.org%2Fv2%2Fapi%2F%23beforeUpdate) | 仅H5平台支持 |          |
| updated       | 由于数据更改导致的虚拟 DOM 重新渲染和打补丁，在这之后会调用该钩子。[详见(opens new window)](https://link.juejin.cn/?target=https%3A%2F%2Fcn.vuejs.org%2Fv2%2Fapi%2F%23updated) | 仅H5平台支持 |          |
| beforeDestroy | 实例销毁之前调用。在这一步，实例仍然完全可用。[详见(opens new window)](https://link.juejin.cn/?target=https%3A%2F%2Fcn.vuejs.org%2Fv2%2Fapi%2F%23beforeDestroy) |              |          |
| destroyed     | Vue 实例销毁后调用。调用后，Vue 实例指示的所有东西都会解绑定，所有的事件监听器会被移除，所有的子实例也会被销毁。[详见(opens new window)](https://link.juejin.cn/?target=https%3A%2F%2Fcn.vuejs.org%2Fv2%2Fapi%2F%23destroyed) |              |          |



## 8. uniapp 多端开发

### 8.1 条件编译

条件编译是用特殊的注释作为标记，在编译时根据这些特殊的注释，将注释里面的代码编译到不同平台。

**写法：**以 `#ifdef` 或 `#ifndef` 加 `%PLATFORM%`开头，以 `#endif` 结尾。

- `#ifdef`：`if defined` 仅在某平台存在
- `#ifndef`：`if not defined` 除了某平台均存在
- `%PLATFORM%`：平台名称

html中

```vue
<!--  #ifdef  %PLATFORM% -->
平台特有的组件
<!--  #endif -->
```

js中

```js
// #ifdef  %PLATFORM%
平台特有的API实现
// #endif
```

css中

```css
/*  #ifdef  %PLATFORM%  */
平台特有样式
/*  #endif  */
```

| 条件编译写法                                             | 说明                                                         |
| -------------------------------------------------------- | ------------------------------------------------------------ |
| #ifdef **APP-PLUS** 需条件编译的代码 #endif              | 仅出现在 App 平台下的代码                                    |
| #ifndef **H5** 需条件编译的代码 #endif                   | 除了 H5 平台，其它平台均存在的代码                           |
| #ifdef **H5** \|\| **MP-WEIXIN** 需条件编译的代码 #endif | 在 H5 平台或微信小程序平台存在的代码（这里只有\|\|，不可能出现&&，因为没有交集） |

**%PLATFORM%** **可取值如下：**

| 值                      | 生效条件                                                     |
| ----------------------- | ------------------------------------------------------------ |
| VUE3                    | HBuilderX 3.2.0+ [详情(opens new window)](https://link.juejin.cn/?target=https%3A%2F%2Fask.dcloud.net.cn%2Farticle%2F37834) |
| APP-PLUS-NVUE或APP-NVUE | App nvue                                                     |
| MP-WEIXIN               | 微信小程序                                                   |
| MP-ALIPAY               | 支付宝小程序                                                 |
| MP-BAIDU                | 百度小程序                                                   |
| MP-TOUTIAO              | 字节跳动小程序                                               |
| MP-LARK                 | 飞书小程序                                                   |
| MP-QQ                   | QQ小程序                                                     |
| MP-KUAISHOU             | 快手小程序                                                   |
| MP-JD                   | 京东小程序                                                   |
| MP-360                  | 360小程序                                                    |
| MP                      | 微信小程序/支付宝小程序/百度小程序/字节跳动小程序/飞书小程序/QQ小程序/360小程序 |
| QUICKAPP-WEBVIEW        | 快应用通用(包含联盟、华为)                                   |
| QUICKAPP-WEBVIEW-UNION  | 快应用联盟                                                   |
| QUICKAPP-WEBVIEW-HUAWEI | 快应用华为                                                   |

**支持的文件**

- .vue
- .js
- .css
- pages.json
- 各预编译语言文件，如：.scss、.less、.stylus、.ts、.pug

**static 目录的条件编译**

在不同平台，引用的静态资源可能也存在差异，通过 static 的的条件编译可以解决此问题，static 目录下新建不同平台的专有目录（目录名称同 `%PLATFORM%` 值域,但字母均为小写），专有目录下的静态资源只有在特定平台才会编译进去。

如以下目录结构，`a.png` 只有在微信小程序平台才会编译进去，`b.png` 在所有平台都会被编译。

```
┌─static                
│  ├─mp-weixin
│  │  └─a.png     
│  └─b.png
├─main.js        
├─App.vue      
├─manifest.json 
└─pages.json 
```

**整体目录条件编译**

如果想把各平台的页面文件更彻底的分开，也可以在uni-app项目根目录创建`platforms`目录，然后在下面进一步创建`app-plus`、`mp-weixin`等子目录，存放不同平台的文件。

**注意**

- `platforms`目录下只支持放置页面文件（即页面vue文件），如果需要对其他资源条件编译建议使用[static 目录的条件编译(opens new window)](https://link.juejin.cn/?target=https%3A%2F%2Funiapp.dcloud.io%2Fplatform%3Fid%3Dstatic-%E7%9B%AE%E5%BD%95%E7%9A%84%E6%9D%A1%E4%BB%B6%E7%BC%96%E8%AF%91)

### 8.2 尺寸单位

1. uniapp通用单位 `px` , `rpx`
2. vue页面中支持 `rem` 、`vh`、`vw`
3. nvue 不支持 `百分比单位`

官网介绍https://uniapp.dcloud.net.cn/tutorial/syntax-css.html#%E5%B0%BA%E5%AF%B8%E5%8D%95%E4%BD%8D

相对长度单位，功能类似于web端的 rem 和 vw，小程序首先推出，uniapp也是直接支持。一种根据屏幕宽度自适应的动态单位。以 750 宽的屏幕为基准，750rpx 恰好为屏幕宽度。

其中uniapp做了以下设置，

1. 默认的设计稿宽度为 `375px` 因此存在 `1px = 2rpx`
2. 默认 rpx支持最大宽度为 `960px`,超出则 按照 设计稿宽度 `375px` 来设置



### 8.3 css变量

| CSS 变量            | 描述                   | App                                                          | 小程序 | H5                   |
| ------------------- | ---------------------- | ------------------------------------------------------------ | ------ | -------------------- |
| --status-bar-height | 系统状态栏高度         | [系统状态栏高度 (opens new window)](https://link.juejin.cn/?target=http%3A%2F%2Fwww.html5plus.org%2Fdoc%2Fzh_cn%2Fnavigator.html%23plus.navigator.getStatusbarHeight)、nvue 注意见下 | 25px   | 0                    |
| --window-top        | 内容区域距离顶部的距离 | 0                                                            | 0      | NavigationBar 的高度 |
| --window-bottom     | 内容区域距离底部的距离 | 0                                                            | 0      | TabBar 的高度        |



## 9. 组件库

`uview` 和 `uni ui` 都是 和uniapp配套的全端UI框架，可以单独使用，也可以共同使用

### 9.1 uView

1. [打开 插件市场，找到 uview 1.x 地址](https://link.juejin.cn/?target=https%3A%2F%2Fext.dcloud.net.cn%2Fplugin%3Fid%3D6682)

2. 点击**导入插件**

   ![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/b455b9968cd496f0df2079ca33cd6eae.webp)

3. 导入成功，可以看到目录下多了 `components` 文件夹

   ![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/b502c69ed73c9249b1ba5f49079ed833.webp)

4. 接着在 `uni.scss` 中导入 uview的主题样式文件 `theme.scss`

   ```scss
   @import './theme.scss';
   ```

5. 在页面上添加测试代码

   ```vue
   <u-button >默认按钮</u-button>
   <u-button type="primary">主要按钮</u-button>
   <u-button type="success">成功按钮</u-button>
   <u-button type="info">信息按钮</u-button>
   <u-button type="warning">警告按钮</u-button>
   <u-button type="error">危险按钮</u-button>
   ```

6. 点击运行

   ![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/31a6508a3e6ee9c0a338007677987102.webp)

7. 成功

   ![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/40cd482c090d0000c8bc492b90d8eb9c.webp)

   



### 9.2 uni-ui

1. [打开 uni ui 的对应的插件市场](https://link.juejin.cn/?target=https%3A%2F%2Fext.dcloud.net.cn%2Fplugin%3Fid%3D55)

2. 使用 HBuilderX 导入插件

   ![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/059c1606524739e79668978990b3afa9.webp)

3. 项目中会多 `uni_modules` 文件夹

   ![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/d36e0069482cd0678fe0e87a57fde07e.webp)

4. 页面中导入代码

   ```vue
   <uni-title title="上报统计数据"></uni-title>
   <uni-title type="h1" title="h1 一级标题 "></uni-title>
   <uni-title type="h1" title="h1 一级标题" color="#027fff"></uni-title>
   <uni-title type="h2" title="h2 居中" align="center"></uni-title>
   ```

5. 观察效果

   ![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/007a0b19b649b1d9a596d3edede09ba5.webp)

   