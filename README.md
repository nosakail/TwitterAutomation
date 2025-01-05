# X (Twitter) Automation Bot 🤖

A free Twitter bot that automatically helps people looking for internships by retweeting their posts and providing support.

## 🎯 Fonctionnalités

- Recherche automatique des tweets contenant "recherche d'un stage"
- Retweet automatique des posts trouvés
- Réponse automatique avec un message d'encouragement
- Gestion des limites de l'API Twitter
- Suivi des tweets déjà traités pour éviter les doublons
- Respect des limites de l'API gratuite (17 tweets/24h)

## 🛠️ Installation

1. Clonez le repository

bash
git clone https://github.com/nosakail/TwitterAutomation.git
cd twitter-stage-bot

2. Installez les dépendances

```bash
pip install tweepy
```

3. Configurez vos clés d'API Twitter et les variables query / response dans `main.py` 

```python
API_KEY = "votre_api_key"
API_SECRET = "votre_api_secret"
ACCESS_TOKEN = "votre_access_token"
ACCESS_TOKEN_SECRET = "votre_access_token_secret"
BEARER_TOKEN = "votre_bearer_token"
```

## 🚀 Utilisation

Lancez simplement le script :
```bash
python main.py
```

Le bot va :
1. Rechercher les tweets contenant "les caractères spéciaux"
2. Retweeter et répondre aux tweets trouvés
3. Attendre 5 minutes avant une nouvelle recherche
4. Répéter le processus

## ⚠️ Notes importantes

- Les clés d'API et tokens montrés dans les commits ont été régénérés et ne sont plus valides
- Le bot (v2) respecte les limites de l'API gratuite de Twitter pour une meilleur expérience prendre le bot v1 (voir les commits)
- Un fichier `responded_tweets.txt` est créé pour suivre les tweets déjà traités

## 📝 Configuration

Le bot est configuré pour :
- Traiter jusqu'à 17 tweets par 24h (limite de l'API gratuite)
- Attendre 5 minutes entre chaque recherche
- Ajouter un petit délai entre les actions pour respecter les limites de taux

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :
1. Fork le projet
2. Créer une branche pour votre fonctionnalité
3. Commit vos changements
4. Push sur votre branche
5. Ouvrir une Pull Request


