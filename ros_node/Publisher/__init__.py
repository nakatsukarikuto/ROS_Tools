#!/usr/bin/python3
# -*- coding: utf-8 -*-
import rospy
from std_msgs.msg import String
class Pub_Module:
    def __init__(self, nodename, pubtopic):
        self.node_name = nodename
        self.pub_topic_name = pubtopictopic
        rospy.loginfo("starting "+ self.node_name +"node!!")
        self.pub = rospy.Publisher(self.pub_topic_name, String, queue_size=1)

    def publish(self, msg):
        while not rospy.is_shutdown():
            self.pub.publish(msg)
            rospy.loginfo("starting " + self.node_name +" node and publish " + self.pub_topic_name + " topic")
            rospy.Rate(1).sleep()