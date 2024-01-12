class capteur_meteo():
    def __init__(self,nom, emplacement, data_instalation):
        self.nom = nom
        self.emplacement = emplacement
        self.data_instalation = data_instalation
        print("Passage du constructeur")
    
    def afficherInfos(self):
        print(f"nom : {self.nom}\n emplacemnt : {self.emplacement}\n data_instalation : {self.data_instalation}\n")



class capteur_temperature (capteur_meteo):
    def __init__(self, nom, emplacement, data_instalation,plage_mesure):
        super().__init__(nom, emplacement,data_instalation)
        self.plage_mesure = plage_mesure
        print("Passage du constructeur ")

    def afficherInfos(self):
        print(f"nom : {self.nom}\nemplacement : {self.emplacement}\ndata Instalation : {self.data_instalation}\nPlage de Mesure : {self.plage_mesure}\n")



class capteur_humidite(capteur_meteo):
    def __init__(self, nom, emplacement, data_instalation, plage_mesure,):
        super().__init__(nom, emplacement, data_instalation)
        self.plage_mesure = plage_mesure

    def afficherInfos(self):
        print(f"nom : {self.nom}\n Emplacement : {self.emplacement}\n data Instalation : {self.data_instalation}\n plage de mesure : {self.plage_mesure}")




    def afficherInfos(self):
        print(f"nom : {self.nom}\n Emplacement : {self.emplacement}\n  data Instalation : {self.data_instalation}\n plage de mesure : {self.plage_mesure}")


print("Classe Capteur Metéo")
lecapteur = capteur_meteo("stationD", "paris","sfr")
lecapteur.afficherInfos()

print("Classe capteur Temperature")
la_temperature = capteur_temperature("stationD", "paris", "sfr","50Cm")
la_temperature.afficherInfos()

print("Classe capteur Humidité")
humide = capteur_humidite ("stationD", "paris", "sfr", "50Cm")
humide.afficherInfos()

