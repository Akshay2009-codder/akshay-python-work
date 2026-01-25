import requests
import pyttsx3

API_KEY = "cda88f3e628c46feb76a3e21e09336a7"
URL = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={API_KEY}"

response = requests.get(URL)
data = response.json()

engine = pyttsx3.init()

if data["status"] == "ok":
    articles = data["articles"]
    engine.say("lisent tudey,s latest news by Akshay dhumda.")
    if articles:
        for i, article in enumerate(articles[:5], start=1):
            news_title = article["title"]
            engine.say(f"News number {i}: {news_title}")
    else:
        engine.say("today not any news availible sorry")
    engine.say("Thanks for using Akshay's news app.")
    engine.runAndWait()
else:
    engine.say("Any error ocurred we current process on that.")
    engine.runAndWait()
