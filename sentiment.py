from textblob import TextBlob

def analyze(text):
  blob =TextBlob(text)
  sentiment = blob.sentiment
  polarity =sentiment.polarity


  if polarity>0 :
      category = "positive"
  elif polarity<0:
      category  = "negative"
  else:
      category ="neutral"
      
      
  return category


text=input("enter your text\n")
result = analyze(text)
print(f"Sentiment:{result}")
  
    
  