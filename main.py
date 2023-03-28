import datetime
from taquin import *
import time


    # resolution d'un taquin 3*3
taquin = Taquin(3,None)
taquin.remplir()
taquinFinal = taquin.clone()
#taquin.remplirWithList([5 ,2 ,3  ,4 ,1 ,6 ,7 ,8,None])

taquin.shuffle(50)
#definition d'un array 6*9
poids =         [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                 [800,400,400,
                  400,300,300,
                  400,300,200,
                  220,
                  400,220,199,129,109,
                  300,180,99,55,55,
                  220,120,99,45,0,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0],
                 [8,7,6,5,3,2,4,1,0,2,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0],
                 [8,7,6,5,4,3,2,1,0,3,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0],
                 [8,7,6,5,4,3,2,1,0,4,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0],
                 [36,12,12,4,1,1,4,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0]    
                 ]



print(taquin.__str__() )
# print if solvable
if taquin.isSolvable(taquinFinal):
        print("Taquin solvable")
else:
        print("Taquin non solvable")
        exit()
      

if (taquin.isSolved(taquinFinal) ):
        print("Taquin resolu")
else:
        print("\t\t\t\tDebut resolutions ")
        taquinsol:Taquin=taquin.clone()
        for p in poids:
                        print("\t\tEssaye de la strategie ",poids.index(p))
                        temps=time.time()
                        taquinsol:Taquin=taquin.solve(taquinFinal,p)
                        time2 = time.time()
                        print(taquinsol.__str__())
                        print(" \t\tTemps de resolution : ",1000*(time2-temps),"\n\t\tNombre de coup ",taquinsol.cout())
                        print("-----------------------------\n")
        
        if taquinsol.isSolved(taquinFinal):
                print("Taquin resolu")
                
               
        else:
                print("Taquin non resolu")










