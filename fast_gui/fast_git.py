#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter
import tkinter.filedialog
import json
import os
import _thread

JSON_PATH = "config.json"

def drawList(row_index):
    i = 0
    for line in config_dict["path"]:
        v = TryGetIntVar(i)
        btn = tkinter.Radiobutton(root, text=line, variable=v, value=i, command=selectRow)
        btn.grid(row=row_index, column=0, sticky="w")
        row_index = row_index + 1
        i = i + 1
    
    tkinter.Button(root, text="Add",command=addPath).grid(row=row_index, column=0, sticky="sw")
    row_index = row_index + 1
    tkinter.Button(root, text="Clear",command=clearPath).grid(row=row_index, column=0, sticky="sw")
    return row_index

def TryGetIntVar(index):
    if index >= len(checkButtonList):
        v = tkinter.IntVar()
        checkButtonList.append(v)
        return v
    else:
        return checkButtonList[index]

def loadJson(path):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            load_dict = json.load(f)
            return load_dict
    else:
        with open(path, "w", encoding="utf-8") as f:
            load_dict = {}
            load_dict["path"] = []
            json.dump(load_dict, f)
            return load_dict

def saveJson1():
    saveJson(JSON_PATH, config_dict)

def saveJson(path, load_dict):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(load_dict, f)

def addPath():
    _path = tkinter.filedialog.askdirectory()
    if _path not in config_dict:
        config_dict["path"].append(_path)
        drawList(1)
        saveJson1()

def clearPath():
    config_dict = {}
    config_dict["path"] = []
    saveJson(JSON_PATH, config_dict)
    drawList(1)

def removeSelect():
    list = []
    i = 0
    for btnV in checkButtonList:
        print (btnV.get())

def selectRow():
    print ("")

def test():
    print ("Click")

def gitGC():
    for path in config_dict["path"]:
        if isGitDir(path):
            gitOperation(path, "git gc")
        else:
            print (path + " is not git dir")

def gitLfsPrune():
    for path in config_dict["path"]:
        if isGitDir(path):
            gitOperation(path, "git lfs prune")
        else:
            print (path + " is not git dir")

def gitStatus():
    for path in config_dict["path"]:
        if isGitDir(path):
            gitOperation(path, "git status")
        else:
            print (path + " is not git dir")

def isGitDir(path):
    if not os.path.isdir(path):
        return False
    sub_files = os.listdir(path)
    for sub_name in sub_files:
        sub_path = path = os.path.join(path, sub_name)
        if os.path.isdir(sub_path) and sub_path.endswith(".git"):
            return True
    return False

def gitOperation(path, opertaion):
    t = _thread.start_new_thread(doGitOperation, (path, opertaion,))

def doGitOperation(path, opertaion):
    os.chdir(path)
    os.system(opertaion)
    print ("\033[44;36m%s \033[0m" % os.getcwd())
    print ("\n\n")

config_dict = loadJson(JSON_PATH)
root = tkinter.Tk()
root.title("dd git")
checkButtonList = []

row_index = 0
tkinter.Label(root, text="list").grid(row=row_index, column=0, sticky="w")
row_index = row_index + 1

row_index = drawList(row_index)

tkinter.Button(root, text="git status",command=gitStatus).grid(row=0, column=3, sticky="e")
tkinter.Button(root, text="git gc",command=gitGC).grid(row=1, column=3, sticky="e")
tkinter.Button(root, text="git lfs prune",command=gitLfsPrune).grid(row=2, column=3, sticky="e")
# tkinter.Button(root, text="git sync",command=test).grid(row=3, column=3, sticky="e")

root.mainloop()