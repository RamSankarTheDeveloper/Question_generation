import replacer
import database.from_nlp_db
import spacy
import preprocessor
from logger import logging

class generator:
    def __init__(self, text: str= database.from_nlp_db.given_paragraph):
        self.text = text

    # compine question parts as a single question
    def generate_question_from_derived_question_structure_dict(self):
        replaced_parts_partedWith_question_structure = replacer.replacer(
            self.text
        ).replaceeach_question_structure_items_from_objective_to_subjective()

        generated_question_from_the_given_phrase = (
            replaced_parts_partedWith_question_structure.values()
        )
        logging.info('generator/generate_question_from_derived_question_structure_dict')
        

        return generated_question_from_the_given_phrase

    def question_generator(self):
        """generate questions from given paragraph"""
        paragraph = database.from_nlp_db.given_paragraph
        for line in preprocessor.prep().line_parser(paragraph=paragraph):
            try:
                question = generator(
                    text=line.text
                ).generate_question_from_derived_question_structure_dict()
                logging.info('generator/question_generator')
                yield(question,line)
            except:
                yield None,None




