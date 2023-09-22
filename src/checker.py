"""To check for trigger words"""
import database.from_nlp_db
from logger import logging

class checker():
    def __init__(self, tokens_of_given_line):
        self.tokens_of_given_line = tokens_of_given_line
        
    def check_for_triggerword_in_line(self) -> str:
        try:

            first_found_trigger_word = list(
                set(database.from_nlp_db.entire_triggerword_list).intersection(
                    self.tokens_of_given_line
                )
            )[0]
            logging.info("checker/check_for_triggerword_in_line")
            return first_found_trigger_word
        except:
            return '*None*'