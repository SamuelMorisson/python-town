from ClasseBrigand import Brigand
from ClasseDame import Dame
from ClasseCowboy import Cowboy
from ClasseBarman import Barman
from ClasseSherif import Sherif


dametest = Dame("nomDame", "rouge")
brigandTest = Brigand("nomBrigand", 0, False)
cowboyTest = Cowboy("nomCowboy")
sherifTest = Sherif("nomSherif")
barmanTest = Barman("nomBarman")


# Test des méthodes:

def presentationPersonnages(humain = [dametest, brigandTest, cowboyTest, sherifTest, barmanTest]):
    for personnage in humain:
        personnage.sePresenter()
        print("---")
#presentationPersonnages()


def connaitreNom(humain = [dametest, brigandTest, cowboyTest, sherifTest, barmanTest]):
    for personnage in humain:
        personnage.quelEstTonNom()
        print("---")
#connaitreNom()


def dameChangeRobe(dame = dametest):
    dame.changerRobe("bleue")
#dameChangeRobe()


def kidnapper(brigand = brigandTest, dame = dametest):
    brigand.kidnapper(dame)
#kidnapper()


def libérer(cowboy = cowboyTest, dame = dametest, brigand = brigandTest):
    brigand.kidnapper(dame)
    cowboy.liberer(dame)
#libérer()


def tirer(cowboy = cowboyTest, brigand = brigandTest):
    cowboy.tirer(brigand)
#tirer()


def emprisonner(sherif = sherifTest, brigand = brigandTest):
    sherif.emprisonner(brigand)
    sherif.sePresenter()
#emprisonner()


def rechercher(sherif = sherifTest, brigand = brigandTest):
    sherif.rechercher(brigand)
#rechercher()


def servirVerre(humain = [dametest, brigandTest, cowboyTest, sherifTest, barmanTest], barman = barmanTest):
    for personnage in humain:
        barman.servirVerre(personnage)
        print("---")
#servirVerre()


def manger(humain = [dametest, brigandTest, cowboyTest, sherifTest, barmanTest]):
    for personnage in humain:
        personnage.manger()
        print("---")
#manger()