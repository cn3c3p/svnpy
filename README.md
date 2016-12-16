# svnpy
迁移 vnpy 到 docker 镜像中

## 制作环境镜像

### 制作环境镜像
在```bin/```目录下运行:
```bash
bash build_images.sh
```

漫长的等待后之后，``````查看
```
➜  ~ docker images
REPOSITORY                   TAG                 IMAGE ID            CREATED             SIZE
svnpy                        latest              f49ebc9bb4f2        4 hours ago         882.5 MB
ubuntu                       16.04               4ca3a192ff2a        2 weeks ago         128.2 MB
```

vnpy 的运行环境镜像 ```svnpy:latest``` 制作成功。

### 测试运行
在```vn.trader/ctpGateway/CTP_connection.json```中配置CTP链接账号的服务器host。

在```bin/```目录下运行
```
➜  user@bin# bash run_docker_shell.sh
➜  root@5bb14b326ac9/#
```
建立容器，并在```bash```中进行交互。尝试启动 vnpy 实例
```
➜  root@5bb14b326ac9/# python /opt/svnpy/vn.trader/vtMain.py
CTP is OK ! balance : 1000000
```
运行成功。

### 直接运行实例
在```bin/```中，直接运行实例的脚本
```
➜  user@bin# bash run_vnpy.sh
CTP is OK ! balance : 1000000
```

