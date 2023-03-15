from taquin import *


    # resolution d'un taquin 3*3
taquin = Taquin(3,None)
taquin.remplir()
taquinFinal = taquin.clone()
print(taquin.__str__())
taquin.shuffle(3)

print(taquin.__str__())
print(taquinFinal.__str__())
if taquin.isSolved(taquinFinal):
        print("Taquin resolu")
else:
        print("Taquin non resolu")

    # taquin.resoudre(taquinFinal)
taquinsol=taquin.solve(taquinFinal,[1,1,1,1,1,1,1,1,1])
print(taquinsol.__str__())

if taquinsol.isSolved(taquinFinal):
        print("Taquin resolu")
else:
        print("Taquin non resolu")






