import requests

API_KEY = "071f3e4b60a5526369ccb0c63810b6d7"  
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def zip_code(text):
    parts = text.split(',')
    return parts[0].isdigit()

def get_weather(location):
    if zip_code(location):
        params = {
            "zip": location,
            "appid": API_KEY,
            "units": "metric"
        }
    else:
        params = {
            "q": location,
            "appid": API_KEY,
            "units": "metric"
        }
    try:
        response = requests.get(BASE_URL, params=params, timeout=5)
        if response.status_code == 200:
            data = response.json()
            city = data.get("name", "Unknown location")
            country = data.get("sys", {}).get("country", "")
            temp = data.get("main", {}).get("temp", "N/A")
            humidity = data.get("main", {}).get("humidity", "N/A")
            description = data.get("weather", [{}])[0].get("description", "No description").capitalize()
            print(f"\nWeather for {city}, {country}:")
            print(f"  Temperature: {temp}°C")
            print(f"  Humidity: {humidity}%")
            print(f"  Condition: {description}\n")
        elif response.status_code == 404:
            print("Sorry, location not found. Please check your spelling or try a different place.\n")
        else:
            print("Oops! Something went wrong. Please try again later.\n")
    except requests.RequestException:
        print("Could not connect to the weather service. Please check your internet connection.\n")

def main():
    print("Welcome to the Python Weather App!")
    print("You can enter a city name (like 'Delhi') or a ZIP code (like '201301' or '400601,in').")
    print("Type 'exit' to close the app.\n")
    while True:
        user_input = input("Enter city name or ZIP code: ").strip()
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        if not user_input:
            print("Please enter something!\n")
            continue
        get_weather(user_input)

if __name__ == "__main__":
    main()
