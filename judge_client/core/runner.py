from multiprocessing import Pool
from judge_client.core.config import Languages


class Runner:
    def __init__(self,
                 language: Languages,
                 work_dir: str,
                 max_cpu_time: int,
                 max_memory: int):
        self.language = language
        self.work_dir = work_dir
        self.max_cpu_time = max_cpu_time
        self.max_memory = max_memory
