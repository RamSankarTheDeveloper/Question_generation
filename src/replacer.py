"""replaces objective items in question-structure-list with subjective items"""
import extractor, database.from_nlp_db as from_nlp_db


class replacer:
    """replaces objective keywords in question_structure in db with subjective elements"""
    def __init__(self, given_line:str= from_nlp_db.given_line):
         self.extractor_of_a_line=extractor.line_parts_extractor(given_line=given_line)

    def replaceeach_question_structure_items_from_objective_to_subjective(self):
        subjective_question_structure= dict()

        for item in self.extractor_of_a_line.extract_the_question_structure_which_pairedWith_theTrigger():
            if (item == 'wh'):
                subjective_question_structure.update({'wh': self.extractor_of_a_line.recieve_wh_questionWord_iePairedTo_trigger() })
            elif (item == 'aux'):
                subjective_question_structure.update({'aux': self.extractor_of_a_line.extract_auxiliary_verb_of_line()})
            elif (item == 'rest'):
                subjective_question_structure.update({'rest': self.extractor_of_a_line.extract_rest_of_line_upto_trigger_word()})
            elif (item == 'trigger'):
                subjective_question_structure.update({'trigger': self.extractor_of_a_line.found_trigger_word})
            elif (item == '?'):
                subjective_question_structure.update({'?': '? '})

        return subjective_question_structure 


if __name__ == '__main__':

    replaced_parts_partedWith_question_structure = replacer(
    ).replaceeach_question_structure_items_from_objective_to_subjective()

    generated_question_from_the_given_phrase=replaced_parts_partedWith_question_structure.values()

    print(generated_question_from_the_given_phrase )