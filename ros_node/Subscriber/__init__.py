#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import rospy
from std_msgs.msg import String
class Subscriber():
    def __init__(self, nodename: str, subtopic: str) -> None:
        self.node_name = nodename
        self.sub_topic = subtopic
        rospy.loginfo("starting " + self.node_name +" subscriber node and waiting for "+ self.sub_topic + " topic")
        self.sub = rospy.Subscriber(self.sub_topic, String, self.callback)
        rospy.spin()

    def callback(self, msg):
        rospy.loginfo(msg.data)
        self.processer(msg.data)

    def processer(self, msg):
        #ここで何か処理させる
        print("ready to subscribe topic")