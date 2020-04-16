import numpy as np
import matplotlib.pyplot as plt
import math

class Point: 
    def __init__(self, x, y): 
        self.x = x 
        self.y = y 
  
def onSegment(p, q, r): 
    if ( (q.x <= max(p.x, r.x)) and (q.x >= min(p.x, r.x)) and 
           (q.y <= max(p.y, r.y)) and (q.y >= min(p.y, r.y))): 
        return True
    return False
  
def orientation(p, q, r):   
    val = (float(q.y - p.y) * (r.x - q.x)) - (float(q.x - p.x) * (r.y - q.y)) 
    if (val > 0):  
        return 1
    elif (val < 0):  
        return 2
    else:  
        return 0
  
def doIntersect(p1,q1,p2,q2): 
      
    o1 = orientation(p1, q1, p2) 
    o2 = orientation(p1, q1, q2) 
    o3 = orientation(p2, q2, p1) 
    o4 = orientation(p2, q2, q1) 
  
    if ((o1 != o2) and (o3 != o4)): 
        return True
  
    if ((o1 == 0) and onSegment(p1, p2, q1)): 
        return True
  
    if ((o2 == 0) and onSegment(p1, q2, q1)): 
        return True
  
    if ((o3 == 0) and onSegment(p2, p1, q2)): 
        return True
  
    if ((o4 == 0) and onSegment(p2, q1, q2)): 
        return True
  
    return False

def get_distance(p1,p2):
    x = p1.x-p2.x
    y = p1.y-p2.y
    x = x*x
    y = y*y
    return math.sqrt(x+y)

def get_lines(each_point,points):
    distances = []
    for each_other_point in points:
        if(each_point != each_other_point):
            distances.append((each_point,each_other_point,get_distance(each_point,each_other_point)))
    return distances

def takeSecond(elem):
    return elem[2]

def intersect(each_line,line2):
    checker = False
    if doIntersect(each_line[0],each_line[1],line2[0],line2[1]):
            checker = True
    return checker

def add_to_arr(arr1,arr2):
    for each_elem in arr2:
        arr1.append(each_elem)

    return arr1

N = 40
x = np.random.rand(N)
y = np.random.rand(N)
colors = (0,0,0)
area = np.pi*3

points = []
color_graph = []


for i in range(N):
    points.append(Point(x[i],y[i]))

for each_point in points:
    lines = get_lines(each_point,points)
    lines.sort(key=takeSecond)

    for each_line in lines:
        temp = []

        if(len(color_graph)==0):
            color_graph.append(lines[0])
            color_graph.append(lines[1])
            color_graph.append(lines[2])
            break
        
        for each_final_line in color_graph:
            if not(intersect(each_final_line,each_line)):
                temp.append(each_line)
        color_graph = add_to_arr(color_graph,temp)

print(len(color_graph))
#plt.scatter(x, y, s=area, c=colors, alpha=0.5)
#plt.title('Scatter plot pythonspot.com')
#plt.xlabel('x')
#plt.ylabel('y')
#plt.show()
