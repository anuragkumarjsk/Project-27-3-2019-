import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
from PIL import Image

pic=Image.open("/root/Desktop/python/brd.jpeg")
picarray=np.asarray(pic)
plt.imshow(picarray)
