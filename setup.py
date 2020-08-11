from setuptools import setup, find_packages

setup(
    name="judge_client",
    version="0.1",
    description="core",
    packages=find_packages(include=('judge_client', 'judge_client.*')),
    author="simonkimi",
    requires=['redis', 'celery'],
    install_requires=['celery', 'redis']
)
