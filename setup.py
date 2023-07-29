# can create the entire project as a python package and even deploy on Python PyPi

from setuptools import find_packages, setup
from typing import List


hyphen_e_dot = "-e ."

def get_requirements(file_path:str)->List[str]:
      # my function will return the list of requirements
    requirements =[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        # to remove \n that is also read from requirements.txt
        requirements = [req.replace("\n","") for req in requirements]

        if hyphen_e_dot in requirements:
            requirements.remove(hyphen_e_dot)

    return requirements



setup(
name= 'MLProject',
version= '0.0.1',
author= 'Preeti',
author_email= 'preeti.k.mukherjee@gmail.com',
packages= find_packages(),
install_requires=get_requirements('requirements.txt')

)
