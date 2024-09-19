import matplotlib.pyplot as plt
from Generator import generator
import random

generator = generator()

generated_image = generator.generate()

plt.imshow(generated_image, cmap='gray', aspect=1.0) #[0, :, :, 0]
plt.show()