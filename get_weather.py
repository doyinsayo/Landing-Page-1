import requests
import re

def get_weather(user_message: str = ""):
    """
    Fetches current weather for a city mentioned in the user's message.
    Defaults to Lagos if no city is found.
    """

    # 🔑 Replace with your OpenWeather API key
    API_KEY = "1dd01f5da46af19d92cd84b638f5db62"
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

    try:
        # 🧠 Try to capture "in [city]" from the user's message
        match = re.search(r"in\s+([a-zA-Z\s]+)", user_message.lower())
        city = match.group(1).strip() if match else "Lagos"

        # 🧹 Clean up filler words that confuse the API
        clean_phrases = ["right now", "today", "please", "currently", "at the moment"]
        for phrase in clean_phrases:
            city = city.replace(phrase, "").strip()

        # 🌐 Prepare request parameters
        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"
        }

        # ⚡ Call the OpenWeather API
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()

        data = response.json()
        temp = data["main"]["temp"]
        condition = data["weather"][0]["description"]

        # 💬 Prepare response
        message = f"🌤️ The weather in {city.title()} is currently {temp}°C with {condition}."
        return message

    except requests.exceptions.HTTPError as http_err:
        return f"⚠️ Couldn't find weather data for '{city.title()}'. ({http_err})"
    except Exception as e:
        return f"⚠️ Sorry, I couldn't fetch the weather right now. ({e})"


# 🧪 Test once (single call)
if __name__ == "__main__":
    user_input = input("Ask Clutch about the weather (e.g. 'What’s the weather in Abuja?'):\n> ")
    print(get_weather(user_input))
