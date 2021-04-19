import rclpy
from rclpy.node import Node
from std_msgs.msg import String
l_direction = 0


class ScaredRobot(Node):
    

    def listener_callback_1(self, msg):
        print("LEFT %s"%msg.data)
        left = int(msg.data[:-2]) #remove the 'cm' and convert to int.
        print("GOT L_INFO")
        self.i = left
        print("GOT L_INFO %s" %l_direction)
            
    def listener_callback(self, msg):
        print(msg.data)
        right = int(msg.data[:-2]) #remove the 'cm' and convert to int.
        msg = String()
        print("l %s"%l_direction)
        
        if right < 40:
            print("CHECKING DIRECTIOn")
            if right >= self.i:
               msg.data = "TURNR:0150\n"
               self.publisher.publish(msg)
            
            else:
               print("CHECKING ELSE")   
               msg.data = "TURNL:0150\n"
               self.publisher.publish(msg)
            
            
        msg.data = "CONTF:0050\n"
        self.publisher.publish(msg)
        

    def __init__(self):
        super().__init__('ScaredRobot')
        self.publisher = self.create_publisher(String, '/robot/control', 10)
        msg = String()
        msg.data = "CONTF:0050\n"
        self.publisher.publish(msg)

        self.subscription1 = self.create_subscription(
            String,
            '/robot/left',
            self.listener_callback_1,
            10)
        self.subscription1  # prevent unused variable warning
        
        self.subscription = self.create_subscription(
            String,
            '/robot/right',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        
        

def main(args=None):
    rclpy.init(args=args)

    scaredrobot = ScaredRobot()
    rclpy.spin(scaredrobot)
    
    scaredrobot.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
