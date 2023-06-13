from distutils import find_packages,setup

from typing import List
HYPEN_E_DOT='-e .' #""" the '-e .' refers to the setup.py as package(?)"""
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name = "Question generation",
    description = "nlp project",
    long_description = """The project is to use classical NLP to generate questions from a given text.
                    Update 1 will be generating questions based on Bloom's taxonomy""",
    version = 0.0.1,
    download_url ="",

    author = "Ram sankar.P",
    author_email = "RamSankarTheDeveloper@gmail.com",
    

    install_requires = get_requirements("requirements.txt"),
    packages = find_packages()
    )