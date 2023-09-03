import requests

def get_data(kind, days, place):
    api_key = "9bbd3edccdc2acbd3d12fd096c8abd6e"
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&units=imperial&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    data = data["list"]
    temps = []
    dates = []
    forecast_rng = 8 * days
    if kind == "Temperature":
        for item in data[:forecast_rng]:
            temps.append(item["main"]["temp"])
            dates.append(item["dt_txt"])
    return dates, temps
    # if kind == "Sky":
    #     for item in data[:8*days]:
    #         temps.append(item["main"]["temp"])
    #         dates.append(item["dt_txt"])
    # return dates, temps


if __name__ == "__main__":
    print(get_data("Temperature", 5, "Tokyo"))