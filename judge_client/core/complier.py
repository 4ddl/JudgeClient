import os
import json
from .config import Languages
from judge_client.core import sandbox
from judge_client.core.exceptions import CompileError


class Compiler:
    def compile(self, work_dir: str, language: Languages):
        """
        :param work_dir: 工作目录, 默认为/tmp/judge/{RANDOM_UUID}
        :param language: 语言
        """
        code_path = os.path.join(work_dir, language.value['code_file'])
        exec_path = os.path.join(work_dir, language.value['exec_file'])
        log_path = os.path.join(work_dir, 'compile.log')
        command = language.value['build']['cmd'].format(code_path=code_path,
                                                        exec_path=exec_path).split(' ')
        if language == language.PYTHON:
            py_cache = os.path.join(work_dir, "__pycache__")
            os.mkdir(py_cache)
            os.chmod(py_cache, 0o711)
        print(command)
        # TODO uid和gid的获取

        result = sandbox.run(
            max_cpu_time=language.value['build']['max_cpu_time'],
            max_real_time=language.value['build']['max_real_time'],
            max_memory=language.value['build']['max_memory'],
            max_stack=128 * 1024 * 1024,
            max_output_size=1024 * 1024,
            max_process_number=sandbox.UNLIMITED,
            exe_path=command[0],
            input_path=code_path,
            output_path=exec_path,
            error_path=exec_path,
            log_path=log_path,
            args=command[1:],
            env=["PATH=" + os.getenv("PATH", '/usr/local/bin')],
            seccomp_rule_name=None,
            uid=0,
            gid=0
        )
        if result["result"] != sandbox.RESULT_SUCCESS:
            if os.path.exists(exec_path):
                with open(exec_path, encoding="utf-8") as f:
                    error = f.read().strip()
                    if error:
                        raise CompileError(error)
            raise CompileError("Compiler runtime error, info: %s" % json.dumps(result))
