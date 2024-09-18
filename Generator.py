import random

class generator:

    # Final image size is 45, 54

    # Scale by 3 each time
    # 5, 6
    # 15, 18
    # 45, 54

    x = 5
    y = 6

    layers = []

    def format(self, layer):

        print("Layer: " + str(len(layer[0])) + " : " + str(len(layer)))

        for y in layer:
            for x in y:
                print("%6.2f" % x, end = " ")
            print()

        print()


    def conv2D(self, layer):

        x = len(layer[0])
        y = len(layer)
    
        kernel_size = 3
        kernel = [[random.random() for i in range(kernel_size)] for j in range(kernel_size)]

        kernel = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]

        stride = 3 
        new_layer = [[0 for i in range(x * stride)] for j in range(y * stride)]

        for l_y in range(y):
            for l_x in range(x):

                for k_y in range(kernel_size):
                    for k_x in range(kernel_size):

                        new_layer[l_y * stride + k_y][l_x * stride + k_x] = layer[l_y][l_x] * kernel[k_y][k_x]

        return new_layer

    def __init__(self):


        self.layers.append([[random.random() for i in range(self.x)] for j in range(self.y)])

        self.format(self.layers[0])

        self.layers.append(self.conv2D(self.layers[0]))

        self.format(self.layers[1])

        print(". . .")

    def generate(self):
        # LOL!
        return [[random.random() for i in self.x] for j in self.y]


