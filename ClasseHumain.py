from abc import ABC, abstractmethod

class Humain:
    @abstractmethod
    def __init__(self, nom : str, boissonFav : str = "eau"):
        self._nom = nom
        self._boissonFav = boissonFav

    def getNom(self):
        return self._nom

    def quelEstTonNom(self):
        print(f"Bonjour, je suis {self._nom}")
        
    def getBoissonFav(self):
        return self._boissonFav
    
    def setNom(self, newNom : str):
        if type(newNom) == str:
            self._nom = newNom

    def setBoissonFav(self, newBoisson : str):
        if type(newBoisson) == str:
            self._boissonFav = newBoisson
        
    def __str__(self):
        return (f"Nom: {self._nom}, boisson favorite: {self._nom}")
    
    def sePresenter(self):
        print (f"Bonjour, je suis {self._nom} et ma boisson préferée est {self._boissonFav}!")

    def boire(self):
        print (f"Ah ! Un bon verre de {self._boissonFav}! GLOUPS!")

    @abstractmethod
    def manger(self):
        print(f"{self._nom} mange.")
    
    @abstractmethod
    def parler(self, texte : str):
        if type(texte) == str:
            print (f"({self._nom}) - {texte}")
        
