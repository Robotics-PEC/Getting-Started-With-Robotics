#include <stdio.h>

// Define a struct to represent the Robot
typedef struct {
    char name[20];
    int position;
    int speed;
} Robot;

// Function to update the state of the robot
Robot update_robot_state(Robot robot, int time) {
    // Update the robot's position based on its speed and time
    robot.position += robot.speed * time;
    return robot;
}

// Function to print the current state of the robot
void print_robot_state(Robot robot) {
    printf("Robot: %s\n", robot.name);
    printf("Position: %d\n", robot.position);
    printf("Speed: %d\n", robot.speed);
    printf("-------------------------\n");
}

int main() {
    // Create a robot instance
    Robot myRobot = {"Robo1", 0, 5};

    // Array representing time intervals
    int time_intervals[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

    // Loop through each time interval and update the robot's state
    for(int i = 0; i < 10; i++) {
        printf("Time Interval: %d\n", time_intervals[i]);
        myRobot = update_robot_state(myRobot, time_intervals[i]);
        print_robot_state(myRobot);
    }

    return 0;
}
