#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo("hey got data %s", data.data)
     
def listener():
    rospy.init_node('smartphone1')
    rospy.Subscriber('publish1', String, callback)
    # spin jen nuti python nekoncit dokud se neukonci node
    rospy.spin()

if __name__ == '__main__':
    listener()