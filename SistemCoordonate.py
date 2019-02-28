import Punct

class SistemCoordonate():
    def __init__(self, x):
        #The constructor for class SistemCoordonate
        self.puncte = [Punct.Punct() for i in range(x)]

    def addPuncte(self, x, maxLine):
        #Function for adding a point in the system of coordinates xyz
        if x != 0:
            for i in range(x):
                for j in range(i):
                    self.puncte[i].pct = chr(ord(self.puncte[i].pct) + 1) #Here are the letters for the points
                self.puncte[i].citirePunct(maxLine) #Here we read the coordinates
                #maxLine is for jumping in the reading file - input.txt
                maxLine = maxLine + 3

    def printPuncte(self, x):
        #Function for printing the points
        for i in range(x):
            if i == 0:
                print("Punctul ", self.puncte[i].pct, " - punctul de plecare")
            elif i == x-1:
                print("Punctul ", self.puncte[i].pct, " - punctul de sosire")
            else:
                print("Punctul ", self.puncte[i].pct)
            self.puncte[i].printPunct()

