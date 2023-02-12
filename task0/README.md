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




