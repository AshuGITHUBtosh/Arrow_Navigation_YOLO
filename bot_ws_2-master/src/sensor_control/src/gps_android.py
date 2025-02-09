#!/usr/bin/env python
import rospy
from sensor_msgs.msg import NavSatFix

def talker():
	rospy.init_node("android",anonymous=True)
	pub = rospy.Publisher("/android/fix", NavSatFix, queue_size=10)
	msg = NavSatFix()
	msg.latitude = 20
	msg.longitude = 60
	while not rospy.is_shutdown():
		pub.publish(msg)

if __name__=="__main__":
	talker()
