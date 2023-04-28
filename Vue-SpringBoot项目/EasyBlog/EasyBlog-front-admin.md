## 1. 项目搭建

1. 下载node
2. 使用vite创建项目

```bash
npm init vite@latest easyblog-front-admin
```

3. 选择使用vue和javascript
4. 本项目使用vue3语法糖setup，不用每个去return

5. 进入项目目录，删除不必要文件，创建router目录

6. 安装vue-router

```bash
npm install vue-router@4 --save
```

7. 安装less，less-loader

```bash
npm install less-loader less
```

8. 编写router.js

```js
import { createRouter, createHistory } from 'vue-router'

const routes = [				// 路由规则
  {
    name: '首页',
    path: '/',
    component: () => import('@/view/index.vue'),
  }
]

// 创建路由
const router = createRouter({
  routes,
  history: createWebHistory(),	// 使用history，使用createWebHashHistory会在尾端加上 # 
})

export default router
```

9. 创建`vite.config.js`设置代理和路径映射(使用`@`)

```js
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'path'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  server: {
    hmr: true,			// 热重载，即修改代码不需要刷新网页
    port: 3001,			// 本地vite服务器端口为3001
    proxy: {			// 代理
      '/api': {     	// 请求链接中包含'/api'时，就会替换为 ‘target/api’。
// 比如，请求链接为http://127.0.0.1:3001/api/1，那么将会替换为http://localhost/api/1
        target: "http://localhost:8081/", // 接口地址
        secure: false,
        changeOrigin: true,   // 表示是否跨域
        pathRewrite: {        // 表示路径重写  
          '^/api': '/api',	// ^/api 表示一个包含 '/api' 的地址，
      //'/api' 表示目标(target)地址中的地址, 在转发时会自动替换为/api的地址
        }
      }
    }
  },
  resolve: {
    // 配置路径别名
    alias: {
      '@': path.resolve(__dirname, './src'), // 路径映射
    }
  }
})
```

10. 在main.js中使用router

```js
import { createApp } from 'vue'
import App from '@/App.vue'
import router from '@/router'

const app = createApp(App)
app.use(router)
app.mount('#app')
```

## 2. 登录页

1. 引入ElementPlus

```bash
npm install element-plus --save
```

2. 在main.js中引入elementplus

```js
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
app.use(ElementPlus)
```

3. 创建Login.vue，编写代码

