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
	#Init Node and Topic
	rospy.init_node('crazyflie_test_controller', anonymous=True)
	p = rospy.Publisher('cmd_vel', Twist)
	twist = Twist()

	#Init Ros Param (LED)
	rospy.wait_for_service('update_params')
	rospy.loginfo("found update_params service")
 	update_params = rospy.ServiceProxy('update_params', UpdateParams)
	rospy.set_param("ring/headlightEnable", 0)
	update_params(["ring/headlightEnable"])
	rospy.set_param("ring/effect", 7)
	rospy.set_param("ring/solidGreen", 0)
	rospy.set_param("ring/solidBlue", 0)
	rospy.set_param("ring/solidRed", 20)
	update_params(["ring/solidGreen"])
	update_params(["ring/solidBlue"])
	update_params(["ring/solidRed"])
	update_params(["ring/effect"])

	r = rospy.Rate(10) #10 Hz
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
