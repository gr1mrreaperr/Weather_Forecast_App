import requests

api_key = "b116db68ed91b48c0458f4f5f4ceeb4e"


def get_data(place, days):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}&units=metric"
    request = requests.get(url)
    data = request.json()
    filtered_data = data["list"]
    nr_val = 8 * days
    filtered_data = filtered_data[:nr_val]
    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Dehradun", days=5))


