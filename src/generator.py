import replacer

class generator():

    def output_values_from_dict(self):
        
        replaced_parts_partedWith_question_structure = replacer.replacer(
        ).replaceeach_question_structure_items_from_objective_to_subjective()

        generated_question_from_the_given_phrase=replaced_parts_partedWith_question_structure.values()

        return (generated_question_from_the_given_phrase)


if __name__ == '__main__':

    print( generator().output_values_from_dict() )