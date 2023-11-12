

学习时间： 2022年11月7日-~

# 1. 常见的桌面GUI工具

| 名称     | 语言   | 优点                     | 缺点                     |
| -------- | ------ | ------------------------ | ------------------------ |
| QT       | C++    | 跨平台、性能好、生态好   | 依赖多，程序包大         |
| PyQT     | Python | 底层集成度高、易上手     | 授权问题                 |
| WPF      | C#     | 类库丰富、扩展灵活       | 只支持windows，程序包大  |
| swing    | Java   | 基于AWT，组件丰富        | 性能差，UI一般           |
| NW.js    | JS     | 跨平台性好，界面美观     | 底层交互差、性能差，包大 |
| Electron | JS     | 相比Nw发展更好           | 底层交互差、性能差，包大 |
| CEF      | C++    | 性能好，灵活集成，UI美观 | 占用资源多，包大         |

- 底层依赖＋调用:CEF、QT、swing
- UI美观:Electron (Nw.js) . PyQT
- 跨平台: Swing (JAVA) 、 PyQT (Python、C++) 、Electron(前端)



# 2. electron 安装入门

## 2.1 安装electron 

由于electron 在安装过程中会通过 [`electron-download`](https://github.com/electron/get)下载 Electron 的预编译二进制文件。(`https://github.com/electron/electron/releases/tag/v$VERSION`, 这里的 `$VERSION` 是 Electron 的确切版本)。这会导致**国内下载无法进行**（但可以通过全局代理下载，一定要全局代理且是clash的TUN模式），进而引发electron安装失败。

按照官方的说法，需要设置两个环境变量

```bash
ELECTRON_MIRROR=http://npm.taobao.org/mirrors/electron/
ELECTRON_CUSTOM_DIR={{ version }}
```

**长期设置方法**

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/8a394e9dfc4b354f173e3ec74f61d7d9.png)

**短期设置方法**

```bash
set ELECTRON_MIRROR=http://npm.taobao.org/mirrors/electron/
set ELECTRON_CUSTOM_DIR={{ version }}
```

配置完成后即可正常下载electron

```bash
npm install electron -D
```



打包electron时会下载一个文件包，此时使用`ELECTRON_MIRROR`下载，故删除`ELECTRON_CUSTOM_DIR`环境变量

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/86f775bca474843d4e15d8782e9dd404.png)

最终解决方案是**使用clash 的 tun模式代理非系统代理应用**

## 2.2 入门配置

1. 创建一个vue3项目，添加electron 依赖

```bash
npm init vite
pnpm install electron@25.1.1 -D
pnpm install vite-plugin-electron@0.12.0 -D
pnpm install electron-builder@24.4.0 -D
pnpm install cross-env
```

2. 设置`package.json`

```json
{
  "name": "electron-demo",
  "private": true,
  "version": "0.0.0",
  "main": "dist-electron/index.js", // 必须设置
    // 删除 `type: module`
  "scripts": {
    "dev": "cross-env NODE_ENV=development vite", // 设置环境变量 开发模式
    "build": "vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "vue": "^3.2.47"
  },
  "devDependencies": {
    "@vitejs/plugin-vue": "^4.1.0",
    "electron": "^15",
    "electron-builder": "^24.4.0",
    "vite": "^4.3.9",
    "vite-plugin-electron": "^0.12.0"
  },
    // 添加打包信息
    "build": {
    "appId": "com.electron.desktop",
    "productName": "electron",
    "asar": true,
    "copyright": "Copyright © 2022 electron",
    "directories": {
      "output": "release/"
    },
    "files": [
      "dist",
      "dist-electron"
    ],
    "mac": {
      "artifactName": "${productName}_${version}.${ext}",
      "target": [
        "dmg"
      ]
    },
    "win": {
      "target": [
        {
          "target": "nsis",
          "arch": [
            "x64"
          ]
        }
      ],
      "artifactName": "${productName}_${version}.${ext}"
    },
    "nsis": {
      "oneClick": false,
      "perMachine": false,
      "allowToChangeInstallationDirectory": true,
      "deleteAppDataOnUninstall": false
    },
    "publish": [
      {
        "provider": "generic",
        "url": "http://127.0.0.1:8080"
      }
    ],
    "releaseInfo": {
      "releaseNotes": "版本更新的具体内容"
    }
  }
}

```

3. `vite.config.js`配置

```js
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import electron from 'vite-plugin-electron'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue(), electron({
    entry: 'electron/index.js'
  })],
})
```

