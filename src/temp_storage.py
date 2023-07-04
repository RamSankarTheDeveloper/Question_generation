# config
text = "him and I like action films since 2019"


# data
# Different question types possible for each discourse marker
trigger_words_dict = {'because': ['Why'], 'since': ['When', 'Why'], 'when': ['When'], 'although': ['Yes/No'], 'as a result': ['Why'],
                      'for example': ['Give an example where'], 'for instance': ['Give an instance where'], 'to': ['Why'],
                      'meanwhile': ['What was happening simultaneously when'], 'thus': ['How can', 'Why did']}


aux_dict = {'i': ['do'], 'we': ['do'], 'you': ['do'], 'they': [
    'do'], 'he': ['does'], 'she': ['does'], 'it': ['does']}

sent_split = {'because': 0,'since':0}

"""wh:1, aux:2, subj:3, verb:4, rest_of_question:5"""
qg_order= {'because':['wh','aux','rest','?'],'since':['trigger','wh','aux','rest','?']}
