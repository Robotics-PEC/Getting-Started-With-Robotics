.. _addition_function_program:

Addition Function Program - C
=============================

This repository contains a simple C program that demonstrates the use of functions by adding two integers and printing the result.

What is a function?
-------------------

A Function is a piece of code which will not run by its own. But when called, the code in the function will be executed to give some output.

.. code-block:: c

    #include <stdio.h>

    int add(int a, int b){
        return a+b;
    }

    int main(){
        int result;
        result = add(5+4);
        printf("%d",result);
        return 0;
    }

Function Prototypes
-------------------

For writing code more beautifully, we may utilize function prototypes.

In function prototypes, the function is declared before the `int main` while the function is written below `int main`.

This makes the code more readable.

.. code-block:: c

    #include <stdio.h>

    // this is a function prototype
    int add(int a, int b);

    int main(){
        int result;
        result = add(5+4);
        printf("%d",result);
        return 0;
    }

    int add(int a, int b){
        return a+b;
    }

Explanation
-----------

1. **Function Declaration:** The function `add` is declared at the beginning of the program with a signature `int add(int a, int b);`. This informs the compiler that a function named `add` will be used and that it takes two integer arguments and returns an integer.
2. **Main Function:** The `main` function calls the `add` function with arguments `5` and `10`, stores the result in the `sum` variable, and then prints the result.
3. **Function Definition:** The `add` function is defined after the `main` function. It takes two integers `a` and `b`, adds them together, and returns the result.
