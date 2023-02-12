<<<<<<< HEAD
#task 4:
```[vit@vm phyton_23]$ git checkout master
Switched to branch 'master'
[vit@vm phyton_23]$ git log --all --oneline --graph
* df6984b (first_branch) feat(add): added gitignore and modified README.md
* c0a4b32 (HEAD -> master) feat(add): added README.md
[vit@vm phyton_23]$ 
```
=======
#task 3
`git checkout -b first_branch`

#working directory status:
```
[vit@vm phyton_23]$ git log --all --graph
* commit c0a4b32a9a03f989d57ffec0c2d35f5fa7f6f432 (HEAD -> first_branch, master)
  Author: drspace17 <drspace17@gmail.com>
  Date:   Wed Feb 8 23:34:32 2023 +0200
  
      feat(add): added README.md
[vit@vm phyton_23]$ git status
On branch first_branch
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   task0/README.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	task0/.gitignore

no changes added to commit (use "git add" and/or "git commit -a")
[vit@vm phyton_23]$ ^C
[vit@vm phyton_23]$ 
[vit@vm phyton_23]$ git add task0/.gitignore
[vit@vm phyton_23]$ git status
On branch first_branch
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	new file:   task0/.gitignore

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   task0/README.md

[vit@vm phyton_23]$ 
```

#task5:
before merge:
```
[vit@vm phyton_23]$ git log --all --oneline --graph
* fbe09b0 (HEAD -> master) feat(add): added new changes to README.md
| * df6984b (first_branch) feat(add): added gitignore and modified README.md
|/  
* c0a4b32 feat(add): added README.md
```
after merge:
```
[vit@vm phyton_23]$ git status
On branch master
nothing to commit, working tree clean
[vit@vm phyton_23]$ git merge first_branch
Auto-merging task0/README.md
CONFLICT (content): Merge conflict in task0/README.md
Automatic merge failed; fix conflicts and then commit the result.
[vit@vm phyton_23]$ git branch
  first_branch
* master
[vit@vm phyton_23]$ git branch
  first_branch
* master
[vit@vm phyton_23]$ git checkout first_branch
task0/README.md: needs merge
error: you need to resolve your current index first
[vit@vm phyton_23]$ git branch
  first_branch
* master
[vit@vm phyton_23]$ git status
On branch master
You have unmerged paths.
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)

Changes to be committed:
	new file:   task0/.gitignore

Unmerged paths:
  (use "git add <file>..." to mark resolution)
	both modified:   task0/README.md

[vit@vm phyton_23]$ git add task0/README.md
[vit@vm phyton_23]$ git commit -m "feat(fix): problem fixed"
[master d259053] feat(fix): problem fixed
[vit@vm phyton_23]$ git status
On branch master
nothing to commit, working tree clean
[vit@vm phyton_23]$ git merge first_branch 
Already up to date.
[vit@vm phyton_23]$ git log --oneline --graph
*   d259053 (HEAD -> master) feat(fix): problem fixed
|\  
| * df6984b (first_branch) feat(add): added gitignore and modified README.md
* | fbe09b0 feat(add): added new changes to README.md
|/  
* c0a4b32 feat(add): added README.md
[vit@vm phyton_23]$ 
```



>>>>>>> first_branch
