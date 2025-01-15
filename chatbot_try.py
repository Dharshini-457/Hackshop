
import spacy
nlp=spacy.load('en_core_web_sm')
text=nlp(u"I am learning how to build chatbots")
for i in text:
    print(f"(i.text,i.pos_,i.lemma_,i.shape_,i.is_alpha,i.is_stop)")
print("Spacy is good")
