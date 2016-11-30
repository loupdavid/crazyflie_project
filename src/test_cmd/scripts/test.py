#!/usr/bin/env python

import rospy
import time
from geometry_msgs.msg import Twist
from crazyflie_driver.srv import UpdateParams
from std_srvs.srv import Empty

def clear_twist(t):
	t.linear.x = 0
	t.linear.y = 0
	t.linear.z = 0
	t.angular.x = 0
	t.angular.y = 0
	t.angular.z = 0

def soft_land(t, p):
	r = rospy.Rate(10)
	clear_twist(t)
	t.linear.z = 28000
	for i in range(0,22):
		p.publish(t)
		r.sleep()
	clear_twist(t)
	p.publish(t)

if __name__ == '__main__':
	rospy.init_node('crazyflie_test_controller', anonymous=True)
	p = rospy.Publisher('cmd_vel', Twist)
	twist = Twist()
	r = rospy.Rate(10) #10 Hz
	#self._land = rospy.ServiceProxy('land', Empty)
#for i in range(0, 100):
#    p.publish(twist)
#    r.sleep()

	twist.linear.z = 38000
	twist.angular.z = 0
	for i in range(0,20):
		p.publish(twist)
		r.sleep()
	twist.linear.z = 34000
	for i in range(0,20):
		p.publish(twist)
		r.sleep()

	soft_land(twist,p)	
	#for i in range(0,20):
	#	twist.linear.z = 20000
	#	twist.linear.y = 10
	#	p.publish(twist)
	#	r.sleep()

	#self._land()

	while not rospy.is_shutdown():
		p.publish(twist)
		r.sleep()

