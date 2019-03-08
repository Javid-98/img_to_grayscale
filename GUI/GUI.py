from Converter import img_to_grayscale
import PIL.Image, PIL.ImageTk
import tkinter as tk
import matplotlib.pyplot as plt

# Creating Window
window = tk.Tk()
# Title of GUI
window.title("Gray-scale converter")
photo = img_to_grayscale.img.copy()
b = tk.Button(window, text="CONVERT",
              command= lambda: plt.imshow(img_to_grayscale.rgb_to_gray(img_to_grayscale.img)))
b.pack(side='left')


# Get the image dimensions (OpenCV stores image data as NumPy ndarray)
height, width, no_channels = photo.shape
# Create a canvas that can fit the above image
canvas = tk.Canvas(window, width=width, height=height)
canvas.pack()


# Use PIL (Pillow) to convert the NumPy ndarray to a PhotoImage
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(photo))

# Add a PhotoImage to the Canvas
canvas.create_image(0, 0, image=photo, anchor=tk.NW)

window.mainloop()
