#!/usr/bin/env python2
#-*-encoding:utf-8-*-
#Author: dd

import os
import sys

GIT_SUFFIX_TAG = ".git"
GIT_ALIAS_STATUS = "git st"
GIT_ALIAS_SYNC = "git sync"
GIT_ALIAS_GC = "git gc"

def is_git_dir(path):
    if os.path.isdir(path):
        sub_files = os.listdir(path)
        for sub_name in sub_files:
            sub_path = path = os.path.join(path, sub_name)
            if os.path.isdir(sub_path) and sub_path.endswith(GIT_SUFFIX_TAG):
                return True
    return False

def auto_sync(name, path):
    os.chdir(path)
    os.system(GIT_ALIAS_STATUS)
    os.system(GIT_ALIAS_GC)
    print ("\033[44;36m%s \033[0m" % os.getcwd())
    print ("========================================\n\n")

cwd = os.getcwd()
files = os.listdir(cwd)
for name in files:
    path = os.path.join(cwd, name)
    is_git = is_git_dir(path)
    if is_git == True:
        auto_sync(name, path)
