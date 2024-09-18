from PIL import Image
import os

desired_size = 45, 54
training_dir = "Training Data"
prepared_training_dir = "Prepared Data"

image_names = os.listdir(training_dir)
print("Converting " + str(len(image_names)) + " images...")

# convert from images to scaled down images of only brightness
i = 0
for image_name in image_names:

    img = Image.open(training_dir + "/" + image_name).convert('L')

    img.thumbnail(desired_size, Image.Resampling.LANCZOS)
    img.save(prepared_training_dir + "/" + image_name)

    percent =      round(100 * (i       / len(image_names)))
    prev_percent = round(100 * ((i - 1) / len(image_names)))
    if percent > prev_percent:
        print(str(percent) + "%")
    i += 1

print("Done")
