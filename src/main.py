"""QG, main"""

import temp_storage
from preprocessor import prep


class question:

    def __init__(self):
        self.tokens = prep().tokens
        self.trigger_word = list(
            set(
                temp_storage.trigger_words_dict.keys()
            ).intersection(self.tokens)
        )[0]

    def wh_part(self):
        self.wh_word = temp_storage.trigger_words_dict[self.trigger_word]
        return (self.wh_word[0])

    def subj_verb_aux(self):
        self.main_subj = prep().dependency_parser("nsubj")
        self.main_verb = prep().dependency_parser("ROOT")
        # aux part have problem by calling before definition?
        self.aux = prep().aux_part(self.main_subj.text.lower())
        return self.aux

    def rest_of_question_parts(self):
        self.splitted_sent = prep().sent_split(self.trigger_word)
        return (self.splitted_sent)
 #   def generate_question(self):


if __name__ == '__main__':
    print(question().wh_part(), question().subj_verb_aux()
          [0], question().rest_of_question_parts(), "?")
