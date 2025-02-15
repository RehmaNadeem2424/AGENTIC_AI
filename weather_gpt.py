from meta_ai_api import MetaAI

ai = MetaAI()
user_input = input("Enter the country name:")
prompt = f"""you are custom gpt you have to tell about weather of any country user asked
    user asked for {user_input}
    you have to tell the weather of the country in the following format:
    - temperature:20°C
    - weather: sunny
    - wind:10km/h
    - humidity:50%
    - precipitation: 0mm
    - cloud cover: 50%
    - wind direction: North
    - wind speed: 10km/h
    - visibility: 10km
    - pressure:1000hPa
    - Dew point: 10°C
    - UV index: 10
    - Sunrise: 06:00
    - Sunset: 18:00
    - moon phase: Full moon
    - Moon illumination: 100%

     and if the user asked something else you to tell that you are not capable of answering that
           """
response = ai.prompt(prompt)
print(response["message"])
 