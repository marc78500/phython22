class camera():
    def __init__(self,ips, img_size):
        self.ips = ips
        self.img_size = img_size
        print("Passage du constructeur")
    
    def afficherInfos(self):
        print(f" emplacemnt : {self.ips}\n img_size : {self.img_size}\n")



class Duration_camera (camera):
    def __init__(self, ips, img_size,duration, calculer):
        super().__init__(ips,img_size)
        self.duration = duration
        self.calculer=calculer
        print("Passage du constructeur ")

    def afficherInfos(self):
        print(f"{self.ips}\ndata Instalation : {self.img_size}\nPlage de Mesure : {self.duration}\n nom : {self.calculer}\n:")


class Hdd_camera(camera):
    def __init__(self,ips, img_size, hdd,calculer,):
        super().__init__( ips, img_size)
        self.hdd = hdd
        self.calculer = calculer

    def afficherInfos(self):
        print(f"nom : {self.nom}\n ips : {self.ips}\n data Instalation : {self.img_size}\n plage de mesure : {self.calculer}\n nom : {self.calculer}")




    def afficherInfos(self):
        print(f"nom : {self.nom}\n ips : {self.ips}\n  data Instalation : {self.img_size}\n plage de mesure : {self.duration}")


print("Classe Capteur Metéo")
lecapteur = camera("stationD", "paris","sfr")
lecapteur.afficherInfos()

print("Classe capteur Temperature")
la_temperature = Duration_camera("stationD", "paris", "sfr","50Cm")
la_temperature.afficherInfos()

print("Classe capteur Humidité")
humide = Hdd_camera ("stationD", "paris", "sfr", "50Cm")
humide.afficherInfos()

def calculerDuree():
    tailleImage= saisir("la taille de l'image en Ko")
    tailleStockage = saisir("la taille du HDD en Go")
    return (1024*1024*tailleStockage)/(tailleImage*ips)


