# Image manipulation
    # sudo apt install python3-pil

import PIL.Image
image = PIL.Image.open("Instalation/houses.jpg")
print(image.size)
print(image.format)