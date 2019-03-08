from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = np.array(Image.open("Images/iss.jpg"))

plt.imshow(img)


def rgb_to_gray(img):
    grayImage = np.zeros(img.shape)
    R = np.array(img[:, :, 0])
    G = np.array(img[:, :, 1])
    B = np.array(img[:, :, 2])

    R = (R * .299)
    G = (G * .587)
    B = (B * .114)

    avg = (R + G + B)
    grayImage = img

    for i in range(3):
        grayImage[:, :, i] = avg

    return grayImage


gimg = rgb_to_gray(img.copy())
plt.imshow(gimg)
plt.show()

