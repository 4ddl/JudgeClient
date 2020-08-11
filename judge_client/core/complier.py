import os
import json
from .config import Languages
from judge_client.core import sandbox
from judge_client.service.exceptions import CompileError


class Compiler:
    def compile(self, work_dir: str, language: Languages) -> str:
        """
        :param work_dir: 工作目录, 默认为/tmp/judge/{RANDOM_UUID}
        :param language: 语言
        :return: 编译完成后可执行文件的目录
        """
        code_path = os.path.join(work_dir, language['code_file'])
        exec_path = os.path.join(work_dir, language['exec_file'])
        command = language['build'].foramt(code_path=code_path,
                                           exec_path=exec_path).split(' ')
        result = sandbox.run(
            max_cpu_time=language['build']['max_cpu_time'],
            max_real_time=language['build']['max_real_time'],
            max_memory=language['build']['max_memory'],
            max_stack=128 * 1024 * 1024,
            max_output_size=1024 * 1024,
            max_process_number=sandbox.UNLIMITED,
            exe_path=command[0],
            input_path=code_path,
            output_path=exec_path,
            error_path=exec_path,
            log_path=work_dir,
            args=command[1:],
            env=["PATH=" + os.getenv(os.getenv("PATH"), '/usr/bin')],
            seccomp_rule_name=None,
            uid=0,
            gid=0
        )
        if result["result"] != sandbox.RESULT_SUCCESS:
            if os.path.exists(exec_path):
                with open(exec_path, encoding="utf-8") as f:
                    error = f.read().strip()
                    os.remove(exec_path)
                    if error:
                        raise CompileError(error)
            raise CompileError("Compiler runtime error, info: %s" % json.dumps(result))
        else:
            os.remove(exec_path)
            return exec_path
