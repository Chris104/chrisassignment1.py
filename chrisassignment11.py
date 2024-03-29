# -*- coding: utf-8 -*-
"""
Created on Fri Oct 09 14:39:26 2015

@author: Chris
"""
import math
import numpy as np
from math import hypot
import cmath


#import sqlite3
#conn= sqlite3.connect('C:\Users\Chris\Downloads\renewable.db') # creating a connection with SQLite
#c = conn.cursor()
#c.execute("SELECT * FROM location;") # execute a SQL Command
#X =np.array(c.fetchall())
# After sending my first code to Github, I was no longer able to extract the database from SQLITE to Python. I understand how to transfer the database into Python. I have also had to manually input all the coordinates as a reseult.

#import sqlite3
#conn= sqlite3.connect('renewable.db') # creating a connection with SQLite
#c = conn.cursor()
#c.execute("SELECT * FROM ports;") # execute a SQL Command
#Y =np.array(c.fetchall())
# I found that other people came across this issue on stackflow. I inputted the full location that the database was saved in, however it was still unable to locate the database.





loc1x=5.265999999999999659e+01 #Ihave copied the grid x location from the table
loc2x=5.285999999999999943e+01
loc3x=5.428000000000000114e+01
loc4x=5.342000000000000171e+01
loc5x=5.234000000000000341e+01
loc6x=5.321999999999999886e+01
loc7x=5.235999999999999943e+01
loc8x=5.284000000000000341e+01
loc9x=5.317999999999999972e+01
loc10x=5.365999999999999659e+01

loc1y=7.259999999999999787e+00
loc2y=8.990000000000000213e+00
loc3y=8.480000000000000426e+00
loc4y=7.950000000000000178e+00
loc5y=6.480000000000000426e+00
loc6y=6.679999999999999716e+00
loc7y=7.709999999999999964e+00
loc8y=6.919999999999999929e+00
loc9y=6.799999999999999822e+00
loc10y=6.690000000000000391e+00

p1 = 2.596960000000000000e+05
p2 = 8.949900000000000000e+04
p3 = 2.716500000000000000e+05
p4 = 8.760600000000000000e+04
p5 = 2.989780000000000000e+05
p6 = 2.000680000000000000e+05
p7 = 6.057300000000000000e+04
p8 = 1.597940000000000000e+05
p9 = 1.633580000000000000e+05
p10 = 2.108170000000000000e+05



distance1 = math.hypot(loc1x - loc2x, loc1y - loc2y) + math.hypot(loc1x - loc3x, loc1y - loc3y) + math.hypot(loc1x - loc4x, loc1y - loc4y) + math.hypot(loc1x - loc5x, loc1y - loc5y) + math.hypot(loc1x - loc6x, loc1y - loc6y) + math.hypot(loc1x - loc7x, loc1y - loc7y) + math.hypot(loc1x - loc8x, loc1y - loc8y) + math.hypot(loc1x - loc9x, loc1y - loc9y) + math.hypot(loc1x - loc10x, loc1y - loc10y)        
print "The total distance in (km) from location 1 is  %f" %distance1 # I have gotten the distance from location 1 to the other 9 locations and added them
prodloc1 = p1/total#I am looking at the extra capacity of units (Trees) coming into this location. Dividing the total production of all ten locations against the total capacity in each location
print "Extra Capacity location 1 = %f" %prodloc1


distance2 = math.hypot(loc2x - loc1x, loc2y - loc1y) + math.hypot(loc2x - loc3x, loc2y - loc3y) + math.hypot(loc2x - loc4x, loc2y - loc4y) + math.hypot(loc2x - loc5x, loc2y - loc5y) + math.hypot(loc2x - loc6x, loc2y - loc6y) + math.hypot(loc2x - loc7x, loc2y - loc7y) + math.hypot(loc2x - loc8x, loc2y - loc8y) + math.hypot(loc2x - loc9x, loc2y - loc9y) + math.hypot(loc2x - loc10x, loc2y - loc10y) 
print "The total distance in (km) from location 2 is  %f" %distance2
prodloc2 = p2/total
print "Extra Capacity location 2 = %f" %prodloc2

