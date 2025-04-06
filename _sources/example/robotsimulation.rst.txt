Robot Simulation
================

This repository contains a simple C program that demonstrates the use of structures to represent a robot with a name, speed, and position, and update the position with respect to time.

**Source File**:

.. literalinclude:: ../../../workspace/5.Robot_Simulation/main.c
   :language: c
   :linenos:

Explanation
-----------

This program demonstrates how to use structures and functions in C to simulate a robot moving over time. Let's break down each component:

1. **Struct Definition:**

.. literalinclude:: ../../../workspace/5.Robot_Simulation/main.c
    :language: c
    :lines: 4-8

- This struct defines the properties of a robot:
    - ``name``: A string to store the robot’s name.
    - ``position``: An integer representing the current position of the robot on a 1D line.
    - ``speed``: An integer representing how many units the robot moves per unit time.

2. **Update Function**

.. literalinclude:: ../../../workspace/5.Robot_Simulation/main.c
    :language: c
    :lines: 10-15
    
- This function takes a Robot structure and a time interval.
- It updates the robot's position by multiplying its speed with the time interval.
- The function returns the updated ``Robot``.
- Note: The robot is passed by value, and the updated structure is reassigned in the main function.

3. Print Function

.. literalinclude:: ../../../workspace/5.Robot_Simulation/main.c
    :language: c
    :lines: 17-23

- Prints the robot's current name, position, and speed in a readable format.

4. Main Function

.. literalinclude:: ../../../workspace/5.Robot_Simulation/main.c
    :language: c
    :lines: 25-40

- A robot named "Robo1" is created with a starting position of 0 and speed of 5.
- The time_intervals array represents how long the robot moves during each iteration.
- A loop iterates through the time intervals:
    - It prints the current time step.
    - It updates the robot’s position using the update_robot_state function.
    - It then prints the robot's updated state using print_robot_state.