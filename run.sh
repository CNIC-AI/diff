#!/bin/bash
clear
export PYTHONDONTWRITEBYTECODE=1

source ~/anaconda3/etc/profile.d/conda.sh
conda activate diff

# python -u main.py
python statistic.py
