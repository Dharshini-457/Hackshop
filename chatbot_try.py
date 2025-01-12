
import spacy

nlp=spacy.blank('en')
text=nlp(u"I am good ")
for i in text:
    print(i.text,i.pos_)
print("Spacy is good")
