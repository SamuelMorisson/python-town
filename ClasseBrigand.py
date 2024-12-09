from ClasseHumain import *

class Brigand(Humain):
    def __init__(self, nom : str, enlevement : int, prison : bool, boissonFav : str ="tord-boyaux", look : str ="méchant", recompense : int =100, ):
        super().__init__(nom, boissonFav)
        self.__enlevement = enlevement
        self.__prison = prison
        self.__look = look
        self.__recompense = recompense

    def getEnlevement(self):
        return self.__enlevement
    
    def getPrison(self):
        return self.__prison
    
    def getLook(self):
        return self.__look
    
    def getRecompense(self):
        return self.__recompense
        
    def setEnlevement(self, newEnlement : int):
        if type(newEnlement) == int:
            self.__enlevement = newEnlement

    def setEnlevement(self, newPrison : bool):
        if type(newPrison) == bool:
            self.__prison = newPrison

    def setLook(self, newLook : str):
        if type(newLook) == str:
            self.__look = newLook

    def setRecompense(self, newRecompense : int):
        if type(newRecompense) == int:
            self.__recompense = newRecompense


    def kidnapper(self, dameCible):
        from ClasseDame import Dame
        if type(dameCible) == Dame:
            self.__enlevement += 1
            dameCible.kidnapperDame()
            print(f"Ah ah! {dameCible.getNom()}, tu es mienne désormais!")

    def seFaireEmprisonner(self, sherif):
        from ClasseSherif import Sherif
        if type(sherif) == Sherif:
            self.__prison = True
            print(f"Damned, je suis fait! {sherif.getNom()} tu m'as eu!")

    def quelEstTonNom(self):
        print(f"Je suis {self.getNom()} le {self.getLook()}")

    def sePresenter(self):
        super().sePresenter()
        print(f"J'ai l'air {self.__look} et j'ai kidnappé {self.__enlevement} dames!")
        print(f"Ma tête est mise à prix {self.__recompense}$!")

    def manger(self):
        print(f"{self.getNom()} mange salement!")


'''brigandTest = Brigand("brigandTest", 0, False)
brigandTest.quelEstTonNom()'''
