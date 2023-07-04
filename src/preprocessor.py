"""Preprocessing actions, specifically tokenisation, parsing syntactic dependency, sentence split."""

import temp_storage
import spacy
import nltk
import nltk.corpus
from nltk.tokenize import word_tokenize


nlp = spacy.load("en_core_web_sm")


class prep():

    def __init__(self):
        self.tokens = word_tokenize(temp_storage.text)
        self.doc = nlp(temp_storage.text)

    def dependency_parser(self, keyword):
        self.deps = [tok for tok in self.doc if tok.dep_ == keyword]
        return (self.deps[0])  # simplify
    
    def nounphrase(self, subj_word):
        for chunk in self.doc.noun_chunks:
          if (subj_word in chunk.text):
            return chunk.text

    def aux_part(self, keyword):
        if keyword in list(temp_storage.aux_dict.keys()):
            return temp_storage.aux_dict[keyword]

    def sent_split(self, base_word_pre):
        self.splitted_sent = temp_storage.text.split(base_word_pre)
        if temp_storage.sent_split[base_word_pre] == 0:
            return (self.splitted_sent[0])
        if temp_storage.sent_split[base_word_pre] == 1:
            return (self.splitted_sent[1])


if __name__ == '__main__':
    prep()
