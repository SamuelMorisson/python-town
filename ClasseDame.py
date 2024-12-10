from ClasseHumain import Humain

class Dame(Humain):
    def __init__(self, nom, robe : str, boissonFav="lait", etat="libre"):
        super().__init__(nom, boissonFav)
        self.__robe = robe
        self.__etat = etat
    
    def getRobe(self):
        return self.__robe
    
    def getEtat(self):
        return self.__etat
    
    def changerRobe(self, couleur):
        # setter robe
        if type(couleur) == str:
            self.__robe = couleur
            print(f"Regardez ma nouvelle robe {self.__robe}")

    def kidnapperDame(self):
        if self.__etat == "libre":
            self.__etat = "captive"
            print("AAAH!")

    def libererDame(self, nomCowboy):
        if self.__etat == "captive":
            self.__etat == "libre"
            print(f"Merci {nomCowboy} de m'avoir libérée!")

    def setEtat(self, newEtat):
        if newEtat in ["libre", "captive"]:
            self.__etat = newEtat

    def quelEstTonNom(self):
        print(f"Bonjour, je suis miss {self._nom}")

    def sePresenter(self):
        self.quelEstTonNom()
        print(f"Ma robe est de couleur {self.__robe}!")

    def manger(self):
        print(f"{self._nom} mange.")



'''dametest = Dame("nomDame", "rouge")
dametest.changerRobe("bleu")
dametest.sePresenter()'''