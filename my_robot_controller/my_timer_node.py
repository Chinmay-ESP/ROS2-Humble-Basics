#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

class Timer_Node (Node):
    def __init__(self):
        super().__init__('my_timer_node')
        self.counter = 0
        self.create_timer(1.0, self.timer_callback)
        
    def timer_callback(self):
        self.get_logger().info('Chinmay-ESP ' + str(self.counter))
        self.counter +=1
        

def main(args=None):
    rclpy.init(args=args)
    node = Timer_Node()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
