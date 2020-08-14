# 此demo运行环境
# docker desktop 2.3.0.4 stable wsl2
# 已编译libjudger.so


import os

os.environ.setdefault("WORK_DIR", '/opt/project/judge')
os.environ.setdefault("DEBUG", '1')

from judge_client.core.judge import JudgeClient
from judge_client.core.config import Languages

code = """
#include<stdio.h>
int main() {
    printf("hello");
}
"""

j = JudgeClient(
    language=Languages.C,
    code=code,
    max_cpu_time=1000,
    max_memory=1024 * 10,
    test_cases=[{'input': 'World'}, {'input': 'Hello'}]
)

j.judge()
