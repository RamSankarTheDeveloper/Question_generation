"""QG"""

"modules"
from preprocessor import prep
from temp_storage import *


class question:
 
 def __init__(self):
   self.tokens= prep().tokens

 def wh_part(self):
   self.wh_word= qtype[
                  list(
                     set(
                        qtype.keys()
                        ).intersection(self.tokens)
                     )[0]
                     ]  
   print("wh_word= ", self.wh_word[0])



#  def aux_part(self):
#    self.pos_tags= [nltk.pos_tag([token]) for token in word_tokenize("I like books very much because I like reading.")]
#    print("post tags= ", self.pos_tags)




question().wh_part()