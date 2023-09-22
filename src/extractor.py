"""extracts parts from a sentence"""

import checker
from preprocessor import prep
import utils
from logger import logging
from database import from_nlp_db



class line_parts_extractor:
    "extracts required question parts from given line"

    def __init__(self, given_line: str = from_nlp_db.given_line):
        self.preprocessor_with_line1 = prep(given_line)
        self.tokens_of_given_line = (
            self.preprocessor_with_line1.convert_line_to_tokens()
        )
        self.found_trigger_word = checker.checker(self.tokens_of_given_line).check_for_triggerword_in_line() 
        logging.info('extractor/init of extractor')
         ##CALL DIRECTLY FROM INIT, THAT WAY, IT IS EASIER TO SPLIT CLASSES IF REQUIRED.



    def recieve_wh_questionWord_iePairedTo_trigger(self, return_key=False) -> str:
        wh_words = from_nlp_db.trigger_and_wh_words_pair[self.found_trigger_word]
        first_wh_word = wh_words[0]
        logging.info('extractor/recieve_wh_questionWord_iePairedTo_trigger')
        return utils.return_key(return_key, "wh", first_wh_word)

    def extract_subj_token_of_given_line(self, return_key=False):
        subj_token = self.preprocessor_with_line1.dependency_parser("nsubj")
        logging.info('extractor/extract_subj_token_of_given_line')
        return utils.return_key(return_key, "subj", subj_token)

    def extract_noun_phrase_of_line(self, return_key=False):
        main_noun_phrase = self.preprocessor_with_line1.pick_chunk_containing_the_word(
            self.extract_subj_token_of_given_line().text
        )
        logging.info('extractor/extract_noun_phrase_of_line')
        return utils.return_key(return_key, "main_np", main_noun_phrase)

    def extract_main_verb_of_line(self, return_key=False):
        main_verb = self.preprocessor_with_line1.dependency_parser("ROOT")
        logging.info('extractor/extract_main_verb_of_line')
        return utils.return_key(return_key, "root", main_verb)

    def extract_auxiliary_verb_of_line(self, return_key=False):
        aux_verb = self.preprocessor_with_line1.aux_part(
            self.extract_subj_token_of_given_line().text.lower()
        )
        logging.info('extractor/extract_auxiliary_verb_of_line')
        return utils.return_key(return_key, "aux", aux_verb)

    def extract_rest_of_line_upto_trigger_word(self, return_key=False):
        splitted_sent = self.preprocessor_with_line1.trigger_and_sent_split_pair(
            self.found_trigger_word
        )
        logging.info('extractor/extract_rest_of_line_upto_trigger_word')
        return utils.return_key(return_key, "rest", splitted_sent)
    

    def extract_the_question_structure_which_pairedWith_theTrigger(self) -> list[str]:
        question_structure = from_nlp_db.trigger_and_question_structure_pair[
            self.found_trigger_word
        ]
        logging.info('extractor/extract_the_question_structure_which_pairedWith_theTrigger')
        return question_structure


"""
if __name__ == '__main__':

    generated_question_from_the_given_phrase = line_parts_extractor(
    ).replaceeach_question_structure_items_from_objective_to_subjective()

    print(generated_question_from_the_given_phrase.values() )"""

