Robot Simulation
================

This repository contains a simple C program that demonstrates the use of structures to represent a robot with a name, speed, and position, and update the position with respect to time.

Explanation
-----------

1. **Update Function**: The ``update_robot_state`` function now takes a ``Robot`` struct by value (instead of using a pointer). It updates the robot's position and returns the updated Robot.

2. **Main Function**: The ``myRobot`` instance is updated by assigning it the value returned by ``update_robot_state`` after each time interval.