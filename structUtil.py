
class ABRt :
    taquin : 'Taquin'
    filsGauche : 'ABRt'
    filsDroit : 'ABRt'
    def __init__(self, taquin:'Taquin', filsGauche:'ABRt' = None, filsDroit:'ABRt' = None):
        self.taquin = taquin
        self.filsGauche = filsGauche
        self.filsDroit = filsDroit

    def insert(self, taquin:'Taquin'):
            if taquin.taquinToInt() < self.taquin.taquinToInt():
                if self.filsGauche == None:
                    self.filsGauche = ABRt(taquin)
                else:
                    self.filsGauche.insert(taquin)
            else:
                if self.filsDroit == None:
                    self.filsDroit = ABRt(taquin)
                else:
                    self.filsDroit.insert(taquin)



    def search(self, taquin:'Taquin'):
        if self.taquin.taquinToInt() == taquin.taquinToInt():
            return self
        elif taquin.taquinToInt() < self.taquin.taquinToInt():
            if self.filsGauche == None:
                return None
            else:
                return self.filsGauche.search(taquin)
        else:
            if self.filsDroit == None:
                return None
            else:
                return self.filsDroit.search(taquin)
    def contains(self, taquin:'Taquin'):
        if self.search(taquin) == None:
            return False
        else:
            return True
            




class listePriorite:
    def __init__(self,taquinFinal:'Taquin',poids,coefNormalisation):
        self.liste = []
        self.taquinFinal=taquinFinal
        self.poids=poids
        self.coefNormalisation=coefNormalisation

    def insertTaquin(self, element:'Taquin'):
        if len(self.liste) == 0:
            self.liste.append(element)
        else:
            for i in range(len(self.liste)):
               
                if element.compareTo(self.liste[i],self.taquinFinal,self.poids,self.coefNormalisation)<0:#element.comparator() - self.liste[i].comparator()<0
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


    