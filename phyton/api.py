import requests
city="Marseille"

key="20a3078403aee6a6c070879405efc915"

url=f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric"
res = requests.get(url)
# print(res.json())
print(res.json()['main'])
print(res.json()['main']['temp'])
print(res.json()['main']['pressure'])
print(res.json()['main']['humidity'])


