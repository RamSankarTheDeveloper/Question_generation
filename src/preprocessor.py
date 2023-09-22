"""Preprocessing actions, specifically tokenisation, parsing syntactic dependency, sentence split."""

import database.from_nlp_db as from_nlp_db
import spacy
import nltk
import nltk.corpus
from nltk.tokenize import word_tokenize
from spacy.tokens import token
nlp = spacy.load("en_core_web_sm")


class prep():

    def __init__(self, line:str=""):
        self.line=line
        self.spacy_doc = nlp(self.line)
    
    def trigger_underscorer():
         for key in list(from_nlp_db.trigger_and_question_structure_pair):
             string = from_nlp_db.given_paragraph.replace((key.replace('_',' ')), key)
         return string

        # split paragraph into sentences(sents)
    def line_parser(self, paragraph: str):
        nlp = spacy.load("en_core_web_sm")
        paragraph = paragraph.lower()
        for key in list(from_nlp_db.trigger_and_question_structure_pair):
            paragraph = paragraph.replace((key.replace('_',' ')), key)
        about_doc = nlp(paragraph)
        lines = list(
            about_doc.sents
        )  ##note: '.sents' have many inbuilt functions that can replace many of this programs's function obsolete.
        return lines

    def convert_line_to_tokens(self):
        convert_line_to_tokens = word_tokenize(self.line)
        return convert_line_to_tokens
    
    def dependency_parser(self, keyword:str)->token:
        "nsubj, ROOT etc."
        self.deps = [tok for tok in self.spacy_doc if tok.dep_ == keyword]
        return (self.deps[0])  # simplify
    
    def pick_chunk_containing_the_word(self, word:str)->str:
        "noun phrase extracted via spacy chunk"
        for chunk in self.spacy_doc.noun_chunks:
          if (word in chunk.text):
            return chunk.text

    def aux_part(self, keyword):
        if keyword in list(from_nlp_db.trigger_and_auxverb_pair.keys()):
            return from_nlp_db.trigger_and_auxverb_pair[keyword]

    def trigger_and_sent_split_pair(self, base_word_pre):
        line_without_keywordcomma = self.line.replace(f'{base_word_pre},', f'{base_word_pre}')
        if line_without_keywordcomma.split(' ')[0] == base_word_pre:
            self.splitted_sent = line_without_keywordcomma.split(',')
            if from_nlp_db.trigger_and_sent_split_pair[base_word_pre] == 0:
                return self.splitted_sent[1]
            if from_nlp_db.trigger_and_sent_split_pair[base_word_pre] == 1:
                return self.splitted_sent[0]
            if from_nlp_db.trigger_and_sent_split_pair[base_word_pre] == 'full':
                return line_without_keywordcomma

            #when the trigger words comes first, the sentence splits goes inverse
        
        else:
            self.splitted_sent = self.line.split(base_word_pre)
            if from_nlp_db.trigger_and_sent_split_pair[base_word_pre] == 0:
                return (self.splitted_sent[0])
            if from_nlp_db.trigger_and_sent_split_pair[base_word_pre] == 1:
                return (self.splitted_sent[1])
            if from_nlp_db.trigger_and_sent_split_pair[base_word_pre] == 'full':
                return (self.line)
        



