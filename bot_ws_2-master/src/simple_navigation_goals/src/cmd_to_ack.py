#!/usr/bin/env python

# Author: christoph.roesmann@tu-dortmund.de

import rospy, math
from geometry_msgs.msg import Twist
from ackermann_msgs.msg import AckermannDriveStamped


def convert_trans_rot_vel_to_steering_angle(v, omega, wheelbase):
  if omega == 0 or v == 0:
    return 0

  radius = v / omega
  return math.atan(wheelbase / radius)


def cmd_callback(data):
  global wheelbase
  global ackermann_cmd_topic
  global frame_id
  global pub
  
  v = data.linear.x
  steering = convert_trans_rot_vel_to_steering_angle(v, data.angular.z, wheelbase)
  
  msg = AckermannDriveStamped()
  msg.header.stamp = rospy.Time.now()
  msg.header.frame_id = frame_id
  msg.drive.steering_angle = steering
  msg.drive.speed = v
  
  pub.publish(msg)


if __name__ == '__main__': 
  try:
    
    rospy.init_node('cmd_vel_to_ackermann_drive', anonymous=True)
        
    wheelbase = 1.0
    frame_id = 'odom'
    
    rospy.Subscriber('/bob/cmd_vel', Twist, cmd_callback, queue_size=1)
    pub = rospy.Publisher('/bob/cmd_ackermann', AckermannDriveStamped, queue_size=1)
    
    rospy.spin()
    
  except rospy.ROSInterruptException:
    pass
