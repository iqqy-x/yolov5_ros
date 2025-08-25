#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

class DroneCameraPublisher:
    def __init__(self):
        rospy.init_node('drone_camera_publisher', anonymous=True)
        self.bridge = CvBridge()
        self.image_pub = rospy.Publisher('/drone/image_raw', Image, queue_size=1)
        self.image_sub = rospy.Subscriber("/webcam2/image_raw_2", Image, self.callback)

        rospy.loginfo("Meneruskan stream kamera drone ke /drone/image_raw")

    def callback(self, msg):
        self.image_pub.publish(msg)

if __name__ == '__main__':
    try:
        node = DroneCameraPublisher()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass