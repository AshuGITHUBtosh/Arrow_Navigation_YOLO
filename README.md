# Arrow-Based Navigation using YOLOv8 and ROS2
## Overview
This project implements an autonomous arrow-based navigation system using ROS, YOLOv8, and Gazebo simulation. The system integrates a webcam to detect arrows in real-time and directs a simulated rover accordingly. When an arrow is detected, the rover changes its direction based on the arrow’s orientation.
## Features
- YOLOv8-based arrow detection for real-time decision-making.
- Gazebo simulation for testing rover navigation in a virtual environment.
- Webcam integration to detect arrows in real-world scenarios.
- ROS2-based control to process detections and adjust rover movement.

  ## Prerequisites
  - ROS2 Humble
  - Gazebo
  - OpenCV
  - YOLOv8 (Ultralytics)
  - Python 3.x

## Execution
- ``` cd Arrow_Navigation_YOLO-master/bot_ws_2-master ```
- ``` roscore ```
- ``` ros2 launch turtlebot3_gazebo empty_world.launch.py ```
- ``` cd 
