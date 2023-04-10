import numpy as np
import matplotlib.pyplot as plt
import random

def getArcPoints(arc_angle, arc_length, x_start, y_start, phi_start, k=1000):
    radius = arc_length / arc_angle
    x_center = x_start - radius * np.sin(phi_start)
    y_center = y_start - radius * np.cos(phi_start)
    print(x_center, y_center)
    x_points = []
    y_points = []
    phi_list = []
    phi_i = 0

    for i in range(k):
        phi_i = phi_start + (arc_angle * (i+1)) / k
        x_i = x_center + radius * np.sin(phi_i)
        y_i = y_center + radius * np.cos(phi_i)
        x_points.append(x_i)
        y_points.append(y_i)
        phi_list.append(phi_i)
            
    return x_points, y_points, x_center, y_center, phi_start

# Arc Parameters: (arc_angle, arc_length)
ARC_PARAMS = {
    'startX': 0,
    'startY': 200,
    'phiStart': 0,
    'arc': [
        (0.5, 30),
        (0.7, 45),
        (1.04, 60)
    ]
}

# Function for generating lists of lists of points coordinates
def generateArcs():
    coordinates_list = []

    x_coordinates, y_coordinates, x_center, y_center, phi = getArcPoints(1.3, 75, ARC_PARAMS.get('startX'), ARC_PARAMS.get('startY'), 0)
    # ARC_PARAMS['startX'] = x_coordinates[len(x_coordinates)-1]
    # ARC_PARAMS['startY'] = y_coordinates[len(y_coordinates)-1]
    # ARC_PARAMS['phiStart'] = phi
    coordinates_list.append({
        'x_center': x_center,
        'y_center': y_center,
        'x_coordinates': x_coordinates,
        'y_coordinates': y_coordinates 
    })
    print(phi)

    for index, tuple in enumerate(ARC_PARAMS.get('arc')):
        arc_angle = tuple[0]
        arc_length = tuple[1]
        new_phi = ARC_PARAMS.get('phiStart') + arc_angle
        
        print(new_phi)
        x_coordinates, y_coordinates, x_center, y_center, phi = getArcPoints(arc_angle, arc_length, ARC_PARAMS.get('startX'), ARC_PARAMS.get('startY'), new_phi)
        ARC_PARAMS['startX'] = x_coordinates[len(x_coordinates)-1]
        ARC_PARAMS['startY'] = y_coordinates[len(y_coordinates)-1]
        ARC_PARAMS['phiStart'] = phi
        coordinates_list.append({
            'x_center': x_center,
            'y_center': y_center,
            'x_coordinates': x_coordinates,
            'y_coordinates': y_coordinates 
        })
    
    return coordinates_list

def visualizeArcs(coordinates_list):
    colors = ['red', 'green', 'blue', 'orchid', 'darkred', 'cadetblue', 'khaki']

    for i, dict in enumerate(coordinates_list):
        x_coord = dict['x_coordinates']
        y_coord = dict['y_coordinates']
        color = random.choice(colors)

        plt.scatter(x=x_coord, y=y_coord, color=color)
        plt.scatter(x=dict['x_center'], y=dict['y_center'], color=color)
    plt.show()

# Second part: Generate Arcs + Visualization for them
coordinates = generateArcs()
visualizeArcs(coordinates)

# Generation + Visualization for the first part
# x_points, y_points, x_center, y_center, phi_start = getArcPoints(0.5, 30, 0, 200, 0, k=1000)
# plt.scatter(x=x_points, y=y_points, color='blue')
# plt.scatter(x=x_center, y=y_center, color='blue')
# plt.show()
