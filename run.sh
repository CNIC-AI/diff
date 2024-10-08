#!/bin/bash
clear
WORKSPACE=$(dirname $(readlink -f "${BASH_SOURCE[0]}"))
export PYTHONDONTWRITEBYTECODE=1
dir_1=../llvm-project
dir_2=../llvm-project-cd9a641613eddf25d4b25eaa96b2c393d401d42c

# env
source ~/anaconda3/etc/profile.d/conda.sh
conda activate diff

# rm -rf logs/*
python -u main.py $dir_1 $dir_2
