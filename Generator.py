import random
from Sequential_Network import sequential_network

class generator:

    # Final image size is 45, 54

    # Scale by 3 each time
    # 5, 6
    # 15, 18
    # 45, 54

    x = 5
    y = 6

    def __init__(self):

        sequential = sequential_network()

        sequential.dense(self.x, self.y)
        sequential.conv2D(stride = 3)
        sequential.conv2D(stride = 3)
        sequential.conv2D(stride = 3)

        self.sequential = sequential

    def generate(self):
        
        noise = [[random.random() for i in range(self.x)] for j in range(self.y)] 

        return self.sequential.feed_forward(noise)        