```vue
<template>
  <div class="login-container">
    <div class="login-panel">
      <div class="login-title">用户登录</div>
      <el-form :model="formData" :rules="rules" ref="formDataRef">
        <el-form-item prop="account">
          <el-input class="input" v-model="formData.account" :prefix-icon="User" placeholder="请输入账号" size="large" />
        </el-form-item>
        <el-form-item prop="password">
          <el-input class="input" v-model="formData.password" type="password" :prefix-icon="Lock" placeholder="请输入密码"
            size="large" show-password />
        </el-form-item>
        <el-form-item prop="checkCode">
          <div class="check-code-panel">
            <el-input class="input check-code-input" v-model="formData.checkCode" :prefix-icon="Grid" placeholder="请输入验证码"
              size="large" @keyup.enter.native="login" />
            <img :src="checkCodeUrl" alt="" class="check-code" @click="checkCodeChange" />
          </div>
        </el-form-item>
        <el-form-item label="">
          <el-checkbox v-model="formData.rememberMe"> 记住我 </el-checkbox>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" :style="{ width: '100%' }" @click="login" @keyup.enter.native="login">登录</el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script setup>
// 一些工具
import VueCookie from "vue-cookies";
import md5 from "js-md5";
import { getCurrentInstance, reactive, ref } from "vue";
import { useRouter } from "vue-router";
// 图标
import { Lock, User, Grid } from "@element-plus/icons-vue";

// 全局变量
const { proxy } = getCurrentInstance();
// 路由
const router = useRouter();

// 获取验证码
const api = {
  checkCode: "api/checkCode",
  login: "login",
};
const checkCodeUrl = ref(api.checkCode);
const checkCodeChange = () => {
  checkCodeUrl.value = api.checkCode + "?" + new Date().getTime();
};

// 表单相关
const formDataRef = ref();
const formData = reactive({});

// 登录表单验证规则
const rules = {
  account: [
    {
      required: true,
      message: "请输入用户名",
    },
  ],
  password: [
    {
      required: true,
      message: "请输入密码",
    },
  ],
  checkCode: [
    {
      required: true,
      message: "请输入验证码",
    },
  ],
};

// 获取cookie中的登录信息
const init = () => {
  const loginInfo = VueCookie.get("loginInfo");
  if (!loginInfo) {
    return;
  }
  Object.assign(formData, loginInfo);
};
init();
// 登录
const login = () => {
  /**
   * 1. 在异步的回调函数中, 通过formDataRef.value.validate方法, 验证表单数据的合法性.
   * 2. 如果表单数据不合法, 则返回, 不执行后续的代码
   */
  formDataRef.value.validate(async (valid) => {
    if (!valid) {
      return;
    }

    /**
     * 1. 先从cookie中获取登录信息
     * 2. 如果cookie中有登录信息, 则获取cookie中的密码
     * 3. 如果cookie中没有登录信息, 则cookiePassword为null
     * 4. 如果输入的密码与cookie中的密码不一致, 则对输入的密码进行md5加密
     * 5. 如果输入的密码与cookie中的密码一致, 则不对输入的密码进行md5加密
     */
    let cookieLoginInfo = VueCookie.get("loginInfo");
    let cookiePassword =
      cookieLoginInfo == null ? null : cookieLoginInfo.password;
    if (formData.password != cookiePassword) {
      formData.password = md5(formData.password);
    }


    const params = {
      account: formData.account,
      password: formData.password,
      checkCode: formData.checkCode,
    };
    let result = await proxy.Request({
      url: api.login,
      params: params,
      showLoading: true,
      errorCallback: () => {
        // 登录失败
        checkCodeChange();
      },
      successCallback: () => {
        // 登录成功
        proxy.Message.success("登录成功");
        checkCodeChange();
      },
    });

    if (!result) {
      return;
    }

    /**
     * 1. VueCookie.set("userInfo", result.data, 0);
     *    这个是设置了一个"userInfo"的cookie, 有效期为0, 即关闭浏览器就失效
     * 2. if (formData.rememberMe) {
     *       VueCookie.set("loginInfo", loginInfo, "7d");
     *     } else {
     *       VueCookie.remove("loginInfo");
     *    这个是设置了一个"loginInfo"的cookie, 有效期为7天, 如果formData.rememberMe为false, 就移除这个cookie
     */
    router.push("/");
    const loginInfo = {
      account: formData.account,
      password: params.password,
      rememberMe: formData.rememberMe,
    };
    VueCookie.set("userInfo", result.data, 0);
    if (formData.rememberMe) {
      VueCookie.set("loginInfo", loginInfo, "7d");
    } else {
      VueCookie.remove("loginInfo");
    }
  });
};
</script>

<style lang="less" scoped>
// element 组件修改样式
// input
.el-input {
  --el-input-bg-color: #ffffff66;
  --el-input-border-radius: 12px;
  font-size: 18px;
}

// button
.el-button {
  border-radius: 12px;
  transition: all 0.3s;
}

.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
  width: 100%;
  background: url(../assets/login_bg.jpg) center center no-repeat;
  background-size: cover;

  .login-panel {
    width: 370px;
    padding: 20px;
    background: rgba(255, 255, 255, 0.2);
    backdrop-filter: blur(10px);
    border: 1px #cccccc99 solid;
    border-radius: 12px;
    box-shadow: 5px 5px 12px #00000033;

    .login-title {
      font: 700 28px 思源黑体;
      color: #444;
      text-align: center;
      letter-spacing: 3px;
      margin: 15px;
      padding: 5px;
    }

    .check-code-panel {
      display: flex;

      .check-code {
        margin-left: 10px;
        cursor: pointer;

        img {
          height: 30px;
        }
      }
    }
  }
}
</style>
```



## 3. 请求模块

1. 安装axios

```bash
npm install axios --save
```

2. 创建utils/Request.js

```js
// 基本骨架
import axios from 'axios';

// 请求头格式
const contentTypeForm = 'application/x-www-form-urlencoded;charset=UTF-8';
const contentTypeJson = 'application/json';
const contnetTypeFile = 'multipart/form-data';

const request = (config) => {
     // 初始化参数
    const {url ,params, dataType, showLoading} = config;
    dataType = dataType ? 'form' : dataType;
    showLoading = showLoading ? true : showLoading;
    
}

export default request;
```

3. 补充请求api代码