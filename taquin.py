
import random
from structUtil import ABRt,listePriorite
from position import *





class Taquin:

    size :int
    cases:list()
    caseVide:CaseVide
    def __init__(self, size,parent:'Taquin') :
        
        self.size = size
        self.parent = parent
        self.cases = list()
       
    def taquinToInt(self):
        liste=self.TaquinToList()
        res=""
        for i in range(len(liste)):
            if liste[i]==None:
                res+="0"
            else :
                res+=str(liste[i])
        return int(res) # (1,2,3,4,5,6,7,8,9,0) => 1234567890
                         # (1,2,3,4,5,6,7,8,0,9) => 1234567809


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
    def cheminSuivi(self):
        chemin=""
        if self.parent==None:
            return ""
        else:
            #parent present
            x,y=self.caseVide.getPositionX(),self.caseVide.getPositionY()
            if self.parent.caseVide.getPositionX()<x:
                chemin=self.parent.cheminSuivi()+"S"
            elif self.parent.caseVide.getPositionX()>x:
                chemin=self.parent.cheminSuivi()+"N"
            elif self.parent.caseVide.getPositionY()<y:
                chemin=self.parent.cheminSuivi()+"E"
            elif self.parent.caseVide.getPositionY()>y:
                chemin=self.parent.cheminSuivi()+"W"
            return chemin


    def remplirWithList(self,liste:list):
        self.cases=list()
        self.parent=None#remplir avec une liste signifie aucun parent 
        z=0
        for i in range(self.size):
            self.cases.append(list())
            for j in range(self.size):
                if(liste[z]==None or liste[z]==0):
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
                j=liste.index(value)#on recupere la position de la valeur dans la liste
                value2=liste[listeResult.index(value)]  # (1,2,3,4,5,6,7,8,9) // result (1,2,3,4,5,6,7,8,9)
                liste[listeResult.index(value)]=value#j=6 ,  value2=7 ,  index(5) <- 6,  index(6) <- 7
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
            #permuter dans le taquin 
            self.cases[x][y]=self.cases[x2][y2]
            self.cases[x2][y2]=self.caseVide
            #permuter dans les cases
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

    def distmanhattan(self, taquinFinal:'Taquin',i:int,j:int) :
        
        c :CaseVide=self.cases[i][j]
        
        cFinal=taquinFinal.getCasebV(c.getValue())
        return abs(c.getPositionX()- cFinal.getPositionX()) + abs(c.getPositionY() - cFinal.getPositionY())
        
   

   
    def shuffle(self, nbMoves:int):
        for i in range(nbMoves):
           
            dir=random.choice(["N", "S", "E", "W"])
            self.movebyPermut(dir)

    def HeuristiqueNew(self,taquinFinal:'Taquin',i:int,j:int):
        c :CaseVide=self.cases[i][j]
        cFinal=taquinFinal.getCasebV(c.getValue())

        dism= 3*(abs(c.getPositionX()- cFinal.getPositionX()) + abs(c.getPositionY() - cFinal.getPositionY())) 
        cFinal=taquinFinal.getCasebV(None)
        disANone= abs(c.getPositionX()- cFinal.getPositionX()) + abs(c.getPositionY() - cFinal.getPositionY())
        if disANone==0:
            return dism-2
        return dism+disANone

  
    def heuristiquePondere(self,taquinFinal:'Taquin',poids:list(),coefNormalisation:int):
        res=0
        
        for i in range(self.size):
            for j in range(self.size):
                if(self.cases[i][j].getValue() != None):#case vide non prise en compte 
                 res+=self.distmanhattan(taquinFinal,i,j)*poids[self.cases[i][j].getValue()-1]
        return res/coefNormalisation

    def fnctEval(self,taquinFinal:'Taquin',poids:list(),coefNormalisation :int ):#f=g+hs
        return self.heuristiquePondere(taquinFinal,poids,coefNormalisation)+self.cout()

   
    def compareTo(self, taquin:'Taquin',taquinFinal:'Taquin',poids:list(),coefNormalisation :int) :
        return self.fnctEval(taquinFinal,poids,coefNormalisation) - taquin.fnctEval(taquinFinal,poids,coefNormalisation)
    
    
    def solve(self, taquinFinal:'Taquin',poids:list(),coefNormalisation :int) :
        if self.isSolvable(taquinFinal):
            entier =0
            openList = listePriorite(taquinFinal,poids,coefNormalisation)
            closedList:ABRt=None
            openList.insertTaquin(self)
            while not openList.isEmpty():
            
                    current:Taquin = openList.pop()
                    if closedList==None:
                        closedList=ABRt(current)
                    else:
                        closedList.insert(current)
                    if current.isSolved(taquinFinal):
                        print("\t\tnombre de taquin parcouru : ",entier)
                        return current
                    
                    for dir in ["N", "S", "E", "W"]:
                    
                        
                            v=current.clone()
                            
                            if v.movebyPermut(dir):#si le taquin est bien déplacé
                                    entier +=1
                                    if not closedList.contains(v):    #si le taquin n'est pas dans la liste fermée
                                            notdoubleM=True
                                            for c in openList.liste:#
                                                    if  v.eg(c) :
                                                        if v.cout()>=c.cout():
                                                            notdoubleM=False
                                                        if  v.cout()<c.cout():
                                                            openList.remove(c)
                                        
                                            if notdoubleM:#
                                                    openList.insertTaquin(v)
                                
                    
        else:
            print("le taquin n'est pas solvable")
            return None
    def eg(self, t) -> bool:
        
       return self.size==t.size and self.isSolved(t)
    

    def __eq__(self, t) -> bool:
        if isinstance(t,Taquin):
            if isinstance(self,Taquin):
                return self.taquinToInt()==t.taquinToInt()
        return False




