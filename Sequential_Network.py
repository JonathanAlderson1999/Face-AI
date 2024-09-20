import random
import numpy as np

class sequential_network:

    weights = []
    biases = []

    def __init__(self):

        print(". . .")

    def __str__(self):

       return "".join([self.format(layer) for layer in self.layers])
        

    def format(self, layer):

        out = ("Layer: " + str(len(layer[0])) + " : " + str(len(layer)))
        out += "\n"

        for y in layer:
            for x in y:
                out += ("%6.2f " % x)
            out += "\n"

        out += "\n"
        
        return out

    def relu(self, x):
        return max(0, x)


    def dense(self, num_input_nodes, num_dense_nodes):

        self.weights.append([np.random.rand(num_input_nodes) for j in range(num_dense_nodes)])
        self.biases.append([np.random.rand(num_dense_nodes)])

    def conv2D(self, stride):

        layer = self.layers[-1]

        x = len(layer[0])
        y = len(layer)
    
        kernel_size = 3
        kernel = [[np.random.rand(kernel_size)] for j in range(kernel_size)]

        stride = 3 
        new_layer = [np.zeros(x * stride) for j in range(y * stride)]

        for layer_y in range(y):

            for layer_x in range(x):

                for kernel_y in range(kernel_size):

                    for kernel_x in range(kernel_size):

                        x_layer_kernal = layer_x * stride + kernel_x
                        y_layer_kernal = layer_y * stride + kernel_y

                        new_layer[y_layer_kernal][x_layer_kernal] = layer[layer_y][layer_x] * kernel[kernel_y][kernel_x]

        self.layers.append(new_layer)

    def feed_forward(self, input):

        i = 0

        s1 = input[i]

        print("!")

