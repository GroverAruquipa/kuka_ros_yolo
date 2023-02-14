#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from gazebo_msgs.msg import ModelState
from geometry_msgs.msg import Pose
from geometry_msgs.msg import Twist
import random
from geometry_msgs.msg import Point
from std_msgs.msg import Int32


factor=1
models=['gripper','cat_panel','elephant_panel'] # Modeles: gripper, cat_panel, elephant_panel
random.shuffle(models) #
S1=2.5*random.random()+1.7


class Echo(object):
    def __init__(self):
        self.value = 0

        rospy.init_node('model_move', anonymous=True)

        self.pub  = rospy.Publisher('/gazebo/set_model_state', ModelState, latch=True)
        panelS1_msg=ModelState() # Message to publish
        panelS1_msg.model_name=models[0]
            
        panelS1_pose=Pose()
        
        
        panelS1_pose.position.y=0
        panelS1_pose.position.x=S1 ## ajustar
        panelS1_pose.orientation.z=0.707106
        #panelS1_pose.orientation.w=0.707106
        panelS1_msg.pose=panelS1_pose

        self.pub.publish(panelS1_msg) # Publish the possitions 
        
        rospy.Subscriber('/kuka_pos', Point, self.update_value)

    def update_value(self, msg):
        self.value = msg.data

    def run(self):
        r = rospy.Rate(10)
        while not rospy.is_shutdown():
            self.pub.publish(self.value)
            r.sleep()
