# ue19-lab-05

# Blagueur

Blagueur est un petit programme en Python qui récupère une blague aléatoire en français depuis l'API JokeAPI et l'affiche dans la console.

## Prérequis

- Python 3.x
- Bibliothèque `requests`

Vous pouvez installer la bibliothèque `requests` en utilisant pip :

```bash
pip install requests

```

## Fonctionnalités
- Récupère une blague aléatoire en français depuis l'API JokeAPI.
- Affiche la blague dans la console.
- Gère les blagues en deux parties (setup et delivery) ainsi que les blagues en une seule partie.
- Affiche un message d'erreur si l'API ne répond pas correctement.

## Exemple de sortie
Si la blague est en deux parties :
```
Pourquoi les plongeurs plongent-ils toujours en arrière et jamais en avant ?

Parce que sinon ils tombent encore dans le bateau !
```