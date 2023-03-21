import random


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
    taquin:"Taquin"
    value:int
    def __init__(self, position, taquin) :
        self.position = position
        self.taquin = taquin
        self.value =None


    def getPositionX(self) :
        return self.position.getX()
    def setPositionX(self, positionX) :
        self.position.setX(positionX)

    def getPositionY(self) :
        return self.position.getY()
    def setPositionY(self, positionY) :
        self.position.setY(positionY)

    def getTaquin(self) :
        return self.taquin
    def setTaquin(self, taquin) :
        self.taquin = taquin
    def getValue(self) :
        return None
    def setValue(self, value) :
        pass
    def clone(self,taq):
        return CaseVide(self.position, taq)
    def moveNorth(self)->bool:
            if self.position.getX() > 0 :
                descendre=self.taquin.getCase(self.position.getX() - 1, self.position.getY())
                descendre.setPositionX(self.position.getX())
                self.position.setX(self.position.getX() - 1)
                self.taquin.setCase(self.position.getX(), self.position.getY(), self)
                self.taquin.setCase(descendre.getPositionX(), descendre.getPositionY(), descendre)
                return True
            else:
                return False
    def moveSouth(self)->bool:
        
           
            
              if self.position.getX() < self.taquin.getSize() - 1 :
                monter=self.taquin.getCase(self.position.getX() + 1, self.position.getY())
                monter.setPositionX(self.position.getX())
                self.position.setX(self.position.getX() + 1)
                self.taquin.setCase(self.position.getX(), self.position.getY(), self)
                self.taquin.setCase(monter.getPositionX(), monter.getPositionY(), monter)
                return True
              else:
                return False
    def moveEast(self)->bool:
       
           if self.position.getY() < self.taquin.getSize() - 1 :
                droite=self.taquin.getCase(self.position.getX(), self.position.getY() + 1)
                droite.setPositionY(self.position.getY())
                self.position.setY(self.position.getY() + 1)
                self.taquin.setCase(self.position.getX(), self.position.getY(), self)
                self.taquin.setCase(droite.getPositionX(), droite.getPositionY(), droite)
                return True
           else:
                return False
    def moveWest(self)->bool:
        
            if self.position.getY() > 0 :
               
                gauche=self.taquin.getCase(self.position.getX(), self.position.getY() - 1)
                gauche.setPositionY(self.position.getY())
                self.position.setY(self.position.getY() - 1)
                self.taquin.setCase(self.position.getX(), self.position.getY(), self)
                self.taquin.setCase(gauche.getPositionX(), gauche.getPositionY(), gauche)
                return True
            else:
                return False


    def __eq__(self, __o: object) -> bool:
        return self.position.__eq__(__o.position)and self.value.__eq__(__o.value)


class Case(CaseVide):
    
    
   
    def __init__(self, value, position, taquin) :
        self.value = value
        self.position = position
        self.taquin = taquin

    def getValue(self) :
        return self.value
    def setValue(self, value) :
        self.value = value

    def moveNorth(self)->bool:
         print("case")
         return False
    def moveSouth(self)->bool:
         print("case")
         return False
    def moveEast(self)->bool:
         print("case")
         return False
    def moveWest(self)->bool:
         print("case")
         return False
    def clone(self,taq):
        return Case(self.value, self.position.clone(), taq)
    def __eq__(self, __o: object) -> bool:
        return super().__eq__(__o)






class listePriorite:
    def __init__(self,taquinFinal:'Taquin',poids):
        self.liste = []
        self.taquinFinal=taquinFinal
        self.poids=poids
    def insertTaquin(self, element:'Taquin'):
        if len(self.liste) == 0:
            self.liste.append(element)
        else:
            for i in range(len(self.liste)):
               
                if element.compareTo(self.liste[i],self.taquinFinal,self.poids)<0:#element.comparator() - self.liste[i].comparator()<0
                    self.liste.insert(i, element)
                    break
                elif i == len(self.liste) - 1:
                    self.liste.append(element)
                    break
    def pop(self):
        return self.liste.pop(0)
    def isEmpty(self):
        return len(self.liste) == 0
    def remove(self,element):
        self.liste.remove(element)


    



