import math
from display import *



#vector functions
#normalize vetor, should modify the parameter
def normalize(vector):
    sum = vector[0] + vector[1] + vector[2]
    sum *= 1.0
    vector[0] /= sum
    vector[1] /= sum
    vector[2] /= sum

#Return the dot porduct of vector a . b
def dot_product(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]

def cross_product(a,b):
    return [a[1]*b[2] - a[2]*b[1], a[2]*b[0] - a[0]*b[2], a[0]*b[1] - a[1]*b[0]]

#Calculate the surface normal for the triangle whose first
#point is located at index i in polygons
#Nz = UxVy - UyVx
def calculate_normal(polygons, i):
    vector1 = [ polygons[i+1][0] - polygons[i][0],  polygons[i+1][1] - polygons[i][1],  polygons[i+1][2] - polygons[i][2] ] 
    vector2 = [ polygons[i+2][0] - polygons[i][0],  polygons[i+2][1] - polygons[i][1],  polygons[i+2][2] - polygons[i][2] ] 
    Normal = cross_product(vector1,vector2)
    return Normal

