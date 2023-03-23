from taquin import *


    # resolution d'un taquin 3*3
taquin = Taquin(3,None)
taquin.remplir()
taquinFinal = taquin.clone()
taquin.shuffle(10)
poids=[1,1,1,1,1,1,1,1,1]
print(taquin.__str__() )
print (taquinFinal.__str__())

if (taquin.isSolved(taquinFinal) ):
        print("Taquin resolu")
else:
        print("Taquin non resolu")


        taquinsol:Taquin=taquin.solve(taquinFinal,poids)
        
        print(taquinsol.__str__())
        print(taquinsol.cout())
        if taquinsol.isSolved(taquinFinal):
                print("Taquin resolu")
                print(taquinsol.__str__())
        else:
                print("Taquin non resolu")










