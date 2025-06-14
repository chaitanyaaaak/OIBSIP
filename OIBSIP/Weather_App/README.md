# ☁️ Weather Checker

A simple Python app to check the current weather conditions for any city or ZIP code using the OpenWeatherMap API.

---

## 🌟 Features

- Check weather by **city name** or **ZIP code**
- Displays:
  - ✅ Temperature (in Celsius)
  - ✅ Humidity
  - ✅ Weather description
- Handles invalid locations and connection errors gracefully

---

## 🧠 How It Works

- If you enter a ZIP code (like `201301`), it queries weather by ZIP.
- Otherwise, it treats the input as a city name (like `Delhi`).
- Uses the OpenWeatherMap API via `requests`.

---

## 🔑 Requirements

- Python 3.x
- `requests` module (install with: `pip install requests`)
- A free API key from [https://openweathermap.org/api](https://openweathermap.org/api)


```python
API_KEY = "071f3e4b60a5526369ccb0c63810b6d7"
