## Azure虚拟机开启root用户

默认情况微软 Azure 云是没有开启 root 账户的，root 账户是禁用状态。

1. 首先执行：`sudo passwd root` 命令初始化`root`用户密码

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/74b92af332c70ce1061225c82f390b15.png)

2. 修改 `sshd_config` 文件 开启 root 访问权限

```bash
sudo vim /etc/ssh/sshd_config
```

3. 在 `sshd_config` 文件里的 `Authentication` 部分加上以下内容，如图所示：

```bash
PermitRootLogin yes
```

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/bd6ed50ef35966c2e3b6706c0b018865.png)

4. 编辑完毕后，重启 ssh 服务，执行如下命令：

```bash
sudo systemctl restart sshd # 重启 ssh 服务以应用更改
```

