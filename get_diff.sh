#!/bin/bash
clear
COMMON_FILES="logs/get_common_files_common.txt"
DIFF_DETAILS=logs/diff.log
DIFF_FILES=logs/diff.txt

dir_1="llvm-project"
dir_2="llvm-project-cd9a641613eddf25d4b25eaa96b2c393d401d42c"

##########

readarray -t lines <$COMMON_FILES

cnt=0
for line in "${lines[@]}"; do
    cnt=$((cnt + 1))
    if ((cnt % 1000 == 0)); then
        echo "Processed $cnt files ..."
        # break
    fi

    if ! diff "$dir_1/$line" "$dir_2/$line" >>$DIFF_DETAILS; then
        echo $line >>$DIFF_DETAILS

        # 记录存在差异的文件（后缀）
        echo $line >>$DIFF_FILES
    fi
done

echo "done! ("$cnt"files)"
