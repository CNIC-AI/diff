#!/bin/bash
clear
dir1="llvm-project"
dir2="llvm-project-cd9a641613eddf25d4b25eaa96b2c393d401d42c"
rm diff.log diff.txt

readarray -t lines <common.txt

cnt=0
for line in "${lines[@]}"; do
    cnt=$((cnt + 1))
    if ((cnt % 1000 == 0)); then
        echo "Processed $cnt files ..."
        # break
    fi

    if ! diff "$dir1/$line" "$dir2/$line" >>diff.log; then
        echo $line >>diff.log
        echo $line >>diff.txt
    fi
done
