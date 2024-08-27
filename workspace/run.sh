#!/bin/bash
clear
WORKSPACE=$(dirname $(readlink -f "${BASH_SOURCE[0]}"))
export PYTHONDONTWRITEBYTECODE=1

# env
source ~/anaconda3/etc/profile.d/conda.sh
conda activate diff

python post_processing.py
