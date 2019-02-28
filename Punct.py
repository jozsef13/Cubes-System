
class Punct():
	
    def __init__(self):
        #The constructor for class Punct
        self.x = 0
        self.y = 0
        self.z = 0
        self.pct = "A"
        self.f = open("input.txt", "r")

    def citirePunct(self, maxLine):
        #Function for reading the coordinates x,y and z of a point
        for j in range(maxLine):
            #Here we jump in the reading file - input.txt - in order to read correctly
            whatever = self.f.readline()
        
        #Here happens the reading
        self.x = float(self.f.readline())
        self.y = float(self.f.readline())
        self.z = float(self.f.readline())

    def printPunct(self):
        #A function for printing the coorinates x,y,z of a point
        print("(", self.x, ",", self.y, ",", self.z, ")")
    


