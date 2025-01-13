
import spacy
nlp=spacy.load('en_core_web_sm')
text=nlp(u"I am learning how to build chatbots")
for i in text:
    print(i.text,i.pos_)
print("Spacy is good")
