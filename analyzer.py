import nltk
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import re

nltk.download('vader_lexicon')
nltk.download('stopwords')
analyzer = SentimentIntensityAnalyzer()

def clean_text(text):
  text = text.lower()  # Lowercase text
  text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
  words = [word for word in text.split() if word not in stopwords.words('english')]  # Remove stopwords
  return " ".join(words)


def analyze_sentiment(text):
    cleaned_text = clean_text(text)
    try:
        scores = analyzer.polarity_scores(cleaned_text)
        sentiment = max(['pos', 'neg', 'neu'], key=scores.get)
        if sentiment == 'pos':
            return "Positive"
        elif sentiment == 'neg':
            return "Negative"
        else:
            return "Neutral"
    except Exception as e:
        return f"Sentiment analysis failed: {e}"



