#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import rospy
from std_msgs.msg import String
sys.path.append("./Subscriber")
sys.path.append("./Publisher")
from Subscriber import Subscriber

#継承して何か作る用
class TEST(Subscriber):
    def __init__(self, nodename: str, subtopic: str) -> None:
        super().__init__(nodename, subtopic)

#Subscriberを使うパターン
def main():
    node_name = "test_node"
    sub_topic = "test_topic"
    rospy.init_node(node_name)
    test_subscriber = TEST(nodename=node_name, subtopic=sub_topic)

if __name__ == "__main__":
    main()