import tweepy
import time
from datetime import datetime, timedelta

# Configuration des clés d'API
API_KEY = "z41NZxHS0GM2LJWCAq9wAVp89"
API_SECRET = "4NsV9Un2pMx23rW5qV5CyFM7lCiW8oCqQyEY8MeLNE9lTMPzmm"
ACCESS_TOKEN = "1733141677806645250-9dv8S00doQDZQ7UeY3ZExvuXzJEGJB"
ACCESS_TOKEN_SECRET = "V6AOBaJBXWUPaD4PRCcsTDSb6oI7UuUrFt8S4IdKIau3I"
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAAs5xwEAAAAAXWoVorZSabpMQ2wj%2B2OoC2P%2FWmE%3DNn7rJISwc3LoyGDN4zjOUYwvvol8zewln34Lu4seKoqZieJanp"

# Authentification avec Tweepy
client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET,
    wait_on_rate_limit=True
)

class TweetTracker:
    def __init__(self):
        self.responded_tweets = self.load_responded_tweets()
        self.daily_tweet_count = 0
        self.last_reset = datetime.now()

    def load_responded_tweets(self):
        try:
            with open('responded_tweets.txt', 'r') as f:
                return set(int(line.strip()) for line in f)
        except FileNotFoundError:
            return set()

    def save_responded_tweet(self, tweet_id):
        with open('responded_tweets.txt', 'a') as f:
            f.write(f"{tweet_id}\n")

    def can_tweet(self):
        # Réinitialiser le compteur après 24h
        if datetime.now() - self.last_reset > timedelta(hours=24):
            self.daily_tweet_count = 0
            self.last_reset = datetime.now()
        
        # Limite de 17 tweets par 24h
        return self.daily_tweet_count < 17

    def add_tweet(self, tweet_id):
        self.responded_tweets.add(tweet_id)
        self.save_responded_tweet(tweet_id)
        self.daily_tweet_count += 1

def search_and_respond():
    tracker = TweetTracker()
    
    while True:
        try:
            query = '"recherche d\'un stage" -is:retweet -is:reply lang:fr'
            tweets = client.search_recent_tweets(
                query=query,
                max_results=100,
                tweet_fields=['author_id', 'created_at']
            )

            if tweets.data:
                print(f"Trouvé {len(tweets.data)} tweets à traiter")
                tweets_processed = 0
                
                for tweet in tweets.data:
                    if tweet.id not in tracker.responded_tweets and tracker.can_tweet():
                        try:
                            # Retweeter et répondre avec un délai minimal
                            print(f"Traitement du tweet {tweet.id}...")
                            client.retweet(tweet.id)
                            time.sleep(2)  # Petit délai entre retweet et réponse
                            
                            response = "Bonjour 😊, je vous souhaite beaucoup de succès dans vos recherches ! J'ai retweeté votre post pour vous donner un coup de pouce. Si possible, pourriez-vous faire de même pour mon post épinglé ? Merci infiniment et bon courage dans vos démarches !"
                            client.create_tweet(
                                text=response,
                                in_reply_to_tweet_id=tweet.id
                            )
                            
                            tracker.add_tweet(tweet.id)
                            tweets_processed += 1
                            print(f"Tweet {tweet.id} traité avec succès")
                            
                            time.sleep(3)  # Petit délai avant le prochain tweet
                            
                        except tweepy.TooManyRequests:
                            print("Limite de taux atteinte, attente de 15 minutes...")
                            time.sleep(900)
                        except Exception as e:
                            if "You cannot retweet a Tweet that you have already retweeted" in str(e):
                                print(f"Tweet {tweet.id} déjà retweeté, marqué comme traité")
                                tracker.add_tweet(tweet.id)
                                tweets_processed += 1
                            else:
                                print(f"Erreur: {str(e)}")
                    
                    if not tracker.can_tweet():
                        print("Limite quotidienne atteinte (17 tweets/24h)")
                        time.sleep(24 * 3600)
                        break
                
                print(f"Session terminée : {tweets_processed} tweets traités sur {len(tweets.data)} trouvés")
            
            print("Attente de 5 minutes avant la prochaine recherche...")
            time.sleep(300)

        except Exception as e:
            print(f"Erreur générale: {str(e)}")
            time.sleep(300)

if __name__ == "__main__":
    search_and_respond()
