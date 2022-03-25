import numpy as np

def radians_to_degrees(rad):
    return (180/np.pi)*rad

print(radians_to_degrees(np.pi/4))
