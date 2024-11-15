import nltk
nltk.download('punkt')

from textblob import TextBlob
from newspaper import Article

url = "https://www.bbc.com/news/articles/cvge9r0vwvdo"

article = Article(url)

article.download()
article.parse()
article.nlp()

text = article.summary
print(text)

blob = TextBlob(text)
sentiment = blob.sentiment.polarity # -1 to 1
print(sentiment)