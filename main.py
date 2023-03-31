
from taquin import *
import time
import sys
import os


#lecture des arguments de la ligne de commande -Ui pour user init
#  -Si pour shuffle -n pour la taille du taquin -p pour les poids
#-s 20 -n 3 -p 1,1,1,1,1,1,1,1,1,1,1,1,1


# initialiser avec une liste 
listInit=[]
boolInit=False
shuffleNumber = 0
n = 3
poids = []
if len(sys.argv) == 1:
        print("Aucun argument")
        exit(1)
else:
        
        for i in range(1,len(sys.argv)):
                if sys.argv[i] == "-Si":
                        shuffleNumber = int(sys.argv[i+1])
                elif sys.argv[i] == "-n":
                        n = int(sys.argv[i+1])
                elif sys.argv[i] == "-p":
                        temp = sys.argv[i+1].split(",")
                        poids=[]
                        print(temp)
                        for i in range(len(temp)):
                                poids.append(int(temp[i]))
                elif sys.argv[i] == "-Ui":
                        boolInit=True
                        temp = sys.argv[i+1].split(",")
                        listInit=[]
                        for i in range(len(temp)):
                                listInit.append(int(temp[i]))





if len(poids) == 0:
        for i in range(n*n):
                poids.append(1)
    # resolution d'un taquin 3*3
taquin :Taquin= Taquin(n,None)
taquin.remplir()
taquinFinal = taquin.clone()

if boolInit:
        taquin.remplirWithList(listInit)
else:
        taquin.shuffle(shuffleNumber)

print("Taquin initial")
print(taquin.__str__() )
print('-----------------------------\n')
print("Taquin final")
print(taquinFinal.__str__())



print("\n\n\t\t\t\t\tDebut resolutions ")

# for p in poids:

temps=time.time()
taquinsol:Taquin=taquin.solve(taquinFinal,poids)
time2 = time.time()
print(taquinsol.__str__())
print(" \t\t Temps de resolution : ",1000*(time2-temps),"\n\t\tNombre de coup ",taquinsol.cout())
print("-----------------------------\n")

if taquinsol.isSolved(taquinFinal):
        print("Taquin resolu")
        
        
else:
        print("Taquin non resolu")










