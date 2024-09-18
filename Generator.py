import random

class Generator:

    def __init__(self, x, y):

        self.x = x
        self.y = y

        print(". . .")

    def generate(self):
        # LOL!
        return [[random.random() for i in self.x] for j in self.y]


