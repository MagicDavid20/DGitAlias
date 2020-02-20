#!/usr/bin/env python3
#-*-encoding:utf-8-*-

# @time : 2020-02-17
# @author : Deming


import os
import sys

git_suffix_tag = ".git"
git_alias_status = "git st"
git_alias_sync = "git sync"
git_alias_gc = "git gc"
git_alias_lfs_prune = "git lfs prune"

paths = [
    "TODO",
]


def is_git_dir(path):
    if os.path.isdir(path):
        sub_files = os.listdir(path)
        for sub_name in sub_files:
            sub_path = path = os.path.join(path, sub_name)
            if os.path.isdir(sub_path) and sub_path.endswith(git_suffix_tag):
                return True
    return false


def input_number_in_range(min_num, max_num):
    """input number in range

    :param min_num: the min number
    :type min_num: int

    :param max_num: the max number
    :type max_num: int
    """
    tip = "Please input number to choose step(range: %d ~ %d):\n" % (
        min_num, max_num)
    while True:
        input_num = input(tip)
        if input_num.isdigit():
            num = int(input_num)
            if num >= min_num and num <= max_num:
                return num
            else:
                print("out of range")


def auto_base(cmd):
    for path in paths:
        if is_git_dir(path):
            os.chdir(path)
            print("\033[44;36m%s \033[0m %s\n" % (os.getcwd(), "begin!"))
            os.system(cmd)
            print("\033[44;36m%s \033[0m %s\n" % (os.getcwd(), "succ!"))


def auto_st():
    auto_base(git_alias_status)


def auto_sync():
    auto_base(git_alias_sync)


def auto_gc():
    auto_base(git_alias_gc)


def auto_lfs_prune():
    auto_base(git_alias_lfs_prune)


def main():
    print("Input num to do next action")
    print("0: auto_st")
    print("1: auto_sync")
    print("2: auto_gc")
    print("3: auto_lfs_prune")

    index = input_number_in_range(0, 3)
    dict_funcs = {
        0: auto_st,
        1: auto_sync,
        2: auto_gc,
        3: auto_lfs_prune,
    }
    dict_funcs.get(index)()


if __name__ == "__main__":
    main()
    os.system("pause")
