from generator import generator

def clean_question():
    
    for question_in_dict_val_format in generator().question_generator():
        question_in_list_format = list(question_in_dict_val_format)
        Unclean_question = " ".join(question_in_list_format)
        yield(Unclean_question)

given_paragraph=("""He loves you, because he fears your cat.
We missed the flight because of you.
We did it because we felt it our duty.
He only helped us because he loves you.""")


def question_generator():
    for question in clean_question():
        print(question)

if __name__ == "__main__":

    question_generator()
