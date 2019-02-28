import math
import Punct

class Cub():
    def __init__(self, x):
        #The construct for class Cub
        self.puncteleCubului = [Punct.Punct() for i in range(x)]
        self.centru = Punct.Punct()

    def addCub(self, maxLine):
        #A function for adding a cube reading the coordinates of every point of the cube
        for j in range(8):
            for k in range(j):
                self.puncteleCubului[j].pct = chr(ord(self.puncteleCubului[j].pct) + 1) #Here are the letters for the points
            self.puncteleCubului[j].citirePunct(maxLine) #Here we read the coordinates
            #maxLine is for jumping in the reading file - input.txt
            maxLine = maxLine + 3

    def printCoordonateleCubului(self):
        #Function for printing the coordinates of the cube
        for j in range(8):
            print("Punctul ", self.puncteleCubului[j].pct)
            self.puncteleCubului[j].printPunct()

    def apartineExteriorCub(self, punct, cub):
        #Function to determine if a point belong to the exterior of a cube
        apartineSus = 0
        apartineJos = 0
        apartineFata = 0
        apartineSpate = 0
        apartineStanga = 0
        apartineDreapta = 0

        #Here we find out if the point belong to the top face of the cube
        if punct.z == self.puncteleCubului[0].z:
            if punct.x >= self.puncteleCubului[7].x and punct.y >= self.puncteleCubului[7].y and punct.x <= self.puncteleCubului[1].x and punct.y <= self.puncteleCubului[1].y:
                apartineSus = 1
        
        #Here we find out if the point belong to the bottom face of the cube
        if punct.z == self.puncteleCubului[4].z:
            if punct.x >= self.puncteleCubului[4].x and punct.y >= self.puncteleCubului[4].y and punct.x <= self.puncteleCubului[2].x and punct.y <= self.puncteleCubului[2].y:
                apartineJos = 1
        
        #Here we find out if the point belong to the front face of the cube
        if punct.x == self.puncteleCubului[0].x:
            if punct.z <= self.puncteleCubului[1].z and punct.y <= self.puncteleCubului[1].y and punct.z >= self.puncteleCubului[3].z and punct.y >= self.puncteleCubului[3].y:
                apartineFata = 1
        
        #Here we find out if the point belong to the back face of the cube
        if punct.x == self.puncteleCubului[7].x:
            if punct.z <= self.puncteleCubului[6].z and punct.y <= self.puncteleCubului[6].y and punct.z >= self.puncteleCubului[4].z and punct.y >= self.puncteleCubului[4].y:
                apartineSpate = 1
        
        #Here we find out if the point belong to the left face of the cube
        if punct.y == self.puncteleCubului[4].y:
            if punct.x <= self.puncteleCubului[0].x and punct.z <= self.puncteleCubului[0].z and punct.x >= self.puncteleCubului[4].x and punct.z >= self.puncteleCubului[4].z:
                apartineStanga = 1
        
        #Here we find out if the point belong to the right face of the cube
        if punct.y == self.puncteleCubului[5].y:
            if punct.x <= self.puncteleCubului[1].x and punct.z <= self.puncteleCubului[1].z and punct.x >= self.puncteleCubului[5].x and punct.z >= self.puncteleCubului[5].z:
                apartineDreapta = 1

        if apartineSus == 1:
            print("Punctul ",punct.pct, " apartine fetei de sus a cubului ", cub)
            return 1
        elif apartineJos == 1:
            print("Punctul ",punct.pct, " apartine fetei de jos a cubului ", cub)
            return 1
        elif apartineFata == 1:
            print("Punctul ",punct.pct, " apartine fetei din fata a cubului ", cub)
            return 1
        elif apartineSpate == 1:
            print("Punctul ",punct.pct, " apartine fetei din spate a cubului ", cub)
            return 1
        elif apartineStanga == 1:
            print("Punctul ",punct.pct, " apartine fetei din stanga a cubului ", cub)
            return 1
        elif apartineDreapta == 1:
            print("Punctul ",punct.pct, " apartine fetei din dreapta a cubului ", cub)
            return 1
        else: 
            return 0

    def calculCentruDeGreutate(self):
        #Function for determining the center of gravity for a cube
        self.centru.x = (self.puncteleCubului[0].x + self.puncteleCubului[6].x + self.puncteleCubului[5].x + self.puncteleCubului[3].x) / 4
        self.centru.y = (self.puncteleCubului[0].y + self.puncteleCubului[6].y + self.puncteleCubului[5].y + self.puncteleCubului[3].y) / 4
        self.centru.z = (self.puncteleCubului[0].z + self.puncteleCubului[6].z + self.puncteleCubului[5].z + self.puncteleCubului[3].z) / 4

    def detSistemEchivalent(self, centruCub1):
        #Function for determining if two cubes are equivalent
        if centruCub1.x >= self.puncteleCubului[4].x and centruCub1.y >= self.puncteleCubului[4].y and centruCub1.z >= self.puncteleCubului[4].z and centruCub1.x <= self.puncteleCubului[1].x and centruCub1.y <= self.puncteleCubului[1].y and centruCub1.z <= self.puncteleCubului[1].z:
            return 1
        else:
            return 0
