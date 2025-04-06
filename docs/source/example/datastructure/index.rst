####################
Data Structures
####################

This documentation provides a comprehensive explanation of essential data structures in C, including static and dynamic arrays, structures, unions, and bit-fields. It also covers memory allocation using `malloc()`.

**************
Memory in C
**************

Before diving into arrays and other data structures, it's important to understand how memory is managed in C. Memory in C is broadly divided into the following segments:

- **Stack**: Used for static memory allocation. Local variables and function call information are stored here. Memory is managed automatically.
- **Heap**: Used for dynamic memory allocation. You can allocate and free memory manually using functions like `malloc()`, `calloc()`, `realloc()`, and `free()`.
- **Data segment**: Stores global and static variables.
- **Code segment (Text segment)**: Stores compiled program code.

C provides several standard library functions for memory allocation:

- `malloc(size_t size)` — Allocates a block of memory of given size.
- `calloc(size_t num, size_t size)` — Allocates memory for an array and initializes it to zero.
- `realloc(void *ptr, size_t size)` — Changes the size of an existing block of memory.
- `free(void *ptr)` — Frees previously allocated memory.

.. code-block:: c

    int *ptr = (int *)malloc(sizeof(int)); // allocates memory for one int
    *ptr = 42;
    free(ptr); // always free dynamically allocated memory

.. warning::

   Always check if memory allocation was successful by verifying the pointer is not `NULL`.

.. note::

   Computers manage memory in **chunks of 8 bits (1 byte)**. When you allocate memory, the compiler assigns a specific number of bytes depending on the data type:

   - `char` → 1 byte (8 bits)
   - `short` → 2 bytes (16 bits)
   - `int` → 4 bytes (32 bits)
   - `float` → 4 bytes (32 bits)
   - `double` → 8 bytes (64 bits)

   Memory is stored in **contiguous byte-addressable cells**. Each byte has a unique address. Larger data types occupy multiple consecutive addresses. For example, an `int` might occupy addresses 1000–1003.

   Modern CPUs and compilers may align data to **8-byte or 4-byte boundaries** for performance reasons. This is known as **alignment** and may cause **padding** bytes to be inserted between members.

******
Arrays
******

What is an Array?
=================

An array is a fixed-size, indexed collection of elements of the same data type stored in contiguous memory locations. Arrays allow fast access to elements using an index, which starts at 0.

.. code-block:: c

    int numbers[5] = {10, 20, 30, 40, 50};

Accessing elements:

.. code-block:: c

    int third = numbers[2]; // third = 30

Characteristics
----------------

- Homogeneous: All elements must be of the same type.
- Fixed size: Cannot grow or shrink during runtime.
- Contiguous memory: Efficient for iteration and access.

.. note::

   The size of an array must be known at compile time when declared statically.

Dynamic Arrays
===============

What is a Dynamic Array?
------------------------

Unlike static arrays, dynamic arrays can be allocated at runtime using functions from the `stdlib.h` library, like `malloc()` or `calloc()`.

`malloc()` — Memory Allocation
------------------------------

`malloc()` stands for "memory allocation." It reserves a specified number of bytes in the heap and returns a pointer to the beginning of the allocated memory block.

.. code-block:: c

    int *numbers = (int *)malloc(5 * sizeof(int));

This allocates memory for 5 integers (assuming 4 bytes each, 20 bytes total) and returns a pointer to that memory.

Full Example
-------------

.. code-block:: c

    #include <stdio.h>
    #include <stdlib.h>

    int main() {
        int *numbers = (int *)malloc(5 * sizeof(int));

        if (numbers == NULL) {
            printf("Memory allocation failed\n");
            return 1;
        }

        for (int i = 0; i < 5; i++) {
            numbers[i] = (i + 1) * 10;
        }

        for (int i = 0; i < 5; i++) {
            printf("%d\n", numbers[i]);
        }

        free(numbers); // Frees the allocated memory
        return 0;
    }

Characteristics
----------------

- Memory is allocated on the heap.
- Lifetime is controlled manually — you must use ``free()`` when done.
- ``malloc()`` returns ``NULL`` if the memory could not be allocated.
- Useful when array size is not known at compile time.

*********************
Structures (`struct`)
*********************

What is a Structure?
=====================

A `struct` is a composite data type that groups variables (called members) under a single name. Members can be of different data types.

Example
--------

.. code-block:: c

    struct Person {
        char name[50];
        int age;
        float height;
    };

    struct Person p1 = {"Alice", 25, 5.7};

    printf("Name: %s, Age: %d\n", p1.name, p1.age);

Characteristics
-----------------

- Members are laid out in memory in order.
- Memory size is the sum of all members (with possible padding).
- Can be nested (a struct inside another struct).

Bit Fields in Structs
======================

What are Bit Fields?
--------------------

Bit-fields allow the allocation of a specific number of bits to structure members. They're commonly used for flags or compact data storage.

Example
---------

.. code-block:: c

    struct Flags {
        unsigned int is_visible : 1;
        unsigned int is_enabled : 1;
        unsigned int has_error  : 1;
    };

    struct Flags status = {1, 0, 1};

    printf("Visible: %d, Enabled: %d, Error: %d\n",
           status.is_visible, status.is_enabled, status.has_error);

Characteristics
-----------------

- Memory-efficient: Useful when only a few bits are needed per field.
- Each field’s width is specified in bits.
- Cannot take address of a bit-field (e.g., `&flag.is_visible` is invalid).

.. note::

   Bit-fields are implementation-defined: behavior can vary between compilers.

*****************
Unions (`union`)
*****************

What is a Union?
=================

A `union` is similar to a `struct`, but all members share the **same memory** location. Only one member can be used at a time.

Example
---------

.. code-block:: c

    union Data {
        int i;
        float f;
        char str[20];
    };

    union Data data;
    data.i = 10;
    data.f = 220.5;

    printf("data.f = %f\n", data.f);

Characteristics
----------------

- Memory-efficient: Takes the size of the **largest** member.
- Changing one member affects others.
- Commonly used in embedded systems, hardware access, or communication protocols.

.. warning::

   Be careful when reading a member that wasn’t the last written; it results in undefined behavior.