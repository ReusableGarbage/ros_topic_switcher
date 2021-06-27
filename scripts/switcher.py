#!/usr/bin/env python
import rospy
from std_msgs.msg import String

#topic =rospy.get_param("topics")

def callback(data):
    rospy.loginfo(data.data)
    pub = rospy.Publisher(rospy.get_param("topics"), String, queue_size=1)
    pub.publish(data.data)
    rospy.Rate(1).sleep()
     
def listener():
    rospy.Subscriber("publish", String, callback)


if __name__ == '__main__':
    rospy.init_node('switcher')
    while not rospy.is_shutdown():
        listener()
