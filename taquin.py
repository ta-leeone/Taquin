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
    def moveNorth(self)->bool:#avec setCaseInsert et getCaseRmove
            if self.position.getX() > 0 :
                descendre=self.taquin.getCaseRemove(self.position.getX() - 1, self.position.getY())
                casevide=self.taquin.getCaseRemove(self.position.getX(), self.position.getY())
                descendre.setPositionX(self.position.getX())
                self.position.setX(self.position.getX() - 1)
                
                self.taquin.setCaseInsert(descendre.getPositionX(), descendre.getPositionY(), descendre)
                self.taquin.setCaseInsert(casevide.position.getX(), casevide.position.getY(), self)
                return True
            else:
                return False
    def moveSouth(self)->bool:
        
           
            
              if self.position.getX() < self.taquin.getSize() - 1 :
                monter=self.taquin.getCaseRemove(self.position.getX() + 1, self.position.getY())
                casevide=self.taquin.getCaseRemove(self.position.getX(), self.position.getY())
                monter.setPositionX(self.position.getX())
                self.position.setX(self.position.getX() + 1)
                
                self.taquin.setCaseInsert(monter.getPositionX(), monter.getPositionY(), monter)
                self.taquin.setCaseInsert(casevide.position.getX(), casevide.position.getY(), self)
                return True
              else:
                return False
    def moveEast(self)->bool:
       
           if self.position.getY() < self.taquin.getSize() - 1 :
                droite=self.taquin.getCase(self.position.getX(), self.position.getY() + 1)
                droite.setPositionY(self.position.getY())
                self.position.setY(self.position.getY() + 1)
               
                self.taquin.setCase(droite.getPositionX(), droite.getPositionY(), droite)
                self.taquin.setCase(self.position.getX(), self.position.getY(), self)
                return True
           else:
                return False
    def moveWest(self)->bool:
        
            if self.position.getY() > 0 :
               
                gauche=self.taquin.getCase(self.position.getX(), self.position.getY() - 1)
                gauche.setPositionY(self.position.getY())
                self.position.setY(self.position.getY() - 1)
                
                self.taquin.setCase(gauche.getPositionX(), gauche.getPositionY(), gauche)
                self.taquin.setCase(self.position.getX(), self.position.getY(), self)
                return True
            else:
                return False


    

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
                    
                else:
                    self.cases[i].append(Case(z,Position(i, j), self))
                    z+=1
   
    def clone(self ):
        taquin=Taquin(self.size,self.parent)

        for i in range(self.size):
            taquin.cases.append([])
            for j in range(self.size):
                cc=self.cases[i][j].clone(taquin)
                taquin.cases[i].append(cc)
        c=0
        for i in range(self.size):
            for j in range(self.size):
                if taquin.cases[i][j].getValue()==None:
                    taquin.caseVide=taquin.cases[i][j]
                    c+=1
        if c!=1:
            print("erreur")
                
        return taquin
        

    def getSize(self) :
        return self.size
    def getCaseRemove(self, x, y) :
        return self.cases[x].pop(y)
    def getCase(self, x, y) :
        return self.cases[x][y]
    def getCasebV(self,val):
        for i in range(self.size):
            for j in range(self.size):
                if self.cases[i][j].getValue() == val:
                    return self.cases[i][j]
                
    def setCase(self, x, y, case) :
        self.cases[x][y] = case
    def setCaseInsert(self, x, y, case) :
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
        moved.setParent(self)
        
        if (direction == "N"):
             moved.getCaseVide().moveNorth()
                       
        if (direction == "S"):
             moved.caseVide.moveSouth()
                
                
        if (direction == "E"):
             moved.caseVide.moveEast()
               
                
        if (direction == "W"):
             moved.caseVide.moveWest()
              
        return moved
            
       

#fonction permut (case1,case2 )pour permuter 2 cases d'une matrice
    def movebyPermut(self,direction):

        moved:Taquin=self.clone()
        moved.setParent(self)
        if (direction == "N"):
          if self.caseVide.position.getX() > 0 :
            x=moved.caseVide.getPositionX()
            y=moved.caseVide.getPositionY()
            x2=x-1
            y2=y
            moved.cases[x][y]=moved.cases[x2][y2]
            moved.cases[x2][y2]=moved.caseVide
            moved.caseVide.setPositionX(x2)
            moved.caseVide.setPositionY(y2)
            moved.cases[x][y].setPositionX(x)
            moved.cases[x][y].setPositionY(y)
            return moved
        if (direction == "S"):
            if self.caseVide.position.getX() < self.size-1 :
                x=moved.caseVide.getPositionX()
                y=moved.caseVide.getPositionY()
                x2=x+1
                y2=y
                moved.cases[x][y]=moved.cases[x2][y2]
                moved.cases[x2][y2]=moved.caseVide
                moved.caseVide.setPositionX(x2)
                moved.caseVide.setPositionY(y2)
                moved.cases[x][y].setPositionX(x)
                moved.cases[x][y].setPositionY(y)
                return moved
        if (direction == "E"):
            if self.caseVide.position.getY() < self.size-1 :
                x=moved.caseVide.getPositionX()
                y=moved.caseVide.getPositionY()
                x2=x
                y2=y+1
                moved.cases[x][y]=moved.cases[x2][y2]
                moved.cases[x2][y2]=moved.caseVide
                moved.caseVide.setPositionX(x2)
                moved.caseVide.setPositionY(y2)
                moved.cases[x][y].setPositionX(x)
                moved.cases[x][y].setPositionY(y)
                return moved
        if (direction == "W"):
            if self.caseVide.position.getY() > 0 :
                x=moved.caseVide.getPositionX()
                y=moved.caseVide.getPositionY()
                x2=x
                y2=y-1
                moved.cases[x][y]=moved.cases[x2][y2]
                moved.cases[x2][y2]=moved.caseVide
                moved.caseVide.setPositionX(x2)
                moved.caseVide.setPositionY(y2)
                moved.cases[x][y].setPositionX(x)
                moved.cases[x][y].setPositionY(y)
                return moved
        return moved


      
    
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

        res+="\n x"+str(self.caseVide.getPositionX())+" y"+str(self.caseVide.getPositionY())+"\n"
        return res
   
    
    
    def distmanhattan(self, taquinFinal:'Taquin',i:int,j:int) :
        
        c :CaseVide=self.cases[i][j]
        if c.getValue() != None:
                    cFinal=taquinFinal.getCasebV(c.getValue())
                    return abs(c.getPositionX()- cFinal.getPositionX()) + abs(c.getPositionY() - cFinal.getPositionY())
        return 0#A revoir pour la case vide
   
    def oppositeDirection(self, direction):
        if direction == "N":
            return "S"
        if direction == "S":
            return "N"
        if direction == "E":
            return "W"
        if direction == "W":
            return "E"
        
   
    def shuffle(self, nbMoves:int):
        for i in range(nbMoves):
            print(self.__str__() + "\n")
            dir=random.choice(["N", "S", "E", "W"])
            self=self.movebyPermut(dir)
               
            


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
            
            for dir in ["N", "S", "E", "W"]:
               v:Taquin = current.movebyPermut(dir)
               
               
               
               if v!=None:
                print(v.__str__())
                
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
