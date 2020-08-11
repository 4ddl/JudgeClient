from enum import Enum
import os


class Languages(Enum):
    """
    work_dir: 工作目录, 默认为 /tmp/judge/{RANDOM_UUID4}
    code_path: 代码完整路径, 例如 /tmp/judge/abcdefghijklmnopqrstuvwxyzabcdef/main.c
    exec_path: 编译文件完整路径, 例如 /tmp/judge/abcdefghijklmnopqrstuvwxyzabcdef/main.o
    """
    C = {
        'index': 0,
        'code_file': 'main.c',
        'exec_file': 'main.o',
        'build': {
            'cmd': '/usr/bin/gcc {code_path} -o {exec_path} -w -lm -O2 -std=c99 --static -DONLINE_JUDGE',
            'max_cpu_time': 3000,
            'max_real_time': 5000,
            'max_memory': 128 * 1024 * 1024
        },
        'run': '{exec_path}'
    }

    CPP = {
        'index': 1,
        'code_file': 'main.cpp',
        'exec_file': 'main.o',
        'build': {
            'cmd': 'g++ {code_path} -o {exec_path} -O2 -Wall -lm --static -DONLINE_JUDGE',
            'max_cpu_time': 3000,
            'max_real_time': 5000,
            'max_memory': 128 * 1024 * 1024
        },
        'run': '{exec_path}'
    }

    JAVA = {
        'index': 2,
        'code_file': 'Main.java',
        'exec_file': 'Main',
        'build': {
            'cmd': 'javac {code_path} -d {work_dir}',
            'max_cpu_time': 3000,
            'max_real_time': 5000,
            'max_memory': -1
        },
        'run': 'java {exec_path}'
    }

    PYTHON = {
        'index': 3,
        'code_file': 'main.py',
        'exec_file': '__pycache__/main.cpython-38.pyc',
        'build': {
            'cmd': 'python3 -m py_compile {code_path}',
            "max_cpu_time": 3000,
            "max_real_time": 5000,
            "max_memory": 128 * 1024 * 1024,
        },
        'run': 'python3 {exec_path}'
    }

    NODEJS = {
        'index': 4,
        'code_file': 'main.js',
        'exec_file': 'main.js',
        'run': 'node {exec_path}'
    }
