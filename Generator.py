import random
from Sequential_Network import sequential_network
import numpy as np

class generator:

    # Final image size is 45, 54

    # Scale by 3 each time
    # 5, 6
    # 15, 18
    # 45, 54

    x = 5
    y = 6

    def __init__(self):

        # TODO: Batch Normalization
        #       Leaky ReLU

        sequential = sequential_network()
        sequential.dense(self.x, self.y, self.x, self.y)
        sequential.conv2DTranspose()
        sequential.conv2DTranspose()

        self.sequential = sequential

    def generate(self):
        
        noise = np.random.rand(self.x * self.y)

        final_layer = self.sequential.feed_forward(noise)

        dim = final_layer.dimension

        activations = final_layer.activations.tolist()

        row = dim[0]

        image = [activations[(row * i) : (row * (i + 1))] for i in range(dim[1])]

        return image


