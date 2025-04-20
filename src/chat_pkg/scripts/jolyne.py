#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def talk():
    pub = rospy.Publisher('/chat', String, queue_size=10)
    rospy.init_node('jolyne', anonymous=True)
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        msg = input("Jolyne: ")
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        talk()
    except rospy.ROSInterruptException:
        pass

