import numpy as np

class Circle:

    def __init__(self, centre, rad):

        self.radius = rad
        self.centre = centre

    def __contains__(self, x):
        x = np.array(x)
        c = np.array(self.centre)
        if (x[0] - c[0])**2 + (x[1]-c[1])**2 <= self.radius**2:
            return True
        else:
            return False

