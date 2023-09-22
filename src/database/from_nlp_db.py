"""dictionaries instead of db"""

# config
given_line="he hasn't come, because he's ill"
given_paragraph=("""He loves you, because he fears your cat.
    We missed the flight because of you.
    We did it because we felt it our duty.
    He only helped us because he loves you.
I didn't go to the party because I had to study for my exams.
She has been working here since 2010.
When I arrived at the restaurant, it was already crowded.
He worked hard, and as a result, he earned a promotion.
Although it rained, we still had a great time at the beach.
I'll prepare dinner; meanwhile, you can finish your homework.
He followed the instructions carefully, thus avoiding any mistakes.
There are many fruits available, for example, apples and oranges.
In addition to English, she speaks French fluently.
She wanted to go out; however, it started raining heavily.
He studied all night, yet he couldn't pass the exam.
He believed it would be easy; on the contrary, it was quite challenging.
In conclusion, I believe we should take action now.
It was getting late; therefore, we decided to leave.
She didn't study for the test; hence, she failed.
He missed the train; consequently, he was late for the meeting.
The flight was canceled due to bad weather.
She woke up early in order to catch the sunrise.
In contrast to the blue sky, the sea was gray and turbulent.
She loves hiking; on the other hand, he prefers swimming.
Besides English, he speaks Spanish and Italian.
It was a difficult task; nevertheless, he completed it successfully.
It was a long journey; nonetheless, they enjoyed every moment.
She's at work, and in the meantime, I'll do the laundry.
She had breakfast, and afterward, she went for a walk.
He enjoys painting, and similarly, his sister loves drawing.
I enjoy reading; likewise, my brother is a bookworm.
Even though it was cold, they went camping.
Take an umbrella in case it rains later.
In fact, the meeting is scheduled for tomorrow.
He's an early bird; in other words, he wakes up very early.
In reality, the situation is much worse than it appears.
For instance, if you're learning a new language, practicing regularly with native speakers can greatly improve your fluency.
Many countries have implemented various environmental policies to combat climate change; for instance, Norway has heavily invested in electric transportation infrastructure.
For instance, when explaining the concept of renewable energy, solar panels are a common example.
For example, when discussing healthy eating habits, fruits and vegetables are essential.
In contrast, the weather in summer is hot and dry, whereas in winter, it's cold and snowy.
On the other hand, some people prefer to work in an office, while others prefer remote work.
In conclusion, after analyzing all the data, we can confidently say that the project was a success.
In reality, behind the glamorous facade of the entertainment industry, there are many challenges and hardships.
Improving your physical fitness involves various activities, For instance, cardio workouts like running or swimming can help improve your cardiovascular health.""")



# data
# Different question types possible for each discourse marker


"""trigger_and_wh_words_pair = {'because': ['Why'], 'since': ['When'], 'when': ['When'], 'although': ['Do'], 
                      
                      #'to': ['Why'],
                      'for instance': ['Give an instance where'], 
                      'for example': ['Give an example where'],
                      'as a result': ['Why'],
                      'meanwhile': ['What was happening simultaneously when'], 'thus': ['How can', 'Why did']}
                      """
trigger_and_wh_words_pair = {
    'because': ['Why'],
    'since': ['When'],
    'when': ['When'],
    'although': ['Do'],
    'for_instance': ['Give an instance where'],
    'for_example': ['Give an example where'],
    'as_a_result': ['Why'],
    'meanwhile': ['What was happening simultaneously when'],
    'in_addition': ['What else'],
    'however': ['Do'],
    'yet': ['Do'],
    'on_the_contrary': ['Do'],
    'in_conclusion': ['What is the final thought'],
    'therefore': ['Why'],
    'hence': ['Why'],
    'consequently': ['Why'],
    'due_to': ['What was the cause of'],
    'in_order_to': ['Why'],
    'in_contrast': ['How does it differ from'],
    'on_the_other_hand': ['What is the alternative'],
    'besides': ['What else'],
    'nevertheless': ['Do'],
    'nonetheless': ['Do'],
    'in_the_meantime': ['What was happening while'],
    'afterward': ['What happened next'],
    'similarly': ['What is similar to'],
    'likewise': ['What is similar to'],
    'even_though': ['Do'],
    'in_case': ['What would happen if'],
    'in_fact': ['What is true'],
    'in_other_words': ['What is another way to say'],
    'in_reality': ['What is the actual situation'],

    # 'for_instance':[''],
    # 'for_example':['Apply it in an example'],

    # 'in_contrast':['Analyse how it differs from'],
    # 'on_the_other_hand':['Analyse the alternative to'],

    # #'besides': ['Evaluate what else is present besides'],
    # 'in_conclusion': ['Evaluate the final thought'],
    # 'in_reality': ['Evaluate the actual situation']
}



entire_triggerword_list = list(trigger_and_wh_words_pair.keys()) #.keys will output in keys format

#entire_triggerword_list_with_spaces_replacedby_underscores = [spaced_word.replace(" ", "_") for spaced_word in entire_triggerword_list if (' ' in spaced_word)]


