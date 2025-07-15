import feedparser
import re

# Простейшие списки слов (можно расширить)
positive_words = {"bullish", "moon", "gain", "pump", "surge", "green", "profit", "win"}
negative_words = {"bearish", "dump", "crash", "loss", "red", "fear", "rekt", "down"}

def clean_text(text):
    return re.sub(r'[^\w\s]', '', text.lower())

def analyze_sentiment(text):
    words = clean_text(text).split()
    pos = sum(1 for w in words if w in positive_words)
    neg = sum(1 for w in words if w in negative_words)
    if pos > neg:
        return "👍 Positive"
    elif neg > pos:
        return "👎 Negative"
    else:
        return "😐 Neutral"

def fetch_and_analyze():
    print("\n🧠 Анализ настроения по последним новостям о криптовалютах (Bitcoin):\n")

    rss_url = "https://nitter.net/search/rss?f=tweets&q=bitcoin"
    feed = feedparser.parse(rss_url)

    for entry in feed.entries[:10]:
        title = entry.title
        sentiment = analyze_sentiment(title)
        print(f"{sentiment}: {title}")

if __name__ == "__main__":
    fetch_and_analyze()
