## 快速入门Django+Vue前后端分离项目

### 1. 创建Django项目

1. 使用PyCharm创建项目

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/5adb2ba7eb1501fa66eaf5f737b41026.png)

2. 这是创建完成的效果

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/c9a93a4f1d1f1103d13547d27a7b01cf.png)

3. 创建一个数据库表，如`SimpleDjango`
4. 安装`mysqlclient`库

```bash
pip install mysqlclient 
```

5. 配置`settings.py`文件，配置MySQL数据库引擎

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'SimpleDjango',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
    }
}
```

6. 执行同步操作，将数据迁移到Mysql

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/9e263cc5ccedb3dbca06777f5eae98fc.png)

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/9a437a59dc712525b301260786a81821.png)

7. 启动项目，验证是否创建成功

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/7a4048eaeb22c6cf02ab5a961599e204.png)

8. 创建一个app作为项目后端

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/0edf1c168096f89248deaa6af3ab254a.png)

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/798876eb422812c942d331474c2c1e20.png)

9. 将`backend`加入到`settings.py`的`INSTALLED_APPS`中

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'backend'
]
```

10. 在`backend/models.py`中写一个简单的`model`如下

```python
import json

from django.core.serializers import serialize
from django.db import models


# Create your models here.
class Book(models.Model):
    bookName = models.CharField(max_length=128, verbose_name='书名')
    createTime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return self.bookName

    def to_json(self):
        json_data = serialize('json', [self], fields=('pk', 'bookName', 'createTime'))
        json_dict = json.loads(json_data)[0]['fields']
        id = json.loads(json_data)[0]['pk']
        # print(json_dict)
        return {
            'id': id,
            'bookName': json_dict['bookName'],
            'createTime': json_dict['createTime']
        }
```

11. 创建迁移文件，并将其应用到数据库中

```bash
# 创建迁移文件
python manage.py makemigrations
# 应用修改到数据库
python manage.py migrate
```

12. 在 backend/views 里我们新增两个接口，一个返回所有的书籍列表，一个往数据库里添加一条book数据。

```python
import json

from django.core import serializers
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from backend.models import Book


# Create your views here.
@require_http_methods(['POST'])
def add_book(request):
    response = {}
    try:
        request_data = json.loads(request.body)
        book_name = request_data.get('book_name')
        book = Book(bookName=book_name)
        # 写入数据库
        book.save()
        # 返回消息
        response['code'] = 200
        response['msg'] = ''
    except Exception as e:
        response['code'] = 500
        response['msg'] = e
    return JsonResponse(response)


@require_http_methods(["GET"])
def show_books(request):
    response = {}
    try:
        books = Book.objects.all()
        book_list = []
        for book in books:
            book_list.append(book.to_json())
        response['list'] = book_list
        response['msg'] = ''
        response['code'] = 200
    except Exception as e:
        print(e)
        response['msg'] = str(e)
        response['code'] = 500
    return JsonResponse(response)
```

13. 在 backend 目录下，新增一个 urls.py 文件，把我们新增的两个接口添加到路由里

```python
from django.urls import path

from backend.views import add_book, show_books

urlpatterns = [
    path("add_book", add_book),
    path("show_books", show_books),
]
```

14. 最后要把`backend` 下的 `urls` 添加到项目 `SimpleDjango`下的 `urls` 中，才算完成路由

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("backend.urls")),
]
```

15. 重新启动服务，测试接口

```bash
python manage.py runserver
```

16. 一开始没有书籍

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/d248044b4af7f26405ef5a860a951a24.png)

17. 添加书籍

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/6f3951385b424e03a727a302a020cf59.png)

18. 再次访问

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/efae8c506063c8aca0f5af7ec3984653.png)



### 2. 创建Vue项目

1. 使用`pnpm`创建`vite`项目

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/527ba4dda7fb0f0d2d68e03f375c806c.png)

2. 创建完成

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/7b3dca0613acd8912ab436e2966a7a9e.png)

3. 添加`alova`请求库

```bash
pnpm install alova
```

```ts
import { createAlova } from 'alova'
import GlobalFetch from 'alova/GlobalFetch'
import VueHook from 'alova/vue'
import { message } from 'ant-design-vue'


let baseURL = 'http://localhost:8000/api'