trigger_and_auxverb_pair = {'i': 'do', 'we': 'do', 'you': 'do', 'they': 'do', 'he': 'does', 'she': 'does', 'it': 'does'}

"""trigger_and_sent_split_pair = {'because': 0,'since':0, 'when':0, 'as a result':1 , 'although': 0, 'meanwhile':1 , 'thus':1, 
              'as a result': 1 ,'for example': 0    ##space between words don't count in tokens
                }"""
trigger_and_sent_split_pair = {
    'for_instance':0,
    'because': 0,
    'since': 0,
    'when': 0,
    'although': 0,
    'meanwhile': 1,
    'as_a_result': 1,
    'for_example': 0,
    'in_addition': 1,
    'however': 0,
    'yet': 0,
    'on_the_contrary': 0,
    'in_conclusion': 1,
    'therefore': 1,
    'hence': 1,
    'consequently': 1,
    'due_to': 0,
    'in_order_to': 0,
    'in_contrast': 1,
    'on_the_other_hand': 0,
    'besides': 0,
    'nevertheless': 0,
    'nonetheless': 0,
    'in_the_meantime': 1,
    'afterward': 1,
    'similarly': 0,
    'likewise': 0,
    'even_though': 0,
    'in_case': 1,
    'in_fact': 0,
    'in_other_words': 0,
    'in_reality': 1,

    # 'for_instance':0,
    # 'for_example':0,

    # 'in_contrast':1,
    # 'on_the_other_hand':0,

    # #'besides': ['Evaluate what else is present'],
    # 'in_conclusion': 1,
    # 'in_reality': 1
}


#wh,aux,rest,trigger,?
"""trigger_and_question_structure_pair= {'because':['wh','aux','rest','?'],'since':['trigger','wh','aux','rest','?'], 'when': ['wh','aux','rest','?'],
             'for example': ['wh', 'rest','?'], 'meanwhile':['wh','rest','?'], 'thus': [], 'as a result':['wh', 'rest','?'], 
             'although': ['wh','rest','?']
               }"""
trigger_and_question_structure_pair = {
    'because': ['wh', 'aux', 'rest', '?'],
    'since': ['trigger', 'wh', 'aux', 'rest', '?'],
    'when': ['wh', 'aux', 'rest', '?'],
    'for_example': ['wh', 'rest', '?'],
    'meanwhile': ['wh', 'rest', '?'],
    'as_a_result': ['wh','aux', 'rest', '?'],
    'although': ['aux', 'rest', '?'],
    'in_addition': ['wh', 'rest', '?'],
    'however': ['aux', 'rest', '?'],
    'yet': ['aux', 'rest', '?'],
    'on_the_contrary': ['aux', 'rest', '?'],
    'in_conclusion': ['wh', '?'],
    'therefore': ['wh', 'aux', 'rest', '?'],
    'hence': ['wh', 'aux', 'rest', '?'],
    'consequently': ['wh', 'aux', 'rest', '?'],
    'due_to': ['wh', 'rest', '?'],
    'in_order_to': ['wh', 'rest', '?'],
    'in_contrast': ['wh', 'rest', '?'],
    'on_the_other_hand': ['wh', 'rest', '?'],
    'besides': ['wh', 'rest', '?'],
    'nevertheless': ['aux', 'rest', '?'],
    'nonetheless': ['aux', 'rest', '?'],
    'in_the_meantime': ['wh', 'rest', '?'],
    'afterward': ['wh', 'rest', '?'],
    'similarly': ['wh', 'rest', '?'],
    'likewise': ['wh', 'rest', '?'],
    'even_though': ['aux', 'rest', '?'],
    'in_case': ['wh', 'rest', '?'],
    'in_fact': ['wh', 'rest', '?'],
    'in_other_words': ['wh', 'rest', '?'],
    'in_reality': ['wh', 'rest', '?'],
    'for_instance':["can you apply",'rest',"in others as well","?"]

    # 'for_instance':["can you apply '",'rest',"' in others as well","?"],
    # 'for_example':['Apply','rest', 'in an example.'],

    # 'in_contrast':["Analyse how '", 'rest', "differs from the alternative"],
    # 'on_the_other_hand':['Analyse both situations'],

    # #'besides': ['Evaluate what else is present'],
    # 'in_conclusion': ['Evaluate','rest'],
    # 'in_reality': ['Evaluate the actual situation','rest']
}



if __name__ == "__main__":

    # Create the new dictionary
    new_trigger_and_question_structure_pair = {}

    for trigger, structure in trigger_and_question_structure_pair.items():
        new_structure = []
        for element in structure:
            if element == 'wh':
                if trigger in trigger_and_wh_words_pair:
                    new_structure.extend(trigger_and_wh_words_pair[trigger])
            else:
                new_structure.append(element)
        new_trigger_and_question_structure_pair[trigger] = new_structure

    print(new_trigger_and_question_structure_pair)


