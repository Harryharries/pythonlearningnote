import random
import numpy as np
import numpy.random

a = np.array([1,2,3,4,5,6])
print (a)
random.shuffle(a) # a will definitely be destroyed
print (a)