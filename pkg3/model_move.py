#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from gazebo_msgs.msg import ModelState
from geometry_msgs.msg import Pose
from geometry_msgs.msg import Twist
import random
from geometry_msgs.msg import Point
factor=1
models=['gripper','cat_panel','elephant_panel'] # Modeles: gripper, cat_panel, elephant_panel
random.shuffle(models) #
#S1=2.5*random.random()+1.7
def talker(msg): # Function to publish the position of the object
	pub = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10) # Publisher
	#get the position of the robot
	
	#rospy.init_node('move_model', anonymous=True)
	
	#rate = rospy.Rate(100) # 10hz
	panelS1_msg=ModelState() # Message to publish
	panelS1_msg.model_name='gripper'
	
	# if msg.x equal to 0 and msg.y equal to 0 and msg.z equal to 0 then the robot is not in the table
	if msg.x==0 and msg.y==0 and msg.z==0:
		panelS1_pose=Pose()
		panelS1_pose.position.y=0
		panelS1_pose.position.x=0
		panelS1_pose.position.z=0
		print("The robot is goin to the poss")

	
	panelS1_pose=Pose()
	panelS1_pose.position.y=msg.y+(0.4) # get from kukapos
	panelS1_pose.position.x=msg.x +(-0.13)## ajustar
	panelS1_pose.position.z=msg.z +(-0.3)
	#panelS1_pose.orientation.z=msg.z+(0.3) # get the orientation of the robot
	panelS1_pose.orientation.w=0.707106*14
	panelS1_msg.pose=panelS1_pose
	xaus=panelS1_pose.position.x
	yaus=panelS1_pose.position.y
	zaus=panelS1_pose.position.z
	# if the values are outside of the workspace return 0
	if xaus>2.5 or xaus<-1.7 or yaus>2.5 or yaus<-0.5 or zaus>2.5 or zaus<0:
		
		print("The robot is goin outside of the workspace")
		panelS1_pose.position.y=0
		panelS1_pose.position.x=0
		panelS1_pose.position.z=0


	pub.publish(panelS1_msg) # Publish the possitions 
	
if __name__ == '__main__':
	try:
		rospy.init_node('model_move', anonymous=True) # Name of the node 
		#subscribe to the topic
		rospy.Subscriber("/kuka_pos",Point,talker) # Subscribe to the topic 
		# spin() simply keeps python from exiting until this node is stopped
		#talker()
		rospy.spin()

	except rospy.ROSInterruptException:
		pass