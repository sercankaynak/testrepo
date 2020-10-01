import requests

url = "http://data.fixer.io/api/latest?base="

birinci_döviz = input("Birinci Döviz : ")
ikinci_döviz = input("İkinci Döviz : ")
miktar = float(input("Miktar : "))

response = requests.get(url + birinci_döviz)

json_verisi = response.json()

print(json_verisi["rates"][ikinci_döviz]*miktar)