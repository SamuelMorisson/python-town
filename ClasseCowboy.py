from ClasseHumain import *

class Cowboy(Humain):
    def __init__(self, nom : str, boissonFav : str ="whisky", popularite : int =0, adjectif : str ="vaillant"):
        super().__init__(nom, boissonFav)
        self.__popularite = popularite
        self.__adjectif = adjectif

    def getPopularite(self):
        return self.__popularite
    
    def getAdjectif(self):
        return self.__adjectif
    
    def setPopularite(self, newPopularite : int):
        if type(newPopularite) == int:
            self.__popularite = newPopularite

    def setAdjectif(self, newAdjectif : str):
        if type(newAdjectif) == str:
            self.__popularite = newAdjectif


    def tirer(self, brigandCible):
        from ClasseBrigand import Brigand
        if type(brigandCible) == Brigand:
            print(f"Le {self.__adjectif} {self.getNom()} tire sur {brigandCible.getNom()}.")
            print("PAN!")
            print("- Prend ça, rascal!")

    def liberer(self, dame):
        from ClasseDame import Dame
        if type(dame)== Dame:
            dame.libererDame(self.getNom())

    def sePresenter(self):
        super().sePresenter()
        print(f"On dit que je suis {self.__adjectif} et ma popularité est de {self.__popularite}!")

    def manger(self):
        return super().manger()



'''cowbowTest = Cowboy("cowboyTest")
cowbowTest.sePresenter()'''