import spacy
from textblob import TextBlob

# Load the spaCy NLP model
nlp = spacy.load("en_core_web_sm")

def analyze_essay(text):
    """
    Process the essay using NLP and return grammar corrections and readability score.
    """
    doc = nlp(text)

    # 1️⃣ Grammar Check: Detect common article mistakes
    grammar_issues = []
    words = text.split()

    for i in range(len(words) - 1):
        if words[i].lower() == "a" and words[i + 1][0] in "aeiouAEIOU":
            grammar_issues.append(f"Grammatical mistake: 'a {words[i + 1]}' should be 'an {words[i + 1]}'.")

    # 2️⃣ Sentiment Analysis: Get the tone of the essay
    sentiment = TextBlob(text).sentiment.polarity
    sentiment_feedback = "Positive tone" if sentiment > 0 else "Neutral/Negative tone"

    # 3️⃣ Readability Score (word length check)
    word_count = len(doc)
    readability = "Good readability" if word_count < 200 else "Consider making it concise."

    return {
        "grammar_suggestions": grammar_issues,
        "sentiment": sentiment_feedback,
        "readability": readability
    }
