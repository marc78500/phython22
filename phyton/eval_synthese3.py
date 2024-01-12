class camera():
    def __init__(self,ips, img_size):
        self.ips = ips
        self.img_size = img_size
        print("Passage du constructeur")
    
    def afficherInfos(self):
        print(f" ips : {self.ips}\n taille image : {self.img_size}\n")



class Duration_camera (camera):
    def __init__(self, ips, img_size,duration,):
        super().__init__(ips,img_size)
        self.duration = duration
        
      


    def calculer(self):
        return (self.img_size*self.ips *self.duration)/(1024*1024)
    



class Hdd_camera(camera):
    def __init__(self,ips, img_size, hdd,):
        super().__init__( ips, img_size)
        self.hdd = hdd

    def calculer(self):
        return(1024*1024*self.hdd)/(self.img_size*self.ips)
    


print("Camera")
lecapteur = camera(30.5, 80.5)
lecapteur.afficherInfos()

print("duration camera")
la_durre = Duration_camera(30.5, 80.5, 10.5)
print(la_durre.calculer())

print("HDD Camera")
h_d = Hdd_camera (30.5, 80.5, 2.5)
print(h_d.calculer())
