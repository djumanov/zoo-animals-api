import requests

# url for zoo api
URL = 'https://zoo-animal-api.herokuapp.com/animals/rand'


def get_animals(data: list) -> list:
    res = data['name']
    return res


def main():
    inp = int(input("how many animlas do you need? (1-10)"))
    payload = {
        'number': inp
    }
    resporse = requests.get(url=URL, params=payload)
    if resporse.status_code == 200:
        list_of_animals = get_animals(resporse.json())

    return list_of_animals

print(main())