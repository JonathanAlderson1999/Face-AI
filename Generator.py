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

        print(sequential)

        sequential.conv2D()

        print(sequential)

        print(". . .")

    def generate(self):
        # LOL!
        return [[random.random() for i in self.x] for j in self.y]


