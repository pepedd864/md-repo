# axios

Axios 是一个基于 promise 的网络请求库，可以用于浏览器和 node.js

[官网](http://axios-http.cn/)

## 1. 入门

1. 安装

```bash
npm install axios --save
```

2. 在使用vue开发时使用axios需要注意请求跨域的问题，在vite.config.js中编写相关配置即可

```js
// vite.config.js 如果是vue-cli方法类似
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
        target: "http://localhost:80/", // 接口地址
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

3. 使用axios完成一个简单的demo

```js
import axios from 'axios'
// 使用axios发起get请求
axios.get('/api/1').then(res => {
  console.log(res);
})
```

这样即可获得后端发来的数据

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/c3faf6a91d907ca3e4be648b3fbf9f24.png)