4. electron入口文件配置

```js
// electron/index.js
import { app, BrowserWindow } from 'electron'
import * as path from 'path'
const createWindow = () => {
  const win = new BrowserWindow({
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false
    }
  })
  if (process.env['NODE_ENV'] !== 'development') {
    win.loadFile(path.join(__dirname, '../dist/index.html'))
  }
  else  {
    win.loadURL(`${process.env['VITE_DEV_SERVER_URL']}`)
  }
}

app.whenReady().then(createWindow)
```

5. 使用正常命令启动electron

```bash
npm run dev
```

6. 打包发布

```bash
npm run build
```



## 2.3 进程的通信

**渲染进程与主进程的通信**

1. 安装`vite-plugin-electron-renderer`

```bash
npm install vite-plugin-electron-renderer
```

2. 再`vite.config.js`中引入`electronRender`

```js
// vite.config.js
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import electron from 'vite-plugin-electron'
import electronRender from 'vite-plugin-electron-renderer'
// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue(), electron({
    entry: 'electron/index.js'
  }), electronRender()],
})

```

3. 再主进程中定义接收函数

```js
// eletron/index.js
import { app, BrowserWindow, ipcMain } from 'electron'
import * as path from 'path'
const createWindow = () => {
  const win = new BrowserWindow({
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false
    }
  })
  if (process.env['NODE_ENV'] !== 'development') {
    win.loadFile(path.join(__dirname, '../dist/index.html'))
  }
  else  {
    win.loadURL(`${process.env['VITE_DEV_SERVER_URL']}`)
  }
  // 接收消息
  ipcMain.on('message', (_,num) => {
    console.log(num);
  })
}

app.whenReady().then(createWindow)
```

4. 在渲染进程中定义发送消息

```vue
<script setup>
import HelloWorld from './components/HelloWorld.vue'
// 引入ipcRenderer
import { ipcRenderer } from 'electron'
const send = () => {
  ipcRenderer.send('message', '你好 from vue')
}
</script>

<template>
  <div>
    <a href="https://vitejs.dev" target="_blank">
      <img src="/vite.svg" class="logo" alt="Vite logo" />
    </a>
    <a href="https://vuejs.org/" target="_blank">
      <img src="./assets/vue.svg" class="logo vue" alt="Vue logo" />
    </a>
  </div>
  <button @click="send">发送消息</button>
  <!-- <HelloWorld msg="Vite + Vue" /> -->
</template>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
```

5. 发送消息为乱码

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/c02a3940885ff7132171eda5c152e47c.png)

6. 定义字符集

```json
"scripts": {
    //  定义字符集
    "dev": "chcp 65001 && cross-env NODE_ENV=development && vite",
    "build": "vite build && electron-builder build",
    "preview": "vite preview"
  },
```

7. 正常显示

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/f758fa3a10a8613b8dbf83c067fc636a.png)



**主进程到渲染进程的通信**

```js
// electron/index.js
import { app, BrowserWindow, ipcMain } from 'electron'
import * as path from 'path'
const createWindow = () => {
  const win = new BrowserWindow({
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false
    }
  })
  if (process.env['NODE_ENV'] !== 'development') {
    win.loadFile(path.join(__dirname, '../dist/index.html'))
  }
  else  {
    win.loadURL(`${process.env['VITE_DEV_SERVER_URL']}`)
  }
  // 接收消息
  ipcMain.on('message', (_,num) => {
    console.log('main: ',num);
  })

  //发送消息
  setTimeout(() => {
    win.webContents.send('load', '你好 from main process')
  }, 3000);
}

app.whenReady().then(createWindow)
```

```vue
// app.vue
<script setup>
import HelloWorld from './components/HelloWorld.vue'
// 引入ipcRenderer
import { ipcRenderer } from 'electron'
ipcRenderer.on('load', (_,message) => {
  console.log('render: ',message);
})
const send = () => {
  ipcRenderer.send('message', '你好 from vue')
}
</script>

<template>
  <div>
    <a href="https://vitejs.dev" target="_blank">
      <img src="/vite.svg" class="logo" alt="Vite logo" />
    </a>
    <a href="https://vuejs.org/" target="_blank">
      <img src="./assets/vue.svg" class="logo vue" alt="Vue logo" />
    </a>
  </div>
  <button @click="send">发送消息</button>
  <!-- <HelloWorld msg="Vite + Vue" /> -->
</template>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
```

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/8fbbe6b4d30e9b3d351af68c7870a519.png)
