#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

def publish_number():
    pub = rospy.Publisher('number_topic', Int32, queue_size=10)
    rospy.init_node('number_input_node', anonymous=True)
    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        try:
            num = int(input("Enter a number: "))
            pub.publish(num)
            rate.sleep()
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == '__main__':
    try:
        publish_number()
    except rospy.ROSInterruptException:
        pass

