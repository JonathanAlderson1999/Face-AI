import random
import numpy as np

class sequential_network:

    weights = []
    biases = []
    activation = []
    num_layers = 0

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
        self.biases.append(np.random.rand(num_dense_nodes))
        self.num_layers += 1

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

