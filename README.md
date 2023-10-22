# Question_generation
NLP project to generate questions from sentences.

How to:
Download the folder.Execute the 'requirements' file. Execute the 'main.py' file which is inside the 'src' folder. You can try different paragraphs by editing the items in 'database' folder.
# Question Generator (Q-Gen)

**Version:** 1.0

![Question Generator Demo](link-to-demo-gif-or-image)

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Basic Usage](#basic-usage)
  - [Advanced Usage](#advanced-usage)
- [License](#license)
- [Sample Output](#sample-output)


## Overview

The Question Generator (Q-Gen) is a modular program designed to generate different types of questions from paragraphs or texts using classical Natural Language Processing (NLP) applications with Spacy and NLTK. Originally intended as a tool to generate questions for Language Models like LLMs (Large Language Models), it can also serve as a rudimentary question generator on its own. This project was created as part of an internship program.

## Features

- Generate a variety of question types from text inputs, with basic database already filled in.
- Offline.
- The properties of questions can be changed to suit specific cases to people who don't know code.
- Modularity for easy integration into larger projects.
- Compatible with language models like LLMs for generating leads and questions.

## Getting Started

Follow these instructions to get the Question Generator up and running on your local machine.

### Prerequisites

- Python 3.11
- Spacy (can install using requirement file)
- NLTK (can install using requirement file)

### Installation

Clone this repository to your local machine: https://github.com/RamSankarTheDeveloper/Question_generation.git

## Usage

Follow these instruction on how to use this code.

### Basic usage
The program already contains a very basic set of question triggers along with their question structures.
  1.Open 'database/from_nlp_df.py' and change 'given paragraph' variable with your required variable
  2.Execute the 'requirements' file.
  3.Execute the 'src/main.py' file.

### Advanced Usage
This section is where you can change the question structures and adds in more elements or specialised questions.
Edit or add the following variables to suit your needs from 'from_nlp_db.py'
  1.trigger_and_wh_words_pair,
  2.trigger_and_sent_split_pair,
  3.trigger_and_question_structure_pair

## License
GPL

## Sample output
Sample paragraph: 

    """She has been working here since 2010. Because of her, we got many works."""
    
sample output in terminal: 

    Line1 =  
    she has been working here since 2010.Que.1) since When does she has been working here ?
    
    Line2 = because of her, we got many works.
    Que.2) Why do we got many works. ?


