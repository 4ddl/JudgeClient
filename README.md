# OnlineJudge 判题机

## 运行环境
> 需要环境Python3.8, Redis
> 需要libjudger.so


构建方法
```
sudo apt-get install libseccomp-dev
git clone https://github.com/WUSTOnlineJudge/Judger.git && cd Judger-newnew && mkdir build && cd build && cmake .. && make && sudo make install
```

## 环境变量
```
PATH: 构建工具路径, 默认为 /usr/bin
WORK_DIR: 代码编译运行工作目录, 默认为 /tmp/judge
CELERY_CONFIG: Celery配置包名, 例如 package.setting
DEBUG: Debug模式, 此模式下不会清理编译目录
```