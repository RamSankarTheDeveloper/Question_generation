"tokens, "
"==nltk=="
import nltk
import nltk.corpus # sample text for performing tokenization
#nltk.download('all')
from nltk.tokenize import word_tokenize

"==spacy=="
import spacy
nlp = spacy.load("en_core_web_sm")

"==modules=="
from temp_storage import *

"==classes=="
class prep():

    def __init__(self):
        self.tokens= word_tokenize(text)
        self.doc=nlp(text)
    def svo_selecter(self, keyword):
        self.svo= [tok for tok in self.doc if tok.dep_ == keyword]
        return(self.svo[0])

if __name__ == '__main__':
    prep()