# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 01:50:37 2020

@author: Toby
"""
print ("hello world")


import geopandas as gpd
import matplotlib.pyplot as plt

""" Plotting shapefiles"""
cities = gpd.read_file(r'C:\Users\hp\Desktop\my python exercises\19thquarter.shp')
cities.plot( cmap = 'jet', column = 'ward_Name' , figsize= (7,7) , legend = True)

#Plotting country files from URL
country = gpd.read_file(gpd.datasets.get_path('naturalearth_cities'))
country.plot()
plt.savefig(r"C:/Users/hp/Desktop/my python exercises/cities.jpg")


world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
world.plot()
plt.savefig(r"C:/Users/hp/Desktop/my python exercises/world.jpg")

aoi = gpd.read_file(r'D:\Personal Data\Termpaper\Shapefiles\aoi.shp')
aoi.plot()

# Plotting Two shapefiles 
f, ax =plt.subplots (1)
cities.plot(ax=ax, cmap='rainbow', column='ward_Name')
aoi.plot(ax=ax, facecolor='yellow')


# Intersection
aoi_cities = gpd.overlay(cities, aoi, how = "intersection" )
aoi_cities.plot( cmap = 'rainbow' , column = 'ward_Name' , legend= True, figsize = (7,7))
plt.savefig(r'C:\Users\hp\Desktop\my python exercises\aoi.jpg')


#exporting aoi 
aoi_cities.to_file(r"C:\Users\hp\Desktop\my python exercises\aoi_cities.shp")
print ("Spatial Analysis with Python has been sucessfully done")


