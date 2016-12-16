#/bin/bash

# 进入制作镜像的路径
cd ../docker

# 下载 miniconda 的安装包
if [ ! -f "./Miniconda2-latest-Linux-x86_64.sh" ]; then
    wget https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh
fi

# 删除旧镜像
docker rmi svnpy:latest

# 制作镜像
docker build --no-cache --force-rm -t svnpy .