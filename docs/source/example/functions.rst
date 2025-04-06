Functions
=========

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

In function prototypes, the function is declared before the ``int main`` while the function is written below ``int main``.

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

Passing Pointers to Functions
-----------------------------

You can pass a pointer to a function when you want the function to modify the original variable or when passing large data structures like arrays efficiently.

.. code-block:: c

    void update(int *p) {
        *p = 20;
    }

    int main() {
        int x = 10;
        update(&x);
        printf("%d", x);  // Outputs 20
        return 0;
    }

**Purpose:**
    - To allow the function to modify the original variable.
    - To save memory by passing the address instead of copying large structures.

Returning Pointers from Functions
---------------------------------

You can return a pointer from a function, but you must be careful with the lifetime of the pointed data.

Valid example:

.. code-block:: c

    int* getValue() {
        static int x = 42;
        return &x;
    }

    int main() {
        int *ptr = getValue();
        printf("%d", *ptr);  // Outputs 42
        return 0;
    }

.. note::
   Never return a pointer to a **local variable** declared inside a function. Local variables are destroyed when the function ends, and the returned pointer becomes invalid.

.. code-block:: c

    int* invalidPointer() {
        int x = 10;
        return &x;  // ❌ Invalid
    }

Scope of Variables and Pointers
-------------------------------

- **Local Variables:** Exist only within the function they are defined. They are stored on the stack.
- **Global Variables:** Declared outside all functions and accessible by any function.
- **Static Variables:** Declared with the ``static`` keyword, they retain their value between function calls.

Pointers follow the same scope rules as variables. When returning or passing pointers, ensure the memory they point to is still valid and accessible.

Pointer to a Function
---------------------

A function pointer stores the address of a function and can be used to call the function indirectly.

.. code-block:: c

    #include <stdio.h>

    int add(int a, int b) {
        return a + b;
    }

    int main() {
        int (*funcPtr)(int, int) = add;
        int result = funcPtr(5, 10);  // Calls add(5, 10)
        printf("%d", result);
        return 0;
    }

Function pointers are useful in:
    - Callback mechanisms
    - Implementing tables of functions
    - Event-driven programming
    - Dynamic function calls (e.g., in drivers or plugin systems)

Passing Arrays to Functions
---------------------------

Arrays are passed to functions by passing a pointer to their first element. You can also pass the array size for use in loops.

.. code-block:: c

    #include <stdio.h>

    void printArray(int arr[], int size) {
        for (int i = 0; i < size; i++) {
            printf("Element %d: %d\n", i, arr[i]);
        }
    }

    int main() {
        int numbers[] = {1, 2, 3, 4, 5};
        int length = sizeof(numbers) / sizeof(numbers[0]);
        printArray(numbers, length);
        return 0;
    }

**Key Points:**
    - ``int arr[]`` in the function parameter is equivalent to ``int *arr``.
    - Always pass the array size separately since the function does not know its length by default.
    - Inside the function, loop over the array using the given size.

This technique allows functions to work with arrays of any length.

