#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Vector3Stamped
from std_msgs.msg import Int32
from geometry_msgs.msg import Point

pub_kuka=rospy.Publisher('/position', Point, queue_size=10)
kuka_point=Point()
trigger=0;
x_limit=[0.1,0.5]
y_limit=[-0.2,0.5]
z_limit=[0.1,0.8]
def detectcallback(msg):
    img_x=msg.x
    img_y=msg.y
    img_w=msg.z
    kuka_point.x=(-(x_limit[1]-x_limit[0])/(430-90))(img_w-90)+x_limit[1]
    kuka_point.y=(-(y_limit[1]-y_limit[0])/(580-50))(img_x-50)+y_limit[1]
    kuka_point.z=(-(z_limit[1]-z_limit[0])/(420-60))(img_y-60)+z_limit[1]
    #w 430 90 axis x(0.1 0.5)
    #h 580 50 axis y(-0.2 0.2)
    #y 60 480 axis z(0.2 0.8)
def triggercallback(msg):
    if msg.data==1:
        pub_kuka.publish(kuka_point)
def subscriber():
    rospy.init_node('yolo_bridge', anonymous=True)
    rospy.Subscriber("/detection_pos", Point, detectcallback)
    rospy.Subscriber("/trigger", Int32, triggercallback)
    rospy.spin()
if __name__ == '__main__':
    try:
        subscriber()
    except rospy.ROSInterruptException:
        pass    


