# Django Rest Framwwork

Django本身并不是为了开发符合REST规范的Web API而设计, 不过借助Django REST Framework (DRF)这个神器我们可以快速开发出优秀而且规范的Web API来。Django REST framework 给Django提供了用于构建Web API 的强大而灵活的工具包, 包括序列化器、认证、权限、分页、过滤和限流。所以我们这里要感谢DRF，因为它，Django的应用前景更广了，减少了被淘汰的风险。

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/5e228b01712a30f976fa5fb473b085be.png)

## 1. 安装

1. 使用pip安装

```bash
pip install djangorestframework
```

2. 添加到`INSTALL_APPS`中

```py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework', # DRF
    'your_app', # 你自己的app
]
```

