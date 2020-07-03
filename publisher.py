#! /usr/bin/env python

import rospy
from std_msgs.msg import String

rospy.init_node('publisher')

pub = rospy.Publisher('Topic', String, queue_size=10)
rate = rospy.Rate(1)
my_msg = String()

my_msg.data = "Hello, this message is from the publisher!"

while not rospy.is_shutdown():
    pub.publish(my_msg)
    rate.sleep()
