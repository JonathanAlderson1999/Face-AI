
class trainer:

    def __init__(self, x, y):
        print("Hi!")
        self.gen = Generator(x, y)
        self.dis = Discriminator

        s = random.random()

    def distriminator_loss(self):

        return [[random.random() * s for i in self.Generator.x] for j in self.Generator.y]

    def generator_loss(self):

        return

    def backproagate(self):

        return