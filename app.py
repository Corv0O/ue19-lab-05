import requests
url =  "https://v2.jokeapi.dev/joke/Any?lang=fr"
jokerequest = requests.get(url)
joke = jokerequest.json()
if jokerequest.status_code == 200:
    if joke['type'] == "twopart":
        print(f"{joke['setup']}\n")
        print(joke['delivery'])
    else:
        print(joke["joke"])
else:
    print("erreur au niveau de l'API, pas de blague :-(")
