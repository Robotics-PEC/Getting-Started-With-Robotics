#################
Basic Linux Commands
#################

****************************
Navigating the Filesystem 🗂️
****************************

Understanding how to navigate the filesystem is fundamental when working with Linux.

1. `pwd` (Print Working Directory)
==================================

The ``pwd`` command shows the full path of the current directory you are in.

.. code-block:: bash

   pwd

**Example:** If you are in the ``/home/user/documents`` directory, running ``pwd`` will output:

.. code-block:: bash

   /home/user/documents

2. `ls` (List Directory Contents)
=================================

The ``ls`` command lists all files and directories in the current directory.

.. code-block:: bash

   ls

**Example:** To list files with details (like file size and permissions):

.. code-block:: bash

   ls -l

3. `cd` (Change Directory)
==========================

The ``cd`` command changes the current directory to a different one.

.. code-block:: bash

   cd /path/to/directory

**Example:** To move to the home directory:

.. code-block:: bash

   cd ~

****************************
File Operations 📁
****************************

These commands help you create, move, and manage files and directories.

1. `touch` (Create a File)
==========================

The `touch` command creates an empty file.

.. code-block:: bash

   touch filename

**Example:** To create a file named `example.txt`:

.. code-block:: bash

   touch example.txt

2. `mkdir` (Create a Directory)
===============================

The `mkdir` command creates a new directory.

.. code-block:: bash

   mkdir directory_name

**Example:** To create a directory named `projects`:

.. code-block:: bash

   mkdir projects

3. `cp` (Copy Files)
====================

The `cp` command copies files or directories from one location to another.

.. code-block:: bash

   cp source_file destination

**Example:** To copy `file.txt` to another directory:

.. code-block:: bash

   cp file.txt /home/user/documents

4. `mv` (Move/Rename Files)
===========================

The `mv` command moves or renames files or directories.

.. code-block:: bash

   mv old_name new_name

**Example:** To move `file.txt` to another directory:

.. code-block:: bash

   mv file.txt /home/user/documents

Or to rename `file.txt` to `newfile.txt`:

.. code-block:: bash

   mv file.txt newfile.txt

5. `rm` (Remove Files/Directories)
==================================

The `rm` command removes files or directories.

.. code-block:: bash

   rm filename

**Example:** To remove a file named `file.txt`:

.. code-block:: bash

   rm file.txt

To remove a directory and its contents:

.. code-block:: bash

   rm -r directory_name