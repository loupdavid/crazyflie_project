#!/usr/bin/env python

import rospy
import time
import collections
from geometry_msgs.msg import Twist
from crazyflie_driver.srv import UpdateParams
from std_srvs.srv import Empty
from std_msgs.msg import String
from sensor_msgs.msg import Imu

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
	rospy.Subscriber('imu', Imu, callback_sensor, twist)
	r = rospy.Rate(10) #10 Hz
	#twist.linear.z = 41000
	twist.angular.z = 0
	#for i in range(0,2):
	#	print "monter"
	#	p.publish(twist)
	#	r.sleep()
	#stable en z
	twist.linear.z = 41000
	for i in range(0,20):
		print "stable"
		p.publish(twist)
		r.sleep()
	twist.linear.y = -30
	for i in range(0,20):
		print "stable"
		p.publish(twist)
		r.sleep()
	p.publish(twist)
	soft_land(twist,p,3)

def callback_sensor(data, args):
	twist = args
	#print ("imu: %s",data.linear_acceleration)
	if data.linear_acceleration.y > 1:
		twist.angular.x = -20
		print("correction on")
	elif data.linear_acceleration.y < -1:
		twist.angular.x = 20
		print("correction on")

def calc_z(delta, current_z_speed, current_z):
	#PID Values
	p = -13
	d = 20
	global equilibre
	global max_pousse
	global min_pousse

	#On est au dessus de la cible
	if int(delta) > 0:
		p = -p
		d = -d
		current_z = min_pousse
		res = current_z 
		#res = current_z + p*int(delta) + d*int(current_z_speed) 
	#On est en dessous de la cible
	else:
		res = int(current_z + p*int(delta) + d*float(current_z_speed))
		#res = current_z + int(delta)

	#Borne min et max
	if res > max_pousse:
		res = max_pousse
	elif res < min_pousse:
		res = min_pousse
	#Le drone n est plus dans le champs de vision de la kinect, il faut descendre
	if int(delta) < -230:
		res = equilibre

	print("old z: %s,  new z: %s = %s + %s + %s" % (str(current_z), str(res), str(current_z), str(p*int(delta)), str(d*float(current_z_speed))))
	return res

def calc_x(delta, current_x_speed, current_x):
	#PID Values
	p = -0.8
	d = 0
	
	#Proche du but
	if abs(float(delta)) < 0.3:
		print("proche du but")
		if current_x > 0:
			res = -1.8
		else:
			res = 1.8
	#Trop loin
	elif delta > 0:
		res = current_x + p*float(delta) - d*float(current_x_speed)
	#Trop pres
	else:
		res = current_x + p*float(delta) - d*float(current_x_speed)
	#res = current_y + int(delta)
	if res > 3:
		res = 3
	elif res < -3:
		res = -3
	print("old x:"+str(current_x)+" new x:"+str(res))
	return res

def calc_y(delta, current_y_speed, current_y):
	#PID Values
	p = -1
	d = 0

	#Par rapport a la kinect
	#delta positif a droite
	#delta negatif a gauche
	#commande positif : go droite
	#commande negative : go gauche
	
	print(delta)
	#delta positif, il faut un ordre negatif
	if int(delta) > 0:
		print("Go gauche (negatif)")
		res = current_y + p*float(delta) - d*float(current_y_speed)
	#delta negatif, il faut un ordre positif
	else:
		print("Go droite (positif)")
		res = current_y + p*float(delta) - d*float(current_y_speed)
	if res > 1:
		res = 1
	elif res < -1:
		res = -1
	print("old y:"+str(current_y)+" new y:"+str(res))
	return res

def callback_kinect(data, args):
	twist = args
	global decollage
	target_pos = str(data).split(" ")
	x = target_pos[1]
	y = target_pos[2]
	z = target_pos[3]
	current_x_speed = target_pos[4]
	current_y_speed = target_pos[5]
	current_z_speed = target_pos[6]
	print("x:"+x+" y:"+y+" z:"+z)
	if int(decollage) == False:
        	twist.linear.z = calc_z(z, current_z_speed, twist.linear.z)
        	twist.linear.y = calc_y(y, current_y_speed, twist.linear.y)	
        	twist.linear.x = calc_x(x, current_x_speed, twist.linear.x)	
	else:
		print("Mode decollage : Delta non pris en compte")	

if __name__ == '__main__':
	rospy.init_node('crazyflie_test_controller', anonymous=True, log_level=rospy.WARN)
	twist = Twist()
	p = rospy.Publisher('cmd_vel', Twist)
	global decollage
	global equilibre
	global max_pousse
	global min_pousse
	#Reglage drone 1
	equilibre = 40000
	max_pousse = 42300
	min_pousse = 40000
	#Reglage drone 2
	#equilibre = 37000
	#max_pousse = 37800
	#min_pousse = 36400

	#Eteindre LED
	rospy.wait_for_service('update_params')
	update_params = rospy.ServiceProxy('update_params', UpdateParams)
	rospy.set_param("ring/effect", 0)
	update_params(["ring/effect"])
	
	decollage = True
	listener = rospy.Subscriber('/coord/pub', String, callback_kinect, (twist))
	try:
		#decollage
		#twist.linear.z = 37500
		#r = rospy.Rate(10)
		#for i in range(15):
		#	print("Decollage")
		#	p.publish(twist)
		#	r.sleep()
		#twist.linear.z = 37000
		#for i in range(5):
		#	print("Stationnaire")
		#	p.publish(twist)
		#	r.sleep()
		#stable
		decollage = False
		#print("Fin decollage")
		twist.linear.z = equilibre
		p.publish(twist)
		while not rospy.is_shutdown():
			p.publish(twist)
	#arret urgence
	except KeyboardInterrupt:
		print("arret urgence")
		clear_twist(twist)
		p.publish(twist)
