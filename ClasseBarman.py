from ClasseHumain import *

class Barman(Humain):
    def __init__(self, nom : str, boissonFav : str ="vin", nomBar=None):
        super().__init__(nom, boissonFav)
        if nomBar == None:
            self.__nomBar = "Chez " + nom
        else:
            self.__nomBar = nomBar

    def getNomBar(self):
        return self.__nomBar
    
    def setNomBar(self, newNomBar):
        if type(newNomBar) == str:
            self.__nomBar = newNomBar

    def sePresenter(self):
        super().sePresenter()
        print(f'Je suis le barman de "{self.__nomBar}"!')

    def parler(self, texte):
        if type(texte) == str:
            super().parler(f"{texte} Coco.")

    def servirVerre(self, humain):
        print(f"{humain.getNom()}, je vous sert un verre de {humain.getBoissonFav()}")

    def manger(self):
        return super().manger()
    


'''barmanTest = Barman("nomBraman")
barmanTest.parler("phrase")'''