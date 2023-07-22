"""dictionaries instead of db"""

# config
given_line = "him and I like action films because 2019 happened"


# data
# Different question types possible for each discourse marker


trigger_and_wh_words_pair = {'because': ['Why'], 'since': ['When'], 'when': ['When'], 
                      #'although': ['do'], 'to': ['Why'],'for instance': ['Give an instance where'], 
                      'for example': ['Give an example where'], 'as a result': ['Why'],
                      'meanwhile': ['What was happening simultaneously when'], 'thus': ['How can', 'Why did']}

entire_triggerword_list = trigger_and_wh_words_pair.keys() 

trigger_and_auxverb_pair = {'i': 'do', 'we': 'do', 'you': 'do', 'they': 'do', 'he': 'does', 'she': 'does', 'it': 'does'}

trigger_and_sent_split_pair = {'because': 0,'since':0, 'when':0, 'as a result':1 , 'although': 0, 'meanwhile':1 , 'thus':1, 
              #'as a result': 1 ,'for example': 0    ##space between words don't count in tokens
                }


#wh,aux,rest,trigger,?
trigger_and_question_structure_pair= {'because':['wh','aux','rest','?'],'since':['trigger','wh','aux','rest','?'], 'when': ['wh','aux','rest','?'],
             'for example': ['wh', 'rest','?'], 'meanwhile':['wh','rest','?'], 'thus': [], 'as a result':['wh', 'rest','?']
               }



"""
since:['when', 'why']
although:
"""