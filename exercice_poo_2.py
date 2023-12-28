import random

class NPC:
    def __init__(self, nom, race, espèce, profession):
        self.nom = nom
        self.race = race
        self.espèce = espèce
        self.profession = profession

        self.force = self._lancer_des(4, 6)
        self.agilité = self._lancer_des(4, 6)
        self.constitution = self._lancer_des(4, 6)
        self.intelligence = self._lancer_des(4, 6)
        self.sagesse = self._lancer_des(4, 6)
        self.charisme = self._lancer_des(4, 6)

        self.classe_armure = self._lancer_des(1, 12)
        self.points_de_vie = self._lancer_des(1, 20)

    def _lancer_des(self, nb_des, faces):
        return sum(sorted([random.randint(1, faces) for _ in range(nb_des)])[1:])

    def afficher_caracteristiques(self):
        print(f"Nom: {self.nom}")
        print(f"Race: {self.race}")
        print(f"Espèce: {self.espèce}")
        print(f"Profession: {self.profession}")
        print(f"Force: {self.force}")
        print(f"Agilité: {self.agilité}")
        print(f"Constitution: {self.constitution}")
        print(f"Intelligence: {self.intelligence}")
        print(f"Sagesse: {self.sagesse}")
        print(f"Charisme: {self.charisme}")
        print(f"Classe d'armure: {self.classe_armure}")
        print(f"Points de vie: {self.points_de_vie}")

class Kobold(NPC):
    def attaquer(self, cible):
        print(f"{self.nom} attaque {cible.nom}!")

    def subir_dommage(self, quantite):
        print(f"{self.nom} subit {quantite} points de dommage!")

class Heros(NPC):
    def attaquer(self, cible):
        print(f"{self.nom} attaque {cible.nom}!")

    def subir_dommage(self, quantite):
        print(f"{self.nom} subit {quantite} points de dommage!")

# Exemple d'utilisation
kobold = Kobold(nom="Kobold1", race="Kobold", espèce="Reptile", profession="Guerrier")
heros = Heros(nom="Héros1", race="Humain", espèce="Humanoid", profession="Paladin")

kobold.afficher_caracteristiques()
heros.afficher_caracteristiques()

kobold.attaquer(heros)
heros.subir_dommage(4)
