import os
import shutil
from uuid import uuid4
from judge_client.core.config import Languages, DEBUG_MODE
from judge_client.core.complier import Compiler


class InitWorkSpace:
    def __init__(self, base_dir: str, language: Languages, code: str, test_cases: list):
        self.base_dir = base_dir
        self.code = code
        self.language = language
        self.test_cases = test_cases
        self.work_dir = ""

    def __enter__(self):
        try:
            # work_dir
            self.work_dir = os.path.join(self.base_dir, str(uuid4()).replace('-', ''))
            os.mkdir(self.work_dir)
            os.chmod(self.work_dir, 0o711)
            # code_dir
            code_path = os.path.join(self.work_dir, self.language.value['code_file'])
            with open(code_path, 'w') as f:
                f.write(self.code)
            Compiler().compile(self.work_dir, self.language)
            # input
            std_in = os.path.join(self.work_dir, 'stdin')
            os.mkdir(std_in)
            for index, test_case in enumerate(self.test_cases):
                with open(os.path.join(std_in, f"{index + 1}.in"), 'wb') as f:
                    if type(test_case['input']) == str:
                        f.write(test_case['input'].encode())
                    else:
                        f.write(test_case['input'])
            return self.work_dir
        except Exception as e:
            raise e

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not DEBUG_MODE:
            shutil.rmtree(self.work_dir)


class JudgeClient:
    def __init__(self,
                 language: Languages,
                 code: str,
                 max_cpu_time: int,
                 max_memory: int,
                 test_cases):
        self.code = code
        self.work_dir = ""
        self.language = language
        self.max_cpu_time = max_cpu_time
        self.max_memory = max_memory
        self.test_cases = test_cases
        self.base_dir = os.getenv("WORK_DIR", '/tmp/judge')

    def judge(self):
        with InitWorkSpace(base_dir=self.base_dir,
                           code=self.code,
                           language=self.language,
                           test_cases=self.test_cases) as work_dir:
            self.work_dir = work_dir

