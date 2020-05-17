# Import image class of matplotlib
import matplotlib.image as img

# Read batman image and print dimensions
image = img.imread('rose.jpg')
print(image.shape)

# Store RGB values of all pixels in lists r, g and b
for row in image:
    for temp_r, temp_g, temp_b in row:
        r.append(temp_r)
        g.append(temp_g)
        b.append(temp_b)
