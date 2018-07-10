echo -e "\n \033[47;30m Start Setup : \033[0m \n"

# 设置 rebase 模式
git config --global branch.autosetuprebase always

# 关闭 行结束符CRLF转换成LF
git config --global core.autocrlf false

# 不会对0×80以上的字符进行quote。中文文件名显示正常
git config --global core.quotepath false

read wait