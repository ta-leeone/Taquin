from taquin import *


    # resolution d'un taquin 3*3
taquin = Taquin(3,None)
taquin.remplir()
taquinFinal = taquin.clone()

taquin.shuffle(100)
print('Testing')
print(taquin.__str__())
print("-----------------------------------------")
print(taquinFinal.__str__())

print("-----------------------------------------")

print("-----------------------------------------")

print("-----------------------------------------")
if taquin.isSolved(taquinFinal):
        print("Taquin resolu")
else:
        print("Taquin non resolu")


        taquinsol=taquin.solve(taquinFinal,[1,1,1,1,1,1,1,1,1])
        print(taquinsol.__str__())

        if taquinsol.isSolved(taquinFinal):
                print("Taquin resolu")
        else:
                print("Taquin non resolu")










