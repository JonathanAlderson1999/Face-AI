import random
from Sequential_Network import sequential_network

class discriminator:

    def __init__(self, dimension):

        # TODO: Dropout
        #       Leaky ReLU
        #       TanH final answer

        sequential = sequential_network()

        sequential.input(dimension)
        sequential.conv2D(num_kernels = 64,  kernel_size = 5, stride = 2)
        sequential.conv2D(num_kernels = 128, kernel_size = 5, stride = 2)
        sequential.dense(128, 1, 1, 1)

        self.bias = random.random()
        self.sequential = sequential

    def discriminate(self, image):
        
        final_layer = self.sequential.feed_forward(image)

        confidence = final_layer.activations[0]

        return (condidence > self.bias)