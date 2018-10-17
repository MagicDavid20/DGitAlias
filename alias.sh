echo -e "\n \033[47;30m Start Register David's Alias: \033[0m \n"


echo -e "\n \033[0;39m Register: git status \033[0m \n"
git config --global alias.st "status"

echo -e "\n \033[0;39m Register: git reset --hard \033[0m \n"
git config --global alias.rh "reset --hard"

echo -e "\n \033[0;39m Register: git log \033[0m \n"
git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset%C(yellow)[%ce]%Creset' --abbrev-commit"

echo -e "\n \033[0;39m Register: git pull \033[0m \n"
git config --global alias.pul "pull"

echo -e "\n \033[0;39m Register: git push \033[0m \n"
git config --global alias.pus "push"

echo -e "\n \033[0;39m Register: sync \033[0m \n"
git config --global alias.sync "! echo -e \"\\n\\033[1;34m === status and reset === \\033[0m \\n\" && git st && git add -A . && git rh && echo -e \"\\n\\033[1;34m === pull === \\033[0m \\n\" && git pul && git lg -8 && git st"

echo -e "\n \033[0;39m Register: rebase --continue \033[0m \n"
git config --global alias.rc "! echo -e \"\\n\\033[1;34m === rebase --continue === \\033[0m \\n\" && git rebase --continue"

echo -e "\n \033[0;39m Register: rebase --skip \033[0m \n"
git config --global alias.rs "! echo -e \"\\n\\033[1;34m === rebase --skip === \\033[0m \\n\" && git rebase --skip"

echo -e "\n \003[0;39m Register:stash push\033[0m \n"
git config --global alias.stashpush "! echo -e \"\\n\\033[1;34m === git add . && git stash === \\033[0m \\n\" && git add . && git stash"

echo -e "\n \003[0;39m Register:stash pop\033[0m \n"
git config --global alias.stashpop "! echo -e \"\\n\\033[1;34m === git stash pop === \\033[0m \\n\" && git stash pop && echo -e \"\\n\\033[1;34m === git reset HEAD === \\033[0m \\n\" && git reset HEAD && echo -e \"\\n\\033[1;34m === status === \\033[0m \\n\" && git st"

echo -e "\n \003[0;39m Register:cherry-pick\033[0m \n"
git config --global alias.cp "cherry-pick"

read wait