import requests
import os
from dotenv import load_dotenv


def get_data(kind, days, place):
    load_dotenv()
    api_key = os.getenv("API_KEY")
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&units=imperial&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    data = data["list"]
    data_res = []
    dates = []
    forecast_rng = 8 * days
    for item in data[:forecast_rng]:
        if kind == "Temperature":
            data_res.append(item["main"]["temp"])
        else:
            match item["weather"][0]["main"]:
                case "Clear":
                    data_res.append("./images/clear.png")
                case "Clouds":
                    data_res.append("./images/cloud.png")
                case "Rain":
                    data_res.append("./images/rain.png")
                case "Snow":
                    data_res.append("./images/snow.png")
        dates.append(item["dt_txt"])

    return dates, data_res


if __name__ == "__main__":
    print(get_data("Sky", 5, "Tokyo"))