const errCode = {
  401: '登录失效，请重新登录',
  403: '没有权限',
  404: '请求地址错误',
  500: '服务器错误',
}

// 1. 创建alova实例
const request = createAlova({
  baseURL,
  // VueHook用于创建ref状态，包括请求状态loading、响应数据data、请求错误对象error等
  statesHook: VueHook,
  // 请求适配器，推荐使用fetch请求适配器
  requestAdapter: GlobalFetch(),
  // 全局的响应拦截器
  responded: {
    onSuccess: async (response, method) => {
      let json
      try {
        json = await response.json()
      } catch (e) {
        message.error('序列化失败')
        throw new Error('序列化失败')
      }
      const msg = json?.msg || errCode[json?.code as keyof typeof errCode]
      if (json.code !== 200) {
        if (msg) {
          message.error(msg)
          throw new Error(msg)
        }
      }
      if (msg) message.success(msg)
      return json.data || json
    },
    onError: async (error, method) => {
      message.error(error.message)
    },
  },
})

export default request
```

4. 在`App.vue`中编写如下代码

```vue
<script setup lang='ts'>
import request from '@/utils/request'
import { nextTick, ref } from 'vue'

const bookName = ref('')
const dataSource = ref()
const columns = ref([
  {
    title: 'ID',
    dataIndex: 'id',
  },
  {
    title: '书名',
    dataIndex: 'bookName',
  },
  {
    title: '添加时间',
    dataIndex: 'createTime',
  },
])

async function init() {
  const data = await request.Get('show_books').send(true) as any
  dataSource.value = data.list
}

async function addBook() {
  console.log(bookName.value)
  await request.Post('add_book', { 'book_name': bookName.value }).send(true)
  bookName.value = ''
  await init()
}

init()

nextTick(() => {

})
</script>

<template>
  <header>
    <h1>Django+Vue前后端分离项目</h1>
  </header>
  <main>
    <div class='input-panel'>
      <a-input v-model:value='bookName' />
      <a-button class='add-btn' type='primary' @click='addBook'>新增</a-button>
    </div>
    <a-table :data-source='dataSource' :columns='columns'>
    </a-table>
  </main>
</template>

<style lang='scss'>
* {
  padding: 0;
  margin: 0;
}

header {
  background-color: #41b883;
  color: #fff;
  text-align: center;
  padding: 20px;
}

main {
  padding: 20px;

  .input-panel {
    display: flex;
    justify-content: center;
    width: 400px;

    .add-btn {
      margin-left: 10px;
    }
  }
}
</style>

```

5. 发现请求跨域，这里使用`cors`即可

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/94ee44967e38c9cfb59244ddbe006102.png)

### 3. 解决跨域问题

安装第三方包`django-cors-headers`

```bash
pip install django-cors-headers
```

修改`settings.py`

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware', # 添加cors
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware', # 关闭csrf
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOW_ALL_ORIGINS = True
```

这个时候前端即可访问后端服务

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/87c0a42a840c846dcdf910d15e8f03cc.png)



### 4. 使用Django的服务器部署前端

使用Django的服务器部署前端即整合Django和Vue到一个项目中，启动Django时便可启动前端项目

1. 修改 djangoVue 下的 urls ，使用通用视图创建最简单的模板控制器，访问 『/』时直接返回 index.html

```python
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('backend.urls')),
    path(r'', TemplateView.as_view(template_name="index.html")),
]
```

2. 配置 Django 项目的模板搜索路径。上一步使用了 Django 的模板系统，所以需要配置一下模板使 Django 知道从哪里找到 index.html。修改 settings.py 文件，如下：

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'DIRS': [os.path.join(BASE_DIR, 'frontend/dist')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

3. 配置静态文件的url和搜索路径

```python
# settings.py 静态文件搜索路径
STATIC_URL = 'assets/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'frontend/dist/assets')
]
```

```python
# urls.py 添加静态文件url到总url配置文件中
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from SimpleDjango import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("backend.urls")),
    path(r'', TemplateView.as_view(template_name="index.html")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```

4. 配置完成，启动 Django 服务 `python manage.py runserver`，就能够看到我们的前端页面在浏览器上展现：

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/73652a13c19789fa25522b170bfa6f89.png)

