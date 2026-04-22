import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import re

# Download once (comment after first run)
nltk.download('vader_lexicon')

# Sample text data
texts = ["I love this product", "This is terrible", "Very good experience", "Worst service"]

# Initialize analyzer
sia = SentimentIntensityAnalyzer()

# Preprocessing function
def preprocess(text):
    # Normalization (lowercase)
    text = text.lower()
    
    # Semi-normalization (remove punctuation)
    text = re.sub(r'[^\w\s]', '', text)
    
    return text

# Sentiment Analysis
for text in texts:
    clean_text = preprocess(text)
    
    score = sia.polarity_scores(clean_text)
    
    # Classification
    if score['compound'] > 0:
        sentiment = "Positive"
    else:
        sentiment = "Negative"
    
    print(text, "->", sentiment)