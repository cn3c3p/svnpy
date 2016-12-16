# svnpy
迁移 vnpy 到 docker 镜像中

## 制作环境镜像

### 获得 miniconda

1. 点[这里](http://conda.pydata.org/miniconda.html)下载 miniconda Linux 64-bit的安装包。
2. 名将其命名为```Miniconda2-latest-Linux-x86_64.sh```。
3. 并放置在```docker/```下。

### 制作环境镜像
在```bin/```目录下运行:
```bash
sh build_docker.sh
```







