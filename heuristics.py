<<<<<<< HEAD
import math

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def euclidean(a, b):
=======
import math

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def euclidean(a, b):
>>>>>>> 45ecbcd2f9039abf6606246d86980f912bf29977
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2) 
