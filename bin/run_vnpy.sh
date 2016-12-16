#/bin/bash

# 直接启动
cd ..

# 直接启动
# python vtMain.py

# 在 docker 中启动
docker run --name run_svnpy --rm -v `pwd`:/opt/svnpy -it svnpy /bin/bash