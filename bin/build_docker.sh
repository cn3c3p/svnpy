#/bin/bash

# 进入制作镜像的路径
cd ../docker

# 下载 miniconda 的安装包

# 删除旧镜像
docker rmi svnpy:latest

# 制作镜像
docker build --no-cache --force-rm -t svnpy .

# ln ../vn.trader 硬链接到

# 解除硬链接