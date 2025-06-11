import requests


city=input("Enter city name: ")
key="your_api_key"

url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric"

response=requests.get(url)
if response.status_code == 200:# Check if the request was successful
    data=response.json()

    print(f"City: {data['name']}")
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"Feels Like:{data['main']['feels_like']}°C")
    print(f"Weather: {data['weather'][0]['description']}")
else:
    print("Error:", response.status_code)
    print("City not found or API request failed.")

    
