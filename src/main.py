"""QG"""

"modules"
from preprocessor import prep
from temp_storage import *


class question:
 
 def __init__(self):
   self.prep_def= prep()
   self.tokens= self.prep_def.tokens
   self.base_word= list(
                     set(
                        qtype.keys()
                        ).intersection(self.tokens)
                     )[0]

 def wh_part(self):
   self.wh_word= qtype[self.base_word]  
   #print("wh_word= ", self.wh_word[0])
   return(self.wh_word[0])

 def subj_verb_aux(self):
   self.subj= self.prep_def.svo_selecter("nsubj")
   self.verb= self.prep_def.svo_selecter("ROOT")
   self.aux= self.aux_part(self.subj.text.lower() )
   #print("subj, verb, aux= ",self.subj,',', self.verb,',', self.aux[0])
   return self.aux

 def aux_part(self, keyword):
   if keyword in list(aux_dict.keys()):
     return aux_dict[keyword]
   #add nouns, including names

 def rest_of_que(self):
   self.splitted_sent= self.prep_def.sent_split(self.base_word)
   #print(splitted_sent)
   return(self.splitted_sent)

if __name__ == '__main__':
    print(question().wh_part(),question().subj_verb_aux()[0], question().rest_of_que(),"?")
