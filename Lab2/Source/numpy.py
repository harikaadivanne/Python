from random import randint
import numpy as np
x = np.random.randint(0,20, size=(15))
print("Original array: %s"  %x)
print("The Most Frequent item in the list:")
print(np.bincount(x).argmax())