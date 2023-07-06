import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download NLTK resources
nltk.download('vader_lexicon')

def analyze_sentiment(text):
    analyzer = SentimentIntensityAnalyzer()
    sentiment = analyzer.polarity_scores(text)
    return sentiment

def main():
    text = input("Enter some text: ")
    sentiment = analyze_sentiment(text)
    print("Sentiment Scores:")
    print(f"Positive: {sentiment['pos']}")
    print(f"Negative: {sentiment['neg']}")
    print(f"Neutral: {sentiment['neu']}")
    print(f"Compound: {sentiment['compound']}")

if __name__ == '__main__':
    main()
