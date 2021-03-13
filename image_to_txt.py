# Autor: Alexander C.M (Dretcm)
# Date: 12/03/2021

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = Image.open('cheems.png').convert('L') # 3 channels (RBG) to 1 (GrayScale).
img = img.resize((400,200))

##plt.imshow(img, cmap='gray')
##plt.show()

arr = np.asarray(img)/255.0  # normalize data of (0.0 - 255.0) to (0.0 - 1.0)
func = np.vectorize(lambda x: round(x,1))
arr = func(arr)

elements = set(tuple(list(arr.flatten()))) # unique elements in the range (0.0-1.0)

colors = 'abcdefghijk'
range_colors = colors[:len(elements)]
data = dict(zip(elements,range_colors))

with open('output.txt','w') as f:
        for row in arr:
                for column in row:
                        f.write(data[column])
                f.write(str('\n'))





