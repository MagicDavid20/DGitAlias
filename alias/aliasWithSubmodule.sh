echo -e "\n \033[47;30m Start Register Submodule Alias: \033[0m \n"

# next for submodule
echo -e "\n \033[0;39m Register: subpul \033[0m \n"
git config --global alias.subpul "! echo -e \"\\n\\033[1;34m === pull all submodule === \\033[0m \\n\" && git submodule foreach \" git pull origin HEAD:master\" "

echo -e "\n \033[0;39m Register: subpus \033[0m \n"
git config --global alias.subpus "! echo -e \"\\n\\033[1;34m === push all submodule === \\033[0m \\n\" && git submodule foreach \"git status && git add . && git commit  && git push origin HEAD:master && git status\" "

echo -e "\n \033[0;39m Register: sinsubpul \033[0m \n"
git config --global alias.sinsubpul "! echo -e \"\\n\\033[1;34m === pull single submodule === \\033[0m \\n\" && git pull origin HEAD:master "

echo -e "\n \033[0;39m Register: sinsubpus \033[0m \n"
git config --global alias.sinsubpus "! echo -e \"\\n\\033[1;34m === push single submodule === \\033[0m \\n\" && git push origin HEAD:master"

echo -e "\n \033[0;39m Register: submodule reset --hard \033[0m \n"
git config --global alias.subrh "! echo -e \"\\n\\033[1;34m === submodule reset --hard === \\033[0m \\n\" && git submodule foreach \" git rh\""

echo -e "\n \033[0;39m Register: sync \033[0m \n"
git config --global alias.sync "! echo -e \"\\n\\033[1;34m === sync === \\033[0m \" && echo -e \"\\n\\033[1;34m === status and reset === \\033[0m \\n\" && git st && git add -A . && git rh && git subrh && echo -e \"\\n\\033[1;34m === pull === \\033[0m \\n\" && git pul && git subpul && git lg -8 && git st"

read wait