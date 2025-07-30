import numpy as np
from numpy import random

num = random.randint(100, size=15)
# use the set() method that remove duplicate elements
unique_elements = np.array(list(set(num)))  # we can use only list() method

# Print the sorted array num
print(np.sort(unique_elements))
