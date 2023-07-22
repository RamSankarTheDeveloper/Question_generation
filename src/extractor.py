"""extracts parts from a sentence"""

import from_nlp_db
from preprocessor import prep
import utils

#generate question from a given line
class extract_parts_from_a_line:


    #find trigger word in line
    def __init__(self,line:str= from_nlp_db.given_line):
        self.line=line
        self.preprocessor_with_line1= prep(line)
        self.tokens_of_given_line = self.preprocessor_with_line1.convert_line_to_tokens()
        self.found_trigger_word = self.check_for_triggerword_in_line()

    def check_for_triggerword_in_line(self) -> str:
        found_trigger_word = list(
            set(
                from_nlp_db.entire_triggerword_list
            ).intersection(self.tokens_of_given_line)
        )[0]
        return (found_trigger_word)

    # get wh part
    def get_wh_questionWord_pairedTo_trigger(self,return_key=False) -> str:
        wh_words = from_nlp_db.trigger_and_wh_words_pair[self.found_trigger_word]
        return (utils.return_key(return_key,'wh',wh_words[0]))


    def extract_subj_token_of_given_line(self, return_key=False):
        subj_token = self.preprocessor_with_line1.dependency_parser("nsubj")
        return utils.return_key(return_key,'subj', subj_token)

    def extract_noun_phrase_of_line(self, return_key=False):
        main_noun_phrase = self.preprocessor_with_line1.pick_chunk_containing_the_word(
            self.extract_subj_token_of_given_line().text)
        return utils.return_key(return_key,'main_np', main_noun_phrase)

    def extract_main_verb_of_line(self, return_key=False):
        main_verb = self.preprocessor_with_line1.dependency_parser("ROOT")
        return utils.return_key(return_key,'root', main_verb)

    def extract_auxiliary_verb_of_line(self, return_key=False):
        aux = self.preprocessor_with_line1.aux_part(self.extract_subj_token_of_given_line().text.lower())
        return utils.return_key(return_key,'aux', aux)

    def extract_rest_of_line_upto_trigger_word(self, return_key=False):
        splitted_sent = self.preprocessor_with_line1.trigger_and_sent_split_pair(self.found_trigger_word)
        return utils.return_key(return_key,'rest', splitted_sent)
    
    def extract_the_question_structure_which_pairedWith_theTrigger(self)->list[str]:
        question_structure=from_nlp_db.trigger_and_question_structure_pair[self.found_trigger_word]
        return question_structure
    
    def replace_keyword_in_question_structure_dict_with_actual_phrasesOrWords_in_line(self):
        pass


    # get the word order and  for each trigger word and join the parts to it
    def generate_a_question_from_found_trigger_word(self):

        question_string, space, question_mark = "", '*', '?'

        for item in self.extract_the_question_structure_which_pairedWith_theTrigger():
            if (item == 'wh'):
                question_string = question_string+self.get_wh_questionWord_pairedTo_trigger() + \
                    space
            elif (item == 'aux'):
                question_string = question_string + \
                    self.extract_auxiliary_verb_of_line() + space
            elif (item == 'rest'):
                question_string = question_string + \
                    self.extract_rest_of_line_upto_trigger_word()+space
            elif (item == 'trigger'):
                question_string = question_string + self.found_trigger_word+space
            elif (item == '?'):
                question_string = question_string + question_mark
        return question_string


if __name__ == '__main__':
    generated_question_from_the_given_phrase = extract_parts_from_a_line(
    ).generate_a_question_from_found_trigger_word()
    print(generated_question_from_the_given_phrase)
