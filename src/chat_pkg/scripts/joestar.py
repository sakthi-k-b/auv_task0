#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def callback(msg):
    print("Joestar heard:", msg.data)

def listen():
    rospy.init_node('joestar', anonymous=True)
    rospy.Subscriber('/chat', String, callback)
    rospy.spin()

if __name__ == '__main__':
    listen()

