Array Iteration Program - C
===========================

This repository contains a simple C program that demonstrates how to iterate over an array and print its elements.

What are Arrays
---------------

An array is a structure that can hold a given amount of data. In this structure, every single data element has an index that can be used to address that data.

Think of arrays as lists; every item has a serial number.

We can access any index (serial number) in an array by just calling that array with the index we want to access.

For example, if we have an array called `numbers`:

.. code-block:: c

    int numbers[5] = {10, 20, 30, 40, 50};

We can access any index by:

.. code-block:: c

    index_num = numbers[2]; // This gives an output of 30

.. note::

   Array indexing starts with the number 0.

   So for `{10, 20, 30, 40, 50}`, the indexes are `{0, 1, 2, 3, 4}`.

Example Code
------------

.. code-block:: c

    #include <stdio.h>

    int main() {
        int numbers[5] = {10, 20, 30, 40, 50};

        for (int i = 0; i < 5; i++) {
            printf("%d\n", numbers[i]);
        }

        return 0;
    }

Explanation
-----------

1. **Array Declaration:** The program defines an integer array `numbers` with 5 elements: `10, 20, 30, 40, 50`.
2. **For Loop:**

   - The `for` loop iterates over each element in the `numbers` array.
   - The loop variable `i` runs from 0 to 4, corresponding to the indices of the array elements.
   - During each iteration, the program prints the value of the corresponding array element.
