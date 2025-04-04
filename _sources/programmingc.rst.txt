Compiling and Executing C Code
==============================

To work with C programs in a Linux environment, you'll need to know how to compile and run your code using the command line. Here's how you can do it:

### 1. Compiling the C Program

To compile the C program, you can use the gcc compiler, which is widely used in Linux environments. The general syntax for compiling a C program is:

.. code-block:: bash

   gcc -o output_name source_file.c

For our example, compile the `main.c` file like this:

.. code-block:: bash

   gcc -o hello hello.c

- `gcc`: The GNU C Compiler.
- `-o hello`: This specifies the output file name. In this case, the compiled program will be named `hello`.
- `hello.c`: The source file you want to compile.

### 2. Executing the Compiled Program

Once your program is compiled successfully, you can run it using the following command:

.. code-block:: bash

   ./hello

This will execute the `hello` program and output:

.. code-block:: bash

   Hello, World!

Examples
========

1. `Hello, World! <workspace/1.Hello_World/README.md>`_
2. `Variables and Data Type <workspace/2.Variables/README.md>`_
3. `If Else Statements <workspace/3.Control_Structures/1.if_else/README.md>`_
4. `While Loop <workspace/3.Control_Structures/2.while_loop/README.md>`_
5. `For Loop <workspace/3.Control_Structures/3.for_loop/README.md>`_
6. `Functions <workspace/4.Functions/README.md>`_
7. `Arrays <workspace/5.Arrays/README.md>`_
8. `Structures <workspace/6.Structures/README.md>`_
9. `Robot Simulation <workspace/7.Robot_Simulation/README.md>`_

Practice Question
#################

2D Robot Simulation
--------------------

### Objective:

Create a simulation for a robot that can move in a 2-dimensional space. The robot should have the ability to move both horizontally (x-axis) and vertically (y-axis). After simulating the movement, calculate and print the total displacement of the robot from its starting position.

### Instructions:

1. **Define a `struct` for the Robot**:

   - The `Robot` struct should include:
     - `name`: The name of the robot.
     - `x_position`: The position of the robot on the x-axis.
     - `y_position`: The position of the robot on the y-axis.
     - `x_speed`: The speed of the robot along the x-axis.
     - `y_speed`: The speed of the robot along the y-axis.

2. **Create a function** to update the robot's position based on its speed and the time interval.

3. **Create a function** to print the robot's current position.

4. **Simulate the robot's movement** over a series of time intervals (e.g., 10 intervals).

5. **Calculate the total displacement** of the robot from its starting position. The displacement is the magnitude of the vector from the starting position `(0, 0)` to the final position `(x_position, y_position)` and can be calculated using the formula:

   .. math::

      \text{Displacement} = \sqrt{(\text{x\_position})^2 + (\text{y\_position})^2}

6. **Print the robot's position** at each time interval and the total displacement at the end.

**Example Output:**

- Time Interval 1: Position (x, y) = (1, 2)
- Time Interval 2: Position (x, y) = (2, 4)
- ...
- **Total Displacement:** 10.77 units

### Additional Challenge:

Allow the robot to change its speed randomly at each time interval and observe how this affects its final displacement.