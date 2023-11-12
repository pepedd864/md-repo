## 1. Github Actions介绍

### 1.1 什么是Github Actions

GitHub Actions 是 GitHub 推出的持续集成（Continuous Integration，简称 **CI**）服务，它提供了整套虚拟服务器环境，基于它可以进行构建、测试、打包、部署项目等等操作。

**持续集成（CI \ CD）**主要有三个： 持续集成、持续交付、持续部署。

我们一般的软件开发流程是：

> 1. 开发人员本地代码 commit
> 2. 通过 git hook 触发自动化测试
> 3. 测试通过后，合并发布分支
> 4. 通过 git hook 触发自动部署服务

我们可以看到，CI \ CD 是由很多操作组成的，比如执行自动化测试、分支合并、服务部署等，而 GitHub 把这一系列的操作都称为 Actions。

GitHub 提供一个官方市场：[GitHub Action Market](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Factions) ，在这里可以搜索到你想要的任何 actions，直接引用别人造好的轮子。

### 1.2 基本概念

GitHub Actions 主要有以下几个概念

- **Workflows**

  工作流，可以添加到存储库中的自动化过程。工作流由一个或多个作业组成，可以由事件调度或触发。

- **Event**

  事件，触发工作流的特定动作。例如，向存储库提交 pr 或 pull 请求。

- **Jobs**

  作业，在同一跑步器上执行的一组步骤。默认情况下，具有多个作业的工作流将并行运行这些作业。

- **Steps**

  步骤，可以在作业中运行命令的单个任务。步骤可以是操作，也可以是 shell 命令。作业中的每个步骤都在同一个运行程序上执行，从而允许该作业中的操作彼此共享数据。

- **Actions**

  操作是独立的命令，它们被组合成创建作业的步骤。操作是工作流中最小的可移植构建块。你可以创建自己的动作，或者使用 GitHub 社区创建的动作。

- **Runners**

  运行器，安装了 GitHub Actions 运行器应用程序的服务器。。Github 托管的运行器基于 Ubuntu Linux、Microsoft Windows 和 macOS，工作流中的每个作业都在一个新的虚拟环境中运行。



## 2. Workflow语法

workflow 文件必须存储在仓库的 `.github/workflows` 的目录中，扩展名为 `.yml` 或 `.yaml`

**name**

- workflow 的名称， GitHub 在仓库的操作页面上显示 workflow 的名称。

**on**

- 触发 workflow 的 GitHub 事件的名称。

```yaml
# 单个事件
on: push

# 多个事件列表
on: [push, pull_request]

# 指定main分支的push
on:
  push:
    branches:
      - main
```

**还可以使用定时调度**：

```yaml
on:
  schedule:
    - cron: '*/30 5,17 * * *'
```

**Jobs**

- 作业，workflow 主要执行的核心任务。

- `jobs.<job_id>`
  - 每项作业必须关联一个 ID。例如上面实例的 ID 为 **build**

- `jobs.<job_id>.name`
  - 作业显示在 GitHub 上的名称。

- `jobs.<job_id>.needs`
  - 识别在此作业运行之前必须成功完成的任何作业。

```yaml
jobs:
  job1:
  job2:
    needs: job1
  job3:
    needs: [job1, job2]
```

在此示例中，`job1` 必须在 `job2` 开始之前成功完成，而 `job3` 要等待 `job1` 和 `job2` 完成。

- `jobs.<job_id>.runs-on`

要运行作业的机器类型。 机器可以是 GitHub 托管的运行器或自托管的运行器。

可用的 GitHub 托管的运行器类型包括：

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/24a367d10847b91c63e19e3167c27432.webp)

- `jobs.<job_id>.steps`

  - 步骤，每个 Job 包含一个或多个步骤。步骤可以是运行命令、运行设置任务，或者运行仓库中的操作和 Dcoker 镜像发布等。

  - 每个步骤都可以定义以下几个字段：

```yaml
jobs..steps[*].id : 步骤的唯一标识符
jobs..steps[*].name : 步骤显示在 GitHub 上的名称
jobs..steps[*].if : 自定义表达式，判断是否满足条件
jobs..steps[*].uses : 选择公共仓库中、或发布 Docker 容器映像作为一部分运行的操作。例如上面的实例都是使用了公共仓库提供的操作
jobs..steps[*].run : 运行 shell 命令程序。
```



## 3. 使用案例-自动部署前端项目

1. 打开仓库地址，点击actions

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/3e5a9f56535f8f97047f1da4c8baf8cb.png)

2. 新建工作流

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/78cc3411b995829a61f499a8a113f4f6.png)

3. 自己设置workflow

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/a8814f8104c83d257f3e703ce68bee70.png)

4. 编写yaml

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/f4dd48c181d4748a325414ad0e683345.png)

5. 在右侧可以使用一些基本的命令，如安装nodejs 安装pnpm 安装jdk等等，类似docker

<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/417c235967d48488d584aaaf8eb68648.png" style="zoom:50%;" />

6. 编写完成提交代码，actions便会自动开始执行

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/62c2038cb54ae3e5ddd9eaf93b02b2ed.png)

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/edafe7cd58eaf029892a37fce8118c80.png)

7. 最后上传代码到云服务器上

8. 对于云服务器IP，用户名，密码，密钥等重要隐私信息，可以使用github仓库的secrets管理

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/2c432f7edd9a317076fc99cb728caa7f.png)

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/705a94fcc14c996a63940e28517dd059.png)

9. 在代码中使用`${{ secrets.REMOTE_HOST }}`的格式引用

