import  PyPDF2
import nltk
from nltk import pos_tag,word_tokenize
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
file=open("data.pdf","rb")
content=PyPDF2.PdfReader(file)
text=""
for page in content.pages:
    pagetext=page.extract_text()
    text+=pagetext+" "
searchword=input("enter a word to search:").strip().lower()
words=text.lower().split()
if searchword in words:
    print("searchword found")
else:
    print("searchword not found")
wordoccur=words.count(searchword)
totalwords=len(words)
letters=[]
for c in text:
    if c.isalpha():
        letters.append(c)
totalletters=len(letters)
totalspaces=text.count(' ')
print("Count of searchedword:",wordoccur)
print("Total no.of words:",totalwords)
print("Total no.of letters:",totalletters)
print("Total no.of spaces:",totalspaces)
wordlist=word_tokenize(searchword)
pos=pos_tag(wordlist)[0][1]
if pos.startswith('N'):
    category="Noun"
elif pos.startswith('V'):
    category="Verb"
elif pos.startswith('J'):
    category="Adjective"
elif pos.startswith('R'):
    category="Adverb"
else:
    category="other"
print("Grammatical Category:",pos)

