from textblob import TextBlob
text = input("Enter a sentence: ")
blob = TextBlob(text)
polarity = blob.sentiment.polarity
print("\nSENTIMENT ANALYSIS")
print("----------------------")
print("Input Text:", text)
print("Polarity Score:", polarity)

if polarity > 0:
    print("Sentiment: Positive")
elif polarity < 0:
    print("Sentiment: Negative")
else:
    print("Sentiment: Neutral")
