#!/bin/bash
clear
export PYTHONDONTWRITEBYTECODE=1

source ~/anaconda3/etc/profile.d/conda.sh
conda activate diff

# python get_common_files.py \
#     "llvm-project" \
#     "llvm-project-cd9a641613eddf25d4b25eaa96b2c393d401d42c"

# python get_functions.py   # test-only
python -u main.py \
    "llvm-project" \
    "llvm-project-cd9a641613eddf25d4b25eaa96b2c393d401d42c"

python post_processing.py
