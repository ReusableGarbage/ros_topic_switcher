import rospy
rospy.set_param("topics", "publish")

if __name__ == '__main__':
    rospy.init_node('topicSwitcher')

    while not rospy.is_shutdown():
        inpt = input("Type 1 or 2: ")
        if inpt == 1:
            print("topic changed to publish1")
            rospy.set_param("topics", "publish1")
        elif inpt == 2:
            print("topic changed to publish2")
            rospy.set_param("topics", "publish2")
        elif inpt == 3:
            print("topic changed to publish")
            rospy.set_param("topics", "publish")
        else:
            print("wrong input try again")