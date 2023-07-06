import tkinter as tk
from tkinter import messagebox
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

# Download NLTK resources
nltk.download('vader_lexicon')

def analyze_sentiment(text):
    analyzer = SentimentIntensityAnalyzer()
    sentiment = analyzer.polarity_scores(text)
    return sentiment

def analyze_button_click():
    text = text_entry.get("1.0", "end").strip()
    if not text:
        messagebox.showinfo("Error", "Text input cannot be empty.")
        return
    
    sentiment = analyze_sentiment(text)
    pos_score = round(sentiment['pos'], 2)
    neg_score = round(sentiment['neg'], 2)
    neu_score = round(sentiment['neu'], 2)
    compound_score = round(sentiment['compound'], 2)
    
    result = f"Positive: {pos_score}\nNegative: {neg_score}\nNeutral: {neu_score}\nCompound: {compound_score}"
    result_text.delete("1.0", "end")
    result_text.insert("1.0", result)

# Create the main window
window = tk.Tk()
window.title("Sentiment Analysis Tool")

# Create and configure text entry widget
text_entry_label = tk.Label(window, text="Enter text:")
text_entry_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

text_entry = tk.Text(window, height=10, width=50)
text_entry.grid(row=1, column=0, padx=10, pady=5)

# Create and configure analyze button
analyze_button = tk.Button(window, text="Analyze", command=analyze_button_click)
analyze_button.grid(row=2, column=0, padx=10, pady=5)

# Create and configure result text widget
result_text_label = tk.Label(window, text="Sentiment Scores:")
result_text_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")

result_text = tk.Text(window, height=4, width=50)
result_text.grid(row=4, column=0, padx=10, pady=5)

# Start the GUI event loop
window.mainloop()
