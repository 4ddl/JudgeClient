FROM python:3.8.5-slim
MAINTAINER simonkimi 805757448@qq.com
USER root
RUN echo "" > /etc/apt/sources.list
RUN echo "deb http://mirrors.aliyun.com/debian/ buster main non-free contrib" >> /etc/apt/sources.list
RUN echo "deb-src http://mirrors.aliyun.com/debian/ buster main non-free contrib" >> /etc/apt/sources.list
RUN echo "deb http://mirrors.aliyun.com/debian-security buster/updates main" >> /etc/apt/sources.list
RUN echo "deb-src http://mirrors.aliyun.com/debian-security buster/updates main" >> /etc/apt/sources.list
RUN echo "deb http://mirrors.aliyun.com/debian/ buster-updates main non-free contrib" >> /etc/apt/sources.list
RUN echo "deb-src http://mirrors.aliyun.com/debian/ buster-updates main non-free contrib" >> /etc/apt/sources.list
RUN echo "deb http://mirrors.aliyun.com/debian/ buster-backports main non-free contrib" >> /etc/apt/sources.list
RUN echo "deb-src http://mirrors.aliyun.com/debian/ buster-backports main non-free contrib" >> /etc/apt/sources.list
RUN apt-get update
RUN apt-get install -y gcc cmake wget unzip libseccomp-dev
# TODO 更多题目运行环境

# 判题环境
RUN pip3 install celery redis -i http://pypi.douban.com/simple/ --trusted-host=pypi.douban.com/simple ipython
WORKDIR /tmp
RUN wget -O Judger.zip https://github.com//WUSTOnlineJudge/Judger/archive/newnew.zip
RUN unzip Judger.zip && cd Judger-newnew && mkdir build && cd build && cmake .. && make && make install