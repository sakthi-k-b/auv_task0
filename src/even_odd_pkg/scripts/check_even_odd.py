#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

def callback(data):
    num = data.data
    if num % 2 == 0:
        rospy.loginfo(f"{num} is EVEN")
    else:
        rospy.loginfo(f"{num} is ODD")

def listener():
    rospy.init_node('check_even_odd_node', anonymous=True)
    rospy.Subscriber('number_topic', Int32, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()

