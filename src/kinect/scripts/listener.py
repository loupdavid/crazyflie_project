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
from datetime import datetime


class ImageConverter(object):
"""Compute position / speed for the crazyflie based on a depth image."""

	def __init__(self):
		rospy.init_node("ImageConverter", anonymous=True)
		# topic to publish position and speed
		self.image_pub = rospy.Publisher("/coord/pub", String)
		self.bridge = CvBridge()
		# topic for the depth image
		self.image_sub = rospy.Subscriber("/camera/depth/image", Image, self.callback)
		self.middle_z = 240
		self.middle_y = 320
		self.middle_x = 90
		self.buffer_y = collections.deque()
		self.buffer_z = collections.deque()
		self.buffer_x = collections.deque()
		self.prev_x = 0
		self.prev_y = 0
		self.prev_z = 0
		self.prev_time = 0

	def moving_average(self, new_x, new_y, new_z):
		"""Compute moving average over 3 samples for x, y, z.
		   (not used in our PID implementation)"""
		if len(self.buffer_x) > 3:
			self.buffer_x.pop()
		if len(self.buffer_y) > 3:
			self.buffer_y.pop()
		if len(self.buffer_z) > 3:
			self.buffer_z.pop()
		self.buffer_x.appendleft(new_x)
		self.buffer_y.appendleft(new_y)
		self.buffer_z.appendleft(new_z)
		avg_x = sum(self.buffer_x)/len(self.buffer_x)
		avg_y = sum(self.buffer_y)/len(self.buffer_y)
		avg_z = sum(self.buffer_z)/len(self.buffer_z)

		return avg_x, avg_y, avg_z

	
	def callback(self, data):
		try:
			# Depth
			depth_image = self.bridge.imgmsg_to_cv(data, "32FC1")

		except CvBridgeError as e:
			print(e)

		# Get the current position samples
		(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(np.asarray(depth_image))
		y = minLoc[0]
		z = minLoc[1]
		x = minVal
		now = datetime.now()
		
		# Compute position deltas and speeds
		y = y - self.middle_y
		z = -(z - self.middle_z)
		dz = z - self.prev_z
		dy = y - self.prev_y
		dt = (now - self.prev_time).total_seconds()
		dv_z = dz / dt
		dv_y = dy / dt
		dv_z = dx / dt

		try:
			l = list(minLoc)
			# Format the result string
			publish_str = "%s %s %s %s %s" % (str(x), str(y), str(z), str(dv_x), str(dv_y), str(dv_z))
			print("%s" % publish_str)
			self.image_pub.publish(str(publish_str))

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
