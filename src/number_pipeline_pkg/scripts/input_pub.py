#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

def pub():
    pub = rospy.Publisher('/input', Int32, queue_size=10)
    rospy.init_node('input_node')
    rate = rospy.Rate(1)
    n = 1
    while not rospy.is_shutdown():
        pub.publish(n * 2)
        n += 1
        rate.sleep()

if __name__ == '__main__':
    pub()

