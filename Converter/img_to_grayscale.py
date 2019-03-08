from PIL import Image
import numpy as np

img = np.array(Image.open("Images/iss.jpg"))

print(img)