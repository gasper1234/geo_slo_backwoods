# program for reading shapefiles with geoPandas

import geopandas as gpd
import numpy as np
import matplotlib.pyplot as plt

# read the shapefile
file_name = 'RPE_SLO_PROSTORSKE_ENOTE_NASELJA_poligon.shp'

gdf = gpd.read_file(file_name)


data = gdf.values.tolist()

coord = []
names = []

for i in data:
    point = i[-1].representative_point()
    names.append(i[3])
    coord.append([point.x, point.y])

coord = np.array(coord)

# create dictionary with names and coordinates
dict = {}
for i in range(len(names)):
    dict[names[i]] = coord[i]

conv_x = lambda x: 15 + (1+(17+27.2/60)/60) * (x/1000-500)/100
conv_y = lambda y: 46+22.5/60 +  (27/60) * (y/1000-137)/50

real_coord = np.array([[conv_x(i[0]), conv_y(i[1])] for i in coord])

real_dict = {}
for i in range(len(names)):
    real_dict[names[i]] = np.flip(real_coord[i])

print(dict['Ljubljana']-dict['Novo mesto'])
print(dict['Oplotnica'])

print(real_dict['Ljubljana'])
print(real_dict['Oplotnica'])
print(real_dict['Radovljica'])