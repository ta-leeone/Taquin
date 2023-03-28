
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
        z=1
        for i in range(self.size):
            self.cases.append(list())
            for j in range(self.size):
                if(j==self.size-1 and i==self.size-1):
                    self.caseVide=CaseVide(Position(i, j))
                    self.cases[i].append(self.caseVide)
                    
                else:
                    self.cases[i].append(Case(z,Position(i, j)))
                    z+=1
    def remplirWithList(self,liste:list):
        self.cases=list()
        self.parent=None#remplir avec une liste signifie aucun parent 
        z=0
        for i in range(self.size):
            self.cases.append(list())
            for j in range(self.size):
                if(liste[z]==None):
                    self.caseVide=CaseVide(Position(i, j))
                    self.cases[i].append(self.caseVide)
                    z=z+1
                    
                else:
                    self.cases[i].append(Case(liste[z],Position(i, j)))
                    z+=1
    def TaquinToList(self):
        liste=[]
        for i in range(self.size):
            for j in range(self.size):
                liste.append(self.cases[i][j].getValue())
        return liste
    
    def isSolvable(self,taquinFinal):
        liste=self.TaquinToList()
        listeResult=taquinFinal.TaquinToList()
        inversions = 0
        for i in range(1,self.size*self.size):
            value=i
            
            if not liste.index(value)==listeResult.index(value) :
                inversions += 1
                j=liste.index(value)
                value2=liste[listeResult.index(value)]   
                liste[listeResult.index(value)]=value
                liste[j]=value2

        return inversions % 2 == self.distmanhattan(taquinFinal,self.caseVide.getPositionX(),self.caseVide.getPositionY()) % 2               
                
    def clone(self ):
        taquin=Taquin(self.size,self)#lien de parente ici !

        for i in range(self.size):
            taquin.cases.append([])
            for j in range(self.size):
                cc=self.cases[i][j].clone()
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

    def getCase(self, x, y) :
        return self.cases[x][y]
    def getCasebV(self,val):
        for i in range(self.size):
            for j in range(self.size):
                if self.cases[i][j].getValue() == val:
                    return self.cases[i][j]
                
    def setCase(self, x, y, case) :
        self.cases[x][y] = case


    def cout(self):
        if self.parent == None:
            return 0
        return self.parent.cout()+1#fonction g

            
       

#fonction permut (case1,case2 )pour permuter 2 cases d'une matrice
    def movebyPermut(self,direction)->bool:

        
        if (direction == "N"):
          if self.caseVide.position.getX() > 0 :
            x=self.caseVide.getPositionX()
            y=self.caseVide.getPositionY()
            x2=x-1
            y2=y
            self.cases[x][y]=self.cases[x2][y2]
            self.cases[x2][y2]=self.caseVide
            self.cases[x2][y2].setPositionX(x2)
            self.cases[x2][y2].setPositionY(y2)
            self.cases[x][y].setPositionX(x)
            self.cases[x][y].setPositionY(y)
            return True
        else :
            if(direction == "S"):
                if self.caseVide.position.getX() < self.size-1 :
                    x=self.caseVide.getPositionX()
                    y=self.caseVide.getPositionY()
                    x2=x+1
                    y2=y
                    self.cases[x][y]=self.cases[x2][y2]
                    self.cases[x2][y2]=self.caseVide
                    self.cases[x2][y2].setPositionX(x2)
                    self.cases[x2][y2].setPositionY(y2)
                    self.cases[x][y].setPositionX(x)
                    self.cases[x][y].setPositionY(y)
                    return True
            else :
                if (direction == "E"):
                    if self.caseVide.position.getY() < self.size-1 :
                        x=self.caseVide.getPositionX()
                        y=self.caseVide.getPositionY()
                        x2=x
                        y2=y+1
                        self.cases[x][y]=self.cases[x2][y2]
                        self.cases[x2][y2]=self.caseVide
                        self.cases[x2][y2].setPositionX(x2)
                        self.cases[x2][y2].setPositionY(y2)
                        self.cases[x][y].setPositionX(x)
                        self.cases[x][y].setPositionY(y)
                        return True
                else :
                    if (direction == "W"):
                        if self.caseVide.position.getY() > 0 :
                            x=self.caseVide.getPositionX()
                            y=self.caseVide.getPositionY()
                            x2=x
                            y2=y-1
                            self.cases[x][y]=self.cases[x2][y2]
                            self.cases[x2][y2]=self.caseVide
                            self.cases[x2][y2].setPositionX(x2)
                            self.cases[x2][y2].setPositionY(y2)
                            self.cases[x][y].setPositionX(x)
                            self.cases[x][y].setPositionY(y)
                            return True
        return False


      
    
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
                res += str(self.cases[i][j].getValue()) +" |"
            
            res += "\n"
            for j in range(self.size):
                res += "----"    
            res += "\n"

        return res
   
    
    
    def distmanhattan(self, taquinFinal:'Taquin',i:int,j:int) :
        
        c :CaseVide=self.cases[i][j]
        
        cFinal=taquinFinal.getCasebV(c.getValue())
        return abs(c.getPositionX()- cFinal.getPositionX()) + abs(c.getPositionY() - cFinal.getPositionY())
        
   

   
    def shuffle(self, nbMoves:int):
        for i in range(nbMoves):
           
            dir=random.choice(["N", "S", "E", "W"])
            self.movebyPermut(dir)
    def disYoucef(self,taquinFinal:'Taquin',i:int,j:int):
        c :CaseVide=self.cases[i][j]
        cFinal=taquinFinal.getCasebV(c.getValue())

        dism= 3*(abs(c.getPositionX()- cFinal.getPositionX()) + abs(c.getPositionY() - cFinal.getPositionY())) 
        cFinal=taquinFinal.getCasebV(None)
        disANone= abs(c.getPositionX()- cFinal.getPositionX()) + abs(c.getPositionY() - cFinal.getPositionY())
        if disANone==0:
            return dism-2
        return dism+disANone

  
    def heuristiquePondere(self,taquinFinal:'Taquin',poids:list()):
        res=0
        for i in range(self.size):
            for j in range(self.size):
                if(self.cases[i][j].getValue() != None):#case vide non prise en compte 
                 res+=self.disYoucef(taquinFinal,i,j)*poids[self.cases[i][j].getValue()]
        return res
    def fnctEval(self,taquinFinal:'Taquin',poids:list()):
        return self.heuristiquePondere(taquinFinal,poids)+self.cout()

   
    def compareTo(self, taquin:'Taquin',taquinFinal:'Taquin',poids:list()) :
        return self.fnctEval(taquinFinal,poids) - taquin.fnctEval(taquinFinal,poids)
    
    
    def solve(self, taquinFinal:'Taquin',poids:list()) :
        openList = listePriorite(taquinFinal,poids)
        closedList = []
        openList.insertTaquin(self)
        while not openList.isEmpty():
           
            current:Taquin = openList.pop()
           
            if current.isSolved(taquinFinal):
                print("\t\tnombre de taquin parcouru : ",len(closedList))
                return current
            
            for dir in ["N", "S", "E", "W"]:
           
               
               v=current.clone()
               
               if v.movebyPermut(dir):#si le taquin est bien déplacé
               
                stop=False
                for c in closedList:
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
                           
            closedList.append(current)
        return None
    
    

    def eg(self, t) -> bool:

            return  self.size==t.size and self.isSolved(t)