class Taquin:
    size :int
    cases:list()
    caseVide:CaseVide
    def __init__(self, size,parent:'Taquin') :
        
        self.size = size
        self.parent = parent
        self.cases = list()
       

    def remplir(self):
        z=0
        for i in range(self.size):
            self.cases.append(list())
            for j in range(self.size):
                if(j==self.size-1 and i==self.size-1):
                    self.caseVide=CaseVide(Position(i, j), self)
                    self.cases[i].append(self.caseVide)
                    
                    break
                self.cases[i].append(Case(z,Position(i, j), self))
                z+=1
   
    def clone(self ):
        taquin=Taquin(self.size,self.parent)

        for i in range(self.size):
            taquin.cases.append([])
            for j in range(self.size):
                cc=self.cases[i][j].clone(taquin)
                taquin.cases[i].append(cc)
                if taquin.cases[i][j].getValue() == None:
                    taquin.caseVide = taquin.cases[i][j]
        return taquin
        

    def getSize(self) :
        return self.size
    
    def getCase(self, x, y) :
        return self.cases[x][y]
    def getCasebV(self,val):
        for i in range(self.size):
            for j in range(self.size):
                if self.cases[i][j].getValue() == val:
                    return self.cases[i][j]
                
    def setCase(self, x, y, case) :
        self.cases[x].remove(self.cases[x][y])
        self.cases[x].insert(y, case)
    def getCaseVide(self) :
        return self.caseVide
    def getParent(self) :
        return self.parent
    def setParent(self, parent) :
        self.parent = parent
    def cout(self):
        if self.parent == None:
            return 0
        return self.parent.cout()+1#fonction g
    
    def move(self, direction) :
        moved:Taquin=self.clone()
        
        if (direction == "N"):
            if moved.getCaseVide().moveNorth():
                moved.setParent(self)
                return moved
        if (direction == "S"):
            if moved.caseVide.moveSouth():
                moved.setParent(self)
                return moved
        if (direction == "E"):
            if moved.caseVide.moveEast():
                moved.setParent(self)
                return moved
        if (direction == "W"):
            if moved.caseVide.moveWest():
                moved.setParent(self)
                return moved
            
        return None



      
    
    def isSolved(self,taquinFinal:'Taquin') :
        for i in range(self.size):
            for j in range(self.size):
                if self.cases[i][j].getValue() != taquinFinal.cases[i][j].getValue():
                    return False
        return True
    
    def __str__(self) :
        res = ""
        for i in range(self.size):
            for j in range(self.size):
                res += str(self.cases[i][j].getValue()) + " "
            res += "\n"

        return res
    def aff(self) :
        res = ""
        for i in range(self.size):
            for j in range(self.size):
                res += str(self.getCase(i,j).getValue()) + " "
            res += "\n"

        return res
    
    
    
    def distmanhattan(self, taquinFinal:'Taquin',i:int,j:int) :
        
        c :CaseVide=self.cases[i][j]
        if c.getValue() != None:
                    cFinal=taquinFinal.getCasebV(c.getValue())
                    return abs(c.getPositionX()- cFinal.getPositionX()) + abs(c.getPositionY() - cFinal.getPositionY())
        return 0#A revoir pour la case vide
   
   
   
    def shuffle(self, nbMoves:int):
        for i in range(nbMoves):
            dir=random.choice(["N", "S", "E", "W"])
            if (dir == "N"):
                 self.getCaseVide().moveNorth()
            if (dir == "S"):
                    self.getCaseVide().moveSouth()
            if (dir == "E"):
                    self.getCaseVide().moveEast()
            if (dir == "W"):
                    self.getCaseVide().moveWest()
               
            


    def heuristiquePondere(self,taquinFinal:'Taquin',poids:list()):
        res=0
        for i in range(self.size):
            for j in range(self.size):
                if(self.cases[i][j].getValue() != None):
                 res+=self.distmanhattan(taquinFinal,i,j)*poids[self.cases[i][j].getValue()]
        return res
    def fnctEval(self,taquinFinal:'Taquin',poids:list()):
        return self.heuristiquePondere(taquinFinal,poids)+self.cout()

   
    def compareTo(self, taquin:'Taquin',taquinFinal:'Taquin',poids:list()) :
        return self.fnctEval(taquinFinal,poids) - taquin.fnctEval(taquinFinal,poids)
    
    
    def solve(self, taquinFinal:'Taquin',poids:list()) :
        openList = listePriorite(taquinFinal,poids)
        closedList = listePriorite(taquinFinal,poids)
        openList.insertTaquin(self)
        while not openList.isEmpty():
           
            current:Taquin = openList.pop()
           
            if current.isSolved(taquinFinal):
                return current
            
            for direction in ["N", "S", "E", "W"]:
                
               v:Taquin = current.move(direction)
               if v!=None:
                print(v.aff())
                
                stop=False
                for c in closedList.liste:
                    if  v.eg(c):#si le taquin est deja dans la liste fermée
                        stop=True
                if not stop:    #si le taquin n'est pas dans la liste fermée
                        notdoubleM=True
                        for c in openList.liste:#
                            if  v.eg(c) and v.cout()>=c.cout():#
                                notdoubleM=False
                            if  v.eg(c) and v.cout()<c.cout():
                                openList.remove(c)
                       
                        if notdoubleM:#
                                openList.insertTaquin(v)
                           
            closedList.insertTaquin(current)
        return None
    
    

    def eg(self, t: 'Taquin') -> bool:
        
            if self.size==t.size:
                
                for i in range (self.size):
                    for j in range (self.size):
                        if  self.getCase(i,j).getValue()!=t.getCase(i,j).getValue():
                            return False
                
                return True
            return False
