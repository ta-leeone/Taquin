import random
from time import sleep


class Case:
    taquin:"Taquin"
    value:int
    x:int
    y:int
    def __init__(self, x,y,value, taquin) :
        self.x = x
        self.y = y
        self.value = value
        self.taquin = taquin
        


    def getPositionX(self) :
        return self.x
    def setPositionX(self, positionX) :
        self.x = positionX

    def getPositionY(self) :
        return self.y
    def setPositionY(self, positionY) :
        self.x = positionY

    def getValue(self) :
        return self.value

   
    def clone(self,taq):
        return Case(self.x,self.y,self.value ,taq)
    def __eq__(self, __o: object) -> bool:
        return super().__eq__(__o)

class Taquin:
    size :int
    cases:list()
    
    def __init__(self, size,parent:'Taquin') :
        
        self.size = size
        self.parent = parent
        self.cases = list()
       

    def remplir(self):
        z=1
        for i in range(self.size):
            self.cases.append(list())
            for j in range(self.size):
                if(z==self.size*self.size):
                    self.cases[i].append(Case(i, j,None, self))
                    
                else:
                    self.cases[i].append(Case(i, j, z,self))
                    z+=1
   
    def clone(self ):
        taquin=Taquin(self.size,self)#lien de parente ici !
        for i in range(self.size):
            taquin.cases.append([])
            for j in range(self.size):
                cc=self.cases[i][j].clone(taquin)
                taquin.cases[i].append(cc)         
        return taquin
        

    def getSize(self) :
        return self.size
    def getCase(self, x, y) :
        return self.cases[x][y]
 
                
    def setCase(self, x, y, case) :
        self.cases[x][y] = case
    
    def getcaseVide(self) :
        case=None
        for i in range(self.size):
            for j in range(self.size):
                if(self.cases[i][j].getValue()==None):
                    case= self.cases[i][j]
                    return case
        

  
            
       

#fonction permut (case1,case2 )pour permuter 2 cases d'une matrice
    def movebyPermut(self,direction)->bool:

        caseVide=self.getcaseVide()
        if (direction == "N"):
          if caseVide.getPositionX() > 0 :
            x=caseVide.getPositionX()
            y=caseVide.getPositionY()
            x2=x-1
            y2=y
            self.cases[x][y]=self.cases[x2][y2]
            self.cases[x2][y2]=caseVide
            self.cases[x2][y2].setPositionX(x2)
            self.cases[x2][y2].setPositionY(y2)
            self.cases[x][y].setPositionX(x)
            self.cases[x][y].setPositionY(y)
            return True
        else :
            if(direction == "S"):
                if caseVide.getPositionX() < self.size-1 :
                    x=caseVide.getPositionX()
                    y=caseVide.getPositionY()
                    x2=x+1
                    y2=y
                    self.cases[x][y]=self.cases[x2][y2]
                    self.cases[x2][y2]=caseVide
                    self.cases[x2][y2].setPositionX(x2)
                    self.cases[x2][y2].setPositionY(y2)
                    self.cases[x][y].setPositionX(x)
                    self.cases[x][y].setPositionY(y)
                    return True
            else :
                if (direction == "E"):
                    if caseVide.getPositionY() < self.size-1 :
                        x=caseVide.getPositionX()
                        y=caseVide.getPositionY()
                        x2=x
                        y2=y+1
                        self.cases[x][y]=self.cases[x2][y2]
                        self.cases[x2][y2]=caseVide
                        self.cases[x2][y2].setPositionX(x2)
                        self.cases[x2][y2].setPositionY(y2)
                        self.cases[x][y].setPositionX(x)
                        self.cases[x][y].setPositionY(y)
                        return True
                else :
                    if (direction == "W"):
                        if caseVide.getPositionY() > 0 :
                            x=caseVide.getPositionX()
                            y=caseVide.getPositionY()
                            x2=x
                            y2=y-1
                            self.cases[x][y]=self.cases[x2][y2]
                            self.cases[x2][y2]=caseVide
                            self.cases[x2][y2].setPositionX(x2)
                            self.cases[x2][y2].setPositionY(y2)
                            self.cases[x][y].setPositionX(x)
                            self.cases[x][y].setPositionY(y)
                            return True
        return False

    def afficherTaquin(self):
        for i in range(self.size):
            for j in range(self.size):
                
                    print(self.cases[i][j].getValue(),end=" ")
            print()

   
  
   

t:Taquin = Taquin(3,None)
t.remplir()
t.afficherTaquin()
v=t.clone()
v.afficherTaquin()
print(t.getcaseVide())
t.movebyPermut("W")
v=t.clone()
v.afficherTaquin()
v.movebyPermut("W")
c=v.clone()
c.afficherTaquin()

# problemme resolu !
                        

   

