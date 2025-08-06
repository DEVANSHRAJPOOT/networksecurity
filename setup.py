'''
setup.py file is an essential part of packaging of
distributing python projects. It is used by setuptools
(or disutils in older python versions) to define the configurations
of your projects, such as its metadata, dependencies and more
'''


from setuptools import find_packages,setup
from typing import List


def get_requirements()->List[str]:
    '''
    This function will return the list of requirments
    '''


    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt', 'r') as file:
            # Read lines from a file
            lines=file.readlines()
            # Process each line
            for line in lines:
                requirement=line.strip()
                # ignore empty lines and -e .
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)

    except FileExistsError:
        print('requirements.txt file not found error')


    return requirement_lst

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Devansh Rajpot",
    author_email="devanshrajpoot638@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)
            



