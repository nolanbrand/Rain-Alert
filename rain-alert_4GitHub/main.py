import requests
import smtplib

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "your_api_key"
MY_EMAIL = "email@gmail.com"
PASSWORD = "your_password"
weather_params = {
    "lat": 29.760427,
    "lon": -95.369804,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(url=OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()["list"]

twelve_hour_id = [weather_data[id]["weather"][0]["id"] for id in range(len(weather_data))]

will_rain = False

for weather_id in twelve_hour_id:
    if weather_id < 700:
        will_rain = True

if will_rain:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Rain is Coming\n\nBe sure to bring a rain coat and umbrella today. Rain is coming!"
        )
