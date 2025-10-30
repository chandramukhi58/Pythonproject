import PyPDF2
import docx
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob
from collections import Counter
from nltk.corpus import stopwords
import nltk
import string
nltk.download('stopwords')
nltk.download('vader_lexicon')
file=input("Enter file name(.pdf/.docx/.txt):")
text=""
if file.endswith(".pdf"):
    f=open(file,"rb")
    content=PyPDF2.PdfReader(f)
    for page in content.pages:
        pagetext=page.extract_text()
        text+=pagetext+" "
elif file.endswith(".docx"):
    document=docx.Document(file)
    for para in document.paragraphs:
        text+=para.text+" "
elif file.endswith(".txt"):
    f=open(file,"r")
    text=f.read()
else:
    print("Unsupported file type")
    exit()
if not text.strip():
    print("no readable text found in the file.")
    exit()
text=text.lower()
cleantext=""
for ch in text:
    if ch not in string.punctuation:
        cleantext+=ch
cleantext=cleantext.replace(" "," ")
cleantext=cleantext.strip()
analyzer=SentimentIntensityAnalyzer()
vader=analyzer.polarity_scores(cleantext)['compound']
if vader>=0.05:
    sentiment="Positive"
elif vader<=-0.05:
    sentiment="Negative"
else:
    sentiment="Neutral"
b=TextBlob(text)
polarity=b.sentiment.polarity
subjectivity=b.sentiment.subjectivity

words=text.split()
sentences=text.split('.')
sen=[]
for s in sentences:
    if s.strip()!="":
        sen.append(s)
paragraphs=text.split('\n')
par=[]
for p in paragraphs:
    if p.strip()!="":
        par.append(p)
totalwords=len(words)
totalsentences=len(sen)
totalparagraphs=len(par)
stopwords=set(stopwords.words("english"))
filter=[]
for w in words:
    if w not in stopwords and w!="":
        filter.append(w)
freq=Counter(filter)
topmost=freq.most_common(10)
print("Sentiment:",sentiment)
print("Polarity:",polarity)
print("Subjectivity:",subjectivity)
print("Total Words:",totalwords)
print("Total Sentences:",totalsentences)
print("Total Paragraphs:",totalparagraphs)
print("Most Frequent words:")
for w,c in topmost:
    print(w,":",c)
searchword=input("enter word to search:").lower()
wordoccurences=words.count(searchword)
print("Searchword Frequency:",wordoccurences)
