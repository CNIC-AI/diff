#!/bin/bash
clear

source ~/anaconda3/etc/profile.d/conda.sh
conda activate diff

python -u dump_files.py
