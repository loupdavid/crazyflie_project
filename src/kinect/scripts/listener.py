#!/usr/bin/env python
from __future__ import division
from __future__ import print_function
import roslib
roslib.load_manifest("kinect")
import rospy
import math
from std_msgs.msg import String
from sensor_msgs.msg import Image
import sys
import cv2
import numpy as np
from cv_bridge import CvBridge, CvBridgeError
import collections


class ImageConverter(object):

	def __init__(self):
		rospy.init_node("ImageConverter", anonymous=True)
		self.image_pub = rospy.Publisher("/coord/pub", String)
		self.bridge = CvBridge()
		self.image_sub = rospy.Subscriber("/camera/depth/image", Image, self.callback)
		self.middle_z = 240
		self.middle_y = 320
		self.buffer_y = collections.deque()
		self.buffer_z = collections.deque()
	
	def to_centimeters(self, x):
		return (x*2.54/96)

	def moving_average(self, new_x, new_y):
		if len(self.buffer_x) > 3:
			self.buffer_x.pop()
		if len(self.buffer_y) > 3:
			self.buffer_y.pop()
		self.buffer_x.appendleft(new_x)
		self.buffer_y.appendleft(new_y)
		avg_x = sum(self.buffer_x)/len(self.buffer_x)
		avg_y = sum(self.buffer_y)/len(self.buffer_y)

		return avg_x, avg_y

	def callback(self, data):
		try:
			# Depth
			depth_image = self.bridge.imgmsg_to_cv(data, "32FC1")
		
		except CvBridgeError as e:
			print(e)

		(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(np.asarray(depth_image))
		y = minLoc[0]
		y_cm = self.to_centimeters(y)
		z = minLoc[1]
		z_cm = self.to_centimeters(z)
		x = minVal
		x_cm = self.to_centimeters(x)

		print("X,Y,Z cm : %s %s %s" % (str(x_cm),str(y_cm),str(z_cm)))

		y = y - self.middle_y
		z = -(z - self.middle_z)

		#y, z = self.moving_average(y, z)
		
		try:
			l = list(minLoc)
			minloc_str = "%s %s %s " % (str(x), str(y), str(z))
			print("X,Y,Z px : %s" %  str(minloc_str))
			#r = rospy.Rate(10)
			
			self.image_pub.publish(str(minloc_str)) 
			#self.image_pub.publish(minloc_str)
		except:
			print("Cannot publish")
	

def main():
	imconv = ImageConverter()
	
	try:
		rospy.spin()
	except KeyboardInterrupt:
		print("Shutting down")
	cv2.destroyAllWindows()

if __name__ == "__main__":
	main()
