####################
Variables and Data Types
####################

Now let us discuss variables, including basic data types, pointers, dereferencing, pointer-to-pointer usage, and strings.

**************
Memory in C
**************

Before diving into variables and pointers, it's important to understand how memory is managed in C. Memory in C is broadly divided into the following segments:

- **Stack**: Used for static memory allocation. Local variables and function call information are stored here. Memory is managed automatically.
- **Heap**: Used for dynamic memory allocation. You can allocate and free memory manually using functions like `malloc()`, `calloc()`, `realloc()`, and `free()`.
- **Data segment**: Stores global and static variables.
- **Code segment (Text segment)**: Stores compiled program code.

.. note::

   Computers manage memory in **chunks of 8 bits (1 byte)**. When you allocate memory, the compiler assigns a specific number of bytes depending on the data type:

   - `char` → 1 byte (8 bits)
   - `short` → 2 bytes (16 bits)
   - `int` → 4 bytes (32 bits)
   - `float` → 4 bytes (32 bits)
   - `double` → 8 bytes (64 bits)

   Memory is stored in **contiguous byte-addressable cells**. Each byte has a unique address. Larger data types occupy multiple consecutive addresses. For example, an `int` might occupy addresses 1000–1003.

   Modern CPUs and compilers may align data to **8-byte or 4-byte boundaries** for performance reasons. This is known as **alignment** and may cause **padding** bytes to be inserted between members.

******************************
Data Types in C
******************************

C provides a variety of data types, both primitive and user-defined. Here's a quick overview of the basic ones:

Basic Data Types
=================

- **char**: Stores a single character. Occupies 1 byte. Can be signed or unsigned.
- **short**: Short integer, usually 2 bytes. Can be signed or unsigned.
- **int**: Standard integer, usually 4 bytes. Can be signed or unsigned.
- **long**: Long integer, usually 4 or 8 bytes depending on the system. Can be signed or unsigned.
- **float**: Single precision floating-point number. 4 bytes.
- **double**: Double precision floating-point number. 8 bytes.
- **long double**: Extended precision floating-point number. Size varies by system.

Modifiers
=========

- `signed` and `unsigned` can be used with `char`, `short`, `int`, and `long` to define whether they can store negative values or not.
- `short` and `long` are used to modify the size of integers.

Examples:

.. code-block:: c

    unsigned int age = 25;
    long double pi = 3.1415926535;

******************************
Pointers and Dereferencing
******************************

What is a Pointer?
==================

A pointer is a variable that stores the memory address of another variable.

.. code-block:: c

    int x = 10;
    int *ptr = &x;  // ptr stores address of x

    printf("Value of x = %d\n", *ptr);  // Dereferencing the pointer

Dereferencing means accessing the value at the memory address held by the pointer.

Pointer to Pointer
==================

A pointer to a pointer stores the address of another pointer.

.. code-block:: c

    int x = 5;
    int *ptr = &x;
    int **pptr = &ptr;

    printf("Value of x = %d\n", **pptr); // Two dereferences to reach value of x

Useful for:

- Passing pointers to functions
- Managing dynamic data structures like linked lists
- Working with arrays and matrix structures

*********
Strings
*********

C does not have a built-in string data type like some higher-level languages. Instead, strings in C are represented using arrays of characters.

String Literals
===============

A string literal like "Hello" is stored as an array of characters terminated by a null character ``\0``.

.. code-block:: c

    char greeting[] = "Hello";  // Equivalent to {'H', 'e', 'l', 'l', 'o', '\0'}

    printf("%s\n", greeting);

You can also use a pointer to refer to a string literal:

.. code-block:: c

    const char *greet = "Hello";
    printf("%s\n", greet);

.. note::

   Always declare string literal pointers as ``const char *`` to avoid accidentally modifying read-only memory.

   String literals like "Hello" are stored in a **read-only section** of memory, typically in the **.rodata** (read-only data) segment of your program. When you declare ``const char *greet = "Hello";``, the pointer ``greet`` points to this read-only memory.

   - Attempting to modify the string content, such as ``greet[0] = 'h';``, results in **undefined behavior**. On many systems, this causes a segmentation fault.
   - In contrast, declaring ``char greet[] = "Hello";`` creates a **writable array** on the stack, which is safe to modify.

   Example of undefined behavior:

   .. code-block:: c

       char *greet = "Hello";
       greet[0] = 'h';  // ❌ Undefined behavior

   Safe alternative:

   .. code-block:: c

       char greet[] = "Hello";
       greet[0] = 'h';  // ✅ Safe

   Compilers often apply **string pooling**, storing identical string literals in one place to save space. However, modifying literals remains unsafe regardless of pooling.

   Even when declared as ``const char *greet = "Hello";``, only the data being pointed to is read-only. The pointer variable ``greet`` itself is **not constant**—it can still be made to point to a different string literal:

   .. code-block:: c

       const char *greet = "Hello";
       greet = "World";  // ✅ Valid. Pointer is not constant, only the data is.

   When you write ``greet = "World";``, the literal "World" is also stored in read-only memory (typically `.rodata`). The pointer ``greet`` is simply updated to point to the new location. This does **not** change the previous literal "Hello" or its memory; that memory remains untouched and read-only.

   If you want to make the pointer itself constant as well, use ``const char * const greet = "Hello";``. This makes both the pointer and the data read-only.

