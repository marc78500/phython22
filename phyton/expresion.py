import re 

password="Passw0rd, trongP@ss,12345678, WeakPassord"
print(password)
mdp=password.split(", ")
print(mdp)

pattern=re.complie(r'(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*/_]).{8,}')

valid_passords=pattern.findall(password)


print('mots de passe vallide:', valid_passords)
