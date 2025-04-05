Hello, World! - C Program
==========================

This repository contains a simple C program that outputs the text "Hello, World!" to the console. This is often the first program beginners write when learning a new programming language, as it introduces basic concepts such as syntax, structure, and the process of compiling and executing code.

Code Explanation
-----------------

1. ``#include <stdio.h>``
    This line is a preprocessor directive that tells the compiler to include the Standard Input Output library (``stdio.h``) in the program. This library contains functions for performing input and output operations, such as ``printf``, which is used to print text to the console.

2. ``int main()``
    The ``main`` function is the entry point of the program. When the program is executed, the code inside the main function is run first. The ``int`` before ``main`` indicates that the function returns an integer value.

3. ``{ ... }``
    The curly braces ``{`` and ``}`` define the beginning and end of the ``main`` function's body. All the code inside these braces is what gets executed when the program runs.

4. ``printf("Hello, World!\n");``
    The ``printf`` function is used to output text to the console. In this case, it prints the string ``"Hello, World!"`` followed by a newline character ``\n``, which moves the cursor to the next line after printing the text. The semicolon ``;`` at the end of the line indicates the end of this statement.

5. ``return 0;``
    The ``return`` statement is used to exit the ``main`` function and return a value to the operating system. Returning ``0`` typically indicates that the program completed successfully. This is a convention in C programming, where a return value of ``0`` means the program executed without errors.