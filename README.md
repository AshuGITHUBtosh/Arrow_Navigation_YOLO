# Arrow-Based Navigation using YOLOv8 and ROS2
## Overview
This project implements an autonomous arrow-based navigation system using ROS, YOLOv8, and Gazebo simulation. The system integrates a webcam to detect arrows in real-time and directs a simulated rover accordingly. When an arrow is detected, the rover changes its direction based on the arrow’s orientation.
## Features
- YOLOv8-based arrow detection for real-time decision-making.
- Gazebo simulation for testing rover navigation in a virtual environment.
- Webcam integration to detect arrows in real-world scenarios.
- ROS2-based control to process detections and adjust rover movement.

## Prerequisites
###R OS2 Humble
-```sudo apt update && sudo apt install -y ros-humble-desktop```
###Gazebo
- ``` sudo apt install -y gazebo```
### OpenCV
- ```pip install opencv-python```
### YOLOv8 (Ultralytics)
- ``` pip install ultralytics```
### Additional Dependencies
- ``` pip install numpy rospy cv_bridge ```

##  Project Setup
### Clone repository
## Execution
- ``` cd Arrow_Navigation_YOLO-master/bot_ws_2-master ```
- ``` roscore ```
- ``` ros2 launch turtlebot3_gazebo empty_world.launch.py ```
- ``` cd /src/simple_navigation_goals/src ```
- ``` python3 new_camera.py ```
- ``` python3 move_fs ```
the above commands should open the turtlrbot3 in an empty world with the web cam of of the system on, now if the arrow is detected by the camera it will give the commands to the /cmd_vel topic accordingly and make the rover turn in the direction of the arrow detected.
