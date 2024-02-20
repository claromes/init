```shell
git branch -D branch_name # delete branch locally

git push origin --delete branch_name # delete branch remotely

# remote add origin/ remote set-url origin
# source https://stackoverflow.com/a/42830632
git remote add origin git@github.com:user/repo.git

git remote set-url origin git@github.com:user/repo.git

git push -u origin main

git stash pop # undo last git stash
```
