from abc import ABC, abstractmethod

class Humain:
    @abstractmethod
    def __init__(self, nom : str, boissonFav : str = "eau"):
        self.__nom = nom
        self.__boissonFav = boissonFav

    def getNom(self):
        return self.__nom

    def quelEstTonNom(self):
        print(f"Bonjour, je suis {self.__nom}")
        
    def getBoissonFav(self):
        return self.__boissonFav
    
    def setNom(self, newNom : str):
        if type(newNom) == str:
            self.__nom = newNom

    def setBoissonFav(self, newBoisson : str):
        if type(newBoisson) == str:
            self.__boissonFav = newBoisson
        
    def __str__(self):
        return (f"Nom: {self.__nom}, boisson favorite: {self.__nom}")
    
    def sePresenter(self):
        print (f"Bonjour, je suis {self.__nom} et ma boisson préferée est {self.__boissonFav}!")

    def boire(self):
        print (f"Ah ! Un bon verre de {self.__boissonFav}! GLOUPS!")

    @abstractmethod
    def manger(self):
        print(f"{self.__nom} mange.")
    
    @abstractmethod
    def parler(self, texte : str):
        if type(texte) == str:
            print (f"({self.__nom}) - {texte}")
        
