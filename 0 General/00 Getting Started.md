# Lab 0: Getting Started
For our very first lab we will be creating a folder to hold all of our labs. This will also be an exercise in utilizing git.

1. Start by making sure you are in the correct folder, we should be inside class_kiwi in our terminal. To verify you can run the command `pwd`. This should show your current working directory.
2. Once we are inside the repository (class_kiwi folder) we can go ahead and create a new branch to store all of our changes. Let's create a branch with our name followed by lab0.
   - The command we will use to create a new branch is: `git checkout -b branch-name`
   - ex. My name is Anthony so my branch would look like anthony-lab0
   - The full command would be `git checkout -b anthony-lab0`
   - You can verify what branch you are on by running the command `git branch`
3. Create a folder inside the `code` folder named 'yourfirstname' all lowercase.
   - ex. My name is Anthony, So I will create a folder called anthony
4. Inside your newly created folder, create a `README.md` file. This is a markdown file and is generally used to provide context to folders within Github.
5. Open your `README.md` file and at the top type in a pound sign `#` followed by your name.
   - ex. `# Anthony Wallace`
   - You can also use this file to keep notes within the class, or to add links later on to your projects.
6. Now let's run a `git status` to see the changes we have made.
    - This should give you a similar output to: 
```
Untracked files:
(use "git add <file>..." to include in what will be committed)
	Code/anthony/

no changes added to commit (use "git add" and/or "git commit -a")
```
7. Let's add our newly created folder to git so it can be tracked in the future.
    - To add a changed file to be tracked we run the command `git add 'filename'`
    - In this case we added a folder so we can run the command `git add 'foldername'`
    - Mine would look like this: `git add Code/anthony/`
8. Let's run another git status, just to verify all the files we want to track have been added `git status`
    - My output looks like this, yours should be similar.
```
On branch anthony-lab0
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	new file:   code/anthony/README.md
```
9. Now we can commit our changes to the git history. We will use the command `git commit -m 'commit message'`
    - The commit message is used to describe the changes this commit adds
    - In this case my message might look something like 'Adds folder for storing lab submissions and adds README.md'
    - The full command would be `git commit -m 'Adds folder for storing lab submissions and adds README.md'`
10. Finally we can push our code up to Github. This will allow the instructors to see and code changes and grade labs.
    - `git push`
    - If you see the following in your terminal, just run the recommend command
```
fatal: The current branch anthony-lab0 has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin anthony-lab0
```
So, I will run the command `git push --set-upstream origin anthony-lab0`

11.  Check Github to verify your code has been pushed up to the remote repository.