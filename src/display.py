from generator import generator
from logger import logging
def display():
        dict=generator().question_generator()
        logging.info('display/display')
        return (dict)

if __name__ == "__main__":
    dict_vals= display()
    print(dict_vals)