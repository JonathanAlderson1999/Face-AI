from Generator import generator
import random

generator = generator()

generated_image = generator.generate()

from matplotlib import pyplot as plt
plt.imshow(generated_image, cmap='gray', aspect=1.0) #[0, :, :, 0]
plt.show()