from generator import generator
from logger import logging
import regex as re

def clean_question():
    line_number = 0 
    question_number = 0
    for question_in_dict_val_format,line in generator().question_generator():
        try:
            question_in_list_format = list(question_in_dict_val_format)
            Unclean_question = " ".join(question_in_list_format)
            line_number += 1 
            question_number +=1
        except Exception as e:
            Unclean_question = '-----no_question_found-----'
            line_number += 1 
        logging.info(f'main/clean_question: {Unclean_question}')
        Unclean_question = str(Unclean_question)
        Unclean_question = re.sub(r'\s+', ' ', Unclean_question)
        Unclean_question = re.sub(r'\n', '', Unclean_question)
        #Unclean_question = re.sub(r'. ', '.', Unclean_question)
        Unclean_question = re.sub(r' ,', ',', Unclean_question)
        yield f'\nLine{line_number} = {line}Que.{question_number}) {Unclean_question}\n{"-"*80}' 

# Assuming generator() and question_generator() are defined elsewhere

        


def question_generator():

    for question in clean_question():
        print(question,end='')
        logging.info('main/question_generator')

if __name__ == "__main__":

    question_generator()
