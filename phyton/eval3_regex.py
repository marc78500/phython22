import re 

maTrame = "$GPGGA,123519,4807.038,N,01131.000,E,1,08,0.9,545.4,M,46.9,M,,*47"


lagitude_pattern = re.compile(r'\d{3}') 
longitude_pattern = re.compile(r'\d+.\d') 
heuure_pattern = re.compile(r'\d+.\d') 
status_pattern = re.compile(r'[A-Z]+$')


maTrameList = maTrame.split(',')
heure = maTrameList[1]
latitude = maTrameList[2] + maTrameList[3]
longitude = maTrameList[4] + maTrameList[5]

print("Latitude :", latitude)
print("Longitude :", longitude)
print("Heure (UTC) :", heure)    