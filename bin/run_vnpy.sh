#/bin/bash

# 直接运行 vnpy 项目代码，将项目代码目录vn.trader绑定到容器的/opt/svnpy/vn.trader路径。
cd ..
docker run --name run_svnpy --rm -v `pwd`/vn.trader:/opt/svnpy/vn.trader svnpy