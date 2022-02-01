
# Git


- [1 Overview](#1-overview)
- [1.1 VCS & Git](#11-vcs--git)
  - [1.2 Links](#12-links)
  - [1.3 Terms](#13-terms)
- [2 Configuration and Status](#2-configuration-and-status)
  - [2.1 .gitignore](#21-gitignore)
  - [2.2 Setting Credentials](#22-setting-credentials)
  - [2.3 Set Connections to Remote Repositories](#23-set-connections-to-remote-repositories)
  - [2.4 Getting Information](#24-getting-information)
- [3 Basics](#3-basics)
  - [3.1 Creating a Repository](#31-creating-a-repository)
- [3.2 Staging and Committing](#32-staging-and-committing)
  - [3.3 Pushing and Pulling](#33-pushing-and-pulling)
- [4 Undoing](#4-undoing)
  - [4.1 Checkout](#41-checkout)
  - [4.2 Rm](#42-rm)
  - [4.4 Revert](#44-revert)
  - [4.3 Reset](#43-reset)
- [5 Branching and Merging](#5-branching-and-merging)
- [6 Examples](#6-examples)


## 1 Overview

## 1.1 VCS & Git

Version control systems (VCS) are software that enables us to keep track of changes to files. This helps us retrieve older versions of code and undo mistakes. It also allows multiple developers to work on a project simultaneously. It can be used with any type of file, but is ordinarily used for source code. [Git](https://git-scm.com/) is one popular form of version control, others include [SVN](https://subversion.apache.org/) and [Mercurial](https://www.mercurial-scm.org/).


Git calls the directory it tracks changes in a **repository**. Git stores timestamped snapshots of the state of the repository called **commits**:

```
commit 6aeba8f3f2c386e4dc97fd3e0b8fbfee8d751ac5
Author: David Selassie <david@pdxcodeguild.com>
Date:   Tue Mar 29 16:29:27 2016 -0700
```

Each commit has a globally unique **hash**, an author, a timestamp, a description of what changed, and a **parent** commit. Each commit stores the exact changes made to the files from the last commit. Commits build on top of each other to form a **history**, the full record of all snapshots of a project. The most recent commit is called the *HEAD*.

```
Time --->
C1 - C2 - C3 - C4
                |
                HEAD
```

Repositories are often hosted on remote servers for safety and convenience. Popular repository hosting websites include [GitHub](http://github.com/), [Bitbucket](https://bitbucket.org/), and [GitLab](https://about.gitlab.com/).

There are several graphical interfaces to Git. You can edit files directly on GitHub, use [GitHub Desktop](https://desktop.github.com/), or use Visual Studio Code or Atom.

### 1.2 Links

- Official
  - [Book](https://git-scm.com/book/en/v2)
  - [Docs](https://git-scm.com/docs)
  - [Tutorial](https://git-scm.com/docs/gittutorial/)
- GitHub
  - [Guides](https://guides.github.com/)
  - [Cheat Sheet](https://github.github.com/training-kit/downloads/github-git-cheat-sheet.pdf)
- Atlassian
  - [Tutorials](https://www.atlassian.com/git/tutorials)
  - [Cheat Sheet](https://www.atlassian.com/git/tutorials/atlassian-git-cheatsheet)
- [The Simple Guide](https://rogerdudler.github.io/git-guide/)
- [Learn Git Branching](https://learngitbranching.js.org/)


### 1.3 Terms

- **git** a popular version control system https://git-scm.com/
- **branch** a thread of commits
- **clone** creating a local copy of a remote repository
- **commit** a list of changes made to files
- **HEAD** the latest commit
- **index** the list of files tracked by git
- **master** the primary branch of the repository
- **merge** combining two branches into one by taking parts from each
- **origin** the default remote repository
- **pull** synchronizing a local repository with a remote repository
- **push** synchronizing a remote repository with our local repository
- **rebase** combining two branches into one by rewriting the commit history
- **remote** a remote repository, stored with a name and url



## 2 Configuration and Status


### 2.1 .gitignore

The `.gitignore` file is a special file at the top level of your repository that lists all files that should not be added to the history. These can include things like API keys, libraries, database passwords, user-specific configuration files, etc.

```
secrets.py
.idea
.DS_Store
```


### 2.2 Setting Credentials

Set your credentials on the current repo:

- `git config user.name "Your Name"`
- `git config user.email you@email.com`
- `git config credential.helper store`

Set your credentials on your entire computer:

- `git config --global user.name "Your Name"`
- `git config --global user.email you@email.com`
- `git config --global credential.helper store`

### 2.3 Set Connections to Remote Repositories

- `git remote` list remote repositories
- `git remote -v` list remote repositories and their urls
- `git remote add <remote_name> <repo_url>` adds a new remote repository with the given name
- `git remote rm <remote_name>` removes a remote repository
- `git remote set-url <remote_name> <repo_url>` updates the url of the remote repository with the given name


### 2.4 Getting Information

- `git diff` shows the difference between files and the last commit
- `git diff --cached` shows the difference between staged files and the last commit
- `git status` shows the current branch, current commit, staged files, changed files, and untracked files
- `git log` shows a history of commits
- `git log --oneline` shows a history of commits, each on one line


## 3 Basics


### 3.1 Creating a Repository

There are two ways of creating a repository [git book](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository)

- `git clone <repo_url>` creates a local repository in the current folder, which is automatically connected to the remote repository.
- `git init` initializes the current folder as a repository. One must then add a remote repo in order to push.


## 3.2 Staging and Committing

Git has a staging area for files to be added to before they're committed to the history.


- `git add <path>` adds a file or folder of files to staging
- `git add .` adds all updated files to staging
- `git commit` commits staged changes to the history and opens a text editor for a commit message
- `git commit -a` add and commit in one line
- `git commit -m "<commit_message>"` commit with the given message
- `git rm --cached <file>` `git reset <file>` removes a file from staging
- `git diff` shows the difference between files and the last commit
- `git diff --cached` shows the difference between staged files and the last commit
- `git status` shows the current branch, current commit, staged files, changed files, and untracked files
- `git log` shows a history of commits


### 3.3 Pushing and Pulling

- `git stash` stash the uncommitted changes to files
- `git stash apply` applies the stashes changes
- `git stash pop` applies the stashed changes and clears the stash
- `git fetch` loads metadata from remote repository without merging changes
- `git push` updates the remote repository with the local respository, shorthand for `git push origin master`
- `git push <remote> <branch>` push to the particular remote and branch
- `git push --set-upstream <remote> <branch>` set the upstream branch and push
- `git pull` update the local repository with the remote repository
- `git pull <remote> <branch>` pull from a particular remote and branch

## 4 Undoing


`<commit>` can be `HEAD~N` where N is the number of commits back from the latest, or the `hash` of the commit.

### 4.1 Checkout

- `git checkout -- <file>` replaces the file with the one last committed
- `git checkout <commit>` moves the repository state to the previous commit

### 4.2 Rm

Rm removes a file from git tracking

- `git rm <file>` remove a file from the index and delete it from disk
- `git rm -r <directory>`  remove a directory from the index and delete it from disk
- `git rm --cached <file>` remove a file from the index without deleting it from disk, making git "forget" it exists
- `git rm -r --cached <directory>` recursively remove a directory from the index

### 4.4 Revert

- `git revert <commit>` add a new commit that undoes the changes from a previous commit.

### 4.3 Reset

- `git reset <file>` unstages a file
- `git reset --soft <commit> ` goes back to a previous commit, does not modify file contents
- `git reset --hard <commit>` goes back to a previous commit, DOES modify file contents
- with both of these you'll need to follow up with `git push origin master --force`


## 5 Branching and Merging

- `git branch` view branches, and which branch you're currently on
- `git branch -a` view local and remote branches
- `git branch <branch>` create a branch
- `git checkout <branch>` switch to a branch
- `git checkout -b <branch>` create a branch and check it out
- `git branch -d <branch>` delete a branch
- `git merge <branch>` merges the given branch into the current branch
- `git push -u origin <branch>` pushes the branch to the remote


<!-- #### 7.5 Tagging -->

## 6 Examples


Create a repo and link it to a remote repository

```
echo "# Git Demo" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin <url>
git push -u origin master
```

Undo a bad commit

```
cd /tmp/example
git init
echo "Initial text" > README.md
git add README.md
git commit -m "initial commit"
echo "bad update" > README.md 
git commit -am "bad update"
git revert HEAD
git log --oneline
```

Contribute to an existing repository

```
git clone <url>
cd repo
git branch -b my-branch
// make changes, for example, edit `file1.md` and `file2.md` using the text editor
git add file1.md file2.md
git commit -m "added file1 and file2"
git push --set-upstream origin my-branch
```

Contribute to an existing branch

```
git clone <url>
cd repo
git pull
git checkout feature-a
// make changes, for example, edit `file1.md` using the text editor
git add file1.md
git commit -m "edit file1"
git push
```