distance3 = math.hypot(loc3x - loc1x, loc3y - loc1y) + math.hypot(loc3x - loc2x, loc3y - loc2y) + math.hypot(loc3x - loc4x, loc3y - loc4y) + math.hypot(loc3x - loc5x, loc3y - loc5y) + math.hypot(loc3x - loc6x, loc3y - loc6y) + math.hypot(loc3x - loc7x, loc3y - loc7y) + math.hypot(loc3x - loc8x, loc3y - loc8y) + math.hypot(loc3x - loc9x, loc3y - loc9y) + math.hypot(loc3x - loc10x, loc3y - loc10y) 
print "The total distance in (km) from location 3 is  %f" %distance3
prodloc3 = p3/total
print "Extra Capacity location 3 = %f" %prodloc3

distance4 = math.hypot(loc4x - loc1x, loc4y - loc1y) + math.hypot(loc4x - loc2x, loc4y - loc2y) + math.hypot(loc4x - loc3x, loc4y - loc3y) + math.hypot(loc4x - loc5x, loc4y - loc5y) + math.hypot(loc4x - loc6x, loc4y - loc6y) + math.hypot(loc4x - loc7x, loc4y - loc7y) + math.hypot(loc4x - loc8x, loc4y - loc8y) + math.hypot(loc4x - loc9x, loc4y - loc9y) + math.hypot(loc4x - loc10x, loc4y - loc10y) 
print "The total distance in (km) from location 4 is  %f" %distance4
prodloc4 = p4/total
print "Extra Capacity location 4 = %f" %prodloc4

distance5 = math.hypot(loc5x - loc1x, loc5y - loc1y) + math.hypot(loc5x - loc3x, loc5y - loc2y) + math.hypot(loc5x - loc3x, loc5y - loc3y) + math.hypot(loc5x - loc4x, loc5y - loc4y) + math.hypot(loc5x - loc6x, loc5y - loc6y) + math.hypot(loc5x - loc7x, loc5y - loc7y) + math.hypot(loc5x - loc8x, loc5y - loc8y) + math.hypot(loc5x - loc9x, loc5y - loc9y) + math.hypot(loc5x - loc10x, loc5y - loc10y) 
print "The total distance in (km) from location 5 is  %f" %distance5
prodloc5 = p5/total
print "Extra Capacity location 5 = %f" %prodloc5

distance6 = math.hypot(loc6x - loc1x, loc6y - loc1y) + math.hypot(loc6x - loc2x, loc6y - loc2y) + math.hypot(loc6x - loc3x, loc6y - loc3y) + math.hypot(loc6x - loc4x, loc6y - loc4y) + math.hypot(loc6x - loc5x, loc6y - loc5y) + math.hypot(loc6x - loc7x, loc6y - loc7y) + math.hypot(loc6x - loc8x, loc6y - loc8y) + math.hypot(loc6x - loc9x, loc6y - loc9y) + math.hypot(loc6x - loc10x, loc6y - loc10y)
print "The total distance in (km) from location 6 is  %f" %distance6
prodloc6 = p6/total
print "Extra Capacity location 6 = %f" %prodloc6

distance7 = math.hypot(loc7x - loc1x, loc7y - loc1y) + math.hypot(loc7x - loc2x, loc7y - loc2y) + math.hypot(loc7x - loc3x, loc7y - loc3y) + math.hypot(loc7x - loc4x, loc7y - loc4y) + math.hypot(loc7x - loc5x, loc7y - loc5y) + math.hypot(loc7x - loc6x, loc7y - loc6y) + math.hypot(loc7x - loc8x, loc7y - loc8y) + math.hypot(loc7x - loc9x, loc7y - loc9y) + math.hypot(loc7x - loc10x, loc7y - loc10y)
print "The total distance in (km) from location 7 is  %f" %distance7
prodloc7 = p7/total
print "Extra Capacity location 7 = %f" %prodloc7

