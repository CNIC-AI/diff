# 比较两个 C/C++ 程序的类、函数差异

遵循以下步骤

## 得到两个目录中的公共文件————公共文件才有比较的价值

``` bash
source ~/anaconda3/etc/profile.d/conda.sh
conda activate diff

python get_common_files.py "llvm-project" "llvm-project-cd9a641613eddf25d4b25eaa96b2c393d401d42c"
```

## 判断哪些公共文件存在差异————使用 diff 命令

``` bash
```

## 针对每个差异文件获取信息（功能）/差异分析（功能）

### 使用 clang（python binding）获取代码信息————哪些信息是我们关注的？

- 函数：

- 类：

- 命名空间：

``` json
{
    "filename": "xxx/xxx.h", 

}

```

### 差异分析

## 关心新增

- 新增文件：right.txt

- 新增函数：
