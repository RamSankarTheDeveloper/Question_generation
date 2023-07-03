"""QG"""

"modules"
from preprocessor import prep
from temp_storage import *


class question:
 
 def __init__(self):
   self.prep_def= prep()
   self.tokens= self.prep_def.tokens

 def wh_part(self):
   self.wh_word= qtype[
                  list(
                     set(
                        qtype.keys()
                        ).intersection(self.tokens)
                     )[0]
                     ]  
   print("wh_word= ", self.wh_word[0])

 def subj_verb(self):
   self.subj= self.prep_def.svo_selecter("nsubj")
   self.verb= self.prep_def.svo_selecter("ROOT")
   print("subj, verb= ",self.subj, self.verb)



#  def aux_part(self):
#    self.pos_tags= [nltk.pos_tag([token]) for token in word_tokenize("I like books very much because I like reading.")]
#    print("post tags= ", self.pos_tags)




question().wh_part()
question().subj_verb()
