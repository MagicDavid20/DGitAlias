#!/usr/bin/env python2
#-*-encoding:utf-8-*-
#Author: dd

import os
import sys

GIT_SUFFIX_TAG = ".git"
GIT_ALIAS_STATUS = "git st"
GIT_ALIAS_SYNC = "git sync"
GIT_ALIAS_GC = "git gc"

DIR_TUPLE = ("E:\\Test1", "E:\\Docs")

def auto_sync(path):
    os.chdir(path)
    os.system(GIT_ALIAS_STATUS)
    print "\033[44;36m%s \033[0m" % os.getcwd()
    print "========================================\n\n"

for path in DIR_TUPLE:
    auto_sync(path)
