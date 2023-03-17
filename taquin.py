class Taquin:
    def __init__(self, etat):
        self.etat = etat
        self.chemin=""
        self.g= 0
        
    def afficher(self):
        for i in range(0, 9,3):
            print(self.etat[i:i+3])
        print("\n")
    
    def deplacer(self, direction):
        index = self.etat.index(0)
        if direction == 'Nord' and index > 2:
            self.etat[index], self.etat[index-3] = self.etat[index-3], self.etat[index]
            self.chemin+='N'
            self.g+=1
        elif direction == 'Sud' and index < 6:
            self.etat[index], self.etat[index+3] = self.etat[index+3], self.etat[index]
            self.chemin+= 'S'
            self.g+=1
        elif direction == 'West' and index not in [0, 3, 6]:
            self.etat[index], self.etat[index-1] = self.etat[index-1], self.etat[index]
            self.chemin+='W'
            self.g+=1
        elif direction == 'Est' and index not in [2, 5, 8]:
            self.etat[index], self.etat[index+1] = self.etat[index+1], self.etat[index]
            self.chemin+='E'
            self.g+=1
        else:
            print("Déplacement invalide")
    
    def afficherchemin(self):
        print(self.chemin)
    
    def deplacements_possibles(self):
        index = self.etat.index(0)
        deplacements = []
        if index > 2:
            deplacements.append('Nord')
        if index < 6:
            deplacements.append('Sud')
        if index not in [0, 3, 6]:
            deplacements.append('West')
        if index not in [2, 5, 8]:
            deplacements.append('Est')
        return deplacements
    
    def afficherG(self):
        print(self.g)
    
    def expand(self):
        deplacements = self.deplacements_possibles()
        taquins_expands = []
        self.afficher()
        for direction in deplacements:
            nouvel_etat = self.etat.copy()
            taquin = Taquin(nouvel_etat)
            taquin.deplacer(direction)
            taquin.afficher()
            taquin.afficherG()
            taquins_expands.append(taquin)
            
        return taquins_expands        
    def manhattan(self):
        #for case in self.etat:    
        pass        
    def heuristtique():
        pass



etat_initial = [1, 2, 3, 4, 5, 6, 7, 8, 0]
t = Taquin(etat_initial)

t.expand()