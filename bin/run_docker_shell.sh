#/bin/bash

# 运行挂在了项目代码的容器的shell
cd ..
docker run --name run_svnpy --rm -v `pwd`/vn.trader:/opt/svnpy/vn.trader -it svnpy /bin/bash