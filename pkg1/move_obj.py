import rospy
from gazebo_msgs.msg import ModelState 
from gazebo_msgs.srv import SetModelState


#GAZEBO SERVICE
rospy.wait_for_service('/gazebo/set_model_state')
try:
    set_state = rospy.ServiceProxy('/gazebo/set_model_state', SetModelState)
except rospy.ServiceException :
    print("Service call failed")

state_msg = ModelState()
state_msg.model_name = 'gripper'


state_msg.pose.position.x =  0.825
state_msg.pose.position.y = 0.25
state_msg.pose.position.z =  -0.48
state_msg.pose.orientation.w = 1
state_msg.pose.orientation.x = 0
state_msg.pose.orientation.y = 0
state_msg.pose.orientation.z = 0

resp = self.set_state(state_msg)