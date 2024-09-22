from Generator import generator
from Discriminator import discriminator
import numpy as np

image_dim = [45, 54]

# todo: real a real picture from disk
image = np.random.rand(image_dim[0] * image_dim[1])

discriminator = discriminator(image_dim)
answer = discriminator.discriminate(image)

#generator = generator()
#generated_image = generator.generate()

#from matplotlib import pyplot as plt
#plt.imshow(generated_image, cmap='gray', aspect=1.0) #[0, :, :, 0]
#plt.show()