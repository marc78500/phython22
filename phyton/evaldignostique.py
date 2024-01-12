import re

iot_frame = "SensorID:123;Temperature:25.5;Humidity:60.2;Status:OK"

list = re.split(r'\s*,\s*', iot_frame)

pattern = re.compile(r'^[0-9]{3}$')


trame = [iot_frame for iot_frame in list if pattern.match(iot_frame)]

# Affichez les mots de passe valides
print(trame)