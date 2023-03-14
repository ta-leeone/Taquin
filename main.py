from taquin import *


    # resolution d'un taquin 3*3
taquin = Taquin(3,None)
taquin.remplir()
taquinFinal = taquin.clone()
taquin.shuffle(100)

print(taquin.__str__())
print(taquinFinal.__str__())
if taquin.isSolved(taquinFinal):
        print("Taquin resolvable")
else:
        print("Taquin non resolvable")

    # taquin.resoudre(taquinFinal)
taquinsol=taquin.solve(taquinFinal,[1,1,1,1,1,1,1,1,1])
print(taquinsol.__str__())





