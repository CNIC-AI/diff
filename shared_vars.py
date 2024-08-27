import os
import datetime


from arguments import *


current_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
logdir = "./logs"
os.makedirs(logdir, exist_ok=True)


args = parse_args()
dirs = [args.dir_1, args.dir_2]


PATH_TO_COMMON_FILES = f"{logdir}/common_files.json"
PATH_TO_RIGHT_ONLY_FILES = f"{logdir}/right_only_files.json"
PATH_TO_DIFF_FILES = f"{logdir}/diff_files.json"
PATH_TO_DIFF = f"{logdir}/diff.txt"


# result
logdir = f"{logdir}/{current_time}"
os.makedirs(logdir, exist_ok=True)


PATH_TO_JSON = f"{logdir}/functions.json"
