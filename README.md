# Sentiment Analysis Tool

The Sentiment Analysis Tool is a Python-based application that allows users to analyze the sentiment of text input. It utilizes the NLTK library and a pre-trained sentiment analysis model to determine the sentiment expressed in the provided text.

## Features

- Sentiment Analysis: The tool employs the VADER (Valence Aware Dictionary and sEntiment Reasoner) sentiment analysis model to analyze the sentiment of text input.
- User-Friendly Interface: The tool provides a graphical user interface (GUI) built using the tkinter library, enabling users to easily enter text and obtain sentiment scores.
- Real-Time Results: Upon analyzing the text, the tool displays sentiment scores for positive, negative, neutral, and compound sentiments.

## Requirements

- Python 3.x
- NLTK library

## Installation

1. Clone the repository:

``` git clone https://github.com/alihadimoghadam/Sentiment-Analysis-Tool.git ```


2. Install the required dependencies:

``` pip install nltk ```


3. Download the NLTK resources:

``` python -m nltk.downloader vader_lexicon ```


## Usage

1. Run the `analys.py` file:

``` python analys.py ```


2. Enter the text you want to analyze in the provided text entry box.

3. Click the "Analyze" button to obtain the sentiment scores.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

