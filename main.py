import requests
import matplotlib.pyplot as plt

API_KEY = "1210aeab4b49be97f272ad2c83c2eb28"  
CITY ="Tirupati"
url = f"https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    dates = []
    temperatures = []

    for forecast in data['list'][:20]:  
        dates.append(forecast['dt_txt'])
        temperatures.append(forecast['main']['temp'])

    print("Dates:", dates)
    print("Temperatures:", temperatures)

    plt.figure(figsize=(12, 5))
    plt.plot(dates, temperatures, marker='o', linestyle='-', color='blue')
    plt.xticks(rotation=45)
    plt.xlabel('Date & Time')
    plt.ylabel('Temperature (°C)')
    plt.title(f'Temperature Forecast for {CITY}')
    plt.tight_layout()
    plt.grid(True)
    plt.show()

else:
    print(" API request failed")
    print("Status code:", response.status_code)
    print("Error:", response.text)
