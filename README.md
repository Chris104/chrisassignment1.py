# chrisassignment11.py

1. I began the assignment by connecting python to sqlite so I could extract the "renewable.db"
2. My plan was to create a code to find the total minimum distance for each location to the other nine (9) locations. 
   I wanted to use cmath and extract each of the co-orinates from the array. I was unable to write this code because my syntax had errors.
   I researched the internet looking for other examples. I found the math.hypot formula. In order to calculate my formula I manually created locx,locy
   for each location longatude and latitude. I inputted the formula getting the minimum distance from location 1 to location 2...etc. I completed this task for each location
   I then added the results from each math.hypot and got the total distance.
3. Once I created the code for each of the ten (10) locations, I then printed the results. 
4. I created a dictionary called selection, which was made up off all the caluclated minimim distances in the dictionary.
5. I also calculated the total production of units from each of the locations. I divided each locations production capacity against the total production capacity in order to identify which 
   location could best manage the additional capacity. Location 7 had the lowest additional capacity percentage, however its total distance was high.
6. Based on the results I determined that location 8 was the most ideal location, as it had the shortest route and could manage the additional units.
7. I then saved my work and pushed the code onto my GitHub repository.
8. I ran into difficulty at this point. I could no longer access the database in python from SQLite. I looked online for solutions. I found that python couldn't identify the location of the database. 
   I found the full location string, however I still got this fault. I had to download SQLite Manager as a Firefox add on. I was able to access the port co-ordinates. I manually inputted the information into Python. I then calculated the minimum distance from location 8 to each port location.
   I calculated that the optimum port location was Port 3.
9. I also tried to import a csv. I came across the same problem and could not access this file.


Observations:

1. I found that I had to use basic formulas when calculating my results.
2. As highlighted above, as a result of issues with my system I had to use alternative soluions in extracting the information from the renewable database.

Chris Kiernan
Student No 15204932 