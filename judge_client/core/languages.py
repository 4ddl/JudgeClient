from enum import Enum
from .sandbox import UNLIMITED


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
        'run': {
            'cmd': '{exec_path}',
            "seccomp_rule": "c_cpp"
        }
    }

    CPP = {
        'index': 1,
        'code_file': 'main.cpp',
        'exec_file': 'main.o',
        'build': {
            'cmd': '/usr/bin/g++ {code_path} -o {exec_path} -O2 -Wall -lm --static -DONLINE_JUDGE',
            'max_cpu_time': 3000,
            'max_real_time': 5000,
            'max_memory': 128 * 1024 * 1024
        },
        'run': {
            'cmd': '{exec_path}',
            "seccomp_rule": "c_cpp"
        }
    }

    JAVA = {
        'index': 2,
        'code_file': 'Main.java',
        'exec_file': 'Main',
        'build': {
            'cmd': '/usr/bin/javac {code_path} -d {work_dir}',
            'max_cpu_time': 3000,
            'max_real_time': 5000,
            'max_memory': UNLIMITED
        },
        'run': {
            'cmd': '/usr/bin/java {exec_path}',
            "seccomp_rule": None
        }
    }

    PYTHON = {
        'index': 3,
        'code_file': 'main.py',
        'exec_file': '__pycache__/main.cpython-38.pyc',
        'build': {
            'cmd': '/usr/local/bin/python3 -m py_compile {code_path}',
            "max_cpu_time": 3000,
            "max_real_time": 5000,
            "max_memory": 128 * 1024 * 1024,
        },
        'run': {
            'cmd': '/usr/bin/python3 {exec_path}',
            "seccomp_rule": None
        }
    }

    NODEJS = {
        'index': 4,
        'code_file': 'main.js',
        'exec_file': 'main.js',
        'run': '/usr/bin/node {exec_path}',
        "seccomp_rule": None
    }

    SPJ_C = {
        'index': -1,
        'code_file': 'spj-{spj_version}.c',
        'exec_file': 'spj-{spj_version}.o',
        'build': {
            'cmd': '/usr/bin/gcc {code_path} -o {exec_path} -w -lm -O2 -std=c99 --static -DONLINE_JUDGE',
            'max_cpu_time': 3000,
            'max_real_time': 5000,
            'max_memory': 128 * 1024 * 1024
        },
        'run': {
            'cmd': '{exec_path} {in_file_path} {user_out_file_path}',
            "seccomp_rule": "c_cpp"
        }
    }
