from taquin import Taquin


t:Taquin = Taquin(3,None)
t.remplir()
t2=t.clone()
t3=t.clone()
t4=t3.clone()
t5=t4.clone()
print(t.__str__())

t.shuffle(500)

print(t.__str__())

print("_________________________________________________________")
t.movebyPermut("N")