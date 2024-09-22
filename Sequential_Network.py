import random
import numpy as np

def relu(x):
    return max(0, x)

class layer:

    weights     = []
    biases      = []
    activations = []
    dimension   = [0, 0]

    # conv2D
    kernel_size = 3
    stride = 3 
    kernels = []

    def input(self, input_x, input_y):
        self.type = "input"

        self.weights = []
        self.biases = []
        self.dimension = [input_x, input_y]

    def dense(self, input_x, input_y, output_x, output_y):
        
        self.type = "dense"
        num_input_nodes  = input_x  * input_y
        num_dense_nodes = output_x * output_y

        self.weights   = ([np.random.rand(num_input_nodes) for j in range(num_dense_nodes)])
        self.biases = (np.random.rand(num_dense_nodes))
        self.dimension = [output_x, output_y]

    def conv2DTranspose(self, prev_layer):

        self.type = "conv2D"
        prev_x = prev_layer.dimension[0]
        prev_y = prev_layer.dimension[1]
    
        self.kernels = [np.random.rand(self.kernel_size * self.kernel_size) for i in range(prev_x * prev_y)]
        self.biases = np.random.random(prev_x * prev_y)
        self.dimension = [prev_x * self.stride, prev_y * self.stride]

    def feed_forward(self, input, dimension):

        num_neurons = len(self.biases)
        biases  = self.biases

        if (self.type == "dense"):
            weights = self.weights
            self.activations = np.array([relu((np.sum(input * weights[j]) - biases[j])) for j in range(num_neurons)])

        elif (self.type == "conv2DTranspose"):
            kernels = self.kernels

            kernel_id = -1

            activations = [np.zeros(dimension[0] * self.stride) for i in range(dimension[1] * self.stride)]

            # TODO: We don't want to be multiplying single elements like a fool
            # when we could be making use of np's vectorized multiplications.
            # I'll come back when training is slow.

            for input_y in range(dimension[1]):
                for input_x in range(dimension[0]):

                    neuron_id = (input_y * dimension[0]) + input_x

                    for kernel_x in range(self.kernel_size):
                        for kernel_y in range(self.kernel_size):

                            x_layer_kernal = input_x * self.stride + kernel_x
                            y_layer_kernal = input_y * self.stride + kernel_y

                            activations[y_layer_kernal][x_layer_kernal] += input[neuron_id] * kernels[neuron_id][(kernel_y * self.kernel_size) + kernel_x]

            self.activations = np.concatenate(activations)

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

    def dense(self, input_x, input_y, output_x, output_y):

        new_layer = layer()
        new_layer.dense(input_x, input_y, output_x, output_y)
        self.layers.append(new_layer)

    def conv2DTranspose(self):

        prev_layer = self.layers[-1]
        new_layer = layer()
        new_layer.conv2DTranspose(prev_layer)
        self.layers.append(new_layer)

    def feed_forward(self, input):

        # for each neruon in the 'next' layer
        #   for each neuron in the 'current' layer
        #       multiply the neuron by the nth weight of the 'next' neuron
        #   subract the 'next' neurons bias
        #   run through relu activation function

        prev_activations = input

        for i in range(len(self.layers)):

            prev_dimension = (self.layers[i - 1].dimension if (i > 0) else [0, 0])

            self.layers[i].feed_forward(prev_activations, prev_dimension)

            prev_activations = self.layers[i].activations

        return (self.layers[-1])