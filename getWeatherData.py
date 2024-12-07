import requests

#This function gets the data from the API
def get_weather(city):

  
  api_key = "f170884b77ed10741d1ede438b0d5dfa"
  base_url = "http://api.openweathermap.org/data/2.5/weather?"
  complete_url = base_url + "appid=" + api_key + "&q=" + city
  response = requests.get(complete_url)
  if response.status_code == 200:
    data = response.json()
    main = data['main']
    temperature = round(main['feels_like'] - 273.15, 2)  # Convert from Kelvin to Celsius
    description = data['weather'][0]['description']
    with open("weatherData.txt", "w") as file:
      file.write (f"{temperature}\n{description}\n")
    return f"{temperature},{description}"
  else:
    return "City not found or an error occurred."



if __name__ == "__main__":
  with open("location.txt", "r") as file:
    city = file.readline().strip()  # Read the first line and remove any trailing whitespace
  weather_info = get_weather(city)
  print(weather_info)