#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

def callback(msg):
    result = msg.data * 10
    pub.publish(result)

rospy.init_node('multiply_node')
pub = rospy.Publisher('/processed', Int32, queue_size=10)
rospy.Subscriber('/input', Int32, callback)
rospy.spin()

