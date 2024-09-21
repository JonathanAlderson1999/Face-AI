import random
import numpy as np

class layer:

    weights    = []
    biases     = []
    activation = []
    dimension  = [0, 0]

class conv2D_layer:

    kernel_size = 3
    stride = 3
    kernels = []
    biases = []
    activation = []
    dimension = []


class sequential_network:

    layers = []

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

    def dense(self, input_x, input_y, output_x, output_y):

        num_input_nodes  = input_x  * input_y
        num_dense_noides = output_x * output_y

        new_layer = layer()
        new_layer.weights   = ([np.random.rand(num_input_nodes) for j in range(num_dense_nodes)])
        new_layer.biases    = (np.random.rand(num_dense_nodes))
        new_layer.dimension = [output_x, output_y]
    
        self.layers.append(new_layer)

    def conv2D(self):

        prev_layer = self.layers[-1]
        prev_x = prev_layer.dimension[0]
        prev_y = prev_layer.dimension[1]
    
        new_layer = conv2D_layer()
        new_layer.kernels = [np.random.rand(kernel_size * kernel_size) for i in range(prev_x * prev_y)]
        new_layer.biases = np.random.random(prev_x * prev_y)

        self.layers.append(new_layer)

    def feed_forward(self, input):

        # for each neruon in the 'next' layer
        #   for each neuron in the 'current' layer
        #       multiply the neuron by the nth weight of the 'next' neuron
        #   subract the 'next' neurons bias
        #   run through relu activation function

        activations = input

        for i in range(self.num_layers):

            weights = self.weights[i]
            biases  = self.biases[i]

            num_neurons_in_next_layer = len(biases)

            activations = [self.relu((np.sum(input * weights[j]) - biases[j])) for j in range(num_neurons_in_next_layer)]

        return activations


    # TODO cleanup
        #    stride = 3 
        #new_layer = np.zeros(x * stride * y * stride)

        #for layer_y in range(prev_x):

        #    for layer_x in range(prev_y):

        #        for kernel_y in range(kernel_size):

        #            for kernel_x in range(kernel_size):

        #                x_layer_kernal = layer_x * stride + kernel_x
        #                y_layer_kernal = layer_y * stride + kernel_y

        #                new_layer[y_layer_kernal][x_layer_kernal] = layer[layer_y][layer_x] * kernel[kernel_y][kernel_x]
