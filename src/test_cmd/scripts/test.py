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

def soft_land(t, p, time):
	r = rospy.Rate(10)
	p.publish(t)
	t.angular.x = 0
	t.angular.y = 0
	t.angular.z = 0
	t.linear.y = 0
	t.linear.x = 0
	t.linear.z = 36000
	p.publish(t)
	for i in range(0,time*10):
		print "ladning"
		p.publish(t)
		r.sleep()
	clear_twist(t)
	p.publish(t)

#Monter Descendre
def test1(p):
	#Init Node and Topic
	twist = Twist()

	r = rospy.Rate(10) #10 Hz
	twist.linear.z = 41000
	twist.angular.z = 0
	for i in range(0,15):
		print "monter"
		p.publish(twist)
		r.sleep()
	twist.linear.z = 39300
	for i in range(0,10):
		print "stable"
		p.publish(twist)
		r.sleep()
	twist.angular.z = 15
	for i in range(0,20):
		print "rotation"
		p.publish(twist)
		r.sleep()

	p.publish(twist)
	soft_land(twist,p,5)

#Translation
def test2(p):
	#Init Node and Topic
	twist = Twist()

	r = rospy.Rate(10) #10 Hz
	#twist.linear.z = 41000
	twist.angular.z = 0
	#for i in range(0,2):
	#	print "monter"
	#	p.publish(twist)
	#	r.sleep()
	#stable en z
	twist.linear.z = 39300
	for i in range(0,20):
		print "stable"
		p.publish(twist)
		r.sleep()
	#translation
	twist.linear.y = 10
	#twist.angular.z = 15
	for i in range(0,10):
		print "translation"
		p.publish(twist)
		r.sleep()
	#translation
	twist.linear.y = -10
	#twist.angular.z = 15
	for i in range(0,10):
		print "translation"
		p.publish(twist)
		r.sleep()

	twist.linear.y = -10
	p.publish(twist)
	soft_land(twist,p,3)

if __name__ == '__main__':
	rospy.init_node('crazyflie_test_controller', anonymous=True, log_level=rospy.WARN)
	p = rospy.Publisher('cmd_vel', Twist)
	test2(p)
