def return_key(return_key_state:bool, return_key, return_value):
 """returns [key, value] if return_key == 1; else value """
 if return_key_state==True:
  return [return_key, return_value]
 else:
  return return_value