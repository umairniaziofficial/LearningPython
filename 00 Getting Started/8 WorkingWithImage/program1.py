from PIL import Image
import os

script_dir = os.path.dirname(os.path.realpath(__file__))
file_dr = os.path.join(script_dir, "DemoImage.jpg")

girl = Image.open(file_dr)

print(girl.format)
print(girl.format_description)

width, height = girl.size
left = (width - 1080) // 2
top = (height - 1080) // 2
right = (width + 1080) // 2
bottom = (height + 1080) // 2

# Crop the image to a centered 1080x1080 pixel square
cropped_girl = girl.crop((left, top, right, bottom))
girl.show()
cropped_girl.show()
