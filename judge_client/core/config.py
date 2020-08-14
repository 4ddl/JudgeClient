import os
import pwd
import grp

DEBUG_MODE = os.getenv("DEBUG", "0") == '1'
WORK_DIR = os.getenv("WORK_DIR", '/tmp/judge')
COMPILER_USER_UID = pwd.getpwnam("compiler").pw_uid
COMPILER_GROUP_GID = grp.getgrnam("compiler").gr_gid
RUN_GROUP_GID = grp.getgrnam("code").gr_gid
RUN_USER_UID = pwd.getpwnam("code").pw_uid
