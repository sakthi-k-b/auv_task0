#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

def callback(msg):
    final_result = msg.data + 5
    rospy.loginfo(f"Final Result: {final_result}")

rospy.init_node('final_node')
rospy.Subscriber('/processed', Int32, callback)
rospy.spin()

