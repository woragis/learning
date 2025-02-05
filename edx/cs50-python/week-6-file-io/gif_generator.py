from sys import argv
from typing import List
from PIL import Image

# Using list comprehension

# images: List[str] = [arg for arg in argv[1:]]
images: List[object] = []

for arg in argv[1:]:
    image = Image.open(arg)
    images.append(image)

images[0].save(
    'output.gif', save_all=True, append_images=[im for im in images[1:]], duration=200, loop=0
)
