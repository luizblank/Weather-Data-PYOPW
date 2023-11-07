import requests, json

api_key = "your_api_here" # Chave para poder usar a API
 
city_name = input("Enter city name : ")

# Link da API que pega as coordenadas geográficas do local especificado (Documentação: https://openweathermap.org/api/geocoding-api)
geocoding = "http://api.openweathermap.org/geo/1.0/direct?q=" + city_name + "&limit=1&appid=" + api_key
georesponse = requests.get(geocoding) # Manda uma requisição para a API
geojson = georesponse.json()[0] # Salva a resposta da API como json em uma variável

# Link que pega a previsão do tempo do local especificado
base_url = "https://api.openweathermap.org/data/2.5/forecast?lat="

# Concatena todas as informações em um link(as informações do json estão sendo convertidas 
# para string para poderem ser concatenadas)
histweather = base_url + str(geojson["lat"]) + "&lon=" + str(geojson["lon"]) + "&appid=" + api_key
histresponse = requests.get(histweather)
histjson = histresponse.json()

# Percorre a lista dentro do json que possui todas as informações de previsão dos proximos 5 dias
for i in range(len(histjson["list"])): 
    list = histjson["list"][i] # Valor atual da lista
    main_info = list["main"] # Pegando os dados principais do valor atual
    print(f"{list["dt_txt"]}:") # Printando a data exata daquelas informações
    print(f"Temperatura: {main_info["temp"]}")
    print(f"Humidade: {main_info["humidity"]}")
    print(f"Pressão: {main_info["pressure"]}\n\n")

# Documentação API de previsão usada acima (entenda como funciona o JSON): https://openweathermap.org/forecast5