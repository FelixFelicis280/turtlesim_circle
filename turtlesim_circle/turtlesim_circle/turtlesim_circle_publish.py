import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist


class TurtlesimCircle(Node):

    def __init__(self):
        super().__init__('turtlesim_circle')
        self.publisher_ = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.timer = self.create_timer(1, self.timer_callback)

        self.declare_parameter('linear_x', 2.0)
        self.declare_parameter('angular_z', 1.8)

        self.linear_x = self.get_parameter('linear_x').value
        self.angular_z = self.get_parameter('angular_z').value

    def timer_callback(self):
        msg = Twist()
        msg.linear.x = self.linear_x
        msg.linear.y = 0.0
        msg.linear.z = 0.0
        msg.angular.x = 0.0
        msg.angular.y = 0.0
        msg.angular.z = self.angular_z

        self.publisher_.publish(msg)
        self.get_logger().info(
            'Linear: x=%.2f, y=%.2f, z=%.2f | Angular: x=%.2f, y=%.2f, z=%.2f'
            % (
                msg.linear.x,
                msg.linear.y,
                msg.linear.z,
                msg.angular.x,
                msg.angular.y,
                msg.angular.z
            )
        )


def main(args=None):
    rclpy.init(args=args)

    turtlesim_circle = TurtlesimCircle()

    rclpy.spin(turtlesim_circle)

    turtlesim_circle.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()