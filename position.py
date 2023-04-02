
class Position :
     x :int 
     y :int 
     def __init__(self, x, y) :
        self.x = x
        self.y = y

     def getX(self) :
        return self.x
     def getY(self) :
        return self.y
     def setX(self, x) :
        self.x = x
     def setY(self, y) :
        self.y = y
     def clone(self):
            return Position(self.x, self.y)




class CaseVide:
    Position:Position
    value:int
    def __init__(self, position) :
        self.position = position
        self.value =None


    def getPositionX(self) :
        return self.position.getX()
    def setPositionX(self, positionX) :
        self.position.setX(positionX)

    def getPositionY(self) :
        return self.position.getY()
    def setPositionY(self, positionY) :
        self.position.setY(positionY)


    def getValue(self) :
        return None
   
    def clone(self):
        return CaseVide(self.position.clone())
    




class Case(CaseVide):
    
    
   
    def __init__(self, value, position) :
        self.value = value
        self.position = position


    def getValue(self) :
        return self.value
    def setValue(self, value) :
        self.value = value

    def clone(self):
        return Case(self.value, self.position.clone())




