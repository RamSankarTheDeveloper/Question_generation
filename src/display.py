from generator import generator

def display():
        dict=generator().question_generator()
        return (dict)

if __name__ == "__main__":
    dict_vals= display()
    print(dict_vals)