########################
Version Control with Git
########################

Version control,a.k.a.,source control, is practice of tracking and managing changes to software code. Version control system keep track of all the changes to source code over time and the user who made those changes.
It is like a time machine that help you save all your progress and then if you did something wrong go back to the last working commit and start working from their.

It is also useful for team collaboration, with multiple members working on same piece of code it is easier to manage and merge the changes made by multiple developers. Back to the time machine analogy, think of it as
multiple members working at different time and then going back in time and combining their efforts into a single activity.

************
What is Git?
************

Git is the most widely adopted and stable verison control system thier exists.
It is a distributed version control system, which means that every developer has a complete copy of the repository on their local machine, so any change you make to the code is saved locally and needs to be pushed to the remote repository.

Their are also other type of version control system like Subversion (SVN) that are centralized, which means that there is a single central repository and all the developers have to connect to that repository to make changes. SVN requires
internet connection to the server to commit changes.

For our purposes we will be using Git as our version control system.

**************
Installing Git
**************
Git is free and open source software, so you can download it from the official website. The installation process is different for each operating system.

==========================
For Windows
==========================

1. Download the latest version of Git for Windows from the `official website <https://git-scm.com/download/win>`_.
2. Run the installer and follow the instructions.
3. During the installation, you can choose the default options or customize them according to your preferences.

==========================
For MacOS
==========================

1. Open the Terminal application.
2. If Homebrew is not installed, install it by running the following command:

.. code-block:: bash

    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

3. Install Git using Homebrew by running the command: 

.. code-block:: bash

    brew install git

4. Verify the installation by running:

.. code-block:: bash

    git --version

*********************
Git commands summary
*********************
This is a summary of the most common Git commands. For more detailed information, please refer to the `official Git documentation <https://git-scm.com/doc>`_.

Git Basics
----------

+--------------------------+-----------------------------------------------------------------------+
| Command                  | Description                                                           |
+==========================+=======================================================================+
| ``git init <directory>`` | Create an empty Git repository in the specified directory.            |
+--------------------------+-----------------------------------------------------------------------+
| ``git clone <repo-url>`` | Clone an existing repository from a remote URL.                       |
+--------------------------+-----------------------------------------------------------------------+
| ``git config user.name`` | Set the author's name for commits (Should match your remote username) |
+--------------------------+-----------------------------------------------------------------------+
| ``git add <directory>``  | Stage all changes in a directory for the next commit.                 |
+--------------------------+-----------------------------------------------------------------------+
| ``git commit -m "msg"``  | Commit staged changes with a message.                                 |
+--------------------------+-----------------------------------------------------------------------+
| ``git status``           | Show the status of files (staged, unstaged, untracked).               |
+--------------------------+-----------------------------------------------------------------------+
| ``git log``              | Display commit history.                                               |
+--------------------------+-----------------------------------------------------------------------+

Undoing Changes
---------------

+-------------------------+-------------------------------------------------------------------+
| Command                 | Description                                                       |
+=========================+===================================================================+
| ``git revert <commit>`` | Create a new commit that undoes the changes of a previous commit. |
+-------------------------+-------------------------------------------------------------------+
| ``git reset <file>``    | Unstage a file but keep the working directory unchanged.          |
+-------------------------+-------------------------------------------------------------------+
| ``git clean -n``        | Show untracked files to be removed.                               |
+-------------------------+-------------------------------------------------------------------+

Rewriting Git History
---------------------

+-------------------------+-------------------------------------------------------------------+
| Command                 | Description                                                       |
+=========================+===================================================================+
| ``git commit --amend``  | Modify the most recent commit message.                            |
+-------------------------+-------------------------------------------------------------------+
| ``git rebase <base>``   | Rebase the current branch onto another branch or commit.          |
+-------------------------+-------------------------------------------------------------------+
| ``git reflog``          | Show a log of changes to HEAD.                                    |
+-------------------------+-------------------------------------------------------------------+

Git Branches
------------

+------------------------------+--------------------------------------------------------------+
| Command                      | Description                                                  |
+==============================+==============================================================+
| ``git branch``               | List all branches.                                           |
+------------------------------+--------------------------------------------------------------+
| ``git checkout -b <branch>`` | Create and switch to a new branch.                           |
+------------------------------+--------------------------------------------------------------+
| ``git merge <branch>``       | Merge another branch into the current branch.                |
+------------------------------+--------------------------------------------------------------+

Remote Repositories
-------------------

+---------------------------------+-----------------------------------------------------------+
| Command                         | Description                                               |
+=================================+===========================================================+
| ``git remote add <name> <url>`` | Add a new remote repository.                              |
+---------------------------------+-----------------------------------------------------------+
| ``git fetch <remote>``          | Fetch updates from a remote repository.                   |
+---------------------------------+-----------------------------------------------------------+
| ``git pull <remote>``           | Fetch and merge changes from a remote branch.             |
+---------------------------------+-----------------------------------------------------------+
| ``git push <remote> <branch>``  | Push local changes to a remote branch.                    |
+---------------------------------+-----------------------------------------------------------+
