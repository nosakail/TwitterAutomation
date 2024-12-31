import tweepy
import time
import os
from PIL import Image

# Configuration des clés d'API
API_KEY = "z41NZxHS0GM2LJWCAq9wAVp89"
API_SECRET = "4NsV9Un2pMx23rW5qV5CyFM7lCiW8oCqQyEY8MeLNE9lTMPzmm"
ACCESS_TOKEN = "1733141677806645250-9dv8S00doQDZQ7UeY3ZExvuXzJEGJB"
ACCESS_TOKEN_SECRET = "V6AOBaJBXWUPaD4PRCcsTDSb6oI7UuUrFt8S4IdKIau3I"

# Authentification avec Tweepy
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

def check_and_respond_to_dms():
    try:
        # Récupérer les DMs
        messages = api.get_direct_messages()
        
        for message in messages:
            sender_id = message.message_create['sender_id']
            text = message.message_create['message_data']['text'].lower()
            
            # Répondre uniquement à la demande de CV
            if "cv" in text:
                send_cv(sender_id)
                
    except Exception as e:
        print(f"Erreur: {str(e)}")

def send_cv(sender_id):
    # Chemin vers votre CV au format jpg
    cv_path = "path/to/your/cv.jpg"
    
    try:
        # Vérifier que le fichier existe et est une image
        if not os.path.exists(cv_path):
            raise FileNotFoundError("Le fichier CV n'existe pas")
            
        # Vérifier que c'est bien une image
        Image.open(cv_path)
        
        # Envoyer le CV
        media = api.media_upload(cv_path)
        api.send_direct_message(sender_id, "Voici mon CV :", attachment_type='media', attachment_media_id=media.media_id)
    except Exception as e:
        print(f"Erreur lors de l'envoi du CV: {str(e)}")
        api.send_direct_message(sender_id, "Désolé, je ne peux pas envoyer mon CV pour le moment.")

def main():
    while True:
        check_and_respond_to_dms()
        # Attendre 1 minute avant de vérifier à nouveau
        time.sleep(60)

if __name__ == "__main__":
    main()
