###################
Control Structures
###################

This documentation covers the core control structures in C, including conditionals, loops, and the `goto` statement. These constructs control the flow of execution in a program.

***********************
Conditional Statements
***********************

if Statement
============

Executes a block of code only if the condition is true.

.. code-block:: c

    int x = 10;
    if (x > 5) {
        printf("x is greater than 5\n");
    }

if-else Statement
==================

Adds an alternate block if the condition is false.

.. code-block:: c

    if (x > 5) {
        printf("x > 5\n");
    } else {
        printf("x <= 5\n");
    }

else-if Ladder
===============

Checks multiple conditions in sequence.

.. code-block:: c

    if (x > 10) {
        printf("x > 10\n");
    } else if (x == 10) {
        printf("x == 10\n");
    } else {
        printf("x < 10\n");
    }

switch Statement
=================

Allows multiple execution paths based on the value of a variable.

.. code-block:: c

    int day = 3;
    switch (day) {
        case 1:
            printf("Monday\n");
            break;
        case 2:
            printf("Tuesday\n");
            break;
        default:
            printf("Another day\n");
    }

******
Loops
******

Loops execute a block of code repeatedly.

while Loop
==========

Executes as long as the condition is true.

.. code-block:: c

    int i = 0;
    while (i < 5) {
        printf("%d\n", i);
        i++;
    }

do-while Loop
==============

Executes the body **at least once**, then checks the condition.

.. code-block:: c

    int i = 0;
    do {
        printf("%d\n", i);
        i++;
    } while (i < 5);

for Loop
=========

Compact loop syntax using initialization, condition, and increment.

.. code-block:: c

    for (int i = 0; i < 5; i++) {
        printf("%d\n", i);
    }

*******************
Loop Control: break and continue
*******************

break Statement
================

Exits the loop immediately.

.. code-block:: c

    for (int i = 0; i < 10; i++) {
        if (i == 5) break;
        printf("%d\n", i);
    }

continue Statement
===================

Skips the current iteration and continues with the next.

.. code-block:: c

    for (int i = 0; i < 5; i++) {
        if (i == 2) continue;
        printf("%d\n", i);
    }

*************
goto Statement
*************

The `goto` statement allows jumping to a labeled part of the program. It's rarely used and can make code harder to follow, but it’s useful in certain low-level or cleanup scenarios.

Syntax
=======

.. code-block:: c

    goto label;
    // ... other code
    label:
    // code to jump to

Example
--------

.. code-block:: c

    #include <stdio.h>

    int main() {
        int x = 1;
        if (x == 1)
            goto skip;

        printf("This line is skipped\n");

    skip:
        printf("Jumped to label\n");
        return 0;
    }

.. warning::

   Use ``goto`` sparingly. Overuse can make code difficult to read and debug. Prefer structured control flow (loops, functions) when possible.