"""dictionaries instead of db"""

# config
given_line="he hasn't come, because he's ill"
given_paragraph=("""He loves you, because he fears your cat.
    We missed the flight because of you.
    We did it because we felt it our duty.
    He only helped us because he loves you.""")



# data
# Different question types possible for each discourse marker


trigger_and_wh_words_pair = {'because': ['Why'], 'since': ['When'], 'when': ['When'], 'although': ['Do'], 
                      
                      #'to': ['Why'],
                      'for instance': ['Give an instance where'], 
                      'for example': ['Give an example where'],
                      'as a result': ['Why'],
                      'meanwhile': ['What was happening simultaneously when'], 'thus': ['How can', 'Why did']}


entire_triggerword_list = list(trigger_and_wh_words_pair.keys()) #.keys will output in keys format

#entire_triggerword_list_with_spaces_replacedby_underscores = [spaced_word.replace(" ", "_") for spaced_word in entire_triggerword_list if (' ' in spaced_word)]


trigger_and_auxverb_pair = {'i': 'do', 'we': 'do', 'you': 'do', 'they': 'do', 'he': 'does', 'she': 'does', 'it': 'does'}

trigger_and_sent_split_pair = {'because': 0,'since':0, 'when':0, 'as a result':1 , 'although': 0, 'meanwhile':1 , 'thus':1, 
              'as a result': 1 ,'for example': 0    ##space between words don't count in tokens
                }


#wh,aux,rest,trigger,?
trigger_and_question_structure_pair= {'because':['wh','aux','rest','?'],'since':['trigger','wh','aux','rest','?'], 'when': ['wh','aux','rest','?'],
             'for example': ['wh', 'rest','?'], 'meanwhile':['wh','rest','?'], 'thus': [], 'as a result':['wh', 'rest','?'], 
             'although': ['wh','rest','?']
               }


"""
since:['when', 'why']
although:
"""
