import os
from uuid import uuid4
from .config import Languages


class JudgeClient:
    def __init__(self,
                 language: Languages,
                 code: str,
                 max_cpu_time: int,
                 max_memory: int,
                 test_case):
        self.code = code
        self.work_dir = os.path.join(os.getenv('WORK_DIR', '/tmp/judge'), str(uuid4()))
        self.language = language
        self.max_cpu_time = max_cpu_time
        self.max_memory = max_memory
        self.test_case = test_case

    def init(self):
        os.mkdir(self.work_dir)
        code_path = os.path.join(self.work_dir, self.language['build']['code_file'])
        with open(code_path, 'w') as f:
            f.write(self.code)










