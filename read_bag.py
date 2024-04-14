#!/usr/bin/src python3

import rospy 
import rosbag 

rospy.init_node('/read_bag')

bag= rosbag.Bag('/home/prateek/catkin_ws/src/pub_sub/bag/test.bag') ##adding the file pathname 

for topic, msg, t in bag.read_messages{topics = "/sam"}:
  if topic == "/sam":
    print("Sam data is:")
    print(msg,data)
    print("it was recorded at ")
    print(t)
    
    
