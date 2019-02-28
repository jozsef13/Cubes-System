"""

Homework problem for OOP course
Problem 13 
Created by Simon Jozsef-Gabriel from CEN 2.3

"""

import Cub
import SistemCoordonate

fmain = open("input.txt", "r") #Declaration of a variable for reading from a file

nrCuburi = int(fmain.readline())#Reading the number of cubes
sistemCuburi = [Cub.Cub(8) for i in range(nrCuburi) ] #Initializating a list for the system composed of cubes

nrPuncte = int(fmain.readline()) #Reading the number of points
sistemDeCoordonate = SistemCoordonate.SistemCoordonate(nrPuncte) #Initializing a variable for the system of coordinates xyz composed by points

lineC = 24
#Statement for the case when we don't have any cubes
if nrCuburi != 0:
    for i in range(nrCuburi):
        sistemCuburi[i].addCub((lineC*i)+2) #Adding cubes in the system of cubes

sistemDeCoordonate.addPuncte(nrPuncte, nrCuburi*lineC+2) #Adding points in the system of coordinates xyz

for i in range(nrCuburi):
    print("Cubul ", i)
    sistemCuburi[i].printCoordonateleCubului() #Calling the function for printing the coordinates of the cubes
    print()

print()
sistemDeCoordonate.printPuncte(nrPuncte) #Calling the function for printing the system of points

apartine = 0
print()
for i in range(nrCuburi):
    for j in range(nrPuncte):
        apartine = sistemCuburi[i].apartineExteriorCub(sistemDeCoordonate.puncte[j], i) #Evaluate if the points belong to the exterior of any cube, in order to determine if we have a road from the start point to the stop point
    #Statement for the case when we have all the points belonging to the exterior of a cube
    if apartine == 1:
        break

print()
if apartine == 1:
    #If statement is true, it means that we can have a road from the start point to stop point
    print("Exista drum fara intreruperi de la punctul de plecare la puntul de sosire trecand prin punctele de mai jos: ")
    sistemDeCoordonate.printPuncte(nrPuncte)
else:
    #If statement is not true, we go on the else statement and that means that we don't have a road from the start point to stop point
    print("Nu exista drum fara intreruperi de la punctul de plecare la punctul de sosire trecand prin punctele de mai jos: ")
    sistemDeCoordonate.printPuncte(nrPuncte)
   
print()

for i in range(nrCuburi):
    sistemCuburi[i].calculCentruDeGreutate() #We calculate the center of gravity for all the cubes

echi = 0
for i in range(nrCuburi-1):
    echi = sistemCuburi[i].detSistemEchivalent(sistemCuburi[i+1].centru) #Determine if the cubes from the system of cubes are equivalent

if echi == 1:
    #If statement is true, it means that the system of cubes is equivalent
    print("Sistemul de cuburi este echivalent!")
else:
    #If statement is not true, we go on the else statement and that means that we don't have an equivalent system of cubes
    print("Sistemul de cuburi nu este echivalent!")