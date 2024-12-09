from ClasseCowboy import *

class Sherif(Cowboy):
    def __init__(self, nom : str, boissonFav : str ="whisky", popularite : int =0, adjectif : str ="vaillant", brigandEmprisonne : int =0):
        super().__init__(("sherif "+nom), boissonFav, popularite, adjectif)
        self.__brigandEmprisonne = brigandEmprisonne

    def getBrigandEmprisonne(self):
        return self.__brigandEmprisonne
    
    def setBrigandEmprisonne(self, newBrigandEmprisonne : int):
        if type(newBrigandEmprisonne) == int:
            self.__brigandEmprisonne = newBrigandEmprisonne

    def incrementerEmprisonnement(self):
        self.__brigandEmprisonne += 1

    def emprisonner(self, brigand):
        from ClasseBrigand import Brigand
        if type(brigand) == Brigand:
            brigand.seFaireEmprisonner(self)
            self.incrementerEmprisonnement()
            print("Au nom de la loi, je vous arrête!")

    def rechercher(self, brigand):
        from ClasseBrigand import Brigand
        if type(brigand) == Brigand:
            print(f"Le {self.getNom()} placarde des affiches dans la ville.")
            print(f"- OYEZ OYEZ BRAVE GENS !! {brigand.getRecompense()}$ à qui arrêtera {brigand.getNom()} le {brigand.getLook()} mort ou vif!")

    def sePresenter(self):
        super().sePresenter()
        print(f"J'ai emrpisonné {self.__brigandEmprisonne} brigand(s)!")



'''sherifTest = Sherif("sherifTest")
sherifTest.sePresenter()'''