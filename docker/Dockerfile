FROM ubuntu:16.04

# 时区设置
ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# 中文支持
RUN locale-gen zh_CN.UTF-8 \
    && DEBIAN_FRONTEND=noninteractive dpkg-reconfigure locales
RUN locale-gen zh_CN.UTF-8
ENV LANG zh_CN.UTF-8
ENV LANGUAGE zh_CN:zh
ENV LC_ALL zh_CN.UTF-8

# 指定安装包
COPY ./Miniconda2-latest-Linux-x86_64.sh /tmp/conda/

# 替换 apt 源为阿里云
RUN echo "" > /etc/apt/sources.list \
    && echo "deb http://mirrors.aliyun.com/ubuntu/ xenial main multiverse restricted universe" >> /etc/apt/sources.list \
    && echo "deb http://mirrors.aliyun.com/ubuntu/ xenial-backports main multiverse restricted universe" >> /etc/apt/sources.list \
    && echo "deb http://mirrors.aliyun.com/ubuntu/ xenial-proposed main multiverse restricted universe" >> /etc/apt/sources.list \
    && echo "deb http://mirrors.aliyun.com/ubuntu/ xenial-security main multiverse restricted universe" >> /etc/apt/sources.list \
    && echo "deb http://mirrors.aliyun.com/ubuntu/ xenial-updates main multiverse restricted universe" >> /etc/apt/sources.list \
    && echo "deb-src http://mirrors.aliyun.com/ubuntu/ xenial main multiverse restricted universe" >> /etc/apt/sources.list \
    && echo "deb-src http://mirrors.aliyun.com/ubuntu/ xenial-backports main multiverse restricted universe" >> /etc/apt/sources.list \
    && echo "deb-src http://mirrors.aliyun.com/ubuntu/ xenial-proposed main multiverse restricted universe" >> /etc/apt/sources.list \
    && echo "deb-src http://mirrors.aliyun.com/ubuntu/ xenial-security main multiverse restricted universe" >> /etc/apt/sources.list \
    && echo "deb-src http://mirrors.aliyun.com/ubuntu/ xenial-updates main multiverse restricted universe" >> /etc/apt/sources.list \
    && apt-get clean \
    && apt-get update

# 网易源
#RUN echo "" > /etc/apt/sources.list \
#    && echo "deb http://mirrors.163.com/ubuntu/ precise-updates main restricted" >> /etc/apt/sources.list \
#    && echo "deb-src http://mirrors.163.com/ubuntu/ precise-updates main restricted" >> /etc/apt/sources.list \
#    && echo "deb http://mirrors.163.com/ubuntu/ precise universe" >> /etc/apt/sources.list \
#    && echo "deb-src http://mirrors.163.com/ubuntu/ precise universe" >> /etc/apt/sources.list \
#    && echo "deb http://mirrors.163.com/ubuntu/ precise-updates universe" >> /etc/apt/sources.list \
#    && echo "deb-src http://mirrors.163.com/ubuntu/ precise-updates universe" >> /etc/apt/sources.list \
#    && echo "deb http://mirrors.163.com/ubuntu/ precise multiverse" >> /etc/apt/sources.list \
#    && echo "deb-src http://mirrors.163.com/ubuntu/ precise multiverse" >> /etc/apt/sources.list \
#    && echo "deb http://mirrors.163.com/ubuntu/ precise-updates multiverse" >> /etc/apt/sources.list \
#    && echo "deb-src http://mirrors.163.com/ubuntu/ precise-updates multiverse" >> /etc/apt/sources.list \
#    && echo "deb http://mirrors.163.com/ubuntu/ precise-backports main restricted universe multiverse" >> /etc/apt/sources.list \
#    && echo "deb-src http://mirrors.163.com/ubuntu/ precise-backports main restricted universe multiverse" >> /etc/apt/sources.list \
#    && apt-get clean

# 安装编译环境
RUN apt-get install -y build-essential libboost-all-dev python-dev cmake

# 安装 conda
RUN echo "从获取 apt 软件" \
    && apt-get install bzip2 \
    && apt-get clean \
    && echo "安装 miniconda" \
    && cd /tmp/conda/ \
    && bash Miniconda2-latest-Linux-x86_64.sh -b -p /opt/conda \
    && rm Miniconda2-latest-Linux-x86_64.sh \
    && ln -s /opt/conda/bin/python /usr/local/bin/python \
    && ln -s /opt/conda/bin/conda /usr/local/bin/conda \
    && ln -s /opt/conda/bin/pip /usr/local/bin/pip \
    && echo "从 conda 安装 python 库" \
    && conda install -y pymongo bsddb \
    && conda clean -ay \
    && echo "安装结束"

# ENTRYPOINT [ "python", "/opt/svnpy/vn.trader/vtMain.py" ]
CMD [ "python", "/opt/svnpy/vn.trader/vtMain.py"]
