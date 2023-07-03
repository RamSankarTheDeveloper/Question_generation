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
import temp_storage

"==classes=="
class prep():

    def __init__(self):
        self.tokens= word_tokenize(temp_storage.text)
        self.doc=nlp(temp_storage.text)

    def svo_selecter(self, keyword):
        self.svo= [tok for tok in self.doc if tok.dep_ == keyword]
        return(self.svo[0])
    
    def sent_split(self, base_word_pre):
        self.splitted_sent= temp_storage.text.split(base_word_pre)
        if temp_storage.sent_split[base_word_pre] == 0:
            return(self.splitted_sent[0])
        if temp_storage.sent_split[base_word_pre] == 1:
            return(self.splitted_sent[1])

        

if __name__ == '__main__':
    prep()