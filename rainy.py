import requests
iran_province = ["Tehran",
"Qom",
"Markazi",
"Qazvin",
"Gilan",
"Ardabil",
"Zanjan",
"East Azarbaijan",
"West Azarbaijan",
"Kurdistan",
"Hamadan",
"Kermanshah",
"Ilam",
"Lorestan",
"Khuzestan",
"Chahar Mahaal and Bakhtiari",
"Kohkiluyeh and Buyer Ahmad",
"Bushehr",
"Fars",
"Hormozgan",
"Sistan and Baluchistan",
"Kerman",
"Yazd",
"Esfahan",
"Semnan",
"Mazandaran",
"Golestan",
"North Khorasan",
"Razavi Khorasan",
"South Khorasan",
"Alborz"]


url = "http://api.weatherstack.com/current?access_key=23d260a9963aabad1867f9279945789d&query=Tehran"
response = requests.get(url)
diction=response.json()
current = diction.get('current')
now_wheater = current.get('weather_descriptions')[0]
#print(now_wheater)
now_temperature = current.get("feelslike")



cludy_province=[]
rain_province=[]
sunny_province=[]

for i in iran_province:
    url = "http://api.weatherstack.com/current?access_key=23d260a9963aabad1867f9279945789d&query="+str(i)
    response = requests.get(url)
    diction=response.json()
    current = diction.get('current')
    now_wheater = current.get('weather_descriptions')[0]
    now_temperature = current.get("feelslike")
    if now_temperature <=10 :
        rain_province.append(i)
    if now_temperature >25 :
        sunny_province.append(i)
    print(i , "is" , now_wheater , "now")

print("rainy cities are :" , rain_province)
print("*********************************************")
print("sunny cities are :" , sunny_province)
print(int(len(rain_province))/int(len(iran_province)),"%","Rainy Cities in iran Right Now !")
print("*********************************************")