distance8 = math.hypot(loc8x - loc1x, loc8y - loc1y) + math.hypot(loc8x - loc2x, loc8y - loc2y) + math.hypot(loc8x - loc3x, loc8y - loc3y) + math.hypot(loc8x - loc4x, loc8y - loc4y) + math.hypot(loc8x - loc5x, loc8y - loc5y) + math.hypot(loc8x - loc6x, loc8y - loc6y) + math.hypot(loc8x - loc7x, loc8y - loc7y) + math.hypot(loc8x - loc9x, loc8y - loc9y) + math.hypot(loc8x - loc10x, loc8y - loc10y)
print "The total distance in (km) from location 8 is  %f" %distance8
prodloc8 = p8/total
print "Extra Capacity location 8 = %f" %prodloc8

distance9 = math.hypot(loc9x - loc1x, loc9y - loc1y) + math.hypot(loc9x - loc2x, loc9y - loc2y) + math.hypot(loc9x - loc3x, loc9y - loc3y) + math.hypot(loc9x - loc4x, loc9y - loc4y) + math.hypot(loc9x - loc5x, loc9y - loc5y) + math.hypot(loc9x - loc6x, loc9y - loc6y) + math.hypot(loc9x - loc7x, loc9y - loc7y) + math.hypot(loc9x - loc8x, loc9y - loc8y) + math.hypot(loc9x - loc10x, loc9y - loc10y)
print "The total distance in (km) from location 9 is  %f" %distance9
prodloc9 = p9/total
print "Extra Capacity location 9 = %f" %prodloc9

distance10 = math.hypot(loc10x - loc1x, loc10y - loc1y) + math.hypot(loc10x - loc2x, loc10y - loc2y) + math.hypot(loc10x - loc3x, loc10y - loc3y) + math.hypot(loc10x - loc4x, loc10y - loc4y) + math.hypot(loc10x - loc5x, loc10y - loc5y) + math.hypot(loc10x - loc6x, loc10y - loc6y) + math.hypot(loc10x - loc7x, loc10y - loc7y) + math.hypot(loc10x - loc8x, loc10y - loc8y) + math.hypot(loc10x - loc9x, loc10y - loc9y)
print "The total distance in (km) from location 10 is %f" %distance10
prodloc10 = p10/total
print "Extra Capacity location 10 = %f" %prodloc10

production = {p1,p2,p3,p4,p5,p6,p7,p8,p9,p10}
total = sum(production)
print "The total capacity from all locations is %f units" %total

selection = {distance1, distance2, distance3, distance4, distance5, distance6, distance7, distance8, distance9, distance10}
bestselection = min(selection)

prodloc ={prodloc1, prodloc2, prodloc3, prodloc4, prodloc5, prodloc6, prodloc7, prodloc8, prodloc9, prodloc10}#I have made dictionary of all prodloc loactions
prodtotal = min(prodloc)#I am identifying which location has the smallest increase in capacity
print "%f" %prodtotal


print "The minimum total distance is from location 8 at  %f km" %bestselection 
print "I would select Location 8"

import csv
import sys

#cr = csv.reader(open("ports.csv","rb"))
#for row in cr:
    #print row
#Another issue trying to upload data from excel.


port1x = 52.700000000000000# I had to download SQLite Manager on Firefox in order to get the coordinates for the Ports.
port2x = 53.330000000000000
port3x = 52.270000000000000

port1y = 8.630000000000000
port2y = 6.250000000000000
port3y = 6.390000000000000

Portdistance1 = math.hypot(loc8x - port1x, loc8y - port1y)
print "Total Distance from Location 8 to Port 1 is (km) %f" %Portdistance1

Portdistance2 = math.hypot(loc8x - port2x, loc8y - port2y)
print "Total Distance from Location 8 to Port 2 is (km) %f" %Portdistance2

Portdistance3 = math.hypot(loc8x - port3x, loc8y - port3y)
print "Total Distance from Location 8 to Port 3 is (km) %f" %Portdistance3


print "The best port location is Port 3"# Using the minimum distance formula I have calculated that Port 3 is the best port to ship to as it is the closest












