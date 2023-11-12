## 1. 初始化

1. 安装脚手架工具

```bash
npm install -g react-native-cli

npm install -g react-native
```

2. 创建项目

```bash
npx react-native init YourProject
```

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/9854efd41eae2bdbe426a9c420096d0e.png)

3. 使用andriod studio 打开项目，刷新gradle 安装依赖

4. 安装依赖后，构建项目

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/cb3b19616cb77c745925b72b5d3d97bb.png)

5. 然后回到react native，运行yarn run start 命令

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/099f7878150a7dbfd88b8453cc8ee36a.png)

6. 运行到andriod

7. 初次运行可能报错，等待一会，让他编译js代码

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/54f8b4356d9152f423879fca9cc63e2b.png)

8. 最后正常运行在模拟器中

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/c58f6b75c7a60142ff6cee38e0629836.png)



## 2. StyleSheet

**RN 中的样式CSS的不同**

- 没有继承性
  -  RN中的继承只发生在Text组件上
- 样式名采用小驼峰命名
  - fontSize VS font-size
- 所有尺寸都是没有单位
  - width : 100
- 有特别的样式名
  - marginHorizontal(水平外边距)
  - marginVertical（垂直外边距)

**RN样式的声明方式**

- 通过style属性直接声明
  - 属性值为对象:`<组件style={{样式}}/>`
  - 属性值为数组:`<组件style={[{样式1},...,{样式N}]}/>`
- 在style属性中调用StyleSheet声明的样式
  - 引入: `import { StyleSheet, View } from 'react-native'`
  - 声明: `const styles = StyleSheet.create({foo:{样式1}, bar:{样式2}})`
  - 使用:`<View style={ [ styles.foo, styles.bar ] }>内容</View>`

## 3. FlexBox

容器(container)

- 采用Flex布局的元素，称为Flex容器（flex container)，简称"容器"

项目(item)

- 容器所有子元素，称为Flex项目(flex item)，简称"项目"

主轴(main axis)

- flexDirection
  - 声明主轴方向:row (Web默认)|column (RN默认)
- justifyContent
  - 声明项目在主轴上的对齐方式
- alignltems
  - 声明项目在交叉轴上的对齐方式
- flex
  - 声明项目在主轴上的尺寸比例

交叉轴 （cross axis)



## 4. 组件

RN 中的核心组件，是对原生组件的封装

- 原生组件:Android或iOS内的组件
- 核心组件:RN中最常用的，来自react-native的组件

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/4c68d8b187e2dbfde3c70b2cb17808f2.png)



### 4.10 图标

1. 安装

```bash
npm install --save react-native-vector-icons
```

2. 根据iOS/Andriod/Windows平台选择不同的配置方法

安卓

1. 编辑`android/app/build.gradle`，添加

```yaml
apply from: file("../../node_modules/react-native-vector-icons/fonts.gradle")
```

2. 重新编译安卓项目

3. 添加`import AntDesign from 'react-native-vector-icons/AntDesign';`
4. 使用`<AntDesign name={'forward'} size={size} color={color} />`

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/e4968ecbe2f12ac83a41b69cec7d6e3b.png)



## 5. 路由

**RN中的路由是通过 React-Navigation来完成的**

-  React 中通过React-Router 实现路由
- RN 0.44之前，React-Navigation在核心中维护，0.44之后，独立维护

**安装**

1. 核心库

```bash
npm install @react-navigation/native
```

2. 依赖

```bash
npm install react-native-screens react-native-safe-area-context
```

`react-native-screens`软件包需要一个额外的配置步骤才能正确 在安卓设备上工作。编辑位于 中的文件。`MainActivity.java` `android/app/src/main/java/<your package name>/MainActivity.java`

将突出显示的代码添加到类的主体中：`MainActivity`

```java
public class MainActivity extends ReactActivity {
  // ...
  @Override
  protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(null);
  }
  // ...
}
```

并确保在此文件的顶部的包语句下方添加以下导入语句：

```java
import android.os.Bundle;
```

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/c2c1da2a2daf2e03c0d11affca1156b3.png)

添加完后重新编译安卓项目，然后在react native中运行

**链接**

- RN 0.60后安卓环境自动链接路由（Android无需任何操作）
- iOS下需要手动链接路由（npx pod-install ios )

**添加头部组件**

- 将如下代码，放到应用的头部（例如:放到index.js或App.js 文件的头部)
  `import 'react-native-gesture-handler'`

**添加导航容器**

- 我们需要在入口文件中，把整个应用，包裹在导航容器(NavigationContainer）中（例如:在index.js或App.js 文件中)

```tsx
import * as React from 'react';
import { NavigationContainer } from '@react-navigation/native';

export default function App() {
  return (
    <NavigationContainer>{/* Rest of your app code */}</NavigationContainer>
  );
}
```



### 5.1 Stack导航

**简介**

- RN中默认没有类似浏览器的history对象
- 在RN中跳转之前，先将路由声明在Stack中

**安装**

```bash
npm install @react-navigation/native-stack
```

**使用**

- `import { createStackNavigator } from '@react-navigation/stack'`

**示例**

<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/94112fb5737baf0283dbf1db8fca19d7.png" alt="" style="zoom:50%;" />

```tsx
// In App.js in a new project

import * as React from 'react';
import { View, Text } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';

function HomeScreen() {
  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Text>Home Screen</Text>
    </View>
  );
}

const Stack = createNativeStackNavigator();

function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator>
        <Stack.Screen name="Home" component={HomeScreen} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}

export default App;
```

- `<Stack.Navigator ...属性/>` 作用于整个导航
- `<Stack.Screen ...属性/>`作用于当前屏幕

**Navigator属性**

- initialRouteName
  - 初始化路由，即默认加载的路由
- headerMode
  - float: iOS头部效果
  - screen:Android头部效果
  - none:不元示头部

- screenOptions

**Screen属性**

- options
- title
- headerTitleStyle
- headerStyle
- headerLeft
- headerRight
- headerTintColor



### 5.2 BottomTab导航

安装

```bash
npm install @react-navigation/bottom-tabs
```

示例

<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/2e93eb330c977a9944b22bde4d6deccb.png" alt="" style="zoom:50%;" />

```tsx
import * as React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { Home } from './src/pages/Home/Home';
import { News } from './src/pages/News/News';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';

const Tab = createBottomTabNavigator();

function App(): JSX.Element {
  return (
    <NavigationContainer>
      <Tab.Navigator>
        <Tab.Screen name="Home" component={Home} />
        <Tab.Screen name="News" component={News} />
      </Tab.Navigator>
    </NavigationContainer>
  );
}

export default App;
```



### 5.3 Drawer导航

安装

```bash
npm install @react-navigation/drawer
```

