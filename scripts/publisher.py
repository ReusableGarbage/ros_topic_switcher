#!/usr/bin/env python

import rospy
from std_msgs.msg import String

pub = rospy.Publisher('publish', String, queue_size=1)
rospy.init_node('smart_publisher')
r = rospy.Rate(1)

while not rospy.is_shutdown():
    pub.publish("publishing to topic publish")
    rospy.loginfo("publishing to topic publish")
    r.sleep